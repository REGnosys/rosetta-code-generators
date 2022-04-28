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
import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.StandardOpenOption

//import org.junit.jupiter.api.Disabled

/**
 * The parser of rosetta files has a particular requirement:
 * namespace declaration should not have any comments,
 * so all text ":<...>" should be removed from the namespace line
 * if present.
 */

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class ElmModelObjectGeneratorTest {

	@Inject extension ModelHelper
	@Inject ElmCodeGenerator generator;

	@Inject extension ParseHelper<RosettaModel>
	@Inject Provider<XtextResourceSet> resourceSetProvider;

	@Test
	def void shouldGenerateRules() {
		val golang = '''
				body Authority CFTC
				corpus Regulation "CFTC 17 CFR Parts 45" Part45
				corpus Software "Morphir" Morphir
				
				report CFTC Part45 Morphir in T+1
				    when IsReportableEvent
				    with type CFTCPart45TransactionReport
				    
				eligibility rule IsReportableEvent
				    filter when ReportableEvent -> reportableTrade exists
				
				type CFTCPart45TransactionReport:
				    tradeDate date (1..1)
				        [ruleReference TradeDate]
«««				    eventTimestamp zonedDateTime (0..1)
«««				        [ruleReference EventTimestampRule]
				    eventTimestamp1 zonedDateTime (0..1)
				        [ruleReference EventTimestampRule1]
«««				    foo1 string (0..1)
«««				        [ruleReference Foo1]
				        
				
				reporting rule TradeDate <"Trade Date">
				    extract ReportableEvent -> reportableTrade -> trade -> tradeDate 
				    as "Trade timestamp"
«««				
«««				reporting rule EventTimestampRule
«««				        extract ReportableEvent -> originatingWorkflowStep -> timestamp
«««				            filter [ item -> qualification = EventTimestampQualificationEnum -> eventCreationDateTime ]
«««				            map [ item -> dateTime ]
«««				            only-element
«««				        as "30 Event timestamp"
«««				
				reporting rule EventTimestampRule1
				        extract ReportableEvent -> originatingWorkflowStep -> timestamp -> dateTime only-element
«««
«««				reporting rule Foo1
«««				        extract ReportableEvent -> originatingWorkflowStep -> timestamp -> foo only-element
«««				        as "30 Event timestamp"
						        
				type ReportableEvent:
				    [rootType]
				    originatingWorkflowStep WorkflowStep (1..1)
				    reportableTrade TradeState (1..1)
				
				type WorkflowStep:
				    [metadata key]
				    [rootType]
				    timestamp EventTimestamp (1..*)
				
				type EventTimestamp:
				    dateTime zonedDateTime (1..1)
				    foo string (1..*)
				    qualification EventTimestampQualificationEnum (1..1)
				
				type TradeState:
				    [metadata key]
				    [rootType]
				    trade Trade (1..1)
				
				type Trade:
				    [metadata key]
				    tradeDate date (1..1)
				        [metadata id]
				
				enum EventTimestampQualificationEnum:
				    clearingDateTime
				    clearingConfirmationDateTime
				    eventCreationDateTime
		 '''.generateCode

    golang.forEach[filename, contents| 
Files.createDirectories(Path.of('/Users/user/Library/Application Support/JetBrains/IdeaIC2022.1/scratches/elm-project/src/' + filename).parent)
    	Files.write(Path.of('/Users/user/Library/Application Support/JetBrains/IdeaIC2022.1/scratches/elm-project/src/' + filename), contents.toString.bytes,StandardOpenOption.TRUNCATE_EXISTING )
    ]
   
    	val rules = golang.get('Com/Rosetta/Test/Model/Rule.elm').toString; 


	
     	
		assertTrue(rules.contains('''
		module Com.Rosetta.Test.Model.Rule exposing (..)
		
		import Morphir.SDK.LocalDate exposing (LocalDate)
		import Morphir.SDK.LocalTime exposing (LocalTime)
		import Com.Rosetta.Model.Type exposing (ZonedDateTime)
		import Com.Rosetta.Model.Type exposing (Date)
		
		-- This file is auto-generated from the ISDA Common Domain Model, do not edit.
		-- Version: test
		
		cFTCPart45TransactionReport : ReportableEvent -> CFTCPart45TransactionReport
		cFTCPart45TransactionReport reportableEvent =
		    { 	tradeDate = tradeDate reportableEvent
		    , 	eventTimestamp = eventTimestampRule reportableEvent
		    }
		
		tradeDate : ReportableEvent -> Date
		tradeDate reportableEvent =
		    reportableEvent.reportableTrade.trade.tradeDate
		
		eventTimestampRuleXXX : ReportableEvent -> ZonedDateTime
		eventTimestampRuleXXX reportableEvent =
			reportableEvent.originatingWorkflowStep
				|> List.map
					(\ item -> item.timespamp.dateTime
					)
				
				|> onlyElement
		
		tradeDate : ReportableEvent -> Date
		tradeDate reportableEvent =
			reportableEvent.reportableTrade.trade.tradeDate
		
		onlyElement : List a -> Maybe a
		onlyElement list =
		    case list of
		        [ a ] ->
		            Just a
		
		        _ ->
		            Nothing
		 ''')
		  )
	}
	
	@Test
	def void shouldGenerateEnums() {
		val golang = '''
			enum TestEnum: <"Test enum description.">
				TestEnumValue1 <"Test enum value 1">
				TestEnumValue2 <"Test enum value 2">
		'''.generateCode
		 
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
				testType2Value3 time (1..1) <"Test time">
				
			type TestType3:
			    tradeDate date (1..1)
			    eventTimestamp zonedDateTime (1..1)
		'''.generateCode

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
		    ,   testType2Value2 : Date -- Test date
		    ,   testType2Value3 : LocalTime -- Test time
		    }
		type alias TestType3 =
		    {   tradeDate : Date 
		    ,   eventTimestamp : ZonedDateTime 
		    }
		'''))


	}	
	
	

	def generateCode(CharSequence model) {
		val eResource = model.parseRosettaWithNoErrors.eResource

		generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
	}
}
