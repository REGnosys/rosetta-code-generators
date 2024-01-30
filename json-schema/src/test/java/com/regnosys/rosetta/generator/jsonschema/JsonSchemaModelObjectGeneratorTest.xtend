package com.regnosys.rosetta.generator.jsonschema

import com.google.inject.Inject
import com.regnosys.rosetta.generators.test.TestUtil
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import java.nio.file.Files
import java.nio.file.Paths
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Disabled
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class JsonSchemaModelObjectGeneratorTest {

	@Inject extension ModelHelper
	
	@Inject extension TestUtil
	
	@Inject JsonSchemaCodeGenerator generator;

	@Test
	@Disabled("Test to generate the json schema for CDM")
	def void generateCdm() {
		val dirs = #[
            '../../../finos/common-domain-model/rosetta-source/src/main/rosetta',
            '../../rosetta-dsl/rosetta-lang/src/main/resources/model'            
        ]

		val resourceSet = dirs.parseAllRosettaFiles
		val models = resourceSet.resources.map[contents.head as RosettaModel]
		
		val generatedFiles = generator.afterAllGenerate(resourceSet, models, "test")

		val cdmDir = Files.createDirectories(Paths.get("cdm"))
		generatedFiles.forEach [ fileName, contents |
			Files.write(cdmDir.resolve(fileName), contents.toString.bytes)
		]
	}

	@Test
	def void shouldGenerateEnums() {
		val json = '''
			enum TestEnum: <"Test enum description.">
				TestEnumValue1 <"Test enum value 1">
				TestEnumValue2 <"Test enum value 2">
		'''.generate

		val enums = json.get('Enums.json').toString
		//println(enums)
		assertTrue(enums.contains('''
		TBD
		'''))
	}

	@Test
	def void shouldGenerateTypes() {
		val json = '''
			type TestType: <"Test type description.">
				testTypeValue1 string (1..1) <"Test string">
				testTypeValue2 string (0..1) <"Test optional string">
				testTypeValue3 string (0..*) <"Test string list">
				testTypeValue4 TestType2 (1..1) <"Test TestType2">
				testEnum TestEnum (0..1) <"Optional test enum">
			
			type TestType2:
				testType2Value1 number(1..*) <"Test number list">
				testType2Value2 date(0..1) <"Test date">
				testEnum TestEnum (1..1) <"Optional test enum">
			
			enum TestEnum: <"Test enum description.">
				TestEnumValue1 <"Test enum value 1">
				TestEnumValue2 <"Test enum value 2">
			
		'''.generate

		val types = json.get('Types.json').toString
		//println(types)
		assertEquals('''
			TBD
			'''.toString, types)
	}

    @Test
    def void shouldGenerateCalculationType() {
        val json = '''
			type Foo:
			     attr calculation (0..1)
        '''.generate

		val types = json.get('Types.json').toString
        
        assertEquals('''
			TBD
        '''.toString, types.toString)
    }
    
    @Test
    def void shouldGenerateProductAndEventType() {
        val json = '''
			type Foo:
			     productAttr productType (0..1)
			     eventAttr eventType (0..1)
        '''.generate

		val types = json.get('Types.json').toString
        
        assertEquals('''
			TBD
        '''.toString, types.toString)
    }



	@Test
	def void shouldGenerateTypesExtends() {
		val json = '''
			type TestType extends TestType2:
				TestTypeValue1 string (1..1) <"Test string">
				TestTypeValue2 int (0..1) <"Test int">
			
			type TestType2 extends TestType3:
				TestType2Value1 number (0..1) <"Test number">
				TestType2Value2 date (0..*) <"Test date">
			
			type TestType3:
				TestType3Value1 string (0..1) <"Test string">
				TestType4Value2 int (1..*) <"Test int">
		'''.generate

		val traits = json.get('Traits.json').toString
		//println(traits)
		assertTrue(traits.contains('''
			TBD
		'''))

		val types = json.get('Types.json').toString
		//println(types)
		assertTrue(types.contains('''
		case class TestType(testTypeValue1: String,
		    testTypeValue2: Option[Int],
		    testType2Value1: Option[json.math.BigDecimal],
		    testType2Value2: List[java.time.LocalDate],
		    testType3Value1: Option[String],
		    testType4Value2: List[Int])
		  extends TestType2Trait {
		}
		'''))
		assertTrue(types.contains('''
		case class TestType2(testType2Value1: Option[json.math.BigDecimal],
		    testType2Value2: List[java.time.LocalDate],
		    testType3Value1: Option[String],
		    testType4Value2: List[Int])
		  extends TestType2Trait with TestType3Trait {
		}
		'''))
		assertTrue(types.contains('''
		case class TestType3(testType3Value1: Option[String],
		    testType4Value2: List[Int])
		  extends TestType3Trait {
		}
		'''))
	}

	@Test
	def void shouldGenerateMetaTypes() {
		val json = '''
			metaType reference string
			metaType scheme string
			metaType id string
			metaType address string
			
			type TestType:
				[metadata key]
				testTypeValue1 TestType2 (1..1)
					[metadata reference]
				
				testTypeValue2 TestType2 (1..1)
					[metadata location]
			
			enum TestEnum: <"Test enum description.">
				TestEnumValue1 <"Test enum value 1">
				TestEnumValue2 <"Test enum value 2">
			
			type TestType2:
				testType2Value1 number (1..1)
					[metadata id]
				
				testType2Value2 string (1..1)
					[metadata id]
					[metadata scheme]
				
				testType2Value3 TestEnum (1..1)
					[metadata scheme]
			
			type TestType3:
				testType3Value1 TestType2 (1..1)
					[metadata address "pointsTo"=TestType->testTypeValue2]
			
		'''.generate

		val types = json.values.join('\n').toString
		
		//println(types)
		
		// types
		
		assertTrue(types.contains('''
		case class TestType(testTypeValue1: ReferenceWithMetaTestType2,
		    testTypeValue2: FieldWithMetaTestType2,
		    meta: Option[MetaFields]) {
		}'''))

		assertTrue(types.contains('''
		case class TestType2(testType2Value1: FieldWithMetaBigDecimal,
		    testType2Value2: FieldWithMetaString,
		    testType2Value3: FieldWithMetaTestEnum) {
		}'''))
		
		assertTrue(types.contains('''
		case class TestType3(testType3Value1: ReferenceWithMetaTestType2) {
		}'''))
		
		// meta fields
		
		assertTrue(types.contains('''
		case class MetaFields(scheme: Option[String],
		    globalKey: Option[String],
		    externalKey: Option[String],
		    location: List[Key]) {}
	    '''))
	    
	    assertTrue(types.contains('''
		case class MetaAndTemplateFields(scheme: Option[String],
		    globalKey: Option[String],
		    externalKey: Option[String],
		    templateGlobalReference: Option[String],
		    location: List[Key]) {}
	    '''))
	    
	    assertTrue(types.contains('''
		case class Key(
		  value: String,
		  scope: Option[String]) {}
	    '''))
	    
	    assertTrue(types.contains('''
		case class Reference(
		  value: String,
		  scope: Option[String]) {}
	    '''))
		
		assertTrue(types.contains('''
		case class FieldWithMetaString(value: Option[String],
		    meta: Option[MetaFields]) {}
	    '''))

		assertTrue(types.contains('''
		case class FieldWithMetaTestEnum(@JsonDeserialize(contentAs = classOf[TestEnum.Value])
		    @JsonJsonSchemaEnumeration(classOf[TestEnum.Class])
		    value: Option[TestEnum.Value],
		    meta: Option[MetaFields]) {}
	    '''))
	    
	    assertTrue(types.contains('''
		case class FieldWithMetaBigDecimal(value: Option[json.math.BigDecimal],
		    meta: Option[MetaFields]) {}
	    '''))
		
		assertTrue(types.contains('''
		case class ReferenceWithMetaTestType2(value: Option[TestType2],
		    globalReference: Option[String],
		    externalReference: Option[String],
		    address: Option[Reference]) {}
	    '''))
	}

    @Test
    @Disabled("TODO fix oneOf code generation for attributes that are Lists")
    def void shouldGenerateOneOfCondition() {
        val json = '''
        type TestType: <"Test type with one-of condition.">
            field1 string (0..1) <"Test string field 1">
            field2 string (0..1) <"Test string field 2">
            field3 number (0..1) <"Test number field 3">
            field4 number (0..*) <"Test number field 4">
            condition: one-of
        '''.generate

        val types = json.get('Types.json').toString
        //println(types)
        assertTrue(types.contains('''
		/**
		  * This file is auto-generated from the ISDA Common Domain Model, do not edit.
		  * Version: test
		  */
		package org.isda.cdm
		
		import com.fasterxml.jackson.core.`type`.TypeReference
		import com.fasterxml.jackson.module.json.JsonJsonSchemaEnumeration
		import com.fasterxml.jackson.databind.annotation.JsonDeserialize
		
		import org.isda.cdm.metafields._
		
		/**
		  * Test type with one-of condition.
		  *
		  * @param field1 Test string field 1
		  * @param field2 Test string field 2
		  * @param field3 Test number field 3
		  * @param field4 Test number field 4
		  */
		case class TestType(field1: Option[String],
		    field2: Option[String],
		    field3: Option[json.math.BigDecimal],
		    field4: List[json.math.BigDecimal]) {
		  //val numberOfPopulatedFields = List(field1, field2, field3, field4).flatten.length
		  //require(numberOfPopulatedFields == 1)
		}
		'''))
    }

	def generate(CharSequence model) {
		val m = model.parseRosettaWithNoErrors
		val resourceSet = m.eResource.resourceSet
		
		generator.afterAllGenerate(resourceSet, #{m}, "test")
	}
}
