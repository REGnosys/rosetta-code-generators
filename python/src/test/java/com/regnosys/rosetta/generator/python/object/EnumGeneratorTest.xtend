package com.regnosys.rosetta.generator.python.object

import com.google.inject.Inject
import com.google.inject.Provider
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import com.regnosys.rosetta.generator.python.PythonCodeGenerator
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

import static org.hamcrest.CoreMatchers.*
import static org.hamcrest.MatcherAssert.*
import static org.junit.jupiter.api.Assertions.*

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class RosettaEnumHelperTest {
    
    @Inject extension ModelHelper
    @Inject PythonCodeGenerator generator;

    @Inject extension ParseHelper<RosettaModel>
    @Inject Provider<XtextResourceSet> resourceSetProvider;
    
   
	@Test
    def void shouldGenerateEnums() {
        val python = '''
	        enum TestEnum: <"Test enum description.">
	        	TestEnumValue1 <"Test enum value 1">
	        	TestEnumValue2 <"Test enum value 2">
	        	TestEnumValue3 <"Test enum value 3">
	        	_1 displayName "1" <"Rolls on the 1st day of the month.">
	        '''.generatePython

        val enums = python.get('Enums.kt').toString
        val expected = '''
        from enum import Enum
        
        class TestEnum(Enum):
            """
            Test enum description.
            """
            TEST_ENUM_VALUE_1 = "TEST_ENUM_VALUE_1"
            """
            Test enum value 1
            """
            TEST_ENUM_VALUE_2 = "TEST_ENUM_VALUE_2"
            """
            Test enum value 2
            """
            TEST_ENUM_VALUE_3 = "TEST_ENUM_VALUE_3"
            """
            Test enum value 3
            """
            _1 = "1"
            """
            Rolls on the 1st day of the month.
            """
        '''
        assertTrue(enums.contains(expected))
        
    }
	
	
    @Test //not developed at the moment
    @Disabled
    def void shouldGenerateAnnotationForEnumSynonyms() {
        
        /*
        val code = '''
        	synonym source FpML
            enum TestEnum:
            	one <"Some description"> [synonym FpML value "oneSynonym"]
            	two <"Some other description"> [synonym FpML value "twoSynonym"]
        '''.generatePython
		
		
        val testEnumCode = code.get(rootPackage.name + ".TestEnum")
        assertThat(testEnumCode, containsString('''RosettaSynonym(value = "oneSynonym", source = "FpML")'''))

        code.compileToClasses
        */
       
    }
    
    @Test
    def void shouldGenerateEnums2() {
        val python = '''
	        enum TestEnum: <"Test enum description.">
	        	TestEnumValue1 <"Test enum value 1">
	        	TestEnumValue2 <"Test enum value 2">
	        	TestEnumValue3 <"Test enum value 3">
	        	_1 displayName "1" <"Rolls on the 1st day of the month.">
	        '''.generatePython

        val enums = python.get('Enums.kt').toString
        val expected = '''
        class TestEnum(Enum):
            """
            Test enum description.
            """
            TEST_ENUM_VALUE_1 = "TEST_ENUM_VALUE_1"
            """
            Test enum value 1
            """
            TEST_ENUM_VALUE_2 = "TEST_ENUM_VALUE_2"
            """
            Test enum value 2
            """
            TEST_ENUM_VALUE_3 = "TEST_ENUM_VALUE_3"
            """
            Test enum value 3
            """
            _1 = "1"
            """
            Rolls on the 1st day of the month.
            """
        '''
        assertTrue(enums.contains(expected))
    }

    @Test
    @Disabled
    def void shouldGenerateAllDisplayName() {
        val code = '''
        	synonym source FpML
        	enum TestEnumWithDisplay:
        		one displayName "uno" <"Some description"> [synonym FpML value "oneSynonym"]
        		two <"Some other description"> [synonym FpML value "twoSynonym"]
        		three displayName "tria" <"Some description"> [synonym FpML value "threeSynonym"]
        		four  displayName "tessera" <"Some description"> [synonym FpML value "fourSynonym"]
        '''.generatePython
       
        /*assertThat(testEnumCode,
            allOf(containsString('''TestEnumWithDisplay()'''),
                containsString('''TestEnumWithDisplay(String displayName)'''),
                containsString('''public String toString()''')))

        code.compileToClasses
        
        */
        
    }

    @Test
    def void shouldGenerateUppercaseUnderscoreFormattedEnumNames() {
        assertThat(EnumHelper.formatEnumName("ISDA1993Commodity"), is("ISDA_1993_COMMODITY"))
        assertThat(EnumHelper.formatEnumName("ISDA1998FX"), is("ISDA1998FX"))
        assertThat(EnumHelper.formatEnumName("iTraxxEuropeDealer"), is("I_TRAXX_EUROPE_DEALER"))
        assertThat(EnumHelper.formatEnumName("StandardLCDS"), is("STANDARD_LCDS"))
        assertThat(EnumHelper.formatEnumName("_1_1"), is("_1_1"))
        assertThat(EnumHelper.formatEnumName("_30E_360_ISDA"), is("_30E_360_ISDA"))
        assertThat(EnumHelper.formatEnumName("ACT_365L"), is("ACT_365L"))
        assertThat(EnumHelper.formatEnumName("OSPPrice"), is("OSP_PRICE"))
        assertThat(EnumHelper.formatEnumName("FRAYield"), is("FRA_YIELD"))
        assertThat(EnumHelper.formatEnumName("AED-EBOR-Reuters"), is("AED_EBOR_REUTERS"))
        assertThat(EnumHelper.formatEnumName("EUR-EURIBOR-Reuters"), is("EUR_EURIBOR_REUTERS"))
        assertThat(EnumHelper.formatEnumName("DJ.iTraxx.Europe"), is("DJ_I_TRAXX_EUROPE"))
        assertThat(EnumHelper.formatEnumName("IVS1OpenMarkets"), is("IVS_1_OPEN_MARKETS"))
        assertThat(EnumHelper.formatEnumName("D"), is("D"))
        assertThat(EnumHelper.formatEnumName("_1"), is("_1"))
        assertThat(EnumHelper.formatEnumName("DJ.CDX.NA"), is("DJ_CDX_NA"))
        assertThat(EnumHelper.formatEnumName("novation"), is("NOVATION"))
        assertThat(EnumHelper.formatEnumName("partialNovation"), is("PARTIAL_NOVATION"))
        assertThat(EnumHelper.formatEnumName("ALUMINIUM_ALLOY_LME_15_MONTH"), is("ALUMINIUM_ALLOY_LME_15_MONTH"))
        assertThat(EnumHelper.formatEnumName("AggregateClient"), is("AGGREGATE_CLIENT"))
        assertThat(EnumHelper.formatEnumName("Currency1PerCurrency2"), is("CURRENCY_1_PER_CURRENCY_2"))
    }

    @Test
    @Disabled
    def void shouldAllowDeprectedAnnotationForEnum() {
        val code = '''
            enum TestEnumDeprecated:
            	[deprecated]
            	one
            	two
        '''.generatePython

    }
    
    def generatePython(CharSequence model) {
    	val eResource = model.parseRosettaWithNoErrors.eResource
    	generator.afterGenerateTest(eResource.contents.filter(RosettaModel).toList)
    }
}
