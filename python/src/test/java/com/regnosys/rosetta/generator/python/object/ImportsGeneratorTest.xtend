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
class ImportsGeneratorTest {

    @Inject extension ModelHelper
    @Inject PythonCodeGenerator generator;

    @Test
    def void testImportsGenerator() {
        val pythonCode = 
            '''namespace rosetta_dsl.test.semantic.deep_path : <"generate Python unit tests from Rosetta.">
               type Deep1:
                   attr int (1..1)
                type Bar1:
                   deep1 Deep1 (1..1)
            '''.generatePython
        val expected = '''class Bar1(BaseDataClass):
    deep1: rosetta_dsl.test.semantic.deep_path.Deep1.Deep1 = Field(..., description="")

import rosetta_dsl 
import rosetta_dsl.test.semantic.deep_path.Deep1'''
        assertTrue(pythonCode.toString.contains(expected))
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