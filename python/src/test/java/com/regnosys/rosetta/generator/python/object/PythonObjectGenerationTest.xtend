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
class PythonObjectGenerationTest {
	
	@Inject extension ModelHelper
	@Inject PythonCodeGenerator generator;

	
	@Test
	def void testConditions1() {
		val python = '''
			type A:
				a0 int (0..1)
				a1 int (0..1)
				condition: one-of

			type B:
				intValue1 int (0..1)
				intValue2 int (0..1)
				aValue A (1..1)

				condition Rule:
					intValue1 < 100

				condition OneOrTwo: <"Choice rule to represent an FpML choice construct.">
					optional choice intValue1, intValue2

				condition SecondOneOrTwo: <"FpML specifies a choice between adjustedDate and [unadjustedDate (required), dateAdjutsments (required), adjustedDate (optional)].">
					if B exists
					then aValue->a0 exists
						or (intValue2 exists and intValue1 exists and intValue1 exists)
						or (intValue2 exists and intValue1 exists and intValue1 is absent)
			'''.generatePython
		
		val expectedA=
		'''
		class A(BaseDataClass):
		  a0: Optional[int] = Field(None, description="")
		  a1: Optional[int] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_(self):
		    return self.check_one_of_constraint('a0', 'a1', necessity=True)
		'''
		
		val expectedB=
		'''
		class B(BaseDataClass):
		  aValue: A = Field(..., description="")
		  intValue1: Optional[int] = Field(None, description="")
		  intValue2: Optional[int] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_Rule(self):
		    return all_elements(self.intValue1, "<", 100)
		  
		  @rosetta_condition
		  def condition_1_OneOrTwo(self):
		    """
		    Choice rule to represent an FpML choice construct.
		    """
		    return self.check_one_of_constraint('intValue1', 'intValue2', necessity=False)
		  
		  @rosetta_condition
		  def condition_2_SecondOneOrTwo(self):
		    """
		    FpML specifies a choice between adjustedDate and [unadjustedDate (required), dateAdjutsments (required), adjustedDate (optional)].
		    """
		    def _then_fn0():
		      return ((((self.aValue.a0) is not None) or ((((self.intValue2) is not None) and ((self.intValue1) is not None)) and ((self.intValue1) is not None))) or ((((self.intValue2) is not None) and ((self.intValue1) is not None)) and ((self.intValue1) is None)))
		    
		    def _else_fn0():
		      return True
		    
		    return if_cond_fn(((B) is not None), _then_fn0, _else_fn0)
		'''
		assertTrue(python.toString.contains(expectedA))
		assertTrue(python.toString.contains(expectedB))
	}
	
	
	@Test
	def void shouldGenerateTypes1() {
		val python = '''
		type TestType: <"Test type description.">
			testTypeValue1 string (1..1) <"Test string">
			testTypeValue2 string (0..1) <"Test optional string">
			testTypeValue3 string (0..*) <"Test string list">
			testTypeValue4 TestType2 (1..1) <"Test TestType2">
			testEnum TestEnum (0..1) <"Optional test enum">

		type TestType2:
			testType2Value1 number(1..*) <"Test number list">
			testType2Value2 date(0..1) <"Test date">
			testEnum TestEnum (0..1) <"Optional test enum">

		enum TestEnum: <"Test enum description.">
			TestEnumValue1 <"Test enum value 1">
			TestEnumValue2 <"Test enum value 2">
		'''.generatePython
				 
		  
		  val expectedTestType = 
			'''
		   class TestType(BaseDataClass):
		     """
		     Test type description.
		     """
		     testEnum: Optional[TestEnum] = Field(None, description="Optional test enum")
		     """
		     Optional test enum
		     """
		     testTypeValue1: str = Field(..., description="Test string")
		     """
		     Test string
		     """
		     testTypeValue2: Optional[str] = Field(None, description="Test optional string")
		     """
		     Test optional string
		     """
		     testTypeValue3: List[str] = Field([], description="Test string list")
		     """
		     Test string list
		     """
		     testTypeValue4: TestType2 = Field(..., description="Test TestType2")
		     """
		     Test TestType2
		     """
			'''
			val expectedTestType2 = 
			'''
		   class TestType2(BaseDataClass):
		     testEnum: Optional[TestEnum] = Field(None, description="Optional test enum")
		     """
		     Optional test enum
		     """
		     testType2Value1: List[Decimal] = Field([], description="Test number list")
		     """
		     Test number list
		     """
		     @rosetta_condition
		     def cardinality_testType2Value1(self):
		       return check_cardinality(self.testType2Value1, 1, None)
		     
		     testType2Value2: Optional[date] = Field(None, description="Test date")
		     """
		     Test date
		     """
			'''
			
		  val expectedTestEnum = 
			'''
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
			'''
		assertTrue(python.toString.contains(expectedTestType))
		assertTrue(python.toString.contains(expectedTestType2))
		assertTrue(python.toString.contains(expectedTestEnum))
		
	}
	
