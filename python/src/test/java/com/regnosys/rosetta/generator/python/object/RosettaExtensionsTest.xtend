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

		
		val expectedBaz=
		'''
		class Baz(BaseDataClass):
		  pass
		'''
		
		val expectedBar=
		'''
		class Bar(Baz):
		  pass
		'''
		
		val expectedFoo=
		'''
		class Foo(Bar):
		  pass
		'''
		
		assertTrue(python.toString.contains(expectedBaz))
		assertTrue(python.toString.contains(expectedBar))	
		assertTrue(python.toString.contains(expectedFoo))
		
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
		
		val expectedBar=
		'''
		class Bar(Enum):
		  BAR = "BAR"
		  FOO_0 = "FOO_0"
		  FOO_1 = "FOO_1"
		'''
		
		val expectedBaz=
		'''
		class Baz(Enum):
		  BAR = "BAR"
		  BAZ = "BAZ"
		  FOO_0 = "FOO_0"
		  FOO_1 = "FOO_1"
		'''
		
		val expectedFoo=
		'''
		class Foo(Enum):
		  FOO_0 = "FOO_0"
		  FOO_1 = "FOO_1"
		'''
		
		assertTrue(python.toString.contains(expectedBar))
		assertTrue(python.toString.contains(expectedBaz))
		assertTrue(python.toString.contains(expectedFoo))
	}
	
	
	def generatePython(CharSequence model) {
    	val eResource = model.parseRosettaWithNoErrors.eResource
    	generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
    	
    }
}