package com.regnosys.rosetta.generator.scala

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
class ScalaModelObjectGeneratorTest {

	@Inject extension ModelHelper
	
	@Inject extension TestUtil
	
	@Inject ScalaCodeGenerator generator;

	@Test
	@Disabled("Test to generate the scala for CDM")
	def void generateCdm() {
		val dirs = #[
            '../../../finos/common-domain-model/rosetta-source/src/main/rosetta',
            '../../rosetta-dsl/rosetta-lang/src/main/resources/model'            
        ]

		val rosettaModels = dirs.parseAllRosettaFiles
		
		val generatedFiles = generator.afterGenerate(rosettaModels)

		val cdmDir = Files.createDirectories(Paths.get("cdm"))
		generatedFiles.forEach [ fileName, contents |
			Files.write(cdmDir.resolve(fileName), contents.toString.bytes)
		]
	}

	@Test
	def void shouldGenerateEnums() {
		val scala = '''
			enum TestEnum: <"Test enum description.">
				TestEnumValue1 <"Test enum value 1">
				TestEnumValue2 <"Test enum value 2">
		'''.generateScala

		val enums = scala.get('Enums.scala').toString
		//println(enums)
		assertTrue(enums.contains('''
		/**
		  * This file is auto-generated from the ISDA Common Domain Model, do not edit.
		  * Version: test
		  */
		package org.isda.cdm
		
		import com.fasterxml.jackson.core.`type`.TypeReference
		
		/**
		  * Test enum description.
		  */
		object TestEnum extends Enumeration {
		  
		  class Class extends TypeReference[this.type]
		  
		  /**
		    * Test enum value 1
		    */
		  val TEST_ENUM_VALUE_1 = Value
		  
		  /**
		    * Test enum value 2
		    */
		  val TEST_ENUM_VALUE_2 = Value
		}
		'''))
	}

	@Test
	def void shouldGenerateTypes() {
		val scala = '''
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
			
		'''.generateScala

		val types = scala.get('Types.scala').toString
		//println(types)
		assertTrue(types.contains('''
			/**
			  * This file is auto-generated from the ISDA Common Domain Model, do not edit.
			  * Version: test
			  */
			package org.isda.cdm
			
			import com.fasterxml.jackson.core.`type`.TypeReference
			import com.fasterxml.jackson.module.scala.JsonScalaEnumeration
			import com.fasterxml.jackson.databind.annotation.JsonDeserialize
			
			import org.isda.cdm.metafields._
			
			/**
			  * Test type description.
			  *
			  * @param testEnum Optional test enum
			  * @param testTypeValue1 Test string
			  * @param testTypeValue2 Test optional string
			  * @param testTypeValue3 Test string list
			  * @param testTypeValue4 Test TestType2
			  */
			case class TestType(@JsonDeserialize(contentAs = classOf[TestEnum.Value])
			    @JsonScalaEnumeration(classOf[TestEnum.Class])
			    testEnum: Option[TestEnum.Value],
			    testTypeValue1: String,
			    testTypeValue2: Option[String],
			    testTypeValue3: List[String],
			    testTypeValue4: TestType2) {
			}
			
			case class TestType2(@JsonScalaEnumeration(classOf[TestEnum.Class])
			    testEnum: TestEnum.Value,
			    testType2Value1: List[scala.math.BigDecimal],
			    testType2Value2: Option[java.time.LocalDate]) {
			}
			
			'''))
	}

    @Test
    def void shouldGenerateCalculationType() {
        val scala = '''
			type Foo:
			     attr calculation (0..1)
        '''.generateScala

		val types = scala.get('Types.scala').toString
        
        assertEquals('''
	        /**
	          * This file is auto-generated from the ISDA Common Domain Model, do not edit.
	          * Version: test
	          */
	        package org.isda.cdm
	        
	        import com.fasterxml.jackson.core.`type`.TypeReference
	        import com.fasterxml.jackson.module.scala.JsonScalaEnumeration
	        import com.fasterxml.jackson.databind.annotation.JsonDeserialize
	        
	        import org.isda.cdm.metafields._
	        
	        case class Foo(attr: Option[String]) {
	        }
	        
        '''.toString, types.toString)
    }
    
    @Test
    def void shouldGenerateProductAndEventType() {
        val scala = '''
			type Foo:
			     productAttr productType (0..1)
			     eventAttr eventType (0..1)
        '''.generateScala

		val types = scala.get('Types.scala').toString
        
        assertEquals('''
	       /**
	         * This file is auto-generated from the ISDA Common Domain Model, do not edit.
	         * Version: test
	         */
	       package org.isda.cdm
	       
	       import com.fasterxml.jackson.core.`type`.TypeReference
	       import com.fasterxml.jackson.module.scala.JsonScalaEnumeration
	       import com.fasterxml.jackson.databind.annotation.JsonDeserialize
	       
	       import org.isda.cdm.metafields._
	       
	       case class Foo(eventAttr: Option[String],
	           productAttr: Option[String]) {
	       }
	       
        '''.toString, types.toString)
    }



	@Test
	def void shouldGenerateTypesExtends() {
		val scala = '''
			type TestType extends TestType2:
				TestTypeValue1 string (1..1) <"Test string">
				TestTypeValue2 int (0..1) <"Test int">
			
			type TestType2 extends TestType3:
				TestType2Value1 number (0..1) <"Test number">
				TestType2Value2 date (0..*) <"Test date">
			
			type TestType3:
				TestType3Value1 string (0..1) <"Test string">
				TestType4Value2 int (1..*) <"Test int">
		'''.generateScala

		val traits = scala.get('Traits.scala').toString
		//println(traits)
		assertTrue(traits.contains('''
		trait TestType2Trait extends TestType3Trait {
		  /**
		    * Test number
		    */
		  val testType2Value1: Option[scala.math.BigDecimal]
		  /**
		    * Test date
		    */
		  val testType2Value2: List[java.time.LocalDate]
		}
		'''))
		assertTrue(traits.contains('''
		trait TestType3Trait {
		  /**
		    * Test string
		    */
		  val testType3Value1: Option[String]
		  /**
		    * Test int
		    */
		  val testType4Value2: List[Int]
		}
		'''))

		val types = scala.get('Types.scala').toString
		//println(types)
		assertTrue(types.contains('''
		case class TestType(testTypeValue1: String,
		    testTypeValue2: Option[Int],
		    testType2Value1: Option[scala.math.BigDecimal],
		    testType2Value2: List[java.time.LocalDate],
		    testType3Value1: Option[String],
		    testType4Value2: List[Int])
		  extends TestType2Trait {
		}
		'''))
		assertTrue(types.contains('''
		case class TestType2(testType2Value1: Option[scala.math.BigDecimal],
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
		val scala = '''
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
			
		'''.generateScala

		val types = scala.values.join('\n').toString
		
		//println(types)
		
		// types
		
		assertTrue(types.contains('''
		case class TestType(meta: Option[MetaFields],
		    testTypeValue1: ReferenceWithMetaTestType2,
		    testTypeValue2: FieldWithMetaTestType2) {
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
		    @JsonScalaEnumeration(classOf[TestEnum.Class])
		    value: Option[TestEnum.Value],
		    meta: Option[MetaFields]) {}
	    '''))
	    
	    assertTrue(types.contains('''
		case class FieldWithMetaBigDecimal(value: Option[scala.math.BigDecimal],
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
        val scala = '''
        type TestType: <"Test type with one-of condition.">
            field1 string (0..1) <"Test string field 1">
            field2 string (0..1) <"Test string field 2">
            field3 number (0..1) <"Test number field 3">
            field4 number (0..*) <"Test number field 4">
            condition: one-of
        '''.generateScala

        val types = scala.get('Types.scala').toString
        //println(types)
        assertTrue(types.contains('''
		/**
		  * This file is auto-generated from the ISDA Common Domain Model, do not edit.
		  * Version: test
		  */
		package org.isda.cdm
		
		import com.fasterxml.jackson.core.`type`.TypeReference
		import com.fasterxml.jackson.module.scala.JsonScalaEnumeration
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
		    field3: Option[scala.math.BigDecimal],
		    field4: List[scala.math.BigDecimal]) {
		  //val numberOfPopulatedFields = List(field1, field2, field3, field4).flatten.length
		  //require(numberOfPopulatedFields == 1)
		}
		'''))
    }

	def generateScala(CharSequence model) {
		val eResource = model.parseRosettaWithNoErrors.eResource

		generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
	}
}