	@Test 
	def void shouldGenerateTypes2() {
		val python = '''
		enum CapacityUnitEnum: <"Provides enumerated values for capacity units, generally used in the context of defining quantities for commodities.">
			ALW <"Denotes Allowances as standard unit.">
			BBL <"Denotes a Barrel as a standard unit.">
			BCF <"Denotes Billion Cubic Feet as a standard unit.">
			BDFT <"Denotes Board Feet as a standard unit.">
			BSH <"Denotes a Bushel as a standard unit of weight (48 lb or 21.7725 kg).">
			BTU <"Denotes British Thermal Units as a standard unit.">
			CBM <"Denotes Cubic Meters as a standard unit.">
			CER <"Denotes Certified Emissions Reduction as a standard unit.">
			CRT <"Denotes Climate Reserve Tonnes as a standard unit.">
			DAG <"Denotes 10 grams as a standard unit used in precious metals contracts (e.g MCX).">
			DAY <"Denotes a single day as a standard unit used in time charter trades.">
			DMTU <"Denotes Dry Metric Ton (Tonne) Units - Consists of a metric ton of mass excluding moisture.">
			DTH <"Denotes a Dekatherm as a standard unit.">
			ENVCRD <"Denotes Environmental Credit as a standard unit.">
			ENVOFST <"Denotes Environmental Offset as a standard unit.">
			FEU <"Denotes a 40 ft. Equivalent Unit container as a standard unit.">
			G <"Denotes a Gram as a standard unit.">
			GBCWT <"Denotes a GB Hundredweight unit as standard unit.">
			GBGAL <"Denotes a GB Gallon unit as standard unit.">
			GBT <"Denotes a GB Ton as a standard unit.">
			GJ <"Denotes a Gigajoule as a standard unit.">
			GW <"Denotes a Gigawatt as a standard unit.">
			GWH <"Denotes a Gigawatt-hour as a standard unit.">
			HL <"Denotes a Hectolitre as a standard unit.">
			INGOT <"Denotes an Ingot as a standard unit.">
			KG <"Denotes a Kilogram as a standard unit.">
			KL <"Denotes a Kilolitre as a standard unit.">
			KW <"Denotes a Kilowatt as a standard unit.">
			KWDC <"Denotes a Kilowatt Day Capacity as a standard unit.">
			KWH <"Denotes a Kilowatt-hour as a standard unit.">
			KWHC <"Denotes a Kilowatt Hours Capacity as a standard unit.">
			KWMC <"Denotes a Kilowatt Month Capacity as a standard unit.">
			KWMINC <"Denotes a Kilowatt Minute Capacity as a standard unit.">
			KWYC <"Denotes a Kilowatt Year Capacity as a standard unit.">
			L <"Denotes a Litre as a standard unit.">
			LB <"Denotes a Pound as a standard unit.">
			MB <"Denotes a Thousand Barrels as a standard unit.">
			MBF <"Denotes a Thousand board feet, which are used in contracts on forestry underlyers as a standard unit.">
			MJ <"Denotes a Megajoule as a standard unit.">
			MMBF <"Denotes a Million board feet, which are used in contracts on forestry underlyers as a standard unit.">
			MMBBL <"Denotes a Million Barrels as a standard unit.">
			MMBTU <"Denotes a Million British Thermal Units as a standard unit.">
			MSF <"Denotes a Thousand square feet as a standard unit.">
			MT <"Denotes a Metric Ton as a standard unit.">
			MW <"Denotes a Megawatt as a standard unit.">
			MWDC <"Denotes a Megawatt Day Capacity as a standard unit.">
			MWH <"Denotes a Megawatt-hour as a standard unit.">
			MWHC <"Denotes a Megawatt Hours Capacity as a standard unit.">
			MWMC <"Denotes a Megawatt Month Capacity as a standard unit.">
			MWMINC <"Denotes a Megawatt Minute Capacity as a standard unit.">
			MWYC <"Denotes a Megawatt Year Capacity as a standard unit.">
			OZT <"Denotes a Troy Ounce as a standard unit.">
			TEU <"Denotes a 20 ft. Equivalent Unit container as a standard unit.">
			THERM <"Denotes a Thermal Unit as a standard unit.">
			USCWT <"Denotes US Hundredweight unit as a standard unit.">
			USGAL <"Denotes a US Gallon unit as a standard unit.">
			UST <"Denotes a US Ton as a standard unit.">
		
		enum WeatherUnitEnum: <"Provides enumerated values for weather units, generally used in the context of defining quantities for commodities.">
			CDD <"Denotes Cooling Degree Days as a standard unit.">
			CPD <"Denotes Critical Precipitation Day as a standard unit.">
			HDD <"Heating Degree Day as a standard unit.">
		
		enum FinancialUnitEnum: <"Provides enumerated values for financial units, generally used in the context of defining quantities for securities.">
			Contract <"Denotes financial contracts, such as listed futures and options.">
			ContractualProduct <"Denotes a Contractual Product as defined in the CDM.  This unit type would be used when the price applies to the whole product, for example, in the case of a premium expressed as a cash amount.">
			IndexUnit <"Denotes a price expressed in index points, e.g. for a stock index.">
			LogNormalVolatility <"Denotes a log normal volatility, expressed in %/month, where the percentage is represented as a decimal. For example, 0.15 means a log-normal volatility of 15% per month.">
			Share <"Denotes the number of units of financial stock shares.">
			ValuePerDay <"Denotes a value (expressed in currency units) for a one day change in a valuation date, which is typically used for expressing sensitivity to the passage of time, also known as theta risk, or carry, or other names.">
			ValuePerPercent <"Denotes a value (expressed in currency units) per percent change in the underlying rate which is typically used for expressing sensitivity to volatility changes, also known as vega risk.">
			Weight <"Denotes a quantity (expressed as a decimal value) represented the weight of a component in a basket.">
		
		type UnitType: <"Defines the unit to be used for price, quantity, or other purposes">
			capacityUnit CapacityUnitEnum (0..1) <"Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.">
			weatherUnit WeatherUnitEnum (0..1) <"Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.">
			financialUnit FinancialUnitEnum (0..1) <"Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.">
			currency string (0..1) <"Defines the currency to be used as a unit for a price, quantity, or other purpose.">
			[metadata scheme]

		condition UnitType: <"Requires that a unit type must be set.">
			one-of
		'''.generatePython
		
		val expectedTestType = 
		'''
		class UnitType(BaseDataClass):
		  """
		  Defines the unit to be used for price, quantity, or other purposes
		  """
		  capacityUnit: Optional[CapacityUnitEnum] = Field(None, description="Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.")
		  """
		  Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.
		  """
		  currency: Optional[AttributeWithMeta[str] | str] = Field(None, description="Defines the currency to be used as a unit for a price, quantity, or other purpose.")
		  """
		  Defines the currency to be used as a unit for a price, quantity, or other purpose.
		  """
		  financialUnit: Optional[FinancialUnitEnum] = Field(None, description="Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.")
		  """
		  Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.
		  """
		  weatherUnit: Optional[WeatherUnitEnum] = Field(None, description="Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.")
		  """
		  Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.
		  """
		  
		  @rosetta_condition
		  def condition_0_UnitType(self):
		    """
		    Requires that a unit type must be set.
		    """
		    return self.check_one_of_constraint('capacityUnit', 'weatherUnit', 'financialUnit', 'currency', necessity=True)
		'''
		assertTrue(python.toString.contains(expectedTestType))
		
	}
	
	
	@Test
	def void shouldGenerateTypes3() {
		val python = 
		'''
		enum AncillaryRoleEnum: <"Defines the enumerated values to specify the ancillary roles to the transaction. The product is agnostic to the actual parties involved in the transaction, with the party references abstracted away from the product definition and replaced by the AncillaryRoleEnum. The AncillaryRoleEnum can then be positioned in the product and the AncillaryParty type, which is positioned outside of the product definition, allows the AncillaryRoleEnum to be associated with an actual party reference.">
			DisruptionEventsDeterminingParty <"Specifies the party which determines additional disruption events.">
			ExtraordinaryDividendsParty <"Specifies the party which determines if dividends are extraordinary in relation to normal levels.">
			PredeterminedClearingOrganizationParty <"Specifies the clearing organization (CCP, DCO) which the trade should be cleared.">
			ExerciseNoticeReceiverPartyManual <"Specifies the party to which notice of a manual exercise should be given.">
			ExerciseNoticeReceiverPartyOptionalEarlyTermination <"Specifies the party to which notice of a optional early termination exercise should be given.">
			ExerciseNoticeReceiverPartyCancelableProvision <"Specifies the party to which notice of a cancelable provision exercise should be given.">
			ExerciseNoticeReceiverPartyExtendibleProvision <"Specifies the party to which notice of a extendible provision exercise should be given.">
			CalculationAgentIndependent <"Specifies the party responsible for performing calculation agent duties as defined in the applicable product definition.">
			CalculationAgentOptionalEarlyTermination <"Specifies the party responsible for performing calculation agent duties associated with an optional early termination.">
			CalculationAgentMandatoryEarlyTermination <"Specifies the party responsible for performing calculation agent duties associated with an mandatory early termination.">
			CalculationAgentFallback <"Specifies the party responsible for deciding the fallback rate.">
			
		enum TelephoneTypeEnum: <"The enumerated values to specify the type of telephone number, e.g. work vs. mobile.">
			Work <"A number used primarily for work-related calls. Includes home office numbers used primarily for work purposes.">
			Mobile <"A number on a mobile telephone that is often or usually used for work-related calls. This type of number can be used for urgent work related business when a work number is not sufficient to contact the person or firm.">
			Fax <"A number used primarily for work-related facsimile transmissions.">
			Personal <"A number used primarily for non work-related calls. (Normally this type of number would be used only as an emergency backup number, not as a regular course of business).">
		
		type LegalEntity: <"A class to specify a legal entity, with a required name and an optional entity identifier (such as the LEI).">
			[metadata key]
		
			entityId string (0..*) <"A legal entity identifier (e.g. RED entity code).">
				[metadata scheme]
			name string (1..1) <"The legal entity name.">
				[metadata scheme]
		
		type TelephoneNumber: <"A class to specify a telephone number as a type of phone number (e.g. work, personal, ...) alongside with the actual number.">
		
			telephoneNumberType TelephoneTypeEnum (0..1) <"The type of telephone number, e.g. work, mobile.">
			number string (1..1) <"The actual telephone number.">
		
		type AncillaryEntity: <"Holds an identifier for an ancillary entity, either identified directly via its ancillary role or directly as a legal entity.">
		
			ancillaryParty AncillaryRoleEnum (0..1) <"Identifies a party via its ancillary role on a transaction (e.g. CCP or DCO through which the trade should be cleared.)">
			legalEntity LegalEntity (0..1)
		
			condition: one-of
		'''.generatePython
		
		
		val expectedTestType1 = 
		'''
		class LegalEntity(BaseDataClass):
		  """
		  A class to specify a legal entity, with a required name and an optional entity identifier (such as the LEI).
		  """
		  entityId: List[AttributeWithMeta[str] | str] = Field([], description="A legal entity identifier (e.g. RED entity code).")
		  """
		  A legal entity identifier (e.g. RED entity code).
		  """
		  name: AttributeWithMeta[str] | str = Field(..., description="The legal entity name.")
		  """
		  The legal entity name.
		  """
		'''
		val expectedTestType2 = 
		'''
		class TelephoneNumber(BaseDataClass):
		  """
		  A class to specify a telephone number as a type of phone number (e.g. work, personal, ...) alongside with the actual number.
		  """
		  number: str = Field(..., description="The actual telephone number.")
		  """
		  The actual telephone number.
		  """
		  telephoneNumberType: Optional[TelephoneTypeEnum] = Field(None, description="The type of telephone number, e.g. work, mobile.")
		  """
		  The type of telephone number, e.g. work, mobile.
		  """
		'''
		val expectedTestType3 = 
		'''
		class AncillaryEntity(BaseDataClass):
		  """
		  Holds an identifier for an ancillary entity, either identified directly via its ancillary role or directly as a legal entity.
		  """
		  ancillaryParty: Optional[AncillaryRoleEnum] = Field(None, description="Identifies a party via its ancillary role on a transaction (e.g. CCP or DCO through which the trade should be cleared.)")
		  """
		  Identifies a party via its ancillary role on a transaction (e.g. CCP or DCO through which the trade should be cleared.)
		  """
		  legalEntity: Optional[LegalEntity] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_(self):
		    return self.check_one_of_constraint('ancillaryParty', 'legalEntity', necessity=True)
		'''
		
		assertTrue(python.toString.contains(expectedTestType1))   
		assertTrue(python.toString.contains(expectedTestType2))				
		assertTrue(python.toString.contains(expectedTestType3))  
		
		
	}
	
		
	
