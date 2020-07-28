package com.regnosys.rosetta.generator.golang.object

import com.regnosys.rosetta.rosetta.RosettaMetaType

import static com.regnosys.rosetta.generator.golang.util.GolangModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.util.Util.*
import static extension com.regnosys.rosetta.generator.golang.util.GolangTranslator.toGOType

class GolangMetaFieldGenerator {
	
	def generateMetaFields(Iterable<RosettaMetaType> metaTypes, String version) {
		fileComment(version) + metaClasses.toString + metaFields(metaTypes.filter[name !== "reference"], version)
	}
	
		private def metaClasses() '''
		package org_isda_cdm_metafields
		
		type FieldWithMeta struct {
		  Value interface{};
		  Meta MetaFields;
		}

		type ReferenceWithMeta struct {
		  GlobalReference string;
		  ExternalReference string;
		  Value interface{};
		}
				
	'''
	
	def metaFields(Iterable<RosettaMetaType> types, String version) '''				
		type MetaFields struct {
			«FOR type : types.distinctBy(t|t.name.toFirstLower)»
				«type.name.toFirstUpper» «type.type.name.toGOType»;
			«ENDFOR»
			GlobalKey string;
			ExternalKey string;
		}
		
	'''
}
