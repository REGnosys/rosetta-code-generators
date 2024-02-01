package com.regnosys.rosetta.generator.jsonschema;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;

import org.eclipse.xtext.resource.XtextResourceSet;

import com.google.inject.Injector;
import com.google.inject.Key;
import com.google.inject.Provider;
import com.google.inject.TypeLiteral;
import com.regnosys.rosetta.tests.RosettaInjectorProvider;
import com.regnosys.rosetta.tests.util.ModelHelper;

public class GenerateCDMJsonSchemas {
	
    public static void main(String[] args) throws IOException {
        Path cdmDir = Path.of("/Users/hugohills/dev/github/rosetta-models/common-domain-model/rosetta-source/src/main/rosetta");
        Path output = Path.of("./json-schema-cdm-5.4.0");
        Files.createDirectories(output);

        RosettaInjectorProvider rosettaInjectorProvider = new RosettaInjectorProvider();
        rosettaInjectorProvider.setupRegistry();
        Injector injector = rosettaInjectorProvider.getInjector();
        ModelHelper modelHelper = injector.getInstance(ModelHelper.class);
        Provider<XtextResourceSet> resourceSetProvider = injector.getInstance(Key.get(new TypeLiteral<Provider<XtextResourceSet>>() {
        }));
        JsonSchemaCodeGenerator generator = injector.getInstance(JsonSchemaCodeGenerator.class);

        Map<String, ? extends CharSequence> generatedFiles = JsonSchemaGenerationTest.getGeneratedFiles(cdmDir, modelHelper, resourceSetProvider, generator);
        for (String generatedFile : generatedFiles.keySet()) {
            Path resolve = output.resolve(generatedFile);
            Files.createFile(resolve);
            Files.write(resolve, generatedFiles.get(generatedFile).toString().getBytes());
        }

    }

}