	@Test
	def void shouldGenerateTypesMethod2() {
		val python = '''
		type UnitType: <"Defines the unit to be used for price, quantity, or other purposes">	  
			currency string (0..1) <"Defines the currency to be used as a unit for a price, quantity, or other purpose.">
		
		type MeasureBase: <"Provides an abstract base class shared by Price and Quantity.">		
			amount number (1..1) <"Specifies an amount to be qualified and used in a Price or Quantity definition.">
			unitOfAmount UnitType (1..1) <"Qualifies the unit by which the amount is measured.">
		
		type Quantity extends MeasureBase: <"Specifies a quantity to be associated to a financial product, for example a trade amount or a cashflow amount resulting from a trade.">	   
			multiplier number (0..1) <"Defines the number to be multiplied by the amount to derive a total quantity.">
			multiplierUnit UnitType (0..1) <"Qualifies the multiplier with the applicable unit.  For example in the case of the Coal (API2) CIF ARA (ARGUS-McCloskey) Futures Contract on the CME, where the unitOfAmount would be contracts, the multiplier would 1,000 and the mulitiplier Unit would be 1,000 MT (Metric Tons).">
		'''.generatePython

		val expectedMeasureBase=
		'''
		class MeasureBase(BaseDataClass):
		  """
		  Provides an abstract base class shared by Price and Quantity.
		  """
		  amount: Decimal = Field(..., description="Specifies an amount to be qualified and used in a Price or Quantity definition.")
		  """
		  Specifies an amount to be qualified and used in a Price or Quantity definition.
		  """
		  unitOfAmount: UnitType = Field(..., description="Qualifies the unit by which the amount is measured.")
		  """
		  Qualifies the unit by which the amount is measured.
		  """
		'''
		val expectedUnitType=
		'''
		class UnitType(BaseDataClass):
		  """
		  Defines the unit to be used for price, quantity, or other purposes
		  """
		  currency: Optional[str] = Field(None, description="Defines the currency to be used as a unit for a price, quantity, or other purpose.")
		  """
		  Defines the currency to be used as a unit for a price, quantity, or other purpose.
		  """
		'''
		val expectedQuantity=
		'''
		class Quantity(MeasureBase):
		  """
		  Specifies a quantity to be associated to a financial product, for example a trade amount or a cashflow amount resulting from a trade.
		  """
		  multiplier: Optional[Decimal] = Field(None, description="Defines the number to be multiplied by the amount to derive a total quantity.")
		  """
		  Defines the number to be multiplied by the amount to derive a total quantity.
		  """
		  multiplierUnit: Optional[UnitType] = Field(None, description="Qualifies the multiplier with the applicable unit.  For example in the case of the Coal (API2) CIF ARA (ARGUS-McCloskey) Futures Contract on the CME, where the unitOfAmount would be contracts, the multiplier would 1,000 and the mulitiplier Unit would be 1,000 MT (Metric Tons).")
		  """
		  Qualifies the multiplier with the applicable unit.  For example in the case of the Coal (API2) CIF ARA (ARGUS-McCloskey) Futures Contract on the CME, where the unitOfAmount would be contracts, the multiplier would 1,000 and the mulitiplier Unit would be 1,000 MT (Metric Tons).
		  """

		'''
		assertTrue(python.toString.contains(expectedMeasureBase))
		assertTrue(python.toString.contains(expectedUnitType))
		assertTrue(python.toString.contains(expectedQuantity))
		
	}

	@Test
	def void shouldGenerateTypesExtends1() {
		val python = '''
		type TestType extends TestType2:
			TestTypeValue1 string (1..1) <"Test string">
			TestTypeValue2 int (0..1) <"Test int">

		type TestType2 extends TestType3:
			TestType2Value1 number (0..1) <"Test number">
			TestType2Value2 date (0..*) <"Test date">

		type TestType3:
			TestType3Value1 string (0..1) <"Test string">
			TestType4Value2 int (1..*) <"Test int">
		'''.generatePython


		val types = python.toString
		
		val expectedTestType=
		'''
		class TestType(TestType2):
		  TestTypeValue1: str = Field(..., description="Test string")
		  """
		  Test string
		  """
		  TestTypeValue2: Optional[int] = Field(None, description="Test int")
		  """
		  Test int
		  """
		'''
		val expectedTestType2=
		'''
		class TestType2(TestType3):
		  TestType2Value1: Optional[Decimal] = Field(None, description="Test number")
		  """
		  Test number
		  """
		  TestType2Value2: List[date] = Field([], description="Test date")
		  """
		  Test date
		  """
		'''
		val expectedTestType3=
		'''
		class TestType3(BaseDataClass):
		  TestType3Value1: Optional[str] = Field(None, description="Test string")
		  """
		  Test string
		  """
		  TestType4Value2: List[int] = Field([], description="Test int")
		  """
		  Test int
		  """
		  @rosetta_condition
		  def cardinality_TestType4Value2(self):
		    return check_cardinality(self.TestType4Value2, 1, None)
		'''
		
		assertTrue(types.contains(expectedTestType))   
		assertTrue(types.contains(expectedTestType2))				
		assertTrue(types.contains(expectedTestType3))		
			 
	}
	
