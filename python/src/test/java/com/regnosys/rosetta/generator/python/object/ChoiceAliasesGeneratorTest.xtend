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
class ChoiceAliasGeneratorTest {

    @Inject extension ModelHelper
    @Inject PythonCodeGenerator generator;

    @Test
    def void testChoiceAliasGenerator() {
        val pythonCode = 
        '''
        type Bar1:
            deep1 Deep1 (1..1)
            b1 int (1..1)
            a int (1..1)

        type Bar2:
            deep1 Deep1 (1..1)
            b1 int (1..1)
            c int (1..1)

        type Bar4:
            deep1 Deep1 (1..1)
            b1 int (1..1)

        type Bar3:
            bar2 Bar2(0..1)
            bar4 Bar4(0..1)
            condition Choice: one-of 

        type Foo:
            bar1 Bar1 (0..1)
            bar3 Bar3 (0..1)
            condition Choice: one-of
            condition Test:
               if bar1 exists then
                   bar1->deep1->attr = 3
               else if bar3 exists then
                   bar3->>deep1->attr =3
               else False 

        type FooBar:
            foo Foo (1..1)
            condition Test: 
               foo->>deep1->attr = 3

        type Deep1:
            attr int (1..1)
        '''.generatePython
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