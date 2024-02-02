package com.regnosys.rosetta.generator.jsonschema

import com.regnosys.rosetta.generator.object.ExpandedAttribute

import com.regnosys.rosetta.generator.object.ExpandedType
import com.regnosys.rosetta.generator.jsonschema.JsonSchemaTranslator
import com.regnosys.rosetta.rosetta.RosettaType

class JsonSchemaGeneratorHelper {

    def replaceTabsWithSpaces(CharSequence code) {
        code.toString.replace('\t', '  ')
    }

	def String getNamespace(RosettaType type) {
		type.model.name
	}

    def getMetaNamespace(ExpandedType type) {
		type.model.name + ".metafields"	
    }

	def String getFilename(RosettaType type) {
		getFilename(type.namespace, type.name)
	}
	
	def String getFilename(String namespace, CharSequence typeName) {
		namespace.replace(".", "-") + "-" + typeName + ".schema.json"
	}

    def toType(ExpandedAttribute attribute) {
		if (!attribute.hasMetas)
			JsonSchemaTranslator.toJsonSchemaType(attribute.type)
		else if (attribute.refIndex >= 0)
			attribute.type.toReferenceWithMetaTypeName
		else
			attribute.type.toFieldWithMetaTypeName
	}

	def toReferenceWithMetaTypeName(ExpandedType type) {
		'''ReferenceWithMeta«type.toMetaTypeName»'''
	}

	def toFieldWithMetaTypeName(ExpandedType type) {
		'''FieldWithMeta«type.toMetaTypeName»'''
	}

	static def toMetaTypeName(ExpandedType type) {
		val name = JsonSchemaTranslator.toJsonSchemaType(type)

		if (type.enumeration) {
			return name
		} else if (name.contains(".")) {
			return name.substring(name.lastIndexOf(".") + 1).toFirstUpper
		}

		return name.toFirstUpper
	}

}