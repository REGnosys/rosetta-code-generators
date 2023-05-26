package com.regnosys.rosetta.generator.python.exceptions

import com.google.inject.Inject
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper

import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith
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
    def void testNoneExistingTypeAtrtribute() {
		
		try{
	         
            '''
            type B:
                intValue1 int (0..1)
                intValue2 int (0..1)
                aValue A (1..1)
            '''.generatePython
            
        }catch(Exception ex){
        	assertTrue(ex.getMessage.contains("Attribute type is null"));     	
        }

    }
    
    //Conditional test: Adding a non-existing attribute in acondition     
    @Test
    def void testNoneExistingTypeCondition() {
		
		try{
            '''
            type TestType: <"Test type with one-of condition.">
            	field1 string (0..1) <"Test string field 1">
                field2 string (0..1) <"Test string field 2">
                condition BusinessCentersChoice: <"Choice rule to represent an FpML choice construct.">
                	 if field1 exists
                	 	then field3 > 0
            '''.generatePython
            
        }catch(Exception ex){
        	assertTrue(ex.getMessage.contains("Unsupported callable type"));
        }

    }
    
   //Conditional test: Adding a non-existing attribute in acondition     
    @Test
    def void testNoneExistingTypeSuperType() {
    
        try{
	        '''
	        type TestType1 extends TestType2:
	        TestType2Value1 number (0..1) <"Test number">
	        TestType2Value2 date (0..*) <"Test date">
	        '''.generatePython
        }catch(Exception ex){
        	assertTrue(ex.getMessage.contains("SuperType is null"))
        }      
    }
    

	def generatePython(CharSequence model) {
    	val eResource = model.parseRosetta.eResource
    	generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
    	
    }
	


	
}
