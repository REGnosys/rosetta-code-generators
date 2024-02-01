package com.regnosys.rosetta.generator.jsonschema;

import com.networknt.schema.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;

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
            if (!Files.exists(sampleFileNamePath)) {
                Files.createFile(sampleFileNamePath);
                Files.writeString(sampleFileNamePath, "{}");
            }

            builder.add(Arguments.of(jsonSchemaFile, sampleFileNamePath));
        }
        return builder.build();
    }

    @ParameterizedTest(name = "{index} {1}")
    @MethodSource("load")
    void runTest(Path jsonSchemaFile, Path sampleFile) throws IOException {
        LOGGER.info("Testing json {} is valid against {}", jsonSchemaFile.toString(), sampleFile.toString());
        Set<ValidationMessage> validationMessages = validateSample(jsonSchemaFile, sampleFile);
        for (ValidationMessage assertion : validationMessages) {
            fail(assertion.toString());
        }
    }

    private Set<ValidationMessage> validateSample(Path jsonSchemaFile, Path sampleFile) throws IOException {
        JsonSchemaFactory jsonSchemaFactory = JsonSchemaFactory.getInstance(JSON_SCHEMA_VERSION, builder ->
                builder.schemaMappers(schemaMappers -> schemaMappers.mapPrefix("https://www.example.org/", "classpath:schema/"))
        );

        SchemaValidatorsConfig config = new SchemaValidatorsConfig();
        config.setPathType(PathType.JSON_POINTER);
        JsonSchema schema = jsonSchemaFactory.getSchema(SchemaLocation.of(jsonSchemaFile.toUri().toString()), config);

        String sampleFileContents = Files.readString(sampleFile);
        Set<ValidationMessage> assertions = schema.validate(sampleFileContents, InputFormat.JSON, executionContext -> {
            // By default since Draft 2019-09 the format keyword only generates annotations and not assertions
            executionContext.getExecutionConfig().setFormatAssertionsEnabled(true);
        });
        return assertions;
    }

}
