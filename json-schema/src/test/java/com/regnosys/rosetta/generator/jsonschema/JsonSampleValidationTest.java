package com.regnosys.rosetta.generator.jsonschema;

import static org.junit.Assert.fail;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.networknt.schema.InputFormat;
import com.networknt.schema.JsonSchema;
import com.networknt.schema.JsonSchemaFactory;
import com.networknt.schema.PathType;
import com.networknt.schema.SchemaLocation;
import com.networknt.schema.SchemaValidatorsConfig;
import com.networknt.schema.SpecVersion;
import com.networknt.schema.ValidationMessage;

public class JsonSampleValidationTest {

    private static final Logger LOGGER = LoggerFactory.getLogger(JsonSampleValidationTest.class);
    public static final SpecVersion.VersionFlag JSON_SCHEMA_VERSION = SpecVersion.VersionFlag.V202012;

    public static Stream<Arguments> load() throws IOException {

        List<Path> jsonSchemaFiles = Files.walk(Path.of("src/test/resources"))
                .filter(x -> x.toString().endsWith(".schema.json"))
                .collect(Collectors.toList());

        Stream.Builder<Arguments> builder = Stream.builder();
        for (Path jsonSchemaFile : jsonSchemaFiles) {
            String schemaFileName = jsonSchemaFile.getFileName().toString();
            String sampleFileName = schemaFileName.replace(".schema", "");
            Path sampleFileNamePath = jsonSchemaFile.getParent().resolve(sampleFileName);
            if (Files.exists(sampleFileNamePath)) {
                builder.add(Arguments.of(sampleFileName, jsonSchemaFile, sampleFileNamePath));
            }

            for (int i = 0; i < 10; i++) {
                String anotherSampleFileName = schemaFileName.replace(".schema", "." + i);
                Path anotherSampleFileNamePath = jsonSchemaFile.getParent().resolve(anotherSampleFileName);

                if (Files.exists(anotherSampleFileNamePath)) {
                    builder.add(Arguments.of(anotherSampleFileName, jsonSchemaFile, anotherSampleFileNamePath));
                }
            }
        }
        return builder.build();
    }

    @ParameterizedTest(name = "{index} {0}")
    @MethodSource("load")
    void runTest(String testName, Path jsonSchemaFile, Path sampleFile) throws IOException {
        LOGGER.info("Testing json {} is valid against {}", jsonSchemaFile.getFileName().toString(), sampleFile.getFileName().toString());
        String sampleFileContents = Files.readString(sampleFile);
        if (sampleFileContents.isEmpty()) {
            fail("No Sample file. Populate " + sampleFile.getFileName().toString());
        }
        Set<ValidationMessage> validationMessages = validateSample(jsonSchemaFile, sampleFileContents);
        for (ValidationMessage assertion : validationMessages) {
            fail(assertion.toString());
        }
    }

    private Set<ValidationMessage> validateSample(Path jsonSchemaFile, String sampleFileContents) throws IOException {
        JsonSchemaFactory jsonSchemaFactory = JsonSchemaFactory.getInstance(JSON_SCHEMA_VERSION, builder ->
                builder.schemaMappers(schemaMappers -> schemaMappers.mapPrefix("https://www.example.org/", "classpath:schema/"))
        );

        SchemaValidatorsConfig config = new SchemaValidatorsConfig();
        config.setPathType(PathType.JSON_POINTER);
        JsonSchema schema = jsonSchemaFactory.getSchema(SchemaLocation.of(jsonSchemaFile.toUri().toString()), config);

        Set<ValidationMessage> assertions = schema.validate(sampleFileContents, InputFormat.JSON, executionContext -> {
            // By default since Draft 2019-09 the format keyword only generates annotations and not assertions
            executionContext.getExecutionConfig().setFormatAssertionsEnabled(true);
        });
        return assertions;
    }

}
