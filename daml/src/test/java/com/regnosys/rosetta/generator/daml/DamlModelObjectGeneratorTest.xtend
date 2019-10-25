package com.regnosys.rosetta.generator.daml

import com.google.inject.Inject
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*
import com.regnosys.rosetta.tests.util.ModelHelper
import com.regnosys.rosetta.rosetta.RosettaModel

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class DamlModelObjectGeneratorTest {

	@Inject extension ModelHelper
	@Inject DamlCodeGenerator generator;
	

	@Test
	def void shouldGenerateClassWithImports() {
		val daml = '''
			type Foo:
			    stringAttr string (0..1)
		'''.generateDaml
		
		val classes = daml.get("Org/Isda/Cdm/Classes.daml").toString
		
		assertTrue(classes.contains('''import Org.Isda.Cdm.Enums'''))
		assertTrue(classes.contains('''import Org.Isda.Cdm.ZonedDateTime'''))
		assertTrue(classes.contains('''import Org.Isda.Cdm.MetaClasses'''))
		assertTrue(classes.contains('''import Prelude hiding (Party, exercise, id, product, agreement)'''))
	}

	@Test
	def void shouldGenerateClassWithBasicTypes() {
		val classes = '''
			type Foo:
			    stringAttr string (1..1)
			    intAttr int (1..1)
			    numberAttr number (1..1)
			    booleanAttr boolean (1..1)
			    dateAttr date (1..1)
			    timeAttr time (1..1)
				zonedDateTimeAttr zonedDateTime (1..1)
		'''.generateDaml.get("Org/Isda/Cdm/Classes.daml").toString

		assertTrue(classes.contains('''
		data Foo = Foo with 
		  booleanAttr : Bool
		  dateAttr : Date
		  intAttr : Int
		  numberAttr : Decimal
		  stringAttr : Text
		  timeAttr : Text
		  zonedDateTimeAttr : ZonedDateTime
		    deriving (Eq, Ord, Show)'''))
	}

	@Test
	def void shouldGenerateClassWithOptionalBasicType() {
		val classes = '''
			type Foo:
			    stringAttr string (0..1)
		'''.generateDaml.get("Org/Isda/Cdm/Classes.daml").toString
		
		assertTrue(classes.contains('''
		data Foo = Foo with 
		  stringAttr : Optional Text
		    deriving (Eq, Ord, Show)'''))
	}

	@Test
	def void shouldGenerateClassWithComments() {
		val classes = '''
			type Foo: <"This is the class comment which should wrap if the line is long enough.">
			    stringAttr string (0..1) <"This is the attribute comment which should also wrap if long enough">
		'''.generateDaml.get("Org/Isda/Cdm/Classes.daml").toString
		
		assertTrue(classes.contains('''
		-- | This is the class comment which should wrap if the
		--   line is long enough.
		data Foo = Foo with 
		  stringAttr : Optional Text
		    -- ^ This is the attribute comment which should also wrap
		    --   if long enough
		    deriving (Eq, Ord, Show)'''))
	}

	@Test
	def void shouldGenerateClassWithBasicTypeList() {
		val classes = '''
			type Foo:
			    stringAttrs string (0..*)
		'''.generateDaml.get("Org/Isda/Cdm/Classes.daml").toString
		
		assertTrue(classes.contains('''
		data Foo = Foo with 
		  stringAttrs : [Text]
		    deriving (Eq, Ord, Show)'''))
	}
	
	@Test
	def void shouldGenerateClassWithBasicTypeAndMetaFieldScheme() {
		val code = '''
			metaType scheme string
			
			type Foo:
			    stringAttr string (1..1)
			    [metadata scheme]
		'''.generateDaml
		
		val classes = code.get("Org/Isda/Cdm/Classes.daml").toString
		
		assertTrue(classes.contains('''
		data Foo = Foo with 
		  stringAttr : (FieldWithMeta Text)
		    deriving (Eq, Ord, Show)'''))

		val metaFields = code.get("Org/Isda/Cdm/MetaFields.daml").toString
		
		assertTrue(metaFields.contains('''
		daml 1.2
		
		-- | This file is auto-generated from the ISDA Common
		--   Domain Model, do not edit.
		--   @version test
		module Org.Isda.Cdm.MetaFields
		  ( module Org.Isda.Cdm.MetaFields ) where
		
		data MetaFields = MetaFields with
		  scheme : Optional Text
		  globalKey : Optional Text
		  externalKey : Optional Text
		    deriving (Eq, Ord, Show)'''))
	}
	
	@Test
	def void shouldGenerateClassWithOptionalRosettaType() {
		val classes = '''
			type Foo:
			    barAttr Bar (0..1)
			
			type Bar:
			    stringAttr string (1..1)
		'''.generateDaml.get("Org/Isda/Cdm/Classes.daml").toString
		
		assertTrue(classes.contains('''
		data Foo = Foo with 
		  barAttr : Optional Bar
		    deriving (Eq, Ord, Show)'''))
	}
	
	@Test
	def void shouldGenerateClassWithRosettaTypeAndMetaReference() {
		val code = '''
			metaType reference string
			
			type Foo:
			    barReference Bar (0..1)
			    [metadata reference]
			
			type Bar:
			    [metadata key]
			    stringAttr string (1..1)
		'''.generateDaml
		
		val classes = code.get("Org/Isda/Cdm/Classes.daml").toString
		
		assertTrue(classes.contains('''
		data Bar = Bar with 
		  meta : Optional MetaFields
		  stringAttr : Text
		    deriving (Eq, Ord, Show)'''))

		assertTrue(classes.contains('''
		data Foo = Foo with 
		  barReference : Optional (ReferenceWithMeta Bar)
		    deriving (Eq, Ord, Show)'''))

		val metaFields = code.get("Org/Isda/Cdm/MetaFields.daml").toString
		
		assertTrue(metaFields.contains('''
		daml 1.2
		
		-- | This file is auto-generated from the ISDA Common
		--   Domain Model, do not edit.
		--   @version test
		module Org.Isda.Cdm.MetaFields
		  ( module Org.Isda.Cdm.MetaFields ) where
		
		data MetaFields = MetaFields with
		  reference : Optional Text
		  globalKey : Optional Text
		  externalKey : Optional Text
		    deriving (Eq, Ord, Show)'''))
	}
	
	@Test
	def void shouldGenerateClassWithRosettaTypeAndMetaBasicReference() {
		val code = '''
			metaType reference string
			
			type Foo:
			    stringReference string (0..1)
			    [metadata reference]
		'''.generateDaml
		
		val classes = code.get("Org/Isda/Cdm/Classes.daml").toString
		
		assertTrue(classes.contains('''
		data Foo = Foo with 
		  stringReference : Optional (BasicReferenceWithMeta Text)
		    deriving (Eq, Ord, Show)'''))

		val metaFields = code.get("Org/Isda/Cdm/MetaFields.daml").toString
		
		// println(metaFields)
		
		assertTrue(metaFields.contains('''
		daml 1.2
		
		-- | This file is auto-generated from the ISDA Common
		--   Domain Model, do not edit.
		--   @version test
		module Org.Isda.Cdm.MetaFields
		  ( module Org.Isda.Cdm.MetaFields ) where
		
		data MetaFields = MetaFields with
		  reference : Optional Text
		  globalKey : Optional Text
		  externalKey : Optional Text
		    deriving (Eq, Ord, Show)'''))
	}
	
	
	
	def generateDaml(CharSequence model) {
		val eResource = model.parseRosettaWithNoErrors.eResource
		
		generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
	}
}