	@Test
	def void shouldGenerateTypesExtends2() {
		val python = 
		'''
		enum CapacityUnitEnum: <"Provides enumerated values for capacity units, generally used in the context of defining quantities for commodities.">
					ALW <"Denotes Allowances as standard unit.">
					BBL <"Denotes a Barrel as a standard unit.">
					BCF <"Denotes Billion Cubic Feet as a standard unit.">
					BDFT <"Denotes Board Feet as a standard unit.">
					BSH <"Denotes a Bushel as a standard unit of weight (48 lb or 21.7725 kg).">
					BTU <"Denotes British Thermal Units as a standard unit.">
					CBM <"Denotes Cubic Meters as a standard unit.">
					CER <"Denotes Certified Emissions Reduction as a standard unit.">
					CRT <"Denotes Climate Reserve Tonnes as a standard unit.">
					DAG <"Denotes 10 grams as a standard unit used in precious metals contracts (e.g MCX).">
					DAY <"Denotes a single day as a standard unit used in time charter trades.">
					DMTU <"Denotes Dry Metric Ton (Tonne) Units - Consists of a metric ton of mass excluding moisture.">
					DTH <"Denotes a Dekatherm as a standard unit.">
					ENVCRD <"Denotes Environmental Credit as a standard unit.">
					ENVOFST <"Denotes Environmental Offset as a standard unit.">
					FEU <"Denotes a 40 ft. Equivalent Unit container as a standard unit.">
					G <"Denotes a Gram as a standard unit.">
					GBCWT <"Denotes a GB Hundredweight unit as standard unit.">
					GBGAL <"Denotes a GB Gallon unit as standard unit.">
					GBT <"Denotes a GB Ton as a standard unit.">
					GJ <"Denotes a Gigajoule as a standard unit.">
					GW <"Denotes a Gigawatt as a standard unit.">
					GWH <"Denotes a Gigawatt-hour as a standard unit.">
					HL <"Denotes a Hectolitre as a standard unit.">
					INGOT <"Denotes an Ingot as a standard unit.">
					KG <"Denotes a Kilogram as a standard unit.">
					KL <"Denotes a Kilolitre as a standard unit.">
					KW <"Denotes a Kilowatt as a standard unit.">
					KWDC <"Denotes a Kilowatt Day Capacity as a standard unit.">
					KWH <"Denotes a Kilowatt-hour as a standard unit.">
					KWHC <"Denotes a Kilowatt Hours Capacity as a standard unit.">
					KWMC <"Denotes a Kilowatt Month Capacity as a standard unit.">
					KWMINC <"Denotes a Kilowatt Minute Capacity as a standard unit.">
					KWYC <"Denotes a Kilowatt Year Capacity as a standard unit.">
					L <"Denotes a Litre as a standard unit.">
					LB <"Denotes a Pound as a standard unit.">
					MB <"Denotes a Thousand Barrels as a standard unit.">
					MBF <"Denotes a Thousand board feet, which are used in contracts on forestry underlyers as a standard unit.">
					MJ <"Denotes a Megajoule as a standard unit.">
					MMBF <"Denotes a Million board feet, which are used in contracts on forestry underlyers as a standard unit.">
					MMBBL <"Denotes a Million Barrels as a standard unit.">
					MMBTU <"Denotes a Million British Thermal Units as a standard unit.">
					MSF <"Denotes a Thousand square feet as a standard unit.">
					MT <"Denotes a Metric Ton as a standard unit.">
					MW <"Denotes a Megawatt as a standard unit.">
					MWDC <"Denotes a Megawatt Day Capacity as a standard unit.">
					MWH <"Denotes a Megawatt-hour as a standard unit.">
					MWHC <"Denotes a Megawatt Hours Capacity as a standard unit.">
					MWMC <"Denotes a Megawatt Month Capacity as a standard unit.">
					MWMINC <"Denotes a Megawatt Minute Capacity as a standard unit.">
					MWYC <"Denotes a Megawatt Year Capacity as a standard unit.">
					OZT <"Denotes a Troy Ounce as a standard unit.">
					TEU <"Denotes a 20 ft. Equivalent Unit container as a standard unit.">
					THERM <"Denotes a Thermal Unit as a standard unit.">
					USCWT <"Denotes US Hundredweight unit as a standard unit.">
					USGAL <"Denotes a US Gallon unit as a standard unit.">
					UST <"Denotes a US Ton as a standard unit.">
				
				enum WeatherUnitEnum: <"Provides enumerated values for weather units, generally used in the context of defining quantities for commodities.">
					CDD <"Denotes Cooling Degree Days as a standard unit.">
					CPD <"Denotes Critical Precipitation Day as a standard unit.">
					HDD <"Heating Degree Day as a standard unit.">
				
				enum FinancialUnitEnum: <"Provides enumerated values for financial units, generally used in the context of defining quantities for securities.">
					Contract <"Denotes financial contracts, such as listed futures and options.">
					ContractualProduct <"Denotes a Contractual Product as defined in the CDM.  This unit type would be used when the price applies to the whole product, for example, in the case of a premium expressed as a cash amount.">
					IndexUnit <"Denotes a price expressed in index points, e.g. for a stock index.">
					LogNormalVolatility <"Denotes a log normal volatility, expressed in %/month, where the percentage is represented as a decimal. For example, 0.15 means a log-normal volatility of 15% per month.">
					Share <"Denotes the number of units of financial stock shares.">
					ValuePerDay <"Denotes a value (expressed in currency units) for a one day change in a valuation date, which is typically used for expressing sensitivity to the passage of time, also known as theta risk, or carry, or other names.">
					ValuePerPercent <"Denotes a value (expressed in currency units) per percent change in the underlying rate which is typically used for expressing sensitivity to volatility changes, also known as vega risk.">
					Weight <"Denotes a quantity (expressed as a decimal value) represented the weight of a component in a basket.">
		
		type UnitType: <"Defines the unit to be used for price, quantity, or other purposes">
			capacityUnit CapacityUnitEnum (0..1) <"Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.">
			weatherUnit WeatherUnitEnum (0..1) <"Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.">
			financialUnit FinancialUnitEnum (0..1) <"Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.">
			currency string (0..1) <"Defines the currency to be used as a unit for a price, quantity, or other purpose.">
				[metadata scheme]
		
			condition UnitType: <"Requires that a unit type must be set.">
				one-of
		
		type Measure extends MeasureBase: <"Defines a concrete measure as a number associated to a unit. It extends MeasureBase by requiring the value attribute to be present. A measure may be unit-less so the unit attribute is still optional.">
		
			condition ValueExists: <"The value attribute must be present in a concrete measure.">
				value exists
				
		type MeasureBase: <"Provides an abstract type to define a measure as a number associated to a unit. This type is abstract because all its attributes are optional. The types that extend it can specify further existence constraints.">
			
			value number (0..1) <"Specifies the value of the measure as a number. Optional because in a measure vector or schedule, this single value may be omitted.">
			unit UnitType (0..1) <"Qualifies the unit by which the amount is measured. Optional because a measure may be unit-less (e.g. when representing a ratio between amounts in the same unit).">
		'''.generatePython
		
		val expectedTestType1 = 
		'''
		class MeasureBase(BaseDataClass):
		  """
		  Provides an abstract type to define a measure as a number associated to a unit. This type is abstract because all its attributes are optional. The types that extend it can specify further existence constraints.
		  """
		  unit: Optional[UnitType] = Field(None, description="Qualifies the unit by which the amount is measured. Optional because a measure may be unit-less (e.g. when representing a ratio between amounts in the same unit).")
		  """
		  Qualifies the unit by which the amount is measured. Optional because a measure may be unit-less (e.g. when representing a ratio between amounts in the same unit).
		  """
		  value: Optional[Decimal] = Field(None, description="Specifies the value of the measure as a number. Optional because in a measure vector or schedule, this single value may be omitted.")
		  """
		  Specifies the value of the measure as a number. Optional because in a measure vector or schedule, this single value may be omitted.
		  """
		'''
		
		val expectedTestType2 = 
		'''
		class Measure(MeasureBase):
		  """
		  Defines a concrete measure as a number associated to a unit. It extends MeasureBase by requiring the value attribute to be present. A measure may be unit-less so the unit attribute is still optional.
		  """
		  
		  @rosetta_condition
		  def condition_0_ValueExists(self):
		    """
		    The value attribute must be present in a concrete measure.
		    """
		    return ((self.value) is not None)
		'''
		
		assertTrue(python.toString.contains(expectedTestType1))   
		assertTrue(python.toString.contains(expectedTestType2))				
		
	} 


