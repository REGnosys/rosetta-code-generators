package com.regnosys.rosetta.generators.csv

import com.google.inject.Inject
import com.regnosys.rosetta.generators.test.TestUtil
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import java.io.File
import java.nio.file.Files
import java.nio.file.Paths
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Disabled

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class CsvGeneratorTest {

	@Inject extension ModelHelper

	@Inject extension TestUtil

	@Inject CsvGenerator generator;

	def generate(CharSequence model) {
		val m = model.parseRosettaWithNoErrors
		val resourceSet = m.eResource.resourceSet

		generator.afterAllGenerate(resourceSet, #{m}, "test")
	}

	@org.junit.Test
	@Disabled
	def void generateCdm() {
		val dirs = #[
			'../../../finos/common-domain-model/rosetta-source/src/main/rosetta',
			'../../rosetta-dsl/rosetta-runtime/src/main/resources/model'
		]

		val models = parseRosetta(dirs.getRosettaFileContents)

		val generatedFiles = generator.afterAllGenerate(models.iterator.next.eResource.resourceSet, models, "test")

		val rootDir = System.getProperty("user.dir")

		generatedFiles.forEach [ fileName, contents |
			{
				val pathString = rootDir + "/" + fileName
				val path = Paths.get(pathString)
				val file = new File(pathString);
				file.getParentFile().mkdirs();
				Files.write(path, contents.toString.bytes)
			}
		]
	}

	@Test
	def void shouldGenerateCsvTypesFile() {
		val csv = '''
			
			type TestType1: <"Test type description.">
				attribute1 string (1..1) <"Test attribute 1">
				attribute2 number (0..*) <"Test attribute 2">
				
			type TestType2: <"Test type description.">
				testType1 TestType1 (1..*) <"Test 
				    Type attribute \"quote1\" 'quote2' ">
				noDef int (0..1)
			
		'''.generate

		val enumString = csv.get('types.csv').toString;

		assertEquals(
			'''
			"Category","Namespace","Type Name","Attribute Name","Type","Cardinality","Definition"
			"data type","com.rosetta.test.model","TestType1","","","","Test type description."
			"attribute","com.rosetta.test.model","TestType1","attribute1","string","(1..1)","Test attribute 1"
			"attribute","com.rosetta.test.model","TestType1","attribute2","number","(0..*)","Test attribute 2"
			"data type","com.rosetta.test.model","TestType2","","","","Test type description."
			"attribute","com.rosetta.test.model","TestType2","testType1","TestType1","(1..*)","Test  	    Type attribute 'quote1' 'quote2' "
			"attribute","com.rosetta.test.model","TestType2","noDef","int","(0..1)",""''',
			enumString
		)

	}

	@Test
	def void shouldGenerateCsvEnumsFile() {
		val csv = '''
			enum TestEnum: <"Test enum description.">
				TestEnumValue1 <"Test enum value 1">
				TestEnumValue2 displayName "Test Enum Value 2" <"Test enum value 2">
				
			
		'''.generate

		val enumString = csv.get('enums.csv').toString;

		assertEquals(
			'''
			"Category","Namespace","Enum Name","Enum Value","Definition"
			"enum","com.rosetta.test.model","TestEnum","","Test enum description."
			"enum value","com.rosetta.test.model","TestEnum","TestEnumValue1","Test enum value 1"
			"enum value","com.rosetta.test.model","TestEnum","TestEnumValue2","Test enum value 2"''',
			enumString
		)

	}

}
