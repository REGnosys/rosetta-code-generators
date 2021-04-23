package com.regnosys.rosetta.generator.daml.object

import com.regnosys.rosetta.rosetta.RosettaMetaType

import static com.regnosys.rosetta.generator.daml.util.DamlModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.daml.util.DamlTranslator.toDamlType
import static extension com.regnosys.rosetta.generator.util.Util.*

class DamlMetaFieldGenerator {
	
	def generateMetaFields(Iterable<RosettaMetaType> metaTypes, String version) {
		metaFields(metaTypes.filter[name!="key" && name!="id" && name!="reference" && name!="template" && name!="address"], version)
	}
	
	def metaFields(Iterable<RosettaMetaType> types, String version) '''
		daml 1.2
		
		«fileComment(version)»
		module Org.Isda.Cdm.MetaFields
		  ( module Org.Isda.Cdm.MetaFields ) where
		
		data MetaFields = MetaFields with
		  «FOR type : types.distinctBy(t|t.name.toFirstLower)»
		      «type.name.toFirstLower» : Optional «type.type.name.toDamlType»
		  «ENDFOR»
		  globalKey : Optional Text
		  externalKey : Optional Text
		  location: [Location]
		    deriving (Eq, Ord, Show)
		
		data MetaAndTemplateFields = MetaAndTemplateFields with
		  «FOR type : types.distinctBy(t|t.name.toFirstLower)»
		      «type.name.toFirstLower» : Optional «type.type.name.toDamlType»
		  «ENDFOR»
		  globalKey : Optional Text
		  externalKey : Optional Text
		  templateGlobalReference : Optional Text
		  location: [Location]
		    deriving (Eq, Ord, Show)
		
		data Location = Location with
		  scope : Optional Text
		  value : Optional Text
		    deriving (Eq, Ord, Show)
		
		data Address = Address with
		  scope : Optional Text
		  value : Optional Text
		    deriving (Eq, Ord, Show)
	'''
}