	@Test
		def void shouldGenerateTypesChoiceCondition() {
			val python = '''
				type TestType: <"Test type with one-of condition.">
					field1 string (0..1) <"Test string field 1">
					field2 string (0..1) <"Test string field 2">
					field3 number (0..1) <"Test number field 3">
					field4 number (0..*) <"Test number field 4">
					condition BusinessCentersChoice: <"Choice rule to represent an FpML choice construct.">
							required choice field1, field2
				'''.generatePython

			val types = python.toString

			val expected =
			'''
			class TestType(BaseDataClass):
			  """
			  Test type with one-of condition.
			  """
			  field1: Optional[str] = Field(None, description="Test string field 1")
			  """
			  Test string field 1
			  """
			  field2: Optional[str] = Field(None, description="Test string field 2")
			  """
			  Test string field 2
			  """
			  field3: Optional[Decimal] = Field(None, description="Test number field 3")
			  """
			  Test number field 3
			  """
			  field4: List[Decimal] = Field([], description="Test number field 4")
			  """
			  Test number field 4
			  """
			  
			  @rosetta_condition
			  def condition_0_BusinessCentersChoice(self):
			    """
			    Choice rule to represent an FpML choice construct.
			    """
			    return self.check_one_of_constraint('field1', 'field2', necessity=True)
			'''
			assertTrue(types.contains(expected))
		}
		
		@Test
		def void shouldGenerateIfThenCondition() {
			val python = '''
				type TestType: <"Test type with one-of condition.">
					field1 string (0..1) <"Test string field 1">
					field2 string (0..1) <"Test string field 2">
					field3 number (0..1) <"Test number field 3">
					field4 number (0..*) <"Test number field 4">
					condition BusinessCentersChoice: <"Choice rule to represent an FpML choice construct.">
							if field1 exists
									then field3 > 0
				'''.generatePython

			val types = python.toString

			val expected =
			'''
			class TestType(BaseDataClass):
			  """
			  Test type with one-of condition.
			  """
			  field1: Optional[str] = Field(None, description="Test string field 1")
			  """
			  Test string field 1
			  """
			  field2: Optional[str] = Field(None, description="Test string field 2")
			  """
			  Test string field 2
			  """
			  field3: Optional[Decimal] = Field(None, description="Test number field 3")
			  """
			  Test number field 3
			  """
			  field4: List[Decimal] = Field([], description="Test number field 4")
			  """
			  Test number field 4
			  """
			  
			  @rosetta_condition
			  def condition_0_BusinessCentersChoice(self):
			    """
			    Choice rule to represent an FpML choice construct.
			    """
			    def _then_fn0():
			      return all_elements(self.field3, ">", 0)
			    
			    def _else_fn0():
			      return True
			    
			    return if_cond_fn(((self.field1) is not None), _then_fn0, _else_fn0)
			'''
			assertTrue(types.contains(expected))
		}
		
		
	@Test
	def void shouldGenerateIfThenElseCondition() {
			val python = '''
				type TestType: <"Test type with one-of condition.">
					field1 string (0..1) <"Test string field 1">
					field2 string (0..1) <"Test string field 2">
					field3 number (0..1) <"Test number field 3">
					field4 number (0..*) <"Test number field 4">
					condition BusinessCentersChoice: <"Choice rule to represent an FpML choice construct.">
							if field1 exists
									then field3 > 0
							else field4 > 0
				'''.generatePython

			val expected =
			'''
			class TestType(BaseDataClass):
			  """
			  Test type with one-of condition.
			  """
			  field1: Optional[str] = Field(None, description="Test string field 1")
			  """
			  Test string field 1
			  """
			  field2: Optional[str] = Field(None, description="Test string field 2")
			  """
			  Test string field 2
			  """
			  field3: Optional[Decimal] = Field(None, description="Test number field 3")
			  """
			  Test number field 3
			  """
			  field4: List[Decimal] = Field([], description="Test number field 4")
			  """
			  Test number field 4
			  """
			  
			  @rosetta_condition
			  def condition_0_BusinessCentersChoice(self):
			    """
			    Choice rule to represent an FpML choice construct.
			    """
			    def _then_fn0():
			      return all_elements(self.field3, ">", 0)
			    
			    def _else_fn0():
			      return all_elements(self.field4, ">", 0)
			    
			    return if_cond_fn(((self.field1) is not None), _then_fn0, _else_fn0)
			'''
			assertTrue(python.toString.contains(expected))
		}
		
	@Test	
	def void testConditionLessOrEqual() {
		val python = 
		'''
		type DateRange: <"A class defining a contiguous series of calendar dates. The date range is defined as all the dates between and including the start and the end date. The start date must fall on or before the end date.">
		
			startDate date (1..1) <"The first date of a date range.">
			endDate date (1..1) <"The last date of a date range.">
		
			condition DatesOrdered: <"The start date must fall on or before the end date (a date range of only one date is allowed).">
				startDate <= endDate
		'''.generatePython
		
		val expectedCondition = 
		'''
		class DateRange(BaseDataClass):
		  """
		  A class defining a contiguous series of calendar dates. The date range is defined as all the dates between and including the start and the end date. The start date must fall on or before the end date.
		  """
		  endDate: date = Field(..., description="The last date of a date range.")
		  """
		  The last date of a date range.
		  """
		  startDate: date = Field(..., description="The first date of a date range.")
		  """
		  The first date of a date range.
		  """
		  
		  @rosetta_condition
		  def condition_0_DatesOrdered(self):
		    """
		    The start date must fall on or before the end date (a date range of only one date is allowed).
		    """
		    return all_elements(self.startDate, "<=", self.endDate)
		'''
		assertTrue(python.toString.contains(expectedCondition))
	}

