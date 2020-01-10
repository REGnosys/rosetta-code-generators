package com.regnosys.rosetta.generator.scala.object

import com.regnosys.rosetta.generator.object.ExpandedAttribute

import static extension com.regnosys.rosetta.generator.scala.util.ScalaTranslator.toScalaType
import com.regnosys.rosetta.generator.object.ExpandedType

class ScalaModelObjectBoilerPlate {
		
	def toAttributeName(ExpandedAttribute attribute) {
		if (attribute.name == "type")
			'''_type'''
		else
			attribute.name.toFirstLower
	}
	
	def replaceTabsWithSpaces(CharSequence code) {
		code.toString.replace('\t', '  ')
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
			if (attribute.type.isType)
				attribute.type.toReferenceWithMetaTypeName
			else 
				attribute.type.toBasicReferenceWithMetaTypeName
		}
		else 
			attribute.type.toFieldWithMetaTypeName
	}
	
	private def toReferenceWithMetaTypeName(ExpandedType type) {
		'''ReferenceWithMeta[«type.toScalaType»]'''
	}
	
	private def toBasicReferenceWithMetaTypeName(ExpandedType type) {
		'''ReferenceWithMeta[«type.toScalaType»]'''
	}
	
	private def toFieldWithMetaTypeName(ExpandedType type) {
		'''FieldWithMeta[«type.toScalaType»]'''
	}
}
