package com.regnosys.rosetta.generator.jsonschema

import com.regnosys.rosetta.generator.object.ExpandedAttribute

import com.regnosys.rosetta.generator.object.ExpandedType
import static extension com.regnosys.rosetta.generator.jsonschema.JsonSchemaTranslator.toJsonSchemaType

class JsonSchemaModelObjectBoilerPlate {
		
	def toAttributeName(ExpandedAttribute attribute) {
		if (attribute.name == "val")
			'''_val'''
		else
			attribute.name.toFirstLower
	}
	
	def replaceTabsWithSpaces(CharSequence code) {
		code.toString.replace('\t', '  ')
	}
	
	def toEnumAnnotationType(ExpandedType type) {
		'''«type.name»'''
	}
	
	def toType(ExpandedAttribute attribute) {
		if (attribute.multiple)
			'''List[«attribute.toRawType»]'''
		else if (attribute.singleOptional)
			'''Option[«attribute.toRawType»]'''
		else
			'''«attribute.toRawType»'''
	}
	
	private def toRawType(ExpandedAttribute attribute) {
		if (!attribute.hasMetas) 
			attribute.type.toJsonSchemaType
		else if (attribute.refIndex >= 0) {
			if (attribute.type.isType)
				attribute.type.toReferenceWithMetaTypeName
			else 
				attribute.type.toBasicReferenceWithMetaTypeName
		}
		else 
			attribute.type.toFieldWithMetaTypeName
	}
	
	def toReferenceWithMetaTypeName(ExpandedType type) {
		'''ReferenceWithMeta«type.toMetaTypeName»'''
	}
	
	def toBasicReferenceWithMetaTypeName(ExpandedType type) {
		'''BasicReferenceWithMeta«type.toMetaTypeName»'''
	}
	
	def toFieldWithMetaTypeName(ExpandedType type) {
		'''FieldWithMeta«type.toMetaTypeName»'''
	}
	
	static def toMetaTypeName(ExpandedType type) {
		val name = type.toJsonSchemaType
		
		if (type.enumeration) {
			// Enums have json types in the form "FooEnum.Value".
			// For the meta type name we just need "FooEnum"
			return name.substring(0, name.lastIndexOf(".")).toFirstUpper
		} else if (name.contains(".")) {
			// Remove any packages from basic types e.g. json.math.BigDecimal
			return name.substring(name.lastIndexOf(".") + 1).toFirstUpper
		}
		
		return name.toFirstUpper
	}
}
