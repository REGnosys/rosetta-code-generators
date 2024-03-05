package com.regnosys.rosetta.generator.python.expression

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
class PythonExpressionGeneratorTest {
	
    @Inject extension ModelHelper
    @Inject PythonCodeGenerator generator;

	
	@Test
    def void shouldGenerateChoiceCondition() {
        val python = '''
	        type Test1:<"Test choice condition.">
	        	field1 string (0..1) <"Test string field 1">
	        	field2 string (0..1) <"Test string field 2">
	        	field3 string (0..1) <"Test string field 3">
	        	condition TestChoice: optional choice field1, field2, field3
	        '''.generatePython    
	     val expected= '''
			class Test1(BaseDataClass):
			    """
			    Test choice condition.
			    """
			    field1: Optional[str] = Field(None, description="Test string field 1")
			    """
			    Test string field 1
			    """
			    field2: Optional[str] = Field(None, description="Test string field 2")
			    """
			    Test string field 2
			    """
			    field3: Optional[str] = Field(None, description="Test string field 3")
			    """
			    Test string field 3
			    """
			    
			    @rosetta_condition
			    def condition_0_TestChoice(self):
			        return self.check_one_of_constraint('field1', 'field2', 'field3', necessity=False)
	     '''
	     assertTrue(python.toString.contains(expected))
	     
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
    