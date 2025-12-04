package com.regnosys.rosetta.generator.scala.object

import com.regnosys.rosetta.types.RType
import com.regnosys.rosetta.types.RAttribute
import jakarta.inject.Inject
import com.regnosys.rosetta.types.REnumType
import com.regnosys.rosetta.generator.scala.util.ScalaTranslator

class ScalaModelObjectBoilerPlate {
	@Inject
	extension ScalaTranslator
		
	def toAttributeName(RAttribute attribute) {
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
	
	def toEnumAnnotationType(RType type) {
		'''«type.name»'''
	}
	
	def toType(RAttribute rawAttribute) {
		val attribute = rawAttribute.originalAttribute
		if (attribute.multi)
			'''List[«attribute.toRawType»]'''
		else if (attribute.cardinality.optional)
			'''Option[«attribute.toRawType»]'''
		else
			'''«attribute.toRawType»'''
	}
	private def originalAttribute(RAttribute attribute) {
		var current = attribute
		while (current.parentAttribute !== null) {
			current = current.parentAttribute
		}
		return current
	}
	
	private def toRawType(RAttribute attribute) {
		val t = attribute.RMetaAnnotatedType
		if (!t.hasAttributeMeta) 
			t.RType.toScalaType
		else if (t.hasMetaAttribute("reference") || t.hasMetaAttribute("address")) {
				t.RType.toReferenceWithMetaTypeName
		}
		else 
			t.RType.toFieldWithMetaTypeName
	}
	
	def toReferenceWithMetaTypeName(RType type) {
		'''ReferenceWithMeta«type.toMetaTypeName»'''
	}
	
	def toFieldWithMetaTypeName(RType type) {
		'''FieldWithMeta«type.toMetaTypeName»'''
	}
	
	def toMetaTypeName(RType rawType) {
		val type = rawType.stripFromTypeAliasesExceptInt
		val name = type.toScalaType
		
		if (type instanceof REnumType) {
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
