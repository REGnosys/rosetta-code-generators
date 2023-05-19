package com.regnosys.rosetta.generator.golang

import com.google.inject.Inject
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*
import java.nio.file.Files
import java.nio.file.Paths
import java.io.File
import org.junit.jupiter.api.Disabled
import com.regnosys.rosetta.generators.test.TestUtil

/**
 * The parser of rosetta files has a particular requirement:
 * namespace declaration should not have any comments,
 * so all text ":<...>" should be removed from the namespace line
 * if present.
 */
@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class GolangModelObjectGeneratorTest {

	@Inject extension ModelHelper
	
    @Inject extension TestUtil
	
	@Inject GolangCodeGenerator generator;

	@Test
	@Disabled("Test to generate the golang for CDM")
	def void generateCdm() {
		val dirs = #[
            '../../../finos/common-domain-model/rosetta-source/src/main/rosetta',
            '../../rosetta-dsl/rosetta-lang/src/main/resources/model'            
        ]

		val rosettaModels = dirs.parseAllRosettaFiles
		
		val generatedFiles = generator.afterGenerate(rosettaModels)		

		val rootDir = System.getProperty("user.dir")
		
		generatedFiles.forEach[fileName, contents | {
			val pathString = rootDir+"/"+fileName
			val path = Paths.get(pathString)
			val file = new File(pathString);
			file.getParentFile().mkdirs();					
			Files.write(path, contents.toString.bytes)			
		}]
	}

	@Test
	def void shouldGenerateEnums() {
		val golang = '''
			enum TestEnum: <"Test enum description.">
				TestEnumValue1 <"Test enum value 1">
				TestEnumValue2 <"Test enum value 2">
		'''.generateGolang
		 
    	val enumString = golang.get('org_isda_cdm/TestEnum/TestEnum.go').toString; 
     	
		assertTrue(enumString.contains('''
		/**
		 * This file is auto-generated from the ISDA Common Domain Model, do not edit.
		 * Version: test
		 */
		  package TestEnum
		  import . "org_isda_cdm"
		  /**
		   * Test enum description.
		   */
		  
		  const (
		  /**
		   * Test enum value 1
		   */
		  TEST_ENUM_VALUE_1 TestEnum = iota + 1
		  /**
		   * Test enum value 2
		   */
		  TEST_ENUM_VALUE_2 TestEnum = iota + 1
		  )    ''')
		  )
	}

	@Test
	def void shouldGenerateTypes() {
		val golang = '''
			type TestType: <"Test type description.">
				testTypeValue1 string (1..1) <"Test string">
				testTypeValue2 string (0..1) <"Test optional string">
				testTypeValue3 string (0..*) <"Test string list">
				testTypeValue4 TestType2 (1..1) <"Test TestType2">
				testTypeValue5 TestType2 (0..*) <"Test TestType2 list">
				
			type TestType2:
				testType2Value1 number (1..1) <"Test number">
				testType2Value2 date (1..1) <"Test date">
		'''.generateGolang

		val types = golang.get('org_isda_cdm/types.go').toString
		
		assertTrue(types.contains('''
		package org_isda_cdm
		
		/**
		 * This file is auto-generated from the ISDA Common Domain Model, do not edit.
		 * Version: test
		 */
		
		import "time"
		import . "org_isda_cdm_metafields";
		  
		
		/**
		 * Test type description.
		 */
		type TestType struct {
		  /**
		   * Test string
		   */
		  TestTypeValue1 string;
		  /**
		   * Test optional string
		   */
		  TestTypeValue2 string;
		  /**
		   * Test string list
		   */
		  TestTypeValue3 []string;
		  /**
		   * Test TestType2
		   */
		  TestTypeValue4 TestType2;
		  /**
		   * Test TestType2 list
		   */
		  TestTypeValue5 []TestType2;
		}
		  
		type TestType2 struct {
		  /**
		   * Test number
		   */
		  TestType2Value1 float64;
		  /**
		   * Test date
		   */
		  TestType2Value2 time.Time;
		}'''))

	}	
	
    @Test
    def void shouldGenerateCalculationType() {
        val golang = '''
			type Foo:
			     attr calculation (0..1)
        '''.generateGolang

		val types = golang.get('org_isda_cdm/types.go').toString
        
        assertEquals('''
	        package org_isda_cdm
	        
	        /**
	         * This file is auto-generated from the ISDA Common Domain Model, do not edit.
	         * Version: test
	         */
	        
	        import "time"
	        import . "org_isda_cdm_metafields";
	          
	        
	        type Foo struct {
	          Attr string;
	        }
	          
        '''.toString, types.toString)
    }
    
    @Test
    def void shouldGenerateProductAndEventType() {
        val golang = '''
			type Foo:
			     productAttr productType (0..1)
			     eventAttr eventType (0..1)
        '''.generateGolang

		val types = golang.get('org_isda_cdm/types.go').toString
        
        assertEquals('''
	        package org_isda_cdm
	        
	        /**
	         * This file is auto-generated from the ISDA Common Domain Model, do not edit.
	         * Version: test
	         */
	        
	        import "time"
	        import . "org_isda_cdm_metafields";
	          
	        
	        type Foo struct {
	          EventAttr string;
	          ProductAttr string;
	        }
	          
        '''.toString, types.toString)
    }
	
	@Test	
	def void shouldGenerateMetaTypes() {
		val golang = '''
			metaType reference string
			metaType scheme string
			metaType id string
			metaType address string
			
			type TestType:
				[metadata key]
				testTypeValue1 TestType2 (1..1)
					[metadata reference]
			
			type TestType2:
				testType2Value1 number (1..1)
					[metadata reference]
					
				testType2Value2 string (1..1)
					[metadata id]
					[metadata scheme]
			
			type TestType3:
				testType3Value1 string (1..1)
			
			type TestType4:
				testType3Location TestType3 (1..1)
					[metadata location]
			
			type TestType5:
				testType3Address TestType3 (1..1)
					[metadata address "pointsTo"=TestType4->testType3Location]
				'''.generateGolang

		val types = golang.values.join('\n').toString
		
		//println(types)
		
		// types

		assertTrue(types.contains('''
		type TestType struct {
		  Meta MetaFields;
		  TestTypeValue1 ReferenceWithMeta;
		}'''))

		assertTrue(types.contains('''
		type TestType2 struct {
		  TestType2Value1 ReferenceWithMeta;
		  TestType2Value2 FieldWithMeta;
		}'''))
		
		assertTrue(types.contains('''
		type TestType3 struct {
		  TestType3Value1 string;
		}'''))
		
		assertTrue(types.contains('''
		type TestType4 struct {
		  TestType3Location FieldWithMeta;
		}'''))
		
		assertTrue(types.contains('''
		type TestType5 struct {
		  TestType3Address ReferenceWithMeta;
		}'''))
		
		// meta fields
		
		assertTrue(types.contains('''
		type FieldWithMeta struct {
		  Value interface{};
		  Meta MetaFields;
		}'''))
		
		assertTrue(types.contains('''
		type ReferenceWithMeta struct {
		  GlobalReference string;
		  ExternalReference string;
		  Address Reference;
		  Value interface{};
		}'''))
		
		assertTrue(types.contains('''
		type MetaFields struct {
		  Scheme string;
		  GlobalKey string;
		  ExternalKey string;
		  Location []Key;
		}'''))
		
		assertTrue(types.contains('''
		type Key struct {
		  Scope string;
		  Value string;
		}'''))
		
		assertTrue(types.contains('''
		type Reference struct {
		  Scope string;
		  Value string;
		}'''))

	}

	def generateGolang(CharSequence model) {
		val eResource = model.parseRosettaWithNoErrors.eResource

		generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
	}
}
