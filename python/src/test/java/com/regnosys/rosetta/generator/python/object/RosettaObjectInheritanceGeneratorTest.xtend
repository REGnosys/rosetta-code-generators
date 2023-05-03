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

		
		val expected=
		'''
		class A(BaseDataClass):
		    aa: Optional[str] = Field(None, description="")
		
		class B(A):
		    bb: Optional[str] = Field(None, description="")
		
		class C(B):
		    cc: Optional[str] = Field(None, description="")
		
		class D(C):
		    dd: Optional[str] = Field(None, description="")
		
		
		A.update_forward_refs()
		B.update_forward_refs()
		C.update_forward_refs()
		D.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.py").toString.contains(expected))
	}
	
	def generatePython(CharSequence model) {
    	val eResource = model.parseRosettaWithNoErrors.eResource
    	generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
    }
}