package com.regnosys.rosetta.generator.python.object

import com.google.inject.Inject
import com.regnosys.rosetta.generator.python.PythonCodeGenerator
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
            TEST_ENUM_VALUE_1 = "TestEnumValue1"
            """
            Test enum value 1
            """
            TEST_ENUM_VALUE_2 = "TestEnumValue2"
            """
            Test enum value 2
            """
            TEST_ENUM_VALUE_3 = "TestEnumValue3"
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
        val m = model.parseRosettaWithNoErrors
        val resourceSet = m.eResource.resourceSet
        val version = m.version
        
        val result = newHashMap
        result.putAll(generator.beforeAllGenerate(resourceSet, #{m}, version))
        result.putAll(generator.beforeGenerate(m.eResource, m, version))
        result.putAll(generator.generate(m.eResource, m, version))
        result.putAll(generator.afterGenerate(m.eResource, m, version))
        result.putAll(generator.afterAllGenerate(resourceSet, #{m}, version))
        
        result
    }
}