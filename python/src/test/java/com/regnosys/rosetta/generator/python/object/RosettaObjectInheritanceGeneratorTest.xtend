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

class RosettaObjectInheritanceGeneratorTest {

    @Inject extension ModelHelper
    @Inject PythonCodeGenerator generator;



    @Test
    def void shouldGeneratePythonClassWithMultipleParents() {
        val python = '''
            type D extends C:
                dd string (0..1)
            type B extends A:
                bb string (0..1)
            type C extends B:
                cc string (0..1)
            type A:
                aa string (0..1)
        '''.generatePython

        val expectedA=
        '''
        class A(BaseDataClass):
            aa: Optional[str] = Field(None, description="")
        '''
        val expectedB=
        '''
        class B(A):
            bb: Optional[str] = Field(None, description="")
        '''
        val expectedC=
        '''
        class C(B):
            cc: Optional[str] = Field(None, description="")
        '''
        val expectedD=
        '''
        class D(C):
            dd: Optional[str] = Field(None, description="")
        '''
        assertTrue(python.toString.contains(expectedA))
        assertTrue(python.toString.contains(expectedB))
        assertTrue(python.toString.contains(expectedC))
        assertTrue(python.toString.contains(expectedD))
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