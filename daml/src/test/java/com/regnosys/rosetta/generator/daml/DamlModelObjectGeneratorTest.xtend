package com.regnosys.rosetta.generator.daml

import com.google.inject.Inject
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*
import com.regnosys.rosetta.tests.util.ModelHelper

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class DamlModelObjectGeneratorTest {

	@Inject extension ModelHelper
	@Inject DamlCodeGenerator generator;
	
	@Test
	def void shouldGenerateFunctions() {
		val classes = '''
			namespace cdm.test
			
			func Foo:
				inputs:
					fooIn string (1..1)
				output:
					fooOut string (1..1)
					
			set fooOut: fooIn
		'''.generateDaml
		
		val fileContent = classes.get("Org/Isda/Cdm/Test/Functions.daml").toString		
		
		assertEquals('''
		daml 1.2
		
		-- | This file is auto-generated from the ISDA Common
		--   Domain Model, do not edit.
		--   @version test
		module Org.Isda.Cdm.Test.Functions
		  ( module Org.Isda.Cdm.Test.Functions ) where
		
		import Org.Isda.Cdm.Test.Classes
		import Org.Isda.Cdm.Test.Enums
		import Org.Isda.Cdm.Test.ZonedDateTime
		import Org.Isda.Cdm.Test.MetaClasses
		import Org.Isda.Cdm.Test.MetaFields
		import Prelude hiding (Party, exercise, id, product, agreement)
		
		-- | Function argument object definition for Foo
		data FooSpec = FooSpec with
		  fooIn : Text
		    deriving (Eq, Ord, Show)
		
		-- | Function definition for Foo
		fooFunc : (FooSpec -> Text) -> FooSpec -> Text
		fooFunc impl spec = impl spec
		
		'''.toString, fileContent)	
	}
	
	@Test
	def void shouldGenerateEnum() {
		val classes = '''
			namespace cdm.test
			
			enum FooEnum:
			    A
			    B
			    C
		'''.generateDaml
		
		val fileContent = classes.get("Org/Isda/Cdm/Test/Enums.daml").toString

		assertEquals('''
			daml 1.2
			
			-- | This file is auto-generated from the ISDA Common
			--   Domain Model, do not edit.
			--   @version test
			module Org.Isda.Cdm.Test.Enums
			  ( module Org.Isda.Cdm.Test.Enums ) where
			
			data FooEnum 
			  = FooEnum_A
			  | FooEnum_B
			  | FooEnum_C
			    deriving (Eq, Ord, Show)
			
	    '''.toString, fileContent)		
	}

	@Test
	def void shouldGenerateClassWithDifferentNamespace() {
		val classes = '''
			namespace other.test
			
			type Foo:
			    stringAttr string (1..1)
		'''.generateDaml
		
		val fileContent = classes.get("Org/Isda/Other/Test/Classes.daml").toString

		assertEquals('''
			daml 1.2
			
			-- | This file is auto-generated from the ISDA Common
			--   Domain Model, do not edit.
			--   @version test
			module Org.Isda.Other.Test.Classes
			  ( module Org.Isda.Other.Test.Classes ) where
			
			import Org.Isda.Other.Test.Enums
			import Org.Isda.Other.Test.ZonedDateTime
			import Org.Isda.Other.Test.MetaClasses
			import Org.Isda.Other.Test.MetaFields
			import Prelude hiding (Party, exercise, id, product, agreement)
			
			data Foo = Foo with 
			  stringAttr : Text
			    deriving (Eq, Ord, Show)
			
	    '''.toString, fileContent)
	}
		
	@Test
	def void shoulHandleLeadingUnderscoreTypeName() {
		val classes = '''
			namespace cdm.test
			
			type _Foo:
			    stringAttr string (1..1)
		'''.generateDaml
		
		val fileContent = classes.get("Org/Isda/Cdm/Test/Classes.daml").toString

		assertEquals('''
			daml 1.2
			
			-- | This file is auto-generated from the ISDA Common
			--   Domain Model, do not edit.
			--   @version test
			module Org.Isda.Cdm.Test.Classes
			  ( module Org.Isda.Cdm.Test.Classes ) where
			
			import Org.Isda.Cdm.Test.Enums
			import Org.Isda.Cdm.Test.ZonedDateTime
			import Org.Isda.Cdm.Test.MetaClasses
			import Org.Isda.Cdm.Test.MetaFields
			import Prelude hiding (Party, exercise, id, product, agreement)
			
			data Foo_ = Foo_ with 
			  stringAttr : Text
			    deriving (Eq, Ord, Show)
			
	    '''.toString, fileContent)
	}

	@Test
	def void shouldGenerateClassWithImports() {
		val daml = '''
			namespace cdm.test
			
			type Foo:
			    stringAttr string (0..1)
		'''.generateDaml
		
		val classes = daml.get("Org/Isda/Cdm/Test/Classes.daml").toString
		
		assertTrue(classes.contains('''import Org.Isda.Cdm.Test.Enums'''))
		assertTrue(classes.contains('''import Org.Isda.Cdm.Test.ZonedDateTime'''))
		assertTrue(classes.contains('''import Org.Isda.Cdm.Test.MetaClasses'''))
		assertTrue(classes.contains('''import Prelude hiding (Party, exercise, id, product, agreement)'''))
	}

	@Test
	def void shouldGenerateClassWithBasicTypes() {
		val classes = '''
			namespace cdm.test
			
			type Foo:
			    stringAttr string (1..1)
			    intAttr int (1..1)
			    numberAttr number (1..1)
			    booleanAttr boolean (1..1)
			    dateAttr date (1..1)
			    timeAttr time (1..1)
				zonedDateTimeAttr zonedDateTime (1..1)
				calculationAttr calculation (1..1)
				productTypeAttr productType (1..1)
				eventTypeAttr eventType (1..1)
		'''.generateDaml
		
		val fileContent = classes.get("Org/Isda/Cdm/Test/Classes.daml").toString

		assertEquals('''
			daml 1.2
			
			-- | This file is auto-generated from the ISDA Common
			--   Domain Model, do not edit.
			--   @version test
			module Org.Isda.Cdm.Test.Classes
			  ( module Org.Isda.Cdm.Test.Classes ) where
			
			import Org.Isda.Cdm.Test.Enums
			import Org.Isda.Cdm.Test.ZonedDateTime
			import Org.Isda.Cdm.Test.MetaClasses
			import Org.Isda.Cdm.Test.MetaFields
			import Prelude hiding (Party, exercise, id, product, agreement)
			
			data Foo = Foo with 
			  stringAttr : Text
			  intAttr : Int
			  numberAttr : Decimal
			  booleanAttr : Bool
			  dateAttr : Date
			  timeAttr : Text
			  zonedDateTimeAttr : ZonedDateTime
			  calculationAttr : Text
			  productTypeAttr : Text
			  eventTypeAttr : Text
			    deriving (Eq, Ord, Show)
			
	    '''.toString, fileContent)
	}

	@Test
	def void shouldGenerateClassWithOptionalBasicType() {
		val classes = '''
			namespace cdm.test
			
			type Foo:
			    stringAttr string (0..1)
		'''.generateDaml.get("Org/Isda/Cdm/Test/Classes.daml").toString
		
		assertTrue(classes.contains('''
		data Foo = Foo with 
		  stringAttr : Optional Text
		    deriving (Eq, Ord, Show)'''))
	}

	@Test
	def void shouldGenerateClassWithComments() {
		val classes = '''
			namespace cdm.test
			
			type Foo: <"This is the class comment which should wrap if the line is long enough.">
			    stringAttr string (0..1) <"This is the attribute comment which should also wrap if long enough">
		'''.generateDaml.get("Org/Isda/Cdm/Test/Classes.daml").toString
		
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
			namespace cdm.test
			
			type Foo:
			    stringAttrs string (0..*)
		'''.generateDaml.get("Org/Isda/Cdm/Test/Classes.daml").toString
		
		assertTrue(classes.contains('''
		data Foo = Foo with 
		  stringAttrs : [Text]
		    deriving (Eq, Ord, Show)'''))
	}
	
	@Test
	def void shouldGenerateClassWithBasicTypeAndMetaFieldScheme() {
		val code = '''
			namespace cdm.test
			
			metaType scheme string
			metaType location string
			
			type Foo:
			    stringAttr string (1..1)
			    [metadata scheme]
		'''.generateDaml
		
		val classes = code.get("Org/Isda/Cdm/Test/Classes.daml").toString
		
		assertTrue(classes.contains('''
		data Foo = Foo with 
		  stringAttr : (FieldWithMeta Text)
		    deriving (Eq, Ord, Show)'''))

		val metaFields = code.get("Org/Isda/Cdm/Test/MetaFields.daml").toString
		
//		println(metaFields)
		
		assertTrue(metaFields.contains('''
		daml 1.2
		
		-- | This file is auto-generated from the ISDA Common
		--   Domain Model, do not edit.
		--   @version test
		module Org.Isda.Cdm.Test.MetaFields
		  ( module Org.Isda.Cdm.Test.MetaFields ) where
		
		data MetaFields = MetaFields with
		  scheme : Optional Text
		  globalKey : Optional Text
		  externalKey : Optional Text
		  location: [Key]
		    deriving (Eq, Ord, Show)
		
		data MetaAndTemplateFields = MetaAndTemplateFields with
		  scheme : Optional Text
		  globalKey : Optional Text
		  externalKey : Optional Text
		  templateGlobalReference : Optional Text
		  location: [Key]
		    deriving (Eq, Ord, Show)'''))
	}
	
	@Test
	def void shouldGenerateClassWithOptionalRosettaType() {
		val classes = '''
			namespace cdm.test
			
			type Foo:
			    barAttr Bar (0..1)
			
			type Bar:
			    stringAttr string (1..1)
		'''.generateDaml.get("Org/Isda/Cdm/Test/Classes.daml").toString
		
		assertTrue(classes.contains('''
		data Foo = Foo with 
		  barAttr : Optional Bar
		    deriving (Eq, Ord, Show)'''))
	}
	
	@Test
	def void shouldGenerateClassWithRosettaTypeAndMetaReference() {
		val code = '''
			namespace cdm.test
			
			metaType reference string
			metaType location string
			
			type Foo:
			    barReference Bar (0..1)
			    [metadata reference]
			
			type Bar:
			    [metadata key]
			    stringAttr string (1..1)
		'''.generateDaml
		
		val classes = code.get("Org/Isda/Cdm/Test/Classes.daml").toString
		
		assertTrue(classes.contains('''
		data Bar = Bar with 
		  stringAttr : Text
		  meta : Optional MetaFields
		    deriving (Eq, Ord, Show)'''))

		assertTrue(classes.contains('''
		data Foo = Foo with 
		  barReference : Optional (ReferenceWithMeta Bar)
		    deriving (Eq, Ord, Show)'''))

		val metaFields = code.get("Org/Isda/Cdm/Test/MetaFields.daml").toString
		
		//println(metaFields)
		
		assertTrue(metaFields.contains('''
		daml 1.2
		
		-- | This file is auto-generated from the ISDA Common
		--   Domain Model, do not edit.
		--   @version test
		module Org.Isda.Cdm.Test.MetaFields
		  ( module Org.Isda.Cdm.Test.MetaFields ) where
		
		data MetaFields = MetaFields with
		  globalKey : Optional Text
		  externalKey : Optional Text
		  location: [Key]
		    deriving (Eq, Ord, Show)
		
		data MetaAndTemplateFields = MetaAndTemplateFields with
		  globalKey : Optional Text
		  externalKey : Optional Text
		  templateGlobalReference : Optional Text
		  location: [Key]
		    deriving (Eq, Ord, Show)'''))
	}
	
	@Test
	def void shouldGenerateClassWithRosettaTypeLocationAndAddress() {
		val code = '''
			namespace cdm.test
			
			metaType reference string
			metaType address string
			metaType location string
			
			type Foo:
			    bazAddress Baz (1..1)
			    	[metadata address "pointsTo"=Bar->bazLocation]
			
			type Bar:
			    bazLocation Baz (1..1)
			    	[metadata location]
			
			type Baz:
			    stringAttr string (1..1)
		'''.generateDaml
		
		val classes = code.get("Org/Isda/Cdm/Test/Classes.daml").toString
		
		assertTrue(classes.contains('''
		data Baz = Baz with 
		  stringAttr : Text
		    deriving (Eq, Ord, Show)'''))

		assertTrue(classes.contains('''
		data Bar = Bar with 
		  bazLocation : (FieldWithMeta Baz)
		    deriving (Eq, Ord, Show)'''))
		
		assertTrue(classes.contains('''
		data Foo = Foo with 
		  bazAddress : (ReferenceWithMeta Baz)
		    deriving (Eq, Ord, Show)'''))

		val metaClasses = code.get("Org/Isda/Cdm/Test/MetaClasses.daml").toString
		
		assertTrue(metaClasses.contains('''
		daml 1.2
		
		-- | This file is auto-generated from the ISDA Common
		--   Domain Model, do not edit.
		--   @version ${project.version}
		module Org.Isda.Cdm.Test.MetaClasses
		  ( module Org.Isda.Cdm.Test.MetaClasses ) where
		
		import Org.Isda.Cdm.Test.MetaFields
		
		data ReferenceWithMeta a = ReferenceWithMeta with
		  globalReference : Optional Text
		  externalReference : Optional Text
		  address: Optional Reference
		  value : Optional a
		    deriving (Eq, Ord, Show)
		
		data BasicReferenceWithMeta a = BasicReferenceWithMeta with
		  globalReference : Optional Text
		  externalReference : Optional Text
		  address: Optional Reference
		  value : Optional a
		    deriving (Eq, Ord, Show)
		
		data FieldWithMeta a = FieldWithMeta with
		  value : a
		  meta : Optional MetaFields
		    deriving (Eq, Ord, Show)'''))

		val metaFields = code.get("Org/Isda/Cdm/Test/MetaFields.daml").toString
		
		assertTrue(metaFields.contains('''
		daml 1.2
		
		-- | This file is auto-generated from the ISDA Common
		--   Domain Model, do not edit.
		--   @version test
		module Org.Isda.Cdm.Test.MetaFields
		  ( module Org.Isda.Cdm.Test.MetaFields ) where
		
		data MetaFields = MetaFields with
		  globalKey : Optional Text
		  externalKey : Optional Text
		  location: [Key]
		    deriving (Eq, Ord, Show)
		
		data MetaAndTemplateFields = MetaAndTemplateFields with
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
		    deriving (Eq, Ord, Show)'''))
	}
	
	@Test
	def void shouldGenerateClassWithRosettaTypeAndMetaBasicReference() {
		val code = '''
			namespace cdm.test
			
			metaType reference string
			metaType id string
			metaType key string
			metaType address string
			metaType location string
			
			type Foo:
			    stringReference string (0..1)
			    [metadata reference]
		'''.generateDaml
		
		val classes = code.get("Org/Isda/Cdm/Test/Classes.daml").toString
		
		assertTrue(classes.contains('''
		data Foo = Foo with 
		  stringReference : Optional (BasicReferenceWithMeta Text)
		    deriving (Eq, Ord, Show)'''))

		val metaFields = code.get("Org/Isda/Cdm/Test/MetaFields.daml").toString
		
//		println(metaFields)
		
		assertTrue(metaFields.contains('''
		daml 1.2
		
		-- | This file is auto-generated from the ISDA Common
		--   Domain Model, do not edit.
		--   @version test
		module Org.Isda.Cdm.Test.MetaFields
		  ( module Org.Isda.Cdm.Test.MetaFields ) where
		
		data MetaFields = MetaFields with
		  globalKey : Optional Text
		  externalKey : Optional Text
		  location: [Key]
		    deriving (Eq, Ord, Show)
		
		data MetaAndTemplateFields = MetaAndTemplateFields with
		  globalKey : Optional Text
		  externalKey : Optional Text
		  templateGlobalReference : Optional Text
		  location: [Key]
		    deriving (Eq, Ord, Show)'''))
	}
	
	@Test
	def void shouldGenerateClassWitOverrideAttribute() {
		val classes = '''
			namespace cdm.test
			
			type Foo:
			    attr string (0..1)
			
			type Bar extends Foo:
			    override attr string (1..1)
		'''.generateDaml.get("Org/Isda/Cdm/Test/Classes.daml").toString

		assertTrue(classes.contains('''
		data Foo = Foo with 
		  attr : Optional Text
		    deriving (Eq, Ord, Show)'''))
	}

	def generateDaml(CharSequence model) {
		val m = model.parseRosettaWithNoErrors
		val resourceSet = m.eResource.resourceSet
		
		generator.afterAllGenerate(resourceSet, #{m}, "test")
	}
}
