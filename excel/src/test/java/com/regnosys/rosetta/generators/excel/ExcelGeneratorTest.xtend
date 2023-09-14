package com.regnosys.rosetta.generators.excel

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
import java.util.Base64
import org.apache.poi.xssf.usermodel.XSSFWorkbook
import java.io.ByteArrayInputStream

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class ExcelGeneratorTest {

	@Inject extension ModelHelper

	@Inject extension TestUtil

	@Inject ExcelGenerator generator;

	def generate(CharSequence model) {
		val m = model.parseRosettaWithNoErrors
		val resourceSet = m.eResource.resourceSet

		generator.afterAllGenerate(resourceSet, #{m}, "test")
	}

	@Test
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
				Files.write(path, Base64.decoder.decode(contents.toString))
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
				
			enum TestEnum: <"Test enum description.">
				TestEnumValue1 <"Test enum value 1">
				TestEnumValue2 displayName "Test Enum Value 2" <"Test enum value 2">
				
				
			
		'''.generate

		val contents = csv.get('model.xlsx').toString;

		val excelFile = Base64.decoder.decode(contents.toString)

		val workbook = new XSSFWorkbook(new ByteArrayInputStream(excelFile));

		val typesSheet = workbook.getSheet("types")
		assertNotNull(typesSheet)

		assertEquals(7, typesSheet.size)

		val typesHeader = typesSheet.toList.get(0)
		assertEquals(7, typesHeader.size)

		val enumsSheet = workbook.getSheet("enums")
		assertNotNull(enumsSheet)

		assertEquals(4, enumsSheet.size)

		val enumsHeader = enumsSheet.toList.get(0)
		assertEquals(5, enumsHeader.size)

	}

}
