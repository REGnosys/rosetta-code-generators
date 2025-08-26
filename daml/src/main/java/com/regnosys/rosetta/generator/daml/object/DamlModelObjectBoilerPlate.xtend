package com.regnosys.rosetta.generator.daml.object

import com.regnosys.rosetta.types.RAttribute
import com.regnosys.rosetta.types.RMetaAttribute

import static extension com.regnosys.rosetta.generator.daml.util.DamlTranslator.*

class DamlModelObjectBoilerPlate {
		
	def toAttributeName(RAttribute rAttr) {
		if (rAttr.name == "type")
			'''_type'''
		else
			rAttr.name.toFirstLower
	}
	
	def toAttributeName(RMetaAttribute rMetaAttr) {
		if (rMetaAttr.name == "type")
			'''_type'''
		else
			rMetaAttr.name.toFirstLower
	}
	
	def replaceTabsWithSpaces(CharSequence code) {
		code.toString.replace('\t', '  ')
	}
	
	def toType(RAttribute rAttr) {
		if (rAttr.isMulti) 
			'''[«rAttr.toRawType»]'''
		else
			rAttr.toRawType
				.wrapSingleMetaInBrackets(rAttr)
				.prefixSingleOptional(rAttr)
	}
	
	def toType(RMetaAttribute rMetaAttr) {
		rMetaAttr.RType.toDamlType
	}
	
	private def toRawType(RAttribute rAttr) {
		val rMetaAnnotatedType = rAttr.RMetaAnnotatedType
		if (!rMetaAnnotatedType.hasMeta) 
			rAttr.RMetaAnnotatedType.RType.toDamlType
		else if (rMetaAnnotatedType.hasMetaAttribute("reference") || rMetaAnnotatedType.hasMetaAttribute("address")) {
			'''ReferenceWithMeta «rMetaAnnotatedType.RType.toDamlType»'''
		}
		else 
			'''FieldWithMeta «rMetaAnnotatedType.RType.toDamlType»'''
	}
	
	private def prefixSingleOptional(CharSequence type, RAttribute rAttr) {
		val card = rAttr.cardinality
		if (!card.multi && card.isOptional)
			'''Optional «type»'''
		else
			type
	}
	
	private def wrapSingleMetaInBrackets(CharSequence type, RAttribute rAttr) {
		if (rAttr.RMetaAnnotatedType.hasMeta) 
			'''(«type»)'''
		else
			type
	}
}
