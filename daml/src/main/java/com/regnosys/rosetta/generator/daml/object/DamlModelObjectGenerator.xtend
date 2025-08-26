package com.regnosys.rosetta.generator.daml.object

import com.google.inject.Inject
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.types.RObjectFactory
import java.util.HashMap
import java.util.List
import java.util.Map

import static com.regnosys.rosetta.generator.daml.util.DamlModelGeneratorUtil.*

class DamlModelObjectGenerator {

	@Inject RObjectFactory rObjectFactory
	@Inject extension DamlModelObjectBoilerPlate
	@Inject extension DamlMetaFieldGenerator
	
	def Map<String, ? extends CharSequence> generate(Iterable<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version) {
		val classesByNamespace = rosettaClasses.groupBy[model.name.split("\\.").first]
		
		val result = new HashMap
		classesByNamespace.forEach[k,v|
			val namespace = k.toFirstUpper
			val class = v.sortBy[name].generateClasses(namespace, version).replaceTabsWithSpaces
			result.put('''Org/Isda/«namespace»/Classes.daml''', class)
		]
		
		val metaFields = generateMetaFields(metaTypes, version).replaceTabsWithSpaces
		result.put('''Com/Regnosys/Meta/MetaFields.daml''', metaFields)
		result.put('''Com/Regnosys/Meta/MetaClasses.daml''', metaClasses)
		result.put('''Com/Regnosys/Meta/ZonedDateTime.daml''', zonedDateTime)
		result.put('''Com/Regnosys/Meta/DateTime.daml''', dateTime)
		
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
	private def generateClasses(List<Data> rosettaClasses, String namespace, String version) {
	'''
		daml 1.2
		
		«fileComment(version)»
		module Org.Isda.«namespace».Classes
		  ( module Org.Isda.«namespace».Classes ) where
		
		import Org.Isda.«namespace».Enums
		import Com.Regnosys.Meta.ZonedDateTime
		import Com.Regnosys.Meta.DateTime
		import Com.Regnosys.Meta.MetaClasses hiding (Reference)
		import Com.Regnosys.Meta.MetaFields
		import Prelude hiding (Party, exercise, id, product, agreement, ContractId)
		
		«FOR c : rosettaClasses»
			«val rType = rObjectFactory.buildRDataType(c)»
			«classComment(c.definition)»
			data «handleUnderscoreNames(c.name)» = «handleUnderscoreNames(c.name)» with 
			  «FOR rAttr : rType.allAttributes»
			      «rAttr.toAttributeName» : «rAttr.toType»
			        «methodComment(rAttr.definition)»
			  «ENDFOR»
			  «IF !rType.metaAttributes.empty»
			    meta : Optional MetaFields
  			  «ENDIF»
			    deriving (Eq, Ord, Show)
			
		«ENDFOR»
	'''}
	
	private def handleUnderscoreNames(String name) {
		if (name.startsWith("_")) {
			return name.substring(1) + "_"
		}
		return name
	}
	
	private def metaClasses() '''
		daml 1.2
		
		-- | This file is auto-generated from the ISDA Common
		--   Domain Model, do not edit.
		--   @version ${project.version}
		module Com.Regnosys.Meta.MetaClasses
		  ( module Com.Regnosys.Meta.MetaClasses ) where
		
		import Com.Regnosys.Meta.MetaFields
		
		data ReferenceWithMeta a = ReferenceWithMeta with
		  globalReference : Optional Text
		  externalReference : Optional Text
		  address: Optional Reference
		  value : Optional a
		    deriving (Eq, Ord, Show)
		
		data FieldWithMeta a = FieldWithMeta with
		  value : a
		  meta : Optional MetaFields
		    deriving (Eq, Ord, Show)
		
		data Reference = Reference with
		  scope : Optional Text
		  value : Optional Text
		    deriving (Eq, Ord, Show)
		
	'''
	
	private def zonedDateTime() '''
		daml 1.2
		
		-- | This file is auto-generated from the ISDA Common
		--   Domain Model, do not edit.
		--   @version ${project.version}
		module Com.Regnosys.Meta.ZonedDateTime
		  ( module Com.Regnosys.Meta.ZonedDateTime ) where
		
		data ZonedDateTime = ZonedDateTime with
		  dateTime : Time
		  timezone : Text
		    deriving (Eq, Ord, Show)
	'''

	
	private def dateTime() '''
		daml 1.2
		
		-- | This file is auto-generated from the ISDA Common
		--   Domain Model, do not edit.
		--   @version ${project.version}
		module Com.Regnosys.Meta.DateTime
		  ( module Com.Regnosys.Meta.DateTime ) where
		
		data DateTime = DateTime with
		  dateTime : Time
		  timezone : Text
		    deriving (Eq, Ord, Show)
	'''
}
