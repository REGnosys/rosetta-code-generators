package com.regnosys.rosetta.generator.jsonschema

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.ArrayList
import java.util.List

class JsonSchemaFileGenerator {

	@Inject extension RosettaExtensions

	def CharSequence generate(List<Data> data, List<RosettaMetaType> metaTypes, List<RosettaEnumeration> enumerations,
		String version) {

		val typeDefinitions = data.sortBy[name].generateTypeDefinitions

		val enumDefinitions = enumerations.sortBy[name].generateEnumDefinitions

		'''
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
		'''
	}

	def String generateTypeDefinitions(List<Data> datas) '''
	'''

	def String generateEnumDefinitions(List<RosettaEnumeration> enums) '''
		««« «allEnumsValues»
	'''

	private def allEnumsValues(RosettaEnumeration enumeration) {
		val enumValues = new ArrayList
		var e = enumeration;

		while (e !== null) {
			e.enumValues.forEach[enumValues.add(it)]
			e = e.superType
		}
		return enumValues.sortBy[name];
	}

}
