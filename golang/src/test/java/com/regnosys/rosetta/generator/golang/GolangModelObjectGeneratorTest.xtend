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
import org.eclipse.xtext.testing.util.ParseHelper
import org.eclipse.xtext.resource.XtextResourceSet
import com.google.inject.Provider
import org.eclipse.lsp4j.generator.TypeAdapterImpl
import org.junit.jupiter.api.Disabled
import java.io.IOException

//import org.junit.jupiter.api.Disabled

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
	@Inject GolangCodeGenerator generator;

	@Inject extension ParseHelper<RosettaModel>
	@Inject Provider<XtextResourceSet> resourceSetProvider;

	@Test
	@Disabled("Test to generate the golang for CDM")
	def void generateCdm() {

		val dirs = newArrayList(			
			('rosetta-cdm/src/main/rosetta'),
			('rosetta-dsl/com.regnosys.rosetta.lib/src/main/java/model')
			//('/home/denis/Downloads/cdm-2.51.0/cdm-distribution-2.51.0/common-domain-model'),
			//('/home/denis/Downloads/Regnosys/rosetta-dsl/com.regnosys.rosetta.lib/src/main/java/model')			
		);

		val resourceSet = resourceSetProvider.get	

		dirs.map[new File(it)].map[listFiles[it.name.endsWith('.rosetta')]].flatMap [
			map[Files.readAllBytes(toPath)].map[new String(it)]
		].forEach[parse(resourceSet)]

		val rosettaModels = resourceSet.resources.map[contents.filter(RosettaModel)].flatten.toList

		val generatedFiles = generator.afterGenerate(rosettaModels)
		
		val enumsDir = Files.createDirectories(Paths.get("cdm/enums"))
		val metaTypesDir = Files.createDirectories(Paths.get("cdm/metatypes"))
		val typesDir = Files.createDirectories(Paths.get("cdm/types"))
		val funcDir = Files.createDirectories(Paths.get("cdm/functions"))
		
		generatedFiles.forEach [ fileName, contents |{
			switch fileName{
				case "enums.go": Files.write(enumsDir.resolve(fileName), contents.toString.bytes)
				case "metatypes.go" : Files.write(metaTypesDir.resolve(fileName), contents.toString.bytes)
				case "types.go" : Files.write(typesDir.resolve(fileName), contents.toString.bytes)
				case "functions.go" : Files.write(funcDir.resolve(fileName), contents.toString.bytes)
				default : throw new IOException("...")
			}
		}
			
		]
	}

	@Test
	def void shouldGenerateEnums() {
		val golang = '''
			enum TestEnum: <"Test enum description.">
				TestEnumValue1 <"Test enum value 1">
				TestEnumValue2 <"Test enum value 2">
		'''.generateGolang
		val fileName = "cdm/TestEnum/TestEnum.go"  
    	val enumString = new String(Files.readAllBytes(Paths.get(fileName))); 
     	
		assertTrue(enumString.contains('''
		/**
		 * This file is auto-generated from the ISDA Common Domain Model, do not edit.
		 * Version: test
		 */
		  package TestEnum
		  import . "cdm/enums"
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
				TestTypeValue1 string(1..1) <"Test string">
				TestTypeValue2 string(0..1) <"Test optional string">
				TestTypeValue3 string(0..*) <"Test string list">
				TestTypeValue4 TestType2(1..1) <"Test TestType2">
				
			type TestType2:
				TestType2Value1 number(1..1) <"Test number">
				TestType2Value2 date(1..1) <"Test date">
		'''.generateGolang

		val types = golang.get('types.go').toString
		println(types)
		assertTrue(types.contains('''
		package types
		
		/**
		 * This file is auto-generated from the ISDA Common Domain Model, do not edit.
		 * Version: test
		 */
		
		import . "cdm/metatypes";
		import . "cdm/enums";
		
		
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
		}
		  
		type TestType2 struct {
		  /**
		   * Test number
		   */
		  TestType2Value1 cdmbase.Decimal;
		  /**
		   * Test date
		   */
		  TestType2Value2 basemodel.Date;
		}
			'''))

	}	
	
	@Test
	@Disabled("Not applicable to Go")
	def void shouldGenerateTypesExtends() {
		val golang = '''
			type TestType extends TestType2:
				TestTypeValue1 string(1..1) <"Test string">
				
			type TestType2:
				TestType2Value1 number(1..1) <"Test number">
				
			
		'''.generateGolang

		val types = golang.get('types.go').toString
		assertTrue(types.contains('''export interface TestType extends TestType2'''))
	}

	@Test	
	def void shouldGenerateMetaTypes() {
		val golang = '''
			metaType reference string
			metaType scheme string
			metaType id string
			
			type TestType:
				[metadata key]
				TestTypeValue1 TestType2(1..1)
					[metadata reference]
			
			type TestType2:
				TestType2Value1 number(1..1)
					[metadata reference]
					
				TestType2Value2 string(1..1)
					[metadata id]
					[metadata scheme]
							'''.generateGolang

		val types = golang.values.join('\n').toString
		println(types)
		
		assertTrue(types.contains('''
		type FieldWithMeta struct {
		  Value interface{};
		  Meta MetaFields;
		}'''))

		assertTrue(types.contains('''
		type TestType struct {
		  TestTypeValue1 ReferenceWithMeta;
		  Meta MetaFields;
		}'''))

		assertTrue(types.contains('''
		type TestType2 struct {
		  TestType2Value1 ReferenceWithMeta;
		  TestType2Value2 FieldWithMeta;
		}'''))

	}

	def generateGolang(CharSequence model) {
		val eResource = model.parseRosettaWithNoErrors.eResource

		generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
	}
}
