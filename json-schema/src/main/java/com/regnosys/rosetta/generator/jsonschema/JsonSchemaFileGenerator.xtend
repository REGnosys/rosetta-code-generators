package com.regnosys.rosetta.generator.jsonschema

import com.regnosys.rosetta.rosetta.simple.Data
import java.util.List
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaMetaType

class JsonSchemaFileGenerator {

	def CharSequence generate(List<Data> data, List<RosettaMetaType> metaTypes, List<RosettaEnumeration> enumerations, String version) {
		
		'''
		{
		  "$schema": "https://json-schema.org/draft/2020-12/schema", ««« Hard coded
		  "$id": "https://example.com/product.schema.json", ««« Id of the model
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

}
