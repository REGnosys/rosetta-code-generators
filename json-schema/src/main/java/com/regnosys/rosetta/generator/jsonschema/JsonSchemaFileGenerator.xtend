package com.regnosys.rosetta.generator.jsonschema

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.rosetta.RosettaNamed
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.ArrayList
import java.util.List
import java.util.Map

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*

class JsonSchemaFileGenerator {

	@Inject extension RosettaExtensions

	def Map<String, ? extends CharSequence> generate(List<Data> data, List<RosettaEnumeration> enumerations,
		String version) {

		val result = newHashMap
		
		result.putAll(data.sortBy[name].generateTypeDefinitions)
		result.putAll(enumerations.sortBy[name].generateEnumDefinitions)
		
		result
	}

	def Map<String, ? extends CharSequence> generateTypeDefinitions(List<Data> dataList) {
		val result = newHashMap

		for (Data data : dataList) {
			val model = data.eContainer as RosettaModel
			val typeDefinitionName = getFilename(model, data)
			val typeDefinitionContents = data.generateTypeDefinition
			result.put(typeDefinitionName, typeDefinitionContents)
		}

		result
	}

	def String generateTypeDefinition(Data data) '''
		{
		  "title": "«data.name»",
		  "description": "«data.definition»",
		  "type": "object",
		  "properties": {
		    «FOR attr : data.expandedAttributes SEPARATOR ","»«attr.generateAttributeDefinition»«ENDFOR»
		  },
		  "required": [
		    «FOR requiredAttrName : data.requiredAttributeNames SEPARATOR ",\n"»"«requiredAttrName»"«ENDFOR»
		  ]
		}
	'''

	def String generateAttributeDefinition(ExpandedAttribute attr) '''
		«val type = JsonSchemaTranslator.toJsonSchemaType(attr.type)»
		"«attr.name»": {
		  "description": "«attr.definition»",
		  «IF attr.isMultiple»
		  "type": "array",
		  "items": {
		    "type": "«type»"
		  },
		  "minItems": «attr.inf»
		  «ELSE»
		  "type": "«type»"
		  «ENDIF»
		}
	'''

	def List<String> getRequiredAttributeNames(Data data) {
		data.expandedAttributes.filter[inf == 1 && sup == 1].map[name].toList
	}

	def Map<String, ? extends CharSequence> generateEnumDefinitions(List<RosettaEnumeration> enumList) {
		val result = newHashMap

		for (RosettaEnumeration enumeration : enumList) {
			val model = enumeration.eContainer as RosettaModel
			val enumDefinitionName = getFilename(model, enumeration)
			val enumDefinitionContents = enumeration.generateEnumDefinition
			result.put(enumDefinitionName, enumDefinitionContents)
		}

		result
	}
	
	def String generateEnumDefinition(RosettaEnumeration e) '''
		{
		  "description": "«e.definition»",
		  "enum": [
		    «FOR enumValue : e.allEnumsValues SEPARATOR ",\n"»"«enumValue.name»"«ENDFOR»
		  ],
		  "oneOf": [
		    {
		      "enum": [
		        "PRIN"
		      ],
		      "title": "Principal",
		      "description": "Trading as Principal."
		    },
		    {
		      "enum": [
		        "AGEN"
		      ],
		      "title": "Agent",
		      "description": "Trading as Agent on behalf of a customer."
		    }
		  ],
		  "type": "string"
		}
	'''
	
	def String getFilename(RosettaModel model, RosettaNamed named) {
		model.name.replace(".", "-") + "-" + named.name + ".schema.json"
	}
	
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
