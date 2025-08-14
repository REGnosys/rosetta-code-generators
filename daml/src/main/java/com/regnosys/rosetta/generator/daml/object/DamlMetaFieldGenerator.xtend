package com.regnosys.rosetta.generator.daml.object

import com.regnosys.rosetta.rosetta.RosettaMetaType

import static com.regnosys.rosetta.generator.daml.util.DamlModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.daml.util.DamlTranslator.toDamlType
import static extension com.regnosys.rosetta.generator.util.IterableUtil.*

class DamlMetaFieldGenerator {
	
	def generateMetaFields(Iterable<RosettaMetaType> metaTypes, String namespace, String version) {
		metaFields(metaTypes.filter[name!="key" && name!="id" && name!="reference" && name!="template" && name!="address" && name != "location"], namespace, version)
	}
	
	def metaFields(Iterable<RosettaMetaType> types, String namespace, String version) '''
		daml 1.2
		
		«fileComment(version)»
		module Org.Isda.«namespace».MetaFields
		  ( module Org.Isda.«namespace».MetaFields ) where
		
		data MetaFields = MetaFields with
		  «FOR type : types.distinctBy(t|t.name.toFirstLower)»
		      «type.name.toFirstLower» : Optional «type.typeCall.type.name.toDamlType»
		  «ENDFOR»
		  globalKey : Optional Text
		  externalKey : Optional Text
		  location: [Key]
		    deriving (Eq, Ord, Show)
		
		data MetaAndTemplateFields = MetaAndTemplateFields with
		  «FOR type : types.distinctBy(t|t.name.toFirstLower)»
		      «type.name.toFirstLower» : Optional «type.typeCall.type.name.toDamlType»
		  «ENDFOR»
		  globalKey : Optional Text
		  externalKey : Optional Text
		  templateGlobalReference : Optional Text
		  location: [Key]
		    deriving (Eq, Ord, Show)
		
		data Key = Key with
		  scope : Optional Text
		  value : Optional Text
		    deriving (Eq, Ord, Show)
		
		data Reference = Reference with
		  scope : Optional Text
		  value : Optional Text
		    deriving (Eq, Ord, Show)
		
	'''
}
