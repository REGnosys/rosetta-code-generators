package com.regnosys.rosetta.generator.golang.object

import com.regnosys.rosetta.rosetta.RosettaMetaType

import static com.regnosys.rosetta.generator.golang.util.GolangModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.util.Util.*
import static extension com.regnosys.rosetta.generator.golang.util.GolangTranslator.toGOType

class GolangMetaFieldGenerator {
	
	def generateMetaFields(Iterable<RosettaMetaType> metaTypes, String version) {
		fileComment(version) + metaClasses.toString + metaFields(metaTypes.filter[name!="key" && name!="id" && name!="reference" && name!="template" && name!="address"], version)
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
		  Address Address;
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
			Location []Location;
		}
		
		type MetaAndTemplateFields struct {
			«FOR type : types.distinctBy(t|t.name.toFirstLower)»
				«type.name.toFirstUpper» «type.type.name.toGOType»;
			«ENDFOR»
			GlobalKey string;
			ExternalKey string;
			TemplateGlobalReference string;
			Location []Location;
		}
		
		type Address struct {
			Scope string;
			Value string;
		}
		
		type Location struct {
			Scope string;
			Value string;
		}
		
	'''
}
