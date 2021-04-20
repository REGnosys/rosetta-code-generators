package com.regnosys.rosetta.generator.kotlin

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
import org.junit.jupiter.api.Disabled
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class KotlinModelObjectGeneratorTest {

    @Inject extension ModelHelper
    @Inject KotlinCodeGenerator generator;

    @Inject extension ParseHelper<RosettaModel>
    @Inject Provider<XtextResourceSet> resourceSetProvider;

    @Test
    //@Disabled("Test to generate the kotlin for CDM")
    def void generateCdm() {
        val dirs = newArrayList(
				// common 'annotations.rosetta & basictypes.rosetta'
                ('/home/vincent/devel/vjuge/rosetta-code-generators/kotlin/src/test/resources/rosetta-samples'),
                //cdm distribution content
				('/home/vincent/Downloads/cdm-2.85.0')
                //('/home/vincent/Downloads/cdm-2.97.8')
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
    //@Disabled
    def void shouldGenerateEnums() {
        val kotlin = '''
        enum TestEnum: <"Test enum description.">
                TestEnumValue1 <"Test enum value 1">
                TestEnumValue2 <"Test enum value 2">
                '''.generateKotlin

        val enums = kotlin.get('Enums.kt').toString
//         println(enums)
        assertTrue(enums.contains('''	
		/** 
		* Test enum description. 
		*/
		@Serializable
		enum class TestEnum {
		  /** 
		  * Test enum value 1 
		  */
		  @SerialName("TEST_ENUM_VALUE_1")
		  TEST_ENUM_VALUE_1,
		  /** 
		  * Test enum value 2 
		  */
		  @SerialName("TEST_ENUM_VALUE_2")
		  TEST_ENUM_VALUE_2
		  ;
		}
        '''))
    }

    @Test
    //@Disabled
    def void shouldGenerateTypes() {
        val kotlin = '''
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

                '''.generateKotlin

        val types = kotlin.get('Types.kt').toString
        println(types)
        assertTrue(types.contains(
        '''
		/**
		 * Test type description.
		 *
		* @param testEnum Optional test enum
		* @param testTypeValue1 Test string
		* @param testTypeValue2 Test optional string
		* @param testTypeValue3 Test string list
		* @param testTypeValue4 Test TestType2
		 */
		@Serializable
		open class TestType (
		var testEnum: TestEnum? = null,
		var testTypeValue1: String? = null,
		var testTypeValue2: String? = null,
		var testTypeValue3: MutableList<String>? = null,
		var testTypeValue4: TestType2? = null,
		)
		
		@Serializable
		open class TestType2 (
		var testEnum: TestEnum? = null,
		var testType2Value1: MutableList<Float>? = null,
		var testType2Value2: Date? = null,
		)
        '''))

    }

    @Test
    //@Disabled
    def void shouldGenerateTypesExtends() {
        val kotlin = 
        '''
		type TestType extends TestType2:
		    TestTypeValue1 string (1..1) <"Test string">
		    TestTypeValue2 int (0..1) <"Test int">

        type TestType2 extends TestType3:
	        TestType2Value1 number (0..1) <"Test number">
	        TestType2Value2 date (0..*) <"Test date">

        type TestType3:
		    TestType3Value1 string (0..1) <"Test string">
		    TestType4Value2 int (1..*) <"Test int">
        '''.generateKotlin


        val types = kotlin.get('Types.kt').toString
//        println(types)
        assertTrue(types.contains(
        '''
		@Serializable
		open class TestType (
		var testTypeValue1: String? = null,
		var testTypeValue2: Int? = null,
		)
		: TestType2()
		
		@Serializable
		open class TestType2 (
		var testType2Value1: Float? = null,
		var testType2Value2: MutableList<Date>? = null,
		)
		: TestType3()
		
		@Serializable
		open class TestType3 (
		var testType3Value1: String? = null,
		var testType4Value2: MutableList<Int>? = null,
		)
        '''))
    }

    @Test
    //@Disabled
    def void shouldGenerateMetaTypes() {
        val kotlin = '''
		metaType reference string
		metaType scheme string
		metaType id string
		
		type TestType:
			[metadata key]
			testTypeValue1 TestType2(1..1)
				[metadata reference]
		
		enum TestEnum: 
		        TestEnumValue1 
		        TestEnumValue2 
		
		type TestType2:
			testType2Value1 number (1..1)
					[metadata reference]
			testType2Value2 string (1..1)
					[metadata id]
					[metadata scheme]
			testType2Value3 TestEnum (1..1)
					[metadata scheme]
        '''.generateKotlin

        val types = kotlin.values.join('\n').toString
        // println(types)
        assertTrue(types.contains(
        '''
        @Serializable
        enum class TestEnum {
          @SerialName("TEST_ENUM_VALUE_1")
          TEST_ENUM_VALUE_1,
          @SerialName("TEST_ENUM_VALUE_2")
          TEST_ENUM_VALUE_2
          ;
        }
        '''))

    }

    @Test
//    @Disabled
//    todo : introduce condition generation later 
    def void shouldGenerateOneOfCondition() {
        val kotlin = '''
        type TestType: <"Test type with one-of condition.">
                field1 string (0..1) <"Test string field 1">
                field2 string (0..1) <"Test string field 2">
                field3 number (0..1) <"Test number field 3">
                field4 number (0..*) <"Test number field 4">
                condition: one-of
        '''.generateKotlin

        val types = kotlin.get('Types.kt').toString
        // println(types)
        assertTrue(types.contains('''
		/**
		 * Test type with one-of condition.
		 *
		* @param field1 Test string field 1
		* @param field2 Test string field 2
		* @param field3 Test number field 3
		* @param field4 Test number field 4
		 */
		@Serializable
		open class TestType (
		var field1: String? = null,
		var field2: String? = null,
		var field3: Float? = null,
		var field4: MutableList<Float>? = null,
		)
        '''))
    }

    def generateKotlin(CharSequence model) {
        val eResource = model.parseRosettaWithNoErrors.eResource

        generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
    }
}
