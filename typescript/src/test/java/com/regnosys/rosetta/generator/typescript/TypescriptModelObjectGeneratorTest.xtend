package com.regnosys.rosetta.generator.typescript

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
class TypescriptModelObjectGeneratorTest {

	@Inject extension ModelHelper
	
	@Inject extension TestUtil
	
	@Inject TypescriptCodeGenerator generator

	@Test
	@Disabled("Test to generate the typescript for CDM")
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
		val typescript = '''
			enum TestEnum: <"Test enum description.">
				TestEnumValue1 <"Test enum value 1">
				TestEnumValue2 <"Test enum value 2">
		'''.generateTypescript

		val enums = typescript.get('enums.ts').toString
		assertTrue(enums.contains('''
		/**
		 * Test enum description.
		 */
		export enum TestEnum {
		
		  /**
		   * Test enum value 1
		   */
		  TEST_ENUM_VALUE_1,
		
		  /**
		   * Test enum value 2
		   */
		  TEST_ENUM_VALUE_2
		}
		'''))
	}

	@Test
	def void shouldGenerateTypes() {
		val typescript = '''
			type TestType: <"Test type description.">
				TestTypeValue1 string(1..1) <"Test string">
				TestTypeValue2 string(0..1) <"Test optional string">
				TestTypeValue3 string(0..*) <"Test string list">
				TestTypeValue4 TestType2(1..1) <"Test TestType2">
				
			type TestType2:
				TestType2Value1 number(1..1) <"Test number">
				TestType2Value2 date(1..1) <"Test date">
				
			
		'''.generateTypescript

		val types = typescript.get('types.ts').toString
		
		assertTrue(types.contains('''
			/**
			 * This file is auto-generated from the ISDA Common Domain Model, do not edit.
			 * Version: test
			 */
			
			import { ReferenceWithMeta, FieldWithMeta, MetaFields } from './metatypes';
			import {
			    } from './enums';
			
			/**
			 * Test type description.
			 */
			export interface TestType {
			  /**
			   * Test string
			   */
			  testTypeValue1?: string;
			  /**
			   * Test optional string
			   */
			  testTypeValue2?: string;
			  /**
			   * Test string list
			   */
			  testTypeValue3?: string[];
			  /**
			   * Test TestType2
			   */
			  testTypeValue4?: TestType2;
			}
			  
			export interface TestType2 {
			  /**
			   * Test number
			   */
			  testType2Value1?: number;
			  /**
			   * Test date
			   */
			  testType2Value2?: Date;
			}
			'''))
	}

    @Test
    def void shouldGenerateCalculationType() {
        val typescript = '''
			type Foo:
			     attr calculation (0..1)
        '''.generateTypescript

		val types = typescript.get('types.ts').toString
        
        assertEquals('''
	        /**
	         * This file is auto-generated from the ISDA Common Domain Model, do not edit.
	         * Version: test
	         */
	        
	        import { ReferenceWithMeta, FieldWithMeta, MetaFields } from './metatypes';
	        import {
	            } from './enums';
	        
	        export interface Foo {
	          attr?: string;
	        }
	          
        '''.toString, types.toString)
    }
    
    @Test
    def void shouldGenerateProductAndEventType() {
        val typescript = '''
			type Foo:
			     productAttr productType (0..1)
			     eventAttr eventType (0..1)
        '''.generateTypescript

		val types = typescript.get('types.ts').toString
        
        assertEquals('''
	        /**
	         * This file is auto-generated from the ISDA Common Domain Model, do not edit.
	         * Version: test
	         */
	        
	        import { ReferenceWithMeta, FieldWithMeta, MetaFields } from './metatypes';
	        import {
	            } from './enums';
	        
	        export interface Foo {
	          eventAttr?: string;
	          productAttr?: string;
	        }
	          
        '''.toString, types.toString)
    }



	@Test
	def void shouldGenerateTypesExtends() {
		val typescript = '''
			type TestType extends TestType2:
				TestTypeValue1 string(1..1) <"Test string">
				
			type TestType2:
				TestType2Value1 number(1..1) <"Test number">
				
			
		'''.generateTypescript

		val types = typescript.get('types.ts').toString
		assertTrue(types.contains('''export interface TestType extends TestType2'''))
	}

	@Test
	def void shouldGenerateMetaTypes() {
		val typescript = '''
			metaType reference string
			metaType scheme string
			metaType id string
			metaType address string
			
			type TestType:
				[metadata key]
				testTypeValue1 TestType2 (1..1)
					[metadata reference]
				testTypeValue2 TestType3 (1..1)
					[metadata location]
			
			enum TestEnum: <"Test enum description.">
				TestEnumValue1 <"Test enum value 1">
				TestEnumValue2 <"Test enum value 2">
			
			type TestType2:
				testType2Value1 number (1..1)
					[metadata reference]
				
				testType2Value2 string (1..1)
					[metadata id]
					[metadata scheme]
				
				testEnum TestEnum (1..1)
					[metadata scheme]
			
			type TestType3:
				testType3Value1 number (1..1)
			
			type TestType4:
				testType4Value1 TestType3 (1..1)
					[metadata address "pointsTo"=TestType->testTypeValue2]
			
		'''.generateTypescript

		val types = typescript.values.join('\n').toString

//		println(types)

		// types
		
		assertTrue(types.contains('''
		export interface TestType {
		  meta?: MetaFields;
		  testTypeValue1?: ReferenceWithMeta<TestType2>;
		  testTypeValue2?: FieldWithMeta<TestType3>;
		}'''))

		assertTrue(types.contains('''
		export interface TestType2 {
		  testEnum?: FieldWithMeta<TestEnum>;
		  testType2Value1?: ReferenceWithMeta<Number>;
		  testType2Value2?: FieldWithMeta<String>;
		}'''))
		
		assertTrue(types.contains('''
		export interface TestType3 {
		  testType3Value1?: number;
		}'''))
		
		assertTrue(types.contains('''
		export interface TestType4 {
		  testType4Value1?: ReferenceWithMeta<TestType3>;
		}'''))

		// meta fields

		assertTrue(types.contains('''
		export interface FieldWithMeta<T> {
		  value?: T;
		  meta?: MetaFields;
		}'''))
		
		assertTrue(types.contains('''
		export interface ReferenceWithMeta<T> {
		  globalReference?: string;
		  externalReference?: string;
		  address?: Reference;
		  value?: T;
		}'''))
		
		assertTrue(types.contains('''
		export interface MetaFields {
		  scheme?: string;
		  globalKey?: string;
		  externalKey?: string;
		  location?: Key[];
		}'''))
		
		assertTrue(types.contains('''
		export interface MetaAndTemplateFields {
		  scheme?: string;
		  globalKey?: string;
		  externalKey?: string;
		  templateGlobalReference?: string;
		  location?: Key[];
		}'''))
		
		assertTrue(types.contains('''
		export interface Key {
		  scope?: string;
		  value?: string;
		}'''))
		
		assertTrue(types.contains('''
		export interface Reference {
		  scope?: string;
		  value?: string;
		}'''))
	}

	def generateTypescript(CharSequence model) {
		val eResource = model.parseRosettaWithNoErrors.eResource

		generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
	}
}
