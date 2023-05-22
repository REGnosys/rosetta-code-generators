package com.regnosys.rosetta.generator.python.exceptions

import com.google.inject.Inject
import com.google.inject.Provider
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper

import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith
import org.junit.jupiter.api.Disabled
import com.regnosys.rosetta.generator.python.PythonCodeGenerator
import static org.junit.jupiter.api.Assertions.*

/*
 * Test Principal
 */
@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class PythonExceptionsTest {
	
	 @Inject extension ModelHelper
     @Inject PythonCodeGenerator generator;

	@Test
    def void testNullTypeException1() {

        val python = 
            '''
            type B:
                intValue1 int (0..1)
                intValue2 int (0..1)
                aValue A (1..1)
            '''
        var exception = assertThrows(AssertionError, [python.generatePython]);
        assertTrue(exception.getMessage.contains("Couldn't resolve reference"));

    }
    
    /* ********************************************************************** */
	/* ***				   Begin extreme case testing				   	  *** */	
	/* ********************************************************************** */
	
	@Test
	def void testDataTypes1() {
		val python = 
		'''
		type A:
		intValue1 int (0..1)
		intValue2 int (0..1)
		
		condition OneOrTwo: <"Choice rule to represent an FpML choice construct.">
			optional choice intValue1, intValue2, intValue3
		'''.generatePython
		
		val expected = 
		'''
		class A(BaseDataClass):
		  intValue1: Optional[int] = Field(None, description="")
		  intValue2: Optional[int] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_OneOrTwo(self):
		    """
		    Choice rule to represent an FpML choice construct.
		    """
		    return self.check_one_of_constraint('intValue1', 'intValue2', '', necessity=False)
		
		'''
		
		assertTrue(python.toString.contains(expected))
	}
	
	
	
	@Test
	def void testContradictoryCondition1() {
		val python = 
		'''
		type A:
		    a0 int (0..1)
		    a1 int (0..1)
		    condition: one-of
		    condition OneOrTwo: <"Choice rule to represent an FpML choice construct.">
		    	optional choice a0,a1
		'''.generatePython
		
		val expected = 
		'''
		class A(BaseDataClass):
		  a0: Optional[int] = Field(None, description="")
		  a1: Optional[int] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_(self):
		    return self.check_one_of_constraint('a0', 'a1', necessity=True)
		  
		  @rosetta_condition
		  def condition_1_OneOrTwo(self):
		    """
		    Choice rule to represent an FpML choice construct.
		    """
		    return self.check_one_of_constraint('a0', 'a1', necessity=False)
		'''
		
		assertTrue(python.toString.contains(expected))
	}
	
	@Test 
	def void testContradictoryCondition2() {
		val python = 
		'''
		type ConditionPositive:
				
			value1 int (0..1) 
			value2 int (0..1) 
			condition sameName: 
				if value1 exists then value2 exists
				and if value2 exists then value1 is absent
		'''.generatePython
		
		val expected = 
		'''
		class ConditionPositive(BaseDataClass):
		  expectedA: int = Field(..., description="")
		  
		  @rosetta_condition
		  def condition_0_sameName(self):
		    return all_elements(self.expectedA, ">", 0)
		  
		  @rosetta_condition
		  def condition_1_sameName(self):
		    return all_elements(self.expectedA, "<", 0)
		'''
		
		assertTrue(python.toString.contains(expected))
	}
	
	@Test 
	def void testContradictoryCondition3() {
		val python = 
		'''
		type ConditionPositive:
				
			expectedA int (1..1) 
			condition sameName: 
				expectedA > 0 and expectedA < 0
			
		'''.generatePython
		
		val expected = 
		'''
		class ConditionPositive(BaseDataClass):
		  expectedA: int = Field(..., description="")
		  
		  @rosetta_condition
		  def condition_0_sameName(self):
		    return (all_elements(self.expectedA, ">", 0) and all_elements(self.expectedA, "<", 0))
		'''
		
		assertTrue(python.toString.contains(expected))
	}
	
	
	@Test	
	def void testWrongCond2() {
		val python = 
		'''
		type A:
		    intValue1 int (0..1)
			intValue2 int (0..1)
		                
		    condition Rule:
		    	intValue1 < '100'
		'''.generatePython
		
		val expected = 
		'''
		class A(BaseDataClass):
		  intValue1: Optional[int] = Field(None, description="")
		  intValue2: Optional[int] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_Rule(self):
		    return all_elements(self.intValue1, "<", "100")
		'''
		
		assertTrue(python.toString.contains(expected))
		
		
	}
	
	@Test 
	def void testSameAttributes() {
		val python = 
		'''
		type A:
			intValue1 int (0..1)
			intValue1 int (0..*)
		'''.generatePython
		System.out.println(python)
		
		val expected = 
		'''
		class A(BaseDataClass):
		  intValue1: Optional[int] = Field(None, description="")
		  intValue1: List[int] = Field([], description="")
		'''
		
		assertTrue(python.toString.contains(expected))
	}
	
	@Test 
	def void testRequired() {
		val python = 
		'''
		type A:
			intValue1 int (1..1)
			intValue2 int (0..1)
			condition Rule
					required choice intValue1, intValue2
		'''.generatePython
		
		val expected = 
		'''
		class A(BaseDataClass):
		  intValue1: int = Field(..., description="")
		  intValue2: Optional[int] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_Rule(self):
		    return self.check_one_of_constraint('intValue1', 'intValue2', necessity=True)
		'''
		
		assertTrue(python.toString.contains(expected))
	}
	
	@Test 
	def void lessAndGreater() {
		val python = 
		'''
		type ConditionPositive:
		
			expectedA int (1..1) 
			condition sameName: 
				expectedA > 0
			condition sameName:
				expectedA < 0
		'''.generatePython
		System.out.println(python)
	}
	
	@Test 
	def void typeString() {
		val python = 
		'''
		type ConditionPositive:
				
			expectedA string (1..1) 
			condition stringNotNumber: 
				expectedA > 0 
			
		'''.generatePython
		
		val expected = 
		'''
		class ConditionPositive(BaseDataClass):
		  expectedA: str = Field(..., description="")
		  
		  @rosetta_condition
		  def condition_0_stringNotNumber(self):
		    return all_elements(self.expectedA, ">", 0)
		'''
		
		assertTrue(python.toString.contains(expected))
	}
	
	/* ********************************************************************** */
	/* ***				   End extreme case testing				   	  *** */	
	/* ********************************************************************** */


	def generatePython(CharSequence model) {
    	val eResource = model.parseRosetta.eResource
    	generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
    	
    }
	


	
}
