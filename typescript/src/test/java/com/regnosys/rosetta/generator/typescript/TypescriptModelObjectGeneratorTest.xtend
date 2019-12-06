package com.regnosys.rosetta.generator.typescript

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
import org.eclipse.xtext.testing.util.ParseHelper
import org.eclipse.xtext.resource.XtextResourceSet
import com.google.inject.Provider
import org.junit.jupiter.api.Disabled

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class TypescriptModelObjectGeneratorTest {

	@Inject extension ModelHelper
	@Inject TypescriptCodeGenerator generator;

	@Inject extension ParseHelper<RosettaModel>
	@Inject Provider<XtextResourceSet> resourceSetProvider;

	@Test
	@Disabled("Test to generate the typescript for CDM")
	def void generateCdm() {
		val dirs = newArrayList(
			('rosetta-cdm/src/main/rosetta'),
			('rosetta-dsl/com.regnosys.rosetta.lib/src/main/java/model')
		);

		val resourceSet = resourceSetProvider.get

		dirs.map[new File(it)].map[listFiles[it.name.endsWith('.rosetta')]].flatMap [
			map[Files.readAllBytes(toPath)].map[new String(it)]
		].forEach[parse(resourceSet)]

		val rosettaModels = resourceSet.resources.map[contents.filter(RosettaModel)].flatten.toList

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
		println(types)
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
			
			type TestType:
				[metadata key]
				TestTypeValue1 TestType2(1..1)
					[metadata reference]
					
			enum TestEnum: <"Test enum description.">
				TestEnumValue1 <"Test enum value 1">
				TestEnumValue2 <"Test enum value 2">
			
			type TestType2:
				TestType2Value1 number(1..1)
					[metadata reference]
					
				TestType2Value2 string(1..1)
					[metadata id]
					[metadata scheme]
				
				testEnum TestEnum(1..1)
					[metadata scheme]
					
		'''.generateTypescript

		val types = typescript.values.join('\n').toString

		assertTrue(types.contains('''
		export interface MetaFields {
		  reference?: string;
		  scheme?: string;
		  id?: string;
		  globalKey?: String;
		  externalKey?: String;
		}'''))

		assertTrue(types.contains('''
		export interface TestType {
		  testTypeValue1?: ReferenceWithMeta<TestType2>;
		  meta?: MetaFields;
		}'''))

		assertTrue(types.contains('''
		  export interface TestType2 {
		    testType2Value1?: ReferenceWithMeta<Number>;
		    testType2Value2?: FieldWithMeta<String>;
		    testEnum?: FieldWithMeta<TestEnum>;
		  }'''))

	}

	def generateTypescript(CharSequence model) {
		val eResource = model.parseRosettaWithNoErrors.eResource

		generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
	}
}
