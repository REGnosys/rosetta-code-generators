package com.regnosys.rosetta.generator.scala

import com.google.inject.Inject
import com.google.inject.Provider
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import java.io.File
import java.nio.file.Files
import java.nio.file.Paths
import org.eclipse.xtext.resource.XtextResourceSet
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.eclipse.xtext.testing.util.ParseHelper
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.Disabled

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class ScalaModelObjectGeneratorTest {

	@Inject extension ModelHelper
	@Inject ScalaCodeGenerator generator;

	@Inject extension ParseHelper<RosettaModel>
	@Inject Provider<XtextResourceSet> resourceSetProvider;

	@Test
	//@Disabled("Test to generate the scala for CDM")
	def void generateCdm() {
		val dirs = newArrayList(
			('/Users/hugohills/code/src/github.com/REGnosys/rosetta-cdm/src/main/rosetta'),
			('/Users/hugohills/code/src/github.com/REGnosys/rosetta-dsl/com.regnosys.rosetta.lib/src/main/java/model')
		);

		val resourceSet = resourceSetProvider.get

		dirs.map[new File(it)].map[listFiles[it.name.endsWith('.rosetta')]].flatMap[
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
		val scala = '''
			enum TestEnum: <"Test enum description.">
				TestEnumValue1 <"Test enum value 1">
				TestEnumValue2 <"Test enum value 2">
		'''.generateScala

		val enums = scala.get('Enums.scala').toString
		println(enums)
		assertTrue(enums.contains('''
		/**
		 * This file is auto-generated from the ISDA Common Domain Model, do not edit.
		 * Version: test
		 */
		package org.isda.cdm
		
		/**
		 * Test enum description.
		 */
		object TestEnum extends Enumeration {
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
				TestTypeValue1 string(1..1) <"Test string">
				TestTypeValue2 string(0..1) <"Test optional string">
				TestTypeValue3 string(0..*) <"Test string list">
				TestTypeValue4 TestType2(1..1) <"Test TestType2">
				
			type TestType2:
				TestType2Value1 number(1..*) <"Test number list">
				TestType2Value2 date(0..1) <"Test date">
				
			
		'''.generateScala

		val types = scala.get('Types.scala').toString
		println(types)
		assertTrue(types.contains('''
			/**
			 * This file is auto-generated from the ISDA Common Domain Model, do not edit.
			 * Version: test
			 */
			package org.isda.cdm
			
			import org.isda.cdm.metafields.{ ReferenceWithMeta, FieldWithMeta, MetaFields }
			
			/**
			 * Test type description.
			 * 
			 * @param TestTypeValue1 Test string
			 * @param TestTypeValue2 Test optional string
			 * @param TestTypeValue3 Test string list
			 * @param TestTypeValue4 Test TestType2
			 */
			case class TestType(testTypeValue1: String,
			    testTypeValue2: Option[String],
			    testTypeValue3: List[String],
			    testTypeValue4: TestType2) {
			}
			
			case class TestType2(testType2Value1: List[scala.math.BigDecimal],
			    testType2Value2: Option[java.time.LocalDate]) {
			}
			'''))

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

		val types = scala.get('Types.scala').toString
		println(types)
		assertTrue(types.contains('''
		case class TestType(testTypeValue1: String,
		    testTypeValue2: Option[Int],
		    override val testType2Value1: Option[scala.math.BigDecimal],
		    override val testType2Value2: List[java.time.LocalDate],
		    override val testType3Value1: Option[String],
		    override val testType4Value2: List[Int])
		  extends TestType2(testType2Value1: Option[scala.math.BigDecimal],
		      testType2Value2: List[java.time.LocalDate],
		      testType3Value1: Option[String],
		      testType4Value2: List[Int]) {
		}
		'''))
		assertTrue(types.contains('''
		case class TestType2(testType2Value1: Option[scala.math.BigDecimal],
		    testType2Value2: List[java.time.LocalDate],
		    override val testType3Value1: Option[String],
		    override val testType4Value2: List[Int])
		  extends TestType3(testType3Value1: Option[String],
		      testType4Value2: List[Int]) {
		}
		'''))
		assertTrue(types.contains('''
		case class TestType3(testType3Value1: Option[String],
		    testType4Value2: List[Int]) {
		}
		'''))
	}

	@Test
	def void shouldGenerateMetaTypes() {
		val scala = '''
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
					
		'''.generateScala

		val types = scala.values.join('\n').toString
		println(types)
		assertTrue(types.contains('''
		case class MetaFields(scheme: Option[String],
		    globalKey: Option[String],
		    externalKey: Option[String]) {
		}'''))
		
		assertTrue(types.contains('''
		case class ReferenceWithMeta[T](value: Option[T],
		    globalReference: Option[String],
		    externalReference: Option[String]) {
		}'''))
		
		assertTrue(types.contains('''
		case class FieldWithMeta[T](value: Option[T],
		    meta: Option[MetaFields]) {
		}'''))

		assertTrue(types.contains('''
		case class TestType(testTypeValue1: ReferenceWithMeta[TestType2],
		    meta: Option[MetaFields]) {
		}'''))

		assertTrue(types.contains('''
		case class TestType2(testType2Value1: ReferenceWithMeta[scala.math.BigDecimal],
		    testType2Value2: FieldWithMeta[String],
		    testEnum: FieldWithMeta[TestEnum.Value]) {
		}'''))

	}

	def generateScala(CharSequence model) {
		val eResource = model.parseRosettaWithNoErrors.eResource

		generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
	}
}
