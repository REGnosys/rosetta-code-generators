package com.regnosys.rosetta.generator.jsonschema

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaType
import com.regnosys.rosetta.rosetta.simple.Attribute
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
			val typeDefinitionContents = generateTypeDefinition(data)
			result.put(data.filename, typeDefinitionContents)
		}

		result
	}

	def String generateTypeDefinition(Data data) '''
		{
		  "$schema": "http://json-schema.org/draft-04/schema#",
		  "$anchor": "«data.namespace»",
		  "type": "object",
		  "title": "«data.name»",
		  «IF data.definition !== null»
		  "description": "«data.definition»",
		  «ENDIF»
		  "properties": {
		    «FOR attr : data.allAttributes SEPARATOR ","»«attr.generateAttributeDefinition»«ENDFOR»
		  }«IF !data.requiredAttributeNames.isEmpty»,
		  "required": [
		    «FOR requiredAttrName : data.requiredAttributeNames SEPARATOR ",\n"»"«requiredAttrName»"«ENDFOR»
		  ]«ENDIF»
		}
	'''

	def String generateAttributeDefinition(Attribute attr) '''
		"«attr.name»": {
		  "description": "«attr.definition»",
		  «IF attr.toExpandedAttribute.multiple»
		  "type": "array",
		  "items": {
		    «attr.attributeType»
		  },
		  "minItems": «attr.card.inf»
		  «ELSE»
		  «attr.attributeType»
		  «ENDIF»
		}
	'''
	def String getAttributeType(Attribute attr) {
		val type = attr.typeCall.type
		val expandedType = type.toExpandedType
		if (expandedType.isBuiltInType) {
			return '''"type": "« JsonSchemaTranslator.toJsonSchemaType(expandedType)»"'''
		}
		else if (expandedType.isEnumeration) {
			return '''"type": "« JsonSchemaTranslator.toJsonSchemaType(expandedType)»"'''
		} 
		else {
			return '''"$ref": "«type.filename»"'''
		}
	}

	def List<String> getRequiredAttributeNames(Data data) {
		data.expandedAttributes.filter[inf == 1 && sup == 1].map[name].toList
	}

	def Map<String, ? extends CharSequence> generateEnumDefinitions(List<RosettaEnumeration> enumList) {
		val result = newHashMap

		for (RosettaEnumeration enumeration : enumList) {
			val enumDefinitionContents = enumeration.generateEnumDefinition
			result.put(enumeration.filename, enumDefinitionContents)
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
	
	def String getNamespace(RosettaType type) {
		type.model.name
	}
	
	def String getFilename(RosettaType type) {
		type.namespace.replace(".", "-") + "-" + type.name + ".schema.json"
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