  	@Test
	def void testConditionsGeneration1() {
		val python = '''
			type A:
				a0 int (0..1)
				a1 int (0..1)
				condition: one-of
			type B:
				intValue1 int (0..1)
				intValue2 int (0..1)
				aValue A (1..1)
				condition Rule:
					intValue1 < 100
				condition OneOrTwo: <"Choice rule to represent an FpML choice construct.">
					optional choice intValue1, intValue2
				condition ReqOneOrTwo: <"Choice rule to represent an FpML choice construct.">
					required choice intValue1, intValue2
				condition SecondOneOrTwo: <"FpML specifies a choice between adjustedDate and [unadjustedDate (required), dateAdjutsments (required), adjustedDate (optional)].">
					if B exists
					then aValue->a0 exists
						or (intValue2 exists and intValue1 exists and intValue1 exists)
						or (intValue2 exists and intValue1 exists and intValue1 is absent)
			'''.generatePython
		
		val expectedA=
		'''
		class A(BaseDataClass):
		  a0: Optional[int] = Field(None, description="")
		  a1: Optional[int] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_(self):
		    return self.check_one_of_constraint('a0', 'a1', necessity=True)
		'''
		
		val expectedB=
		'''
		class B(BaseDataClass):
		  aValue: A = Field(..., description="")
		  intValue1: Optional[int] = Field(None, description="")
		  intValue2: Optional[int] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_Rule(self):
		    return all_elements(self.intValue1, "<", 100)
		  
		  @rosetta_condition
		  def condition_1_OneOrTwo(self):
		    """
		    Choice rule to represent an FpML choice construct.
		    """
		    return self.check_one_of_constraint('intValue1', 'intValue2', necessity=False)
		  
		  @rosetta_condition
		  def condition_2_ReqOneOrTwo(self):
		    """
		    Choice rule to represent an FpML choice construct.
		    """
		    return self.check_one_of_constraint('intValue1', 'intValue2', necessity=True)
		  
		  @rosetta_condition
		  def condition_3_SecondOneOrTwo(self):
		    """
		    FpML specifies a choice between adjustedDate and [unadjustedDate (required), dateAdjutsments (required), adjustedDate (optional)].
		    """
		    def _then_fn0():
		      return ((((self.aValue.a0) is not None) or ((((self.intValue2) is not None) and ((self.intValue1) is not None)) and ((self.intValue1) is not None))) or ((((self.intValue2) is not None) and ((self.intValue1) is not None)) and ((self.intValue1) is None)))
		    
		    def _else_fn0():
		      return True
		    
		    return if_cond_fn(((B) is not None), _then_fn0, _else_fn0)
		'''
		
		assertTrue(python.toString.contains(expectedA))
		assertTrue(python.toString.contains(expectedB))
	}
	
