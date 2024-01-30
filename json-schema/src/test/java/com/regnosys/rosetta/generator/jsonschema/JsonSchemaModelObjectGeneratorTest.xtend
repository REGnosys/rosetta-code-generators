package com.regnosys.rosetta.generator.jsonschema

import com.google.inject.Inject
import com.regnosys.rosetta.generators.test.TestUtil
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import java.nio.file.Files
import java.nio.file.Paths
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Disabled
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class JsonSchemaModelObjectGeneratorTest {

	@Inject extension ModelHelper
	
	@Inject extension TestUtil
	
	@Inject JsonSchemaCodeGenerator generator;

	@Test
	@Disabled("Test to generate the json schema for CDM")
	def void generateCdm() {
		val dirs = #[
            '../../../finos/common-domain-model/rosetta-source/src/main/rosetta',
            '../../rosetta-dsl/rosetta-lang/src/main/resources/model'            
        ]

		val resourceSet = dirs.parseAllRosettaFiles
		val models = resourceSet.resources.map[contents.head as RosettaModel]
		
		val generatedFiles = generator.afterAllGenerate(resourceSet, models, "test")

		val cdmDir = Files.createDirectories(Paths.get("cdm"))
		generatedFiles.forEach [ fileName, contents |
			Files.write(cdmDir.resolve(fileName), contents.toString.bytes)
		]
	}

	@Test
	def void shouldGenerateType() {
		val rosetta = '''
				type Product: <"A product from a catalog.">
				  productId   int    (1..1) <"The unique identifier for a product">
				  productName string (1..1) <"Name of the product">
				  price       number (0..1) <"The price of the product">
				  tags        string (1..*) <"Tags for the product">			
		'''.generate

		val schemaFile = rosetta.get('schema-test.json').toString
		//println(types)
		assertEquals('''
				{
				  "$schema": "https://json-schema.org/draft/2020-12/schema",
				  "$id": "https://example.com/product.schema.json",
				  "title": "Product",
				  "description": "A product from a catalog.",
				  "type": "object",
				  "properties": {
				    "productId": {
				      "description": "The unique identifier for a product",
				      "type": "integer"
				    },
				    "productName": {
				      "description": "Name of the product",
				      "type": "string"
				    },
				    "price": {
				      "description": "The price of the product",
				      "type": "number"
				    },
				    "tags": {
				      "description": "Tags for the product",
				      "type": "array",
				      "items": {
				        "type": "string"
				      },
				      "minItems": 1
				    }
				  },
				  "required": [ "productId", "productName" ]
				}
			'''.toString, schemaFile)
	}
	


	def generate(CharSequence model) {
		val m = model.parseRosettaWithNoErrors
		val resourceSet = m.eResource.resourceSet
		
		generator.afterAllGenerate(resourceSet, #{m}, "test")
	}
}
