package com.regnosys.rosetta.generator.golang.object

import com.regnosys.rosetta.generator.object.ExpandedAttribute

import static extension com.regnosys.rosetta.generator.golang.util.GolangTranslator.toGOType

class GolangModelObjectBoilerPlate {
		
	def toAttributeName(ExpandedAttribute attribute) {
		if (attribute.name == "type")
			'''_type'''
		else
			attribute.name.toFirstUpper
	}
	
	def replaceTabsWithSpaces(CharSequence code) {
		code.toString.replace('\t', '  ')
	}
	
	def toType(ExpandedAttribute attribute) 
		'''«IF attribute.isMultiple»[]«ENDIF»«attribute.toRawType»'''
	
	private def toRawType(ExpandedAttribute attribute) {
		if (!attribute.hasMetas) 
			attribute.type.name.toGOType
		else if (attribute.refIndex >= 0) {
			if (attribute.type.isType)
				attribute.type.name.toReferenceWithMetaTypeName
			else 
				attribute.type.name.toBasicReferenceWithMetaTypeName
		}
		else 
			attribute.type.name.toFieldWithMetaTypeName
	}
	
	//DB: since there are no generics in Go, for now, just ignore those 
	
//	private def toReferenceWithMetaTypeName(String type) {
//		'''ReferenceWithMeta<«type.toGOType.toFirstUpper»>'''
//	}
//	
//	private def toBasicReferenceWithMetaTypeName(String type) {
//		'''ReferenceWithMeta<«type.toGOType.toFirstUpper»>'''
//	}
//	
//	private def toFieldWithMetaTypeName(String type) {
//		'''FieldWithMeta<«type.toGOType.toFirstUpper»>'''
//	}
	
	private def toReferenceWithMetaTypeName(String type) {
		'''ReferenceWithMeta'''
	}
	
	private def toBasicReferenceWithMetaTypeName(String type) {
		'''ReferenceWithMeta'''
	}
	
	private def toFieldWithMetaTypeName(String type) {
		'''FieldWithMeta'''
	}
}
