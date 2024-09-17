package com.regnosys.rosetta.generator.jsonschema

import com.google.inject.Inject
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.ArrayList
import java.util.List
import java.util.Map

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*
import com.regnosys.rosetta.RosettaEcoreUtil

class JsonSchemaTypeGenerator {

	@Inject extension JsonSchemaGeneratorHelper
	
	@Inject extension RosettaEcoreUtil

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
		  «IF attr.definition !== null»
		  	"description": "«attr.definition»",
		  «ENDIF»
		  «IF attr.toExpandedAttribute.multiple»
		  	"type": "array",
		  	"items": {
		  	  «attr.attributeType»
		  	},
		  	"minItems": «attr.card.inf»«IF attr.card.sup > 1»,
		  	"maxItems": «attr.card.sup»«ENDIF»
		  «ELSE»
		  	«attr.attributeType»
		  «ENDIF»
		}
	'''

	def String getAttributeType(Attribute attr) {
		val type = attr.typeCall.type
		val expandedType = type.toExpandedType
		if (expandedType.isBuiltInType && !attr.toExpandedAttribute.hasMetas) {
			return '''"type": "«JsonSchemaTranslator.toJsonSchemaType(expandedType)»"'''
		} else if (attr.toExpandedAttribute.hasMetas) {
			return '''"$ref": "«getFilename(type.toExpandedType.metaNamespace, attr.toExpandedAttribute.toType)»"'''
		} else {
			return '''"$ref": "«getFilename(type.namespace, attr.toExpandedAttribute.toType)»"'''
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
