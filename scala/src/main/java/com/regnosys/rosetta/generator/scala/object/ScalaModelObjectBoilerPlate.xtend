package com.regnosys.rosetta.generator.scala.object

import com.regnosys.rosetta.generator.object.ExpandedAttribute

import static extension com.regnosys.rosetta.generator.scala.util.ScalaTranslator.toScalaType
import com.regnosys.rosetta.generator.object.ExpandedType

class ScalaModelObjectBoilerPlate {
		
	def toAttributeName(ExpandedAttribute attribute) {
		if (attribute.name == "val")
			'''_val'''
		else if (attribute.name == "object")
			'''_object'''
		else if (attribute.name == "return")
			'''_return'''
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
			attribute.type.toScalaType
		else if (attribute.refIndex >= 0) {
				attribute.type.toReferenceWithMetaTypeName
		}
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
		val name = type.toScalaType
		
		if (type.enumeration) {
			// Enums have scala types in the form "FooEnum.Value".  
			// For the meta type name we just need "FooEnum"
			return name.substring(0, name.lastIndexOf(".")).toFirstUpper
		} else if (name.contains(".")) {
			// Remove any packages from basic types e.g. scala.math.BigDecimal
			return name.substring(name.lastIndexOf(".") + 1).toFirstUpper
		}
		
		return name.toFirstUpper
	}
}
