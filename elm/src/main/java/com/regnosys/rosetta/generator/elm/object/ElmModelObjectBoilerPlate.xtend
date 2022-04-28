package com.regnosys.rosetta.generator.elm.object

import com.regnosys.rosetta.generator.object.ExpandedAttribute

import static extension com.regnosys.rosetta.generator.elm.util.ElmTranslator.toElmType
import com.regnosys.rosetta.rosetta.simple.Attribute

class ElmModelObjectBoilerPlate {
		
	def toAttributeName(Attribute attribute) {
			attribute.name
	}
	
	def replaceTabsWithSpaces(CharSequence code) {
		code.toString.replace('\t', '  ')
	}
	
	def toType(Attribute attribute) 
		'''«IF attribute.card.isMany»List «ELSEIF attribute.card.optional»Maybe «ENDIF»«IF attribute.card.inf == 0»«ENDIF»«attribute.toRawType»'''
	
	private def toRawType(Attribute attribute) {
			attribute.type.name.toElmType

	}
	
		
}