	@Test
	def void testConditionsGeneration2() {
		val python =
		'''
		enum EU_EMIR_EligibleCollateralEnum: <"Identifies European Union Eligible Collateral Assets classification categories based on EMIR Uncleared Margin Rules. Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities. Please note: EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM.">
						EU_EMIRTypeA <"Denotes Cash in the form of money credited to an account in any currency, or similar claims for the repayment of money, such as money market deposits.">
						EU_EMIRTypeB <" Denotes gold in the form of allocated pure gold bullion of recognised good delivery.">
						EU_EMIRTypeC <" Denotes debt securities issued by Member States' central governments or central banks.">
						EU_EMIRTypeD <" Denotes debt securities issued by Member States' regional governments or local authorities whose exposures are treated as exposures to the central government of that Member State in accordance with Article 115(2) of Regulation (EU) No 575/2013.">
						EU_EMIRTypeE <" Denotes debt securities issued by Member States' public sector entities whose exposures are treated as exposures to the central government, regional government or local authority of that Member State in accordance with Article 116(4) of Regulation (EU) No 575/2013.">
						EU_EMIRTypeF <" Denotes debt securities issued by Member States' regional governments or local authorities other than those referred to in (TypeD.)">
						EU_EMIRTypeG <" Denotes debt securities issued by Member States' public sector entities other than those referred to in (TypeE).">
						EU_EMIRTypeH <" Denotes debt securities issued by multilateral development banks listed in Article 117(2) of Regulation (EU) No 575/2013.">
						EU_EMIRTypeI <" Denotes debt securities issued by the international organisations listed in Article 118 of Regulation (EU) No 575/2013.">
						EU_EMIRTypeJ <" Denotes debt securities issued by third countries' governments or central banks.">
						EU_EMIRTypeK <" Denotes debt securities issued by third countries' regional governments or local authorities that meet the requirements of (TypeD) and (TypeE).">
						EU_EMIRTypeL <" Denotes debt securities issued by third countries' regional governments or local authorities other than those referred to in (TypeD) and (TypeE).">
						EU_EMIRTypeM <" Denotes debt securities issued by credit institutions or investment firms including bonds referred to in Article 52(4) of Directive 2009/65/EC of the European Parliament and of the Council.">
						EU_EMIRTypeN <" Denotes corporate bonds.">
						EU_EMIRTypeO <" Denotes the most senior tranche of a securitisation, as defined in Article 4(61) of Regulation (EU) No 575/2013, that is not a re-securitisation as defined in Article 4(63) of that Regulation.">
						EU_EMIRTypeP <" Denotes convertible bonds provided that they can be converted only into equities which are included in an index specified pursuant to point (a) of Article 197 (8) of Regulation (EU) No 575/2013.">
						EU_EMIRTypeQ <" Denotes equities included in an index specified pursuant to point (a) of Article 197(8) of Regulation (EU) No 575/2013.">
						EU_EMIRTypeR <" Denotes shares or units in undertakings for collective investments in transferable securities (UCITS), provided that the conditions set out in Article 5 of EU Regulation 2016/2251 are met.">
					
					enum UK_EMIR_EligibleCollateralEnum: <"Identifies United Kingdom Eligible Collateral Assets classification categories based on UK Onshored EMIR Uncleared Margin Rules. Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities. Please note: UK EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM.">
					
						UK_EMIRTypeA <"Denotes cash in the form of money credited to an account in any currency, or similar claims for the repayment of money, such as money market deposits.">
						UK_EMIRTypeB <"Denotes gold in the form of allocated pure gold bullion of recognised good delivery.">
						UK_EMIRTypeC <"Denotes debt securities issued by the central government of the United Kingdom or the Bank of England.">
						UK_EMIRTypeD <"Denotes debt securities issued by United Kingdom regional governments or local authorities whose exposures are treated as exposures to the central government of the United Kingdom in accordance with Article 115(2) of Regulation (EU) No 575/2013.">
						UK_EMIRTypeE <"Denotes debt securities issued by United Kingdom public sector entities whose exposures are treated as exposures to the central government, regional government or local authority of the United Kingdom in accordance with Article 116(4) of Regulation (EU) No 575/2013.">
						UK_EMIRTypeF <"Denotes debt securities issued by United Kingdom regional governments or local authorities other than those referred to in (TypeD).">
						UK_EMIRTypeG <"Denotes debt securities issued by United Kingdom public sector entities other than those referred to in (TypeE).">
						UK_EMIRTypeH <"Denotes debt securities issued by multilateral development banks listed in Article 117(2) of Regulation (EU) No 575/2013.">
						UK_EMIRTypeI <"Denotes debt securities issued by the international organisations listed in Article 118 of Regulation (EU) No 575/2013.">
						UK_EMIRTypeJ <"Denotes debt securities issued by third countries' governments or central banks.">
						UK_EMIRTypeK <"Denotes debt securities issued by third countries' regional governments or local authorities that meet the requirements of (TypeD) and (TypeE).">
						UK_EMIRTypeL <"Denotes debt securities issued by third countries' regional governments or local authorities other than those referred to in (TypeD) and (TypeE).">
						UK_EMIRTypeM <"Denotes debt securities issued by credit institutions or investment firms including bonds admitted to the register of regulated covered bonds maintained under Regulation 7(1)(b) of the Regulated Covered Bonds Regulations 2008 (SI 2008/346).">
						UK_EMIRTypeN <"Denotes corporate bonds.">
						UK_EMIRTypeO <"Denotes the most senior tranche of a securitisation, as defined in Article 4(61) of Regulation (EU) No 575/2013, that is not a re-securitisation as defined in Article 4(63) of that Regulation.">
						UK_EMIRTypeP <"Denotes convertible bonds provided that they can be converted only into equities which are included in an index specified pursuant to point (a) of Article 197 (8) of Regulation (EU) No 575/2013.">
						UK_EMIRTypeQ <"Denotes equities included in an index specified pursuant to point (a) of Article 197(8) of Regulation (EU) No 575/2013.">
						UK_EMIRTypeR <"Denotes shares or units in undertakings for UK UCITS, provided that the conditions set out in Article 5 of EU Regulation 2016/2251 (as modified by the Technical Standards (European Market Infrastructure) (EU Exit) (No. 3) Instrument 2019) are met.">
					
					enum US_CFTC_PR_EligibleCollateralEnum: <"Identifies US Eligible Collateral Assets classification categories based on Uncleared Margin Rules published by the CFTC and the US Prudential Regulator. Note: While the same basic categories exist in the CFTC and US Prudential Regulators margin rules, the precise definitions or application of those rules could differ between the two rules.">
					
						US_CFTC_PRType1 <"Denotes immediately available cash funds denominated in USD, a major currency, a currency of settlement for the uncleared swap.">
						US_CFTC_PRType2 <"Denotes a security that is issued by, or unconditionally guaranteed as to the timely payment of principal and interest by, the U.S. Department of the Treasury.">
						US_CFTC_PRType3 <"Denotes a security that is issued by, or unconditionally guaranteed as to the timely payment of principal and interest by, a U.S. government agency (other than the U.S. Department of Treasury) whose obligations are fully guaranteed by the full faith and credit of the United States government.">
						US_CFTC_PRType4 <"Denotes a security that is issued by, or fully guaranteed as to the payment of principal and interest by, the European Central Bank or a sovereign entity that is assigned no higher than a 20 percent risk weight under the capital rules applicable to swap dealers subject to regulation by a prudential regulator.">
						US_CFTC_PRType5A <"Denotes a publicly traded debt security issued by, or an asset-backed security fully guaranteed as to the timely payment of principal and interest by, a U.S. Government-sponsored enterprise that is operating with capital support or another form of direct financial assistance received from the U.S. government that enables the repayments of the U.S. Government-sponsored enterprise's eligible securities.">
						US_CFTC_PRType5B <"Denotes a publicly traded debt security, but not an asset backed security, that is investment grade and issued by a U.S. Government-sponsored enterprise that is not operating with capital support or another form of direct financial assistance received from the U.S. government.">
						US_CFTC_PRType6 <"Denotes a security that is issued by, or fully guaranteed as to the payment of principal and interest by, the Bank for International Settlements, the International Monetary Fund, or a multilateral development bank.">
						US_CFTC_PRType7 <"Denotes publicly-traded debt, but not an asset backed security, that is investment grade and is not a debt security issued by a  U.S. Government-sponsored enterprise. This category excludes a security issued by a non-bank financial institution supervised by the board of governors of the Federal Reserve System under Title I of the Dodd-Frank Wall Street Reform and Consumer Protection Act. This category also excludes a security issued by any of the following entities, by a company that would be any of the following entities if it were the organized under the laws of the United States or any State, or in either case by an affiliate of such an entity: the party posting the collateral, a bank holding company, a savings and loan holding company, a U.S. intermediate holding company, a foreign bank, a depositary institution, a securities holding company, a broker, a dealer, a futures commission merchant, a swap dealer, or a security-based swap dealer.">
						US_CFTC_PRType8A <"Denotes a publicly traded common equity security that is included in the Standard & Poor's Composite 500 Index or related indexes. This category excludes a security issued by a non-bank financial institution supervised by the board of governors of the Federal Reserve System under Title I of the Dodd-Frank Wall Street Reform and Consumer Protection Act. This category also excludes a security issued by any of the following entities, by a company that would be any of the following entities if it were the organized under the laws of the United States or any State, or in either case by an affiliate of such an entity: the party posting the collateral, a bank holding company, a savings and loan holding company, a U.S. intermediate holding company, a foreign bank, a depositary institution, a securities holding company, a broker, a dealer, a futures commission merchant, a swap dealer, or a security-based swap dealer.">
						US_CFTC_PRType8B <" Denotes a publicly traded common equity security that is included in the Standard & Poor's Composite 1500 Index or related indexes. This category excludes a security issued by a non-bank financial institution supervised by the board of governors of the Federal Reserve System under Title I of the Dodd-Frank Wall Street Reform and Consumer Protection Act. This category also excludes a security issued by any of the following entities, by a company that would be any of the following entities if it were the organized under the laws of the United States or any State, or in either case by an affiliate of such an entity: the party posting the collateral, a bank holding company, a savings and loan holding company, a U.S. intermediate holding company, a foreign bank, a depositary institution, a securities holding company, a broker, a dealer, a futures commission merchant, a swap dealer, or a security-based swap dealer.">
						US_CFTC_PRType8C <"Denotes a publicly traded common equity security that is included in an index that a regulated swap entity's supervisor in a foreign jurisdiction recognizes for purposes of including publicly traded common equity as initial margin under applicable regulatory policy, if held in that foreign jurisdiction. This category excludes a security issued by a non-bank financial institution supervised by the board of governors of the Federal Reserve System under Title I of the Dodd-Frank Wall Street Reform and Consumer Protection Act. This category also excludes a security issued by any of the following entities, by a company that would be any of the following entities if it were the organized under the laws of the United States or any State, or in either case by an affiliate of such an entity: the party posting the collateral, a bank holding company, a savings and loan holding company, a U.S. intermediate holding company, a foreign bank, a depositary institution, a securities holding company, a broker, a dealer, a futures commission merchant, a swap dealer, or a security-based swap dealer.">
						US_CFTC_PRType9<"Denotes securities in the form of redeemable securities in a pooled investment fund representing the security-holder's proportional interest in the fund's net assets and that are issued and redeemed only on the basis of the market value of the fund's net assets prepared each business day after the security-holder makes its investment commitment or redemption request to the fund, if the fund's investments are limited to the following: (A) securities that are issued by, or unconditionally guaranteed as to the timely payment of principal and interest by, the U.S. Department of the Treasury, and immediately-available cash funds denominated in U.S. dollars; or (B) securities denominated in a common currency and issued by, or fully guaranteed as to the payment of principal and interest by, the European Central Bank or a sovereign entity that is assigned no higher than a 20 percent risk weight under the capital rules applicable to swap dealers subject to regulation by a prudential regulator, and immediately-available cash funds denominated in the same currency; and (C) assets of the fund may not be transferred through securities lending, securities borrowing, repurchase agreements, reverse repurchase agreements, or other means that involve the fund having rights to acquire the same or similar assets from the transferee.">
						US_CTFC_PRType10 <"Denotes Gold.">
					
					enum TaxonomySourceEnum: <"Represents the enumerated values to specify taxonomy sources.">
						CFI <"Represents the ISO 10962 Classification of Financial Instruments code.">
						ISDA <"Represents the ISDA product taxonomy.">
						ICAD <"Represents the ISDA Collateral Asset Definition Idenifier code.">
						EMIR <"Represents the EMIR Article 9 Asset Definition Identifier code.">
						EU_EMIR_EligibleCollateralAssetClass <"Identifies European Union Eligible Collateral Assets classification categories based on EMIR Uncleared Margin Rules.">
						UK_EMIR_EligibleCollateralAssetClass <"Identifies United Kingdom Eligible Collateral Assets classification categories based on UK Onshored EMIR Uncleared Margin Rules Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities.Please note: UK EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM.">
						US_CFTC_PR_EligibleCollateralAssetClass <"Identifies US Eligible Collateral Assets classification categories based on Uncleared Margin Rules published by the CFTC and the US Prudential Regulator. Note: While the same basic categories exist in the CFTC and US Prudential Regulators margin rules, the precise definitions or application of those rules could differ between the two rules.">
						Other <"Denotes a user-specific scheme or taxonomy or other external sources not listed here.">
					
					
					type CollateralTaxonomyValue: <"Specifies the collateral taxonomy value, either as a specified enumeration or as a string.">
						eu_EMIR_EligibleCollateral EU_EMIR_EligibleCollateralEnum (0..*) <"Identifies European Union Eligible Collateral Assets classification categories based on EMIR Uncleared Margin Rules. Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities. Please note: EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM">
						uk_EMIR_EligibleCollateral UK_EMIR_EligibleCollateralEnum (0..*) <"Identifies United Kingdom Eligible Collateral Assets classification categories based on UK Onshored EMIR Uncleared Margin Rules Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities. Please note: UK EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM.">
						us_CFTC_PR_EligibleCollateral US_CFTC_PR_EligibleCollateralEnum (0..*) <"Identifies US Eligible Collateral Assets classification categories based on Uncleared Margin Rules published by the CFTC and the US Prudential Regulator. Note: While the same basic categories exist in the CFTC and US Prudential Regulators’ margin rules, the precise definitions or application of those rules could differ between the two rules.">
						nonEnumeratedTaxonomyValue string (0..*) <"Identifies the taxonomy value when not specified as an enumeration.">
							[metadata scheme]
					
						condition: one-of
					
		 			type CollateralTaxonomy: <"Specifies the collateral taxonomy, which is composed of a taxonomy value and a taxonomy source.">
		 				taxonomyValue CollateralTaxonomyValue (1..1) <"Specifies the taxonomy value.">
		 				taxonomySource TaxonomySourceEnum (1..1) <"Specifies the taxonomy source.">
		 				
		 				condition Eu_EligibleCollateralTaxonomy: <"If the Taxonomy Source is specified as EU EMIR Eligible Collateral then the enumeration must be EU EMIR Eligible Collateral.">
		 					if taxonomySource = TaxonomySourceEnum -> EU_EMIR_EligibleCollateralAssetClass
		 						then taxonomyValue -> eu_EMIR_EligibleCollateral exists
		 				
		 				condition UkEligibleCollateralTaxonomy: <"If the Taxonomy Source is specified as UK EMIR Eligible Collateral then the enumeration must be UK EMIR Eligible Collateral.">
		 					if taxonomySource = TaxonomySourceEnum-> UK_EMIR_EligibleCollateralAssetClass
		 						then taxonomyValue -> uk_EMIR_EligibleCollateral exists
		 				
		 				condition UsEligibleCollateralTaxonomy: <"If the Taxonomy Source is specified as US CFTCPR Eligbile Collateral then the enumeration must be US CFTCPR Eligible Collateral.">
		 					if taxonomySource = TaxonomySourceEnum-> US_CFTC_PR_EligibleCollateralAssetClass
		 						then taxonomyValue -> us_CFTC_PR_EligibleCollateral exists
		 				
		 				condition TaxonomyValue: <"If the Taxonomy Value is specified as a string then the taxonomy Source cannot be either EU Eligible Collateral or Uk Eligible Collateral or US Eligible Collateral.">
		 					if taxonomyValue -> nonEnumeratedTaxonomyValue exists
		 						then taxonomySource <> TaxonomySourceEnum -> EU_EMIR_EligibleCollateralAssetClass
		 							and taxonomySource <> TaxonomySourceEnum -> UK_EMIR_EligibleCollateralAssetClass
		 							and taxonomySource <> TaxonomySourceEnum -> US_CFTC_PR_EligibleCollateralAssetClass
		'''.generatePython
		

		
		val expectedCollateralTaxonomy=
		'''
		class CollateralTaxonomyValue(BaseDataClass):
		  """
		  Specifies the collateral taxonomy value, either as a specified enumeration or as a string.
		  """
		  eu_EMIR_EligibleCollateral: List[EU_EMIR_EligibleCollateralEnum] = Field([], description="Identifies European Union Eligible Collateral Assets classification categories based on EMIR Uncleared Margin Rules. Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities. Please note: EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM")
		  """
		  Identifies European Union Eligible Collateral Assets classification categories based on EMIR Uncleared Margin Rules. Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities. Please note: EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM
		  """
		  nonEnumeratedTaxonomyValue: List[AttributeWithMeta[str] | str] = Field([], description="Identifies the taxonomy value when not specified as an enumeration.")
		  """
		  Identifies the taxonomy value when not specified as an enumeration.
		  """
		  uk_EMIR_EligibleCollateral: List[UK_EMIR_EligibleCollateralEnum] = Field([], description="Identifies United Kingdom Eligible Collateral Assets classification categories based on UK Onshored EMIR Uncleared Margin Rules Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities. Please note: UK EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM.")
		  """
		  Identifies United Kingdom Eligible Collateral Assets classification categories based on UK Onshored EMIR Uncleared Margin Rules Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities. Please note: UK EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM.
		  """
		  us_CFTC_PR_EligibleCollateral: List[US_CFTC_PR_EligibleCollateralEnum] = Field([], description="Identifies US Eligible Collateral Assets classification categories based on Uncleared Margin Rules published by the CFTC and the US Prudential Regulator. Note: While the same basic categories exist in the CFTC and US Prudential Regulators’ margin rules, the precise definitions or application of those rules could differ between the two rules.")
		  """
		  Identifies US Eligible Collateral Assets classification categories based on Uncleared Margin Rules published by the CFTC and the US Prudential Regulator. Note: While the same basic categories exist in the CFTC and US Prudential Regulators’ margin rules, the precise definitions or application of those rules could differ between the two rules.
		  """
		  
		  @rosetta_condition
		  def condition_0_(self):
		    return self.check_one_of_constraint('eu_EMIR_EligibleCollateral', 'uk_EMIR_EligibleCollateral', 'us_CFTC_PR_EligibleCollateral', 'nonEnumeratedTaxonomyValue', necessity=True)
		'''
		

		assertTrue(python.toString.contains(expectedCollateralTaxonomy))

	}
	
	
	
	
	def generatePython(CharSequence model) {
		 val eResource = model.parseRosetta.eResource
		 generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
	}
	
}