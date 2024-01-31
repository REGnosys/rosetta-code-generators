package com.regnosys.rosetta.generator.jsonschema;


import com.google.inject.Provider;
import com.regnosys.rosetta.tests.RosettaInjectorProvider;
import com.regnosys.rosetta.tests.util.ModelHelper;
import org.eclipse.xtext.resource.XtextResourceSet;
import org.eclipse.xtext.testing.InjectWith;
import org.eclipse.xtext.testing.extensions.InjectionExtension;
import org.junit.Assert;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import javax.inject.Inject;
import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static org.junit.Assert.assertEquals;

@ExtendWith(InjectionExtension.class)
@InjectWith(RosettaInjectorProvider.class)
public class JsonSchemaGenerationTest {

    @Inject
    private ModelHelper modelHelper;
    @Inject
    private Provider<XtextResourceSet> resourceSetProvider;
    @Inject
    private JsonSchemaCodeGenerator generator;

    public static Stream<Arguments> load() throws IOException {
        return Files.list(Path.of("src/test/resources")).map(x -> Arguments.of(x));
    }

    @ParameterizedTest
    @MethodSource("load")
    void runTest(Path testPath) throws IOException {
        String[] rosettaFiles = loadRosettaFiles(testPath);
        var m = modelHelper.parseRosettaWithNoErrors(rosettaFiles);
        Map<String, ? extends CharSequence> generatedFiles = generator.afterAllGenerate(resourceSetProvider.get(), m, "test");

        for (String generatedFile : generatedFiles.keySet()) {
            Path expectationFile = testPath.resolve(generatedFile);
            if (!Files.exists(expectationFile)) {
                Files.createFile(expectationFile);
            }

            String expectedFile = Files.readString(expectationFile);
            CharSequence charSequence = generatedFiles.get(generatedFile);
            assertEquals(expectedFile, charSequence);
        }
    }

    private String[] loadRosettaFiles(Path testPath) throws IOException {
        return Files.list(testPath)
                .filter(x -> x.toString().endsWith(".rosetta"))
                .map(this::readString)
                .toArray(String[]::new);
    }

    String readString(Path p) {
        try {
            return Files.readString(p);
        } catch (IOException e) {
            throw new UncheckedIOException(e);
        }

    }

    private Map<String, ? extends CharSequence> generate(String model) {
        var m = modelHelper.parseRosettaWithNoErrors(model);
        var resourceSet = m.eResource().getResourceSet();
        return generator.afterAllGenerate(resourceSet, List.of(m), "test");
    }
}
