package com.regnosys.rosetta.generator.python.object

import com.google.inject.Inject
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import com.regnosys.rosetta.generator.python.PythonCodeGenerator
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Disabled
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.hamcrest.CoreMatchers.*
import static org.hamcrest.MatcherAssert.*
import static org.junit.jupiter.api.Assertions.*

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class EnumGeneratorTest {
    
    @Inject extension ModelHelper
    @Inject PythonCodeGenerator generator;


    
   
	@Test
    def void shouldGenerateEnums() {
        val python = '''
	        enum TestEnum: <"Test enum description.">
	        	TestEnumValue1 <"Test enum value 1">
	        	TestEnumValue2 <"Test enum value 2">
	        	TestEnumValue3 <"Test enum value 3">
	        	_1 displayName "1" <"Rolls on the 1st day of the month.">
	        '''.generatePython

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
        assertTrue(python.toString.contains(expected))
        
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
        assertTrue(python.toString.contains(expected))
    }
    
    @Test
    def void shouldGenerateEnums3() {
    	val python = 
     	'''enum ConfirmationStatusEnum: <"Enumeration for the different types of confirmation status.">
			Confirmed
			Unconfirmed
		'''.generatePython

		
		val expected = '''
		class ConfirmationStatusEnum(Enum):
		  """
		  Enumeration for the different types of confirmation status.
		  """
		  CONFIRMED = "CONFIRMED"
		  UNCONFIRMED = "UNCONFIRMED"
		'''
		assertTrue(python.toString.contains(expected))
    }
    
    @Test
    def void shouldGenerateEnums4() {
    	val python = 
     	 '''enum TransferStatusEnum: <"The enumeration values to specify the transfer status.">
     		Disputed <"The transfer is disputed.">
     		Instructed <"The transfer has been instructed.">
     		Pending <"The transfer is pending instruction.">
     		Settled <"The transfer has been settled.">
     		Netted <"The transfer has been netted into a separate Transfer.">
			'''.generatePython
		
		val expected = 
		'''
		class TransferStatusEnum(Enum):
		  """
		  The enumeration values to specify the transfer status.
		  """
		  DISPUTED = "DISPUTED"
		  """
		  The transfer is disputed.
		  """
		  INSTRUCTED = "INSTRUCTED"
		  """
		  The transfer has been instructed.
		  """
		  NETTED = "NETTED"
		  """
		  The transfer has been netted into a separate Transfer.
		  """
		  PENDING = "PENDING"
		  """
		  The transfer is pending instruction.
		  """
		  SETTLED = "SETTLED"
		  """
		  The transfer has been settled.
		  """
		'''
		assertTrue(python.toString.contains(expected))
	}
    
    @Test
    def void shouldGenerateEnums5() {
    	val python = 
    	'''
    	enum FinancialUnitEnum: <"Provides enumerated values for financial units, generally used in the context of defining quantities for securities.">
    		Contract <"Denotes financial contracts, such as listed futures and options.">
    		ContractualProduct <"Denotes a Contractual Product as defined in the CDM.  This unit type would be used when the price applies to the whole product, for example, in the case of a premium expressed as a cash amount.">
    		IndexUnit <"Denotes a price expressed in index points, e.g. for a stock index.">
    		LogNormalVolatility <"Denotes a log normal volatility, expressed in %/month, where the percentage is represented as a decimal. For example, 0.15 means a log-normal volatility of 15% per month.">
    		Share <"Denotes the number of units of financial stock shares.">
    		ValuePerDay <"Denotes a value (expressed in currency units) for a one day change in a valuation date, which is typically used for expressing sensitivity to the passage of time, also known as theta risk, or carry, or other names.">
    		ValuePerPercent <"Denotes a value (expressed in currency units) per percent change in the underlying rate which is typically used for expressing sensitivity to volatility changes, also known as vega risk.">
    		Weight <"Denotes a quantity (expressed as a decimal value) represented the weight of a component in a basket.">
    	'''.generatePython
		
   		val expected = 
   		'''
   		class FinancialUnitEnum(Enum):
   		  """
   		  Provides enumerated values for financial units, generally used in the context of defining quantities for securities.
   		  """
   		  CONTRACT = "CONTRACT"
   		  """
   		  Denotes financial contracts, such as listed futures and options.
   		  """
   		  CONTRACTUAL_PRODUCT = "CONTRACTUAL_PRODUCT"
   		  """
   		  Denotes a Contractual Product as defined in the CDM.  This unit type would be used when the price applies to the whole product, for example, in the case of a premium expressed as a cash amount.
   		  """
   		  INDEX_UNIT = "INDEX_UNIT"
   		  """
   		  Denotes a price expressed in index points, e.g. for a stock index.
   		  """
   		  LOG_NORMAL_VOLATILITY = "LOG_NORMAL_VOLATILITY"
   		  """
   		  Denotes a log normal volatility, expressed in %/month, where the percentage is represented as a decimal. For example, 0.15 means a log-normal volatility of 15% per month.
   		  """
   		  SHARE = "SHARE"
   		  """
   		  Denotes the number of units of financial stock shares.
   		  """
   		  VALUE_PER_DAY = "VALUE_PER_DAY"
   		  """
   		  Denotes a value (expressed in currency units) for a one day change in a valuation date, which is typically used for expressing sensitivity to the passage of time, also known as theta risk, or carry, or other names.
   		  """
   		  VALUE_PER_PERCENT = "VALUE_PER_PERCENT"
   		  """
   		  Denotes a value (expressed in currency units) per percent change in the underlying rate which is typically used for expressing sensitivity to volatility changes, also known as vega risk.
   		  """
   		  WEIGHT = "WEIGHT"
   		  """
   		  Denotes a quantity (expressed as a decimal value) represented the weight of a component in a basket.
   		  """
   		'''
   		assertTrue(python.toString.contains(expected))
   		
    	
    }
    

    @Test
    @Disabled
    def void shouldGenerateAllDisplayName() {
        '''
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
        '''
            enum TestEnumDeprecated:
            	[deprecated]
            	one
            	two
        '''.generatePython

    }
    
    def generatePython(CharSequence model) {
    	val eResource = model.parseRosettaWithNoErrors.eResource
    	generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
    }
}
