package com.regnosys.rosetta.generator.jsonschema;


import com.google.inject.Injector;
import com.google.inject.Key;
import com.google.inject.Provider;
import com.google.inject.TypeLiteral;
import com.networknt.schema.*;
import com.regnosys.rosetta.tests.RosettaInjectorProvider;
import com.regnosys.rosetta.tests.util.ModelHelper;
import org.eclipse.xtext.resource.XtextResourceSet;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

public class JsonSchemaGenerationTest {

    public static final String JSON_SCHEMA_VERSION = SchemaId.V4;

	private static final Logger LOGGER = LoggerFactory.getLogger(JsonSchemaGenerationTest.class);

    public static Stream<Arguments> load() throws IOException {

        RosettaInjectorProvider rosettaInjectorProvider = new RosettaInjectorProvider();

        rosettaInjectorProvider.setupRegistry();
        Injector injector = rosettaInjectorProvider.getInjector();
        ModelHelper modelHelper = injector.getInstance(ModelHelper.class);
        Provider<XtextResourceSet> resourceSetProvider = injector.getInstance(Key.get(new TypeLiteral<Provider<XtextResourceSet>>() {
        }));
        JsonSchemaCodeGenerator generator = injector.getInstance(JsonSchemaCodeGenerator.class);


        Stream.Builder<Arguments> builder = Stream.builder();
        List<Path> testDirs = Files.list(Path.of("src/test/resources")).collect(Collectors.toList());

        for (Path testDir : testDirs) {
            Map<String, ? extends CharSequence> generatedFiles = getGeneratedFiles(testDir, modelHelper, resourceSetProvider, generator);

            for (String generatedFile : generatedFiles.keySet()) {
                Path expectationFile = testDir.resolve(generatedFile);
                if (!Files.exists(expectationFile)) {
                    Files.createFile(expectationFile);
                }
                String expectedFile = Files.readString(expectationFile);
                CharSequence actualFile = generatedFiles.get(generatedFile);
                Files.write(expectationFile,actualFile.toString().getBytes());
                builder.add(Arguments.of(generatedFile, expectedFile, actualFile));
            }
        }


        return builder.build();
    }

    @ParameterizedTest(name = "{index} {0}")
    @MethodSource("load")
    void runTest(String generatedFileName, String expectedFile, String actualFile) {
    	LOGGER.info("Testing {}", generatedFileName);
        assertEquals(expectedFile, actualFile);
        validateJsonSchema(actualFile);
    }

    private static Map<String, ? extends CharSequence> getGeneratedFiles(Path testPath, ModelHelper modelHelper, Provider<XtextResourceSet> resourceSetProvider, JsonSchemaCodeGenerator generator) throws IOException {
        String[] rosettaFiles = loadRosettaFiles(testPath);
        var m = modelHelper.parseRosettaWithNoErrors(rosettaFiles);
        Map<String, ? extends CharSequence> generatedFiles = generator.afterAllGenerate(resourceSetProvider.get(), m, "test");
        return generatedFiles;
    }

    private static String[] loadRosettaFiles(Path testPath) throws IOException {
        return Files.list(testPath)
                .filter(x -> x.toString().endsWith(".rosetta"))
                .map(JsonSchemaGenerationTest::readString)
                .toArray(String[]::new);
    }

    private static String readString(Path p) {
        try {
            return Files.readString(p);
        } catch (IOException e) {
            throw new UncheckedIOException(e);
        }

    }

    public void validateJsonSchema(String input) {
        JsonSchemaFactory jsonSchemaFactory = JsonSchemaFactory.getInstance(SpecVersion.VersionFlag.V202012,
                builder -> builder.schemaMappers(schemaMappers -> schemaMappers
                        .mapPrefix("https://json-schema.org", "classpath:")
                        .mapPrefix("http://json-schema.org", "classpath:")));

        SchemaValidatorsConfig config = new SchemaValidatorsConfig();

        config.setPathType(PathType.JSON_POINTER);

        // Due to the mapping the meta schema will be retrieved from the classpath at classpath:draft/2020-12/schema.
        JsonSchema schema = jsonSchemaFactory.getSchema(SchemaLocation.of(JSON_SCHEMA_VERSION), config);

        Set<ValidationMessage> assertions = schema.validate(input, InputFormat.JSON, executionContext -> {
            executionContext.getExecutionConfig().setFormatAssertionsEnabled(true);
        });

        for (ValidationMessage assertion : assertions) {
            fail(assertion.toString());
        }

    }

}
