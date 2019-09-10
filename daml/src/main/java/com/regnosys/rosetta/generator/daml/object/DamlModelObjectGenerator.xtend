package com.regnosys.rosetta.generator.daml.object

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.rosetta.RosettaClass
import com.regnosys.rosetta.rosetta.RosettaMetaType
import java.util.List

import static com.regnosys.rosetta.generator.daml.util.DamlModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*
import java.util.Map
import java.util.HashMap
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.RosettaType
import com.regnosys.rosetta.generator.object.ExpandedAttribute

class DamlModelObjectGenerator {

	@Inject extension RosettaExtensions
	@Inject extension DamlModelObjectBoilerPlate
	@Inject extension DamlMetaFieldGenerator
	
	static final String CLASSES_FILENAME = 'Org/Isda/Cdm/Classes.daml'
	static final String META_FIELDS_FILENAME = 'Org/Isda/Cdm/MetaFields.daml'
	static final String META_CLASSES_FILENAME = 'Org/Isda/Cdm/MetaClasses.daml'
	static final String ZONE_DATTTIME_FILENAME = 'Org/Isda/Cdm/ZonedDateTime.daml'
	
	def Map<String, ? extends CharSequence> generate(Iterable<? extends RosettaType> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version) {
		val result = new HashMap
		val classes = rosettaClasses.sortBy[name].generateClasses(version).replaceTabsWithSpaces
		result.put(CLASSES_FILENAME, classes)
		val metaFields = generateMetaFields(metaTypes, version).replaceTabsWithSpaces
		result.put(META_FIELDS_FILENAME, metaFields)
		result.put(META_CLASSES_FILENAME, metaClasses)
		result.put(ZONE_DATTTIME_FILENAME, zonedDateTime)
		result;
	}

	/**
	 * DAML requires:
	 * - tabs not spaces
	 * - keyword "deriving" should in indented as additional 2 spaces
	 * - class name and folders in title case
	 * - must contain "import Prelude hiding (...)" line to avoid name clashes with DAML keywords
	 * - nullable fields must be declared with the keyword "Optional"
	 */
	private def generateClasses(List<? extends RosettaType> rosettaClasses, String version) {
	'''
		daml 1.2
		
		«fileComment(version)»
		module Org.Isda.Cdm.Classes
		  ( module Org.Isda.Cdm.Classes ) where
		
		import Org.Isda.Cdm.Enums
		import Org.Isda.Cdm.ZonedDateTime
		import Org.Isda.Cdm.MetaClasses
		import Org.Isda.Cdm.MetaFields
		import Prelude hiding (Party, exercise, id, product, agreement)
		
		«FOR c : rosettaClasses»
			«classComment(c.definition)»
			data «c.name» = «c.name» with 
			  «FOR attribute : c.allExpandedAttributes»
			      «attribute.toAttributeName» : «attribute.toType»
			        «methodComment(attribute.definition)»
			  «ENDFOR»
			    deriving (Eq, Ord, Show)
			
		«ENDFOR»
	'''}
	
	
	def dispatch Iterable<ExpandedAttribute> allExpandedAttributes(RosettaClass type) {
		type.allSuperTypes.expandedAttributes
	}
	
	def dispatch Iterable<ExpandedAttribute> allExpandedAttributes(Data type){
		type.allSuperTypes.map[it.expandedAttributes].flatten
	}
	
	def dispatch String definition(RosettaClass element) {
		element.definition
	}
	def dispatch String definition(Data element){
		element.definition
	}
	
	private def metaClasses() '''
		daml 1.2
		
		-- | This file is auto-generated from the ISDA Common
		--   Domain Model, do not edit.
		--   @version ${project.version}
		module Org.Isda.Cdm.MetaClasses
		  ( module Org.Isda.Cdm.MetaClasses ) where
		
		import Org.Isda.Cdm.MetaFields
		
		data ReferenceWithMeta a = ReferenceWithMeta with
		  globalReference : Optional Text
		  externalReference : Optional Text
		  value : Optional a
		  meta : Optional MetaFields
		    deriving (Eq, Ord, Show)
		
		data BasicReferenceWithMeta a = BasicReferenceWithMeta with
		  globalReference : Optional Text
		  externalReference : Optional Text
		  value : Optional a
		  meta : Optional MetaFields
		    deriving (Eq, Ord, Show)
		
		data FieldWithMeta a = FieldWithMeta with
		  value : a
		  meta : Optional MetaFields
		    deriving (Eq, Ord, Show)
			
	'''
	
	private def zonedDateTime() '''
		daml 1.2
		
		-- | This file is auto-generated from the ISDA Common
		--   Domain Model, do not edit.
		--   @version ${project.version}
		module Org.Isda.Cdm.ZonedDateTime
		  ( module Org.Isda.Cdm.ZonedDateTime ) where
		
		data ZonedDateTime = ZonedDateTime with
		  dateTime : Time
		  timezone : Text
		    deriving (Eq, Ord, Show)
	'''
	
}
