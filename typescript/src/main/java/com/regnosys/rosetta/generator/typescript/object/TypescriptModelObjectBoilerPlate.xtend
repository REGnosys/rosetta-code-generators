package com.regnosys.rosetta.generator.typescript.object

import com.regnosys.rosetta.generator.object.ExpandedAttribute

import static extension com.regnosys.rosetta.generator.typescript.util.TypescriptTranslator.toTSType

class TypescriptModelObjectBoilerPlate {
		
	def toAttributeName(ExpandedAttribute attribute) {
		if (attribute.name == "type")
			'''_type'''
		else
			attribute.name.toFirstLower
	}
	
	def replaceTabsWithSpaces(CharSequence code) {
		code.toString.replace('\t', '  ')
	}
	
	def toType(ExpandedAttribute attribute) 
		'''«attribute.toRawType»«IF attribute.isMultiple»[]«ENDIF»'''
	
	private def toRawType(ExpandedAttribute attribute) {
		if (!attribute.hasMetas) 
			attribute.type.name.toTSType
		else if (attribute.refIndex >= 0) {
			if (attribute.type.isType)
				attribute.type.name.toReferenceWithMetaTypeName
			else 
				attribute.type.name.toBasicReferenceWithMetaTypeName
		}
		else 
			attribute.type.name.toFieldWithMetaTypeName
	}
	
	private def toReferenceWithMetaTypeName(String type) {
		'''ReferenceWithMeta<«type.toTSType.toFirstUpper»>'''
	}
	
	private def toBasicReferenceWithMetaTypeName(String type) {
		'''ReferenceWithMeta<«type.toTSType.toFirstUpper»>'''
	}
	
	private def toFieldWithMetaTypeName(String type) {
		'''FieldWithMeta<«type.toTSType.toFirstUpper»>'''
	}
}
