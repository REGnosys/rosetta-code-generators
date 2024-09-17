package com.regnosys.rosetta.generator.jsonschema

import com.google.inject.Inject
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import java.util.ArrayList
import java.util.List
import java.util.Map

class JsonSchemaEnumGenerator {

	@Inject extension JsonSchemaGeneratorHelper
	
	def Map<String, ? extends CharSequence> generateEnumDefinitions(List<RosettaEnumeration> enumList) {
		val result = newHashMap

		for (RosettaEnumeration enumeration : enumList) {
			val enumDefinitionContents = enumeration.generateEnumDefinition
			result.put(enumeration.filename, enumDefinitionContents)
		}

		result
	}

	def String generateEnumDefinition(RosettaEnumeration enumeration) '''
		{
		  "$schema": "http://json-schema.org/draft-04/schema#",
		  "$anchor": "«enumeration.namespace»",
		  "type": "string",
		  "title": "«enumeration.name»",
		  «IF enumeration.definition !== null»
		  	"description": "«enumeration.definition»",
		  «ENDIF»
		  "enum": [
		    «FOR enumValue : enumeration.allEnumsValues SEPARATOR ",\n"»"«enumValue.enumValueString»"«ENDFOR»
		  ],
		  "oneOf": [
		    «FOR enumValue : enumeration.allEnumsValues SEPARATOR ",\n"»«enumValue.generateEnumValue»«ENDFOR»
		  ]
		}
	'''

	def String generateEnumValue(RosettaEnumValue enumValue) '''
		{
		  "enum": [
		    "«enumValue.enumValueString»"
		  ],
		  "title": "«enumValue.name»"«IF enumValue.definition !== null»,
		  "description": "«enumValue.definition»"«ENDIF»
		}
	'''

	private def String getEnumValueString(RosettaEnumValue enumValue) {
		if (enumValue.display !== null)
			return enumValue.display
		else
			return enumValue.name
	}

	private def allEnumsValues(RosettaEnumeration enumeration) {
		val enumValues = new ArrayList
		var e = enumeration;

		while (e !== null) {
			e.enumValues.forEach[enumValues.add(it)]
			e = e.parent
		}
		return enumValues.sortBy[name];
	}
}
