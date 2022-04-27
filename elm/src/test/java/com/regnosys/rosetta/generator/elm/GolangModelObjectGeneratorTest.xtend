package com.regnosys.rosetta.generator.elm

import com.google.inject.Inject
import com.google.inject.Provider
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import org.eclipse.xtext.resource.XtextResourceSet
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.eclipse.xtext.testing.util.ParseHelper
import org.junit.jupiter.api.Disabled
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*

//import org.junit.jupiter.api.Disabled

/**
 * The parser of rosetta files has a particular requirement:
 * namespace declaration should not have any comments,
 * so all text ":<...>" should be removed from the namespace line
 * if present.
 */

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class GolangModelObjectGeneratorTest {

	@Inject extension ModelHelper
	@Inject ElmCodeGenerator generator;

	@Inject extension ParseHelper<RosettaModel>
	@Inject Provider<XtextResourceSet> resourceSetProvider;


	@Test
	def void shouldGenerateEnums() {
		val golang = '''
			enum TestEnum: <"Test enum description.">
				TestEnumValue1 <"Test enum value 1">
				TestEnumValue2 <"Test enum value 2">
		'''.generateGolang
		 
    	val enums = golang.get('Com/Rosetta/Test/Model/Enum.elm').toString; 
     	println(enums)
     	
		assertTrue(enums.contains('''
		module Com.Rosetta.Test.Model.Enum exposing (..)
		
		
		-- This file is auto-generated from the ISDA Common Domain Model, do not edit.
		-- Version: test
		
		
		  -- Test enum description.
		type TestEnum
		    =   TestEnumValue1
		    |   TestEnumValue2
		    ''')
		  )
	}

	@Test
	def void shouldGenerateTypes() {
		val golang = '''
			type TestType: <"Test type description.">
				testTypeValue1 string (1..1) <"Test string">
				testTypeValue2 string (0..1) <"Test optional string">
				testTypeValue3 string (0..*) <"Test string list">
				testTypeValue4 TestType2 (1..1) <"Test TestType2">
				testTypeValue5 TestType2 (0..*) <"Test TestType2 list">
				
			type TestType2:
				testType2Value1 number (1..1) <"Test number">
				testType2Value2 date (1..1) <"Test date">
				
			type TestType3:
			    tradeDate date (1..1)
			    eventTimestamp zonedDateTime (1..1)
		'''.generateGolang

		val types = golang.get('Com/Rosetta/Test/Model/Type.elm').toString
		
		
		println(types)
		
		assertTrue(types.contains( '''
		module Com.Rosetta.Test.Model.Type exposing (..)
		
		import Morphir.SDK.LocalDate exposing (LocalDate)
		import Morphir.SDK.LocalTime exposing (LocalTime)
		import Com.Rosetta.Model.Type exposing (ZonedDateTime)
		import Com.Rosetta.Model.Type exposing (Date)
		
		
		
		-- This file is auto-generated from the ISDA Common Domain Model, do not edit.
		-- Version: test
		
		
		  -- Test type description.
		type alias TestType =
		    {   testTypeValue1 : String -- Test string
		    ,   testTypeValue2 : Maybe String -- Test optional string
		    ,   testTypeValue3 : List String -- Test string list
		    ,   testTypeValue4 : TestType2 -- Test TestType2
		    ,   testTypeValue5 : List TestType2 -- Test TestType2 list
		    }
		type alias TestType2 =
		    {   testType2Value1 : Float -- Test number
		    ,   testType2Value2 : LocalDate -- Test date
		    }
		type alias TestType3 =
		    {   tradeDate : LocalDate 
		    ,   eventTimestamp : ZonedDateTime 
		    }
		'''))


	}	
	
	

	def generateGolang(CharSequence model) {
		val eResource = model.parseRosettaWithNoErrors.eResource

		generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
	}
}
