package com.regnosys.rosetta.generator.python.object

import com.google.inject.Inject
import com.regnosys.rosetta.generator.python.PythonCodeGenerator
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class PythonEnumGeneratorTest {
	
    @Inject extension ModelHelper
    @Inject PythonCodeGenerator generator;


	
	
	@Test
    def void shouldGenerateEnums() {
        val python = '''
	        enum TestEnum: <"Test enum description.">
	        	TestEnumValue1 <"Test enum value 1">
	        	TestEnumValue2 <"Test enum value 2">
	        	TestEnumValue3 <"Test enum value 3">
	        	_1 displayName "1" <"Rolls on the 1st day of the month.">
	        '''.generatePython

        val enums = python.toString
        val expected = '''
        class TestEnum(Enum):
          """
          Test enum description.
          """
          TEST_ENUM_VALUE_1 = "TEST_ENUM_VALUE_1"
          """
          Test enum value 1
          """
          TEST_ENUM_VALUE_2 = "TEST_ENUM_VALUE_2"
          """
          Test enum value 2
          """
          TEST_ENUM_VALUE_3 = "TEST_ENUM_VALUE_3"
          """
          Test enum value 3
          """
          _1 = "1"
          """
          Rolls on the 1st day of the month.
          """
        '''
        assertTrue(enums.contains(expected))
    }
    
    def generatePython(CharSequence model) {
    	val eResource = model.parseRosettaWithNoErrors.eResource
    	generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
    }
    
	
}