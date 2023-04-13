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

class RosettaExtensionsTest {

    @Inject extension ModelHelper
    @Inject PythonCodeGenerator generator;

	
	@Test
	def testSuperClasses() {
		val python = '''
			namespace test
			
			type Foo extends Bar:
			type Bar extends Baz:
			type Baz:
		'''.generatePython

		
		val expected=
		'''
		class Baz(BaseDataClass):
		    pass
		
		class Bar(Baz):
		    pass
		
		class Foo(Bar):
		    pass
		
		
		Baz.update_forward_refs()
		Bar.update_forward_refs()
		Foo.update_forward_refs()
		'''
		
		assertTrue(python.toString.contains(expected))
	}
	
	
	@Test 
	def testEnumValue() {
		val python = '''
			namespace test
			version "1.2.3"
			
			enum Foo:
				foo0 foo1
			
			enum Bar extends Foo:
				bar
			enum Baz extends Bar:
				baz
		'''.generatePython

		
		val expected=
		'''
		class Bar(Enum):
		    BAR = "BAR"
		    FOO_0 = "FOO_0"
		    FOO_1 = "FOO_1"
		
		class Baz(Enum):
		    BAR = "BAR"
		    BAZ = "BAZ"
		    FOO_0 = "FOO_0"
		    FOO_1 = "FOO_1"
		
		class Foo(Enum):
		    FOO_0 = "FOO_0"
		    FOO_1 = "FOO_1"
		'''
		
		assertTrue(python.get("Enums.py").toString.contains(expected))
	}
	
	
	def generatePython(CharSequence model) {
    	val eResource = model.parseRosettaWithNoErrors.eResource
    	generator.afterGenerateTest(eResource.contents.filter(RosettaModel).toList)
    	
    }
}