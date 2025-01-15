package com.regnosys.rosetta.generator.python.object

import com.google.inject.Inject
import com.regnosys.rosetta.generator.python.PythonCodeGenerator
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
    def void testMultilineAttributeDefinition() {
        val python = '''type Foo:
            attr int (1..1) 
                <"This is a
multiline
definition">
        '''.generatePython
        val expected = '''class Foo(BaseDataClass):
    attr: int = Field(..., description="This is a multiline definition")
    """
    This is a
    multiline
    definition
    """'''
        assertTrue(python.get("src/com/rosetta/test/model/Foo.py").toString.contains(expected))
    }
    
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
                    aValue->a0 exists
                        or (intValue2 exists and intValue1 exists and intValue1 exists)
                        or (intValue2 exists and intValue1 exists and intValue1 is absent)
            '''.generatePython
        
        val expectedA='''class A(BaseDataClass):
    a0: Optional[int] = Field(None, description="")
    a1: Optional[int] = Field(None, description="")
    
    @rosetta_condition
    def condition_0_(self):
        item = self
        return rosetta_check_one_of(self, 'a0', 'a1', necessity=True)'''

        val expectedB='''class B(BaseDataClass):
    intValue1: Optional[int] = Field(None, description="")
    intValue2: Optional[int] = Field(None, description="")
    aValue: com.rosetta.test.model.A.A = Field(..., description="")
    
    @rosetta_condition
    def condition_0_Rule(self):
        item = self
        return all_elements(rosetta_resolve_attr(self, "intValue1"), "<", 100)
    
    @rosetta_condition
    def condition_1_OneOrTwo(self):
        """
        Choice rule to represent an FpML choice construct.
        """
        item = self
        return rosetta_check_one_of(self, 'intValue1', 'intValue2', necessity=False)
    
    @rosetta_condition
    def condition_2_SecondOneOrTwo(self):
        """
        FpML specifies a choice between adjustedDate and [unadjustedDate (required), dateAdjutsments (required), adjustedDate (optional)].
        """
        item = self
        return ((rosetta_attr_exists(rosetta_resolve_attr(rosetta_resolve_attr(self, "aValue"), "a0")) or ((rosetta_attr_exists(rosetta_resolve_attr(self, "intValue2")) and rosetta_attr_exists(rosetta_resolve_attr(self, "intValue1"))) and rosetta_attr_exists(rosetta_resolve_attr(self, "intValue1")))) or ((rosetta_attr_exists(rosetta_resolve_attr(self, "intValue2")) and rosetta_attr_exists(rosetta_resolve_attr(self, "intValue1"))) and (not rosetta_attr_exists(rosetta_resolve_attr(self, "intValue1")))))'''
        assertTrue(python.toString.contains(expectedA))
        assertTrue(python.toString.contains(expectedB))
    }
    
    
    @Test
    def void testGenerateTypes1() {
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
                 
          
          val expectedTestType = '''class TestType(BaseDataClass):
    """
    Test type description.
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
    testTypeValue4: com.rosetta.test.model.TestType2.TestType2 = Field(..., description="Test TestType2")
    """
    Test TestType2
    """
    testEnum: Optional[com.rosetta.test.model.TestEnum.TestEnum] = Field(None, description="Optional test enum")
    """
    Optional test enum
    """'''
        val expectedTestType2 ='''class TestType2(BaseDataClass):
    testType2Value1: List[Decimal] = Field([], description="Test number list")
    """
    Test number list
    """
    @rosetta_condition
    def cardinality_testType2Value1(self):
        return check_cardinality(self.testType2Value1, 1, None)
    
    testType2Value2: Optional[datetime.date] = Field(None, description="Test date")
    """
    Test date
    """
    testEnum: Optional[com.rosetta.test.model.TestEnum.TestEnum] = Field(None, description="Optional test enum")
    """
    Optional test enum
    """'''

        val expectedTestEnum ='''class TestEnum(Enum):
    """
    Test enum description.
    """
    TEST_ENUM_VALUE_1 = "TestEnumValue1"
    """
    Test enum value 1
    """
    TEST_ENUM_VALUE_2 = "TestEnumValue2"
    """
    Test enum value 2
    """'''
        
        assertTrue(python.toString.contains(expectedTestType))
        assertTrue(python.toString.contains(expectedTestType2))
        assertTrue(python.toString.contains(expectedTestEnum))
    }
    
    @Test 
    def void testGenerateTypes2() {
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

        val expectedTestType2='''class FinancialUnitEnum(Enum):
    """
    Provides enumerated values for financial units, generally used in the context of defining quantities for securities.
    """
    CONTRACT = "Contract"
    """
    Denotes financial contracts, such as listed futures and options.
    """
    CONTRACTUAL_PRODUCT = "ContractualProduct"
    """
    Denotes a Contractual Product as defined in the CDM.  This unit type would be used when the price applies to the whole product, for example, in the case of a premium expressed as a cash amount.
    """
    INDEX_UNIT = "IndexUnit"
    """
    Denotes a price expressed in index points, e.g. for a stock index.
    """
    LOG_NORMAL_VOLATILITY = "LogNormalVolatility"
    """
    Denotes a log normal volatility, expressed in %/month, where the percentage is represented as a decimal. For example, 0.15 means a log-normal volatility of 15% per month.
    """
    SHARE = "Share"
    """
    Denotes the number of units of financial stock shares.
    """
    VALUE_PER_DAY = "ValuePerDay"
    """
    Denotes a value (expressed in currency units) for a one day change in a valuation date, which is typically used for expressing sensitivity to the passage of time, also known as theta risk, or carry, or other names.
    """
    VALUE_PER_PERCENT = "ValuePerPercent"
    """
    Denotes a value (expressed in currency units) per percent change in the underlying rate which is typically used for expressing sensitivity to volatility changes, also known as vega risk.
    """
    WEIGHT = "Weight"
    """
    Denotes a quantity (expressed as a decimal value) represented the weight of a component in a basket.
    """'''
    val expectedTestType ='''class UnitType(BaseDataClass):
    """
    Defines the unit to be used for price, quantity, or other purposes
    """
    capacityUnit: Optional[com.rosetta.test.model.CapacityUnitEnum.CapacityUnitEnum] = Field(None, description="Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.")
    """
    Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.
    """
    weatherUnit: Optional[com.rosetta.test.model.WeatherUnitEnum.WeatherUnitEnum] = Field(None, description="Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.")
    """
    Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.
    """
    financialUnit: Optional[com.rosetta.test.model.FinancialUnitEnum.FinancialUnitEnum] = Field(None, description="Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.")
    """
    Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.
    """
    currency: Optional[AttributeWithMeta[str] | str] = Field(None, description="Defines the currency to be used as a unit for a price, quantity, or other purpose.")
    """
    Defines the currency to be used as a unit for a price, quantity, or other purpose.
    """
    
    @rosetta_condition
    def condition_0_UnitType(self):
        """
        Requires that a unit type must be set.
        """
        item = self
        return rosetta_check_one_of(self, 'capacityUnit', 'weatherUnit', 'financialUnit', 'currency', necessity=True)
    '''
        val expectedTestType3='''class WeatherUnitEnum(Enum):
    """
    Provides enumerated values for weather units, generally used in the context of defining quantities for commodities.
    """
    CDD = "CDD"
    """
    Denotes Cooling Degree Days as a standard unit.
    """
    CPD = "CPD"
    """
    Denotes Critical Precipitation Day as a standard unit.
    """
    HDD = "HDD"
    """
    Heating Degree Day as a standard unit.
    """'''
        val expectedTestType4='''class CapacityUnitEnum(Enum):
    """
    Provides enumerated values for capacity units, generally used in the context of defining quantities for commodities.
    """
    ALW = "ALW"
    """
    Denotes Allowances as standard unit.
    """
    BBL = "BBL"
    """
    Denotes a Barrel as a standard unit.
    """
    BCF = "BCF"
    """
    Denotes Billion Cubic Feet as a standard unit.
    """
    BDFT = "BDFT"
    """
    Denotes Board Feet as a standard unit.
    """
    BSH = "BSH"
    """
    Denotes a Bushel as a standard unit of weight (48 lb or 21.7725 kg).
    """
    BTU = "BTU"
    """
    Denotes British Thermal Units as a standard unit.
    """
    CBM = "CBM"
    """
    Denotes Cubic Meters as a standard unit.
    """
    CER = "CER"
    """
    Denotes Certified Emissions Reduction as a standard unit.
    """
    CRT = "CRT"
    """
    Denotes Climate Reserve Tonnes as a standard unit.
    """
    DAG = "DAG"
    """
    Denotes 10 grams as a standard unit used in precious metals contracts (e.g MCX).
    """
    DAY = "DAY"
    """
    Denotes a single day as a standard unit used in time charter trades.
    """
    DMTU = "DMTU"
    """
    Denotes Dry Metric Ton (Tonne) Units - Consists of a metric ton of mass excluding moisture.
    """
    DTH = "DTH"
    """
    Denotes a Dekatherm as a standard unit.
    """
    ENVCRD = "ENVCRD"
    """
    Denotes Environmental Credit as a standard unit.
    """
    ENVOFST = "ENVOFST"
    """
    Denotes Environmental Offset as a standard unit.
    """
    FEU = "FEU"
    """
    Denotes a 40 ft. Equivalent Unit container as a standard unit.
    """
    G = "G"
    """
    Denotes a Gram as a standard unit.
    """
    GBCWT = "GBCWT"
    """
    Denotes a GB Hundredweight unit as standard unit.
    """
    GBGAL = "GBGAL"
    """
    Denotes a GB Gallon unit as standard unit.
    """
    GBT = "GBT"
    """
    Denotes a GB Ton as a standard unit.
    """
    GJ = "GJ"
    """
    Denotes a Gigajoule as a standard unit.
    """
    GW = "GW"
    """
    Denotes a Gigawatt as a standard unit.
    """
    GWH = "GWH"
    """
    Denotes a Gigawatt-hour as a standard unit.
    """
    HL = "HL"
    """
    Denotes a Hectolitre as a standard unit.
    """
    INGOT = "INGOT"
    """
    Denotes an Ingot as a standard unit.
    """
    KG = "KG"
    """
    Denotes a Kilogram as a standard unit.
    """
    KL = "KL"
    """
    Denotes a Kilolitre as a standard unit.
    """
    KW = "KW"
    """
    Denotes a Kilowatt as a standard unit.
    """
    KWDC = "KWDC"
    """
    Denotes a Kilowatt Day Capacity as a standard unit.
    """
    KWH = "KWH"
    """
    Denotes a Kilowatt-hour as a standard unit.
    """
    KWHC = "KWHC"
    """
    Denotes a Kilowatt Hours Capacity as a standard unit.
    """
    KWMC = "KWMC"
    """
    Denotes a Kilowatt Month Capacity as a standard unit.
    """
    KWMINC = "KWMINC"
    """
    Denotes a Kilowatt Minute Capacity as a standard unit.
    """
    KWYC = "KWYC"
    """
    Denotes a Kilowatt Year Capacity as a standard unit.
    """
    L = "L"
    """
    Denotes a Litre as a standard unit.
    """
    LB = "LB"
    """
    Denotes a Pound as a standard unit.
    """
    MB = "MB"
    """
    Denotes a Thousand Barrels as a standard unit.
    """
    MBF = "MBF"
    """
    Denotes a Thousand board feet, which are used in contracts on forestry underlyers as a standard unit.
    """
    MJ = "MJ"
    """
    Denotes a Megajoule as a standard unit.
    """
    MMBBL = "MMBBL"
    """
    Denotes a Million Barrels as a standard unit.
    """
    MMBF = "MMBF"
    """
    Denotes a Million board feet, which are used in contracts on forestry underlyers as a standard unit.
    """
    MMBTU = "MMBTU"
    """
    Denotes a Million British Thermal Units as a standard unit.
    """
    MSF = "MSF"
    """
    Denotes a Thousand square feet as a standard unit.
    """
    MT = "MT"
    """
    Denotes a Metric Ton as a standard unit.
    """
    MW = "MW"
    """
    Denotes a Megawatt as a standard unit.
    """
    MWDC = "MWDC"
    """
    Denotes a Megawatt Day Capacity as a standard unit.
    """
    MWH = "MWH"
    """
    Denotes a Megawatt-hour as a standard unit.
    """
    MWHC = "MWHC"
    """
    Denotes a Megawatt Hours Capacity as a standard unit.
    """
    MWMC = "MWMC"
    """
    Denotes a Megawatt Month Capacity as a standard unit.
    """
    MWMINC = "MWMINC"
    """
    Denotes a Megawatt Minute Capacity as a standard unit.
    """
    MWYC = "MWYC"
    """
    Denotes a Megawatt Year Capacity as a standard unit.
    """
    OZT = "OZT"
    """
    Denotes a Troy Ounce as a standard unit.
    """
    TEU = "TEU"
    """
    Denotes a 20 ft. Equivalent Unit container as a standard unit.
    """
    THERM = "THERM"
    """
    Denotes a Thermal Unit as a standard unit.
    """
    USCWT = "USCWT"
    """
    Denotes US Hundredweight unit as a standard unit.
    """
    USGAL = "USGAL"
    """
    Denotes a US Gallon unit as a standard unit.
    """
    UST = "UST"
    """
    Denotes a US Ton as a standard unit.
    """'''
        assertTrue(python.toString.contains(expectedTestType))
        assertTrue(python.toString.contains(expectedTestType2))
        assertTrue(python.toString.contains(expectedTestType3))
        assertTrue(python.toString.contains(expectedTestType4))
    }
    
    @Test
    def void testGenerateTypes3() {
        val python =
        '''
        enum AncillaryRoleEnum: <"Defines the enumerated values to specify the ancillary roles to the transaction. The product is agnostic to the actual parties involved in the transaction, with the party references abstracted away from the product definition and replaced by the AncillaryRoleEnum. The AncillaryRoleEnum can then be positioned in the product and the AncillaryParty type, which is positioned outside of the product definition, allows the AncillaryRoleEnum to be associated with an actual party reference.">
            DisruptionEventsDeterminingParty <"Specifies the party which determines additional disruption events.">
            ExtraordinaryDividendsParty <"Specifies the party which determines if dividends are extraordinary in relation to normal levels.">
            PredeterminedClearingOrganizationParty <"Specifies the clearing organization (CCP, DCO) which the trade test be cleared.">
            ExerciseNoticeReceiverPartyManual <"Specifies the party to which notice of a manual exercise test be given.">
            ExerciseNoticeReceiverPartyOptionalEarlyTermination <"Specifies the party to which notice of a optional early termination exercise test be given.">
            ExerciseNoticeReceiverPartyCancelableProvision <"Specifies the party to which notice of a cancelable provision exercise test be given.">
            ExerciseNoticeReceiverPartyExtendibleProvision <"Specifies the party to which notice of a extendible provision exercise test be given.">
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

            ancillaryParty AncillaryRoleEnum (0..1) <"Identifies a party via its ancillary role on a transaction (e.g. CCP or DCO through which the trade test be cleared.)">
            legalEntity LegalEntity (0..1)

            condition: one-of
        '''.generatePython


        val expectedTestType1 ='''class LegalEntity(BaseDataClass):
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
    """'''
        val expectedTestType2 ='''class TelephoneNumber(BaseDataClass):
    """
    A class to specify a telephone number as a type of phone number (e.g. work, personal, ...) alongside with the actual number.
    """
    telephoneNumberType: Optional[com.rosetta.test.model.TelephoneTypeEnum.TelephoneTypeEnum] = Field(None, description="The type of telephone number, e.g. work, mobile.")
    """
    The type of telephone number, e.g. work, mobile.
    """
    number: str = Field(..., description="The actual telephone number.")
    """
    The actual telephone number.
    """'''
        val expectedTestType3 ='''class AncillaryEntity(BaseDataClass):
    """
    Holds an identifier for an ancillary entity, either identified directly via its ancillary role or directly as a legal entity.
    """
    ancillaryParty: Optional[com.rosetta.test.model.AncillaryRoleEnum.AncillaryRoleEnum] = Field(None, description="Identifies a party via its ancillary role on a transaction (e.g. CCP or DCO through which the trade test be cleared.)")
    """
    Identifies a party via its ancillary role on a transaction (e.g. CCP or DCO through which the trade test be cleared.)
    """
    legalEntity: Optional[com.rosetta.test.model.LegalEntity.LegalEntity] = Field(None, description="")
    
    @rosetta_condition
    def condition_0_(self):
        item = self
        return rosetta_check_one_of(self, 'ancillaryParty', 'legalEntity', necessity=True)'''

        val expectedTestType4='''class AncillaryRoleEnum(Enum):
    """
    Defines the enumerated values to specify the ancillary roles to the transaction. The product is agnostic to the actual parties involved in the transaction, with the party references abstracted away from the product definition and replaced by the AncillaryRoleEnum. The AncillaryRoleEnum can then be positioned in the product and the AncillaryParty type, which is positioned outside of the product definition, allows the AncillaryRoleEnum to be associated with an actual party reference.
    """
    CALCULATION_AGENT_FALLBACK = "CalculationAgentFallback"
    """
    Specifies the party responsible for deciding the fallback rate.
    """
    CALCULATION_AGENT_INDEPENDENT = "CalculationAgentIndependent"
    """
    Specifies the party responsible for performing calculation agent duties as defined in the applicable product definition.
    """
    CALCULATION_AGENT_MANDATORY_EARLY_TERMINATION = "CalculationAgentMandatoryEarlyTermination"
    """
    Specifies the party responsible for performing calculation agent duties associated with an mandatory early termination.
    """
    CALCULATION_AGENT_OPTIONAL_EARLY_TERMINATION = "CalculationAgentOptionalEarlyTermination"
    """
    Specifies the party responsible for performing calculation agent duties associated with an optional early termination.
    """
    DISRUPTION_EVENTS_DETERMINING_PARTY = "DisruptionEventsDeterminingParty"
    """
    Specifies the party which determines additional disruption events.
    """
    EXERCISE_NOTICE_RECEIVER_PARTY_CANCELABLE_PROVISION = "ExerciseNoticeReceiverPartyCancelableProvision"
    """
    Specifies the party to which notice of a cancelable provision exercise test be given.
    """
    EXERCISE_NOTICE_RECEIVER_PARTY_EXTENDIBLE_PROVISION = "ExerciseNoticeReceiverPartyExtendibleProvision"
    """
    Specifies the party to which notice of a extendible provision exercise test be given.
    """
    EXERCISE_NOTICE_RECEIVER_PARTY_MANUAL = "ExerciseNoticeReceiverPartyManual"
    """
    Specifies the party to which notice of a manual exercise test be given.
    """
    EXERCISE_NOTICE_RECEIVER_PARTY_OPTIONAL_EARLY_TERMINATION = "ExerciseNoticeReceiverPartyOptionalEarlyTermination"
    """
    Specifies the party to which notice of a optional early termination exercise test be given.
    """
    EXTRAORDINARY_DIVIDENDS_PARTY = "ExtraordinaryDividendsParty"
    """
    Specifies the party which determines if dividends are extraordinary in relation to normal levels.
    """
    PREDETERMINED_CLEARING_ORGANIZATION_PARTY = "PredeterminedClearingOrganizationParty"
    """
    Specifies the clearing organization (CCP, DCO) which the trade test be cleared.
    """'''
        val expectedTestType5='''class TelephoneTypeEnum(Enum):
    """
    The enumerated values to specify the type of telephone number, e.g. work vs. mobile.
    """
    FAX = "Fax"
    """
    A number used primarily for work-related facsimile transmissions.
    """
    MOBILE = "Mobile"
    """
    A number on a mobile telephone that is often or usually used for work-related calls. This type of number can be used for urgent work related business when a work number is not sufficient to contact the person or firm.
    """
    PERSONAL = "Personal"
    """
    A number used primarily for non work-related calls. (Normally this type of number would be used only as an emergency backup number, not as a regular course of business).
    """
    WORK = "Work"
    """
    A number used primarily for work-related calls. Includes home office numbers used primarily for work purposes.
    """'''

        assertTrue(python.toString.contains(expectedTestType1))
        assertTrue(python.toString.contains(expectedTestType2))
        assertTrue(python.toString.contains(expectedTestType3))
        assertTrue(python.toString.contains(expectedTestType4))
        assertTrue(python.toString.contains(expectedTestType5))
    }
    
    @Test
    def void testGenerateTypesMethod2() {
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

        val expectedMeasureBase='''class MeasureBase(BaseDataClass):
    """
    Provides an abstract base class shared by Price and Quantity.
    """
    amount: Decimal = Field(..., description="Specifies an amount to be qualified and used in a Price or Quantity definition.")
    """
    Specifies an amount to be qualified and used in a Price or Quantity definition.
    """
    unitOfAmount: com.rosetta.test.model.UnitType.UnitType = Field(..., description="Qualifies the unit by which the amount is measured.")
    """
    Qualifies the unit by which the amount is measured.
    """'''
    val expectedUnitType='''class UnitType(BaseDataClass):
    """
    Defines the unit to be used for price, quantity, or other purposes
    """
    currency: Optional[str] = Field(None, description="Defines the currency to be used as a unit for a price, quantity, or other purpose.")
    """
    Defines the currency to be used as a unit for a price, quantity, or other purpose.
    """'''
    val expectedQuantity='''class Quantity(MeasureBase):
    """
    Specifies a quantity to be associated to a financial product, for example a trade amount or a cashflow amount resulting from a trade.
    """
    multiplier: Optional[Decimal] = Field(None, description="Defines the number to be multiplied by the amount to derive a total quantity.")
    """
    Defines the number to be multiplied by the amount to derive a total quantity.
    """
    multiplierUnit: Optional[com.rosetta.test.model.UnitType.UnitType] = Field(None, description="Qualifies the multiplier with the applicable unit. For example in the case of the Coal (API2) CIF ARA (ARGUS-McCloskey) Futures Contract on the CME, where the unitOfAmount would be contracts, the multiplier would 1,000 and the mulitiplier Unit would be 1,000 MT (Metric Tons).")
    """
    Qualifies the multiplier with the applicable unit.  For example in the case of the Coal (API2) CIF ARA (ARGUS-McCloskey) Futures Contract on the CME, where the unitOfAmount would be contracts, the multiplier would 1,000 and the mulitiplier Unit would be 1,000 MT (Metric Tons).
    """'''
        assertTrue(python.toString.contains(expectedMeasureBase))
        assertTrue(python.toString.contains(expectedUnitType))
        assertTrue(python.toString.contains(expectedQuantity))
    }

    @Test
    def void testGenerateTypesExtends1 () {
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
        
        val expectedTestType='''class TestType(TestType2):
    TestTypeValue1: str = Field(..., description="Test string")
    """
    Test string
    """
    TestTypeValue2: Optional[int] = Field(None, description="Test int")
    """
    Test int
    """
      '''
        val expectedTestType2='''class TestType2(TestType3):
    TestType2Value1: Optional[Decimal] = Field(None, description="Test number")
    """
    Test number
    """
    TestType2Value2: List[datetime.date] = Field([], description="Test date")
    """
    Test date
    """
    '''
        val expectedTestType3='''class TestType3(BaseDataClass):
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
    def void testGenerateTypesExtends2() {
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

        val expectedTestType1 ='''class MeasureBase(BaseDataClass):
    """
    Provides an abstract type to define a measure as a number associated to a unit. This type is abstract because all its attributes are optional. The types that extend it can specify further existence constraints.
    """
    value: Optional[Decimal] = Field(None, description="Specifies the value of the measure as a number. Optional because in a measure vector or schedule, this single value may be omitted.")
    """
    Specifies the value of the measure as a number. Optional because in a measure vector or schedule, this single value may be omitted.
    """
    unit: Optional[com.rosetta.test.model.UnitType.UnitType] = Field(None, description="Qualifies the unit by which the amount is measured. Optional because a measure may be unit-less (e.g. when representing a ratio between amounts in the same unit).")
    """
    Qualifies the unit by which the amount is measured. Optional because a measure may be unit-less (e.g. when representing a ratio between amounts in the same unit).
    """'''

        val expectedTestType2 ='''class Measure(MeasureBase):
    """
    Defines a concrete measure as a number associated to a unit. It extends MeasureBase by requiring the value attribute to be present. A measure may be unit-less so the unit attribute is still optional.
    """
    
    @rosetta_condition
    def condition_0_ValueExists(self):
        """
        The value attribute must be present in a concrete measure.
        """
        item = self
        return rosetta_attr_exists(rosetta_resolve_attr(self, "value"))'''
        
        val expectedTestType3='''class WeatherUnitEnum(Enum):
    """
    Provides enumerated values for weather units, generally used in the context of defining quantities for commodities.
    """
    CDD = "CDD"
    """
    Denotes Cooling Degree Days as a standard unit.
    """
    CPD = "CPD"
    """
    Denotes Critical Precipitation Day as a standard unit.
    """
    HDD = "HDD"
    """
    Heating Degree Day as a standard unit.
    """'''
    
        val expectedTestType4='''class FinancialUnitEnum(Enum):
    """
    Provides enumerated values for financial units, generally used in the context of defining quantities for securities.
    """
    CONTRACT = "Contract"
    """
    Denotes financial contracts, such as listed futures and options.
    """
    CONTRACTUAL_PRODUCT = "ContractualProduct"
    """
    Denotes a Contractual Product as defined in the CDM.  This unit type would be used when the price applies to the whole product, for example, in the case of a premium expressed as a cash amount.
    """
    INDEX_UNIT = "IndexUnit"
    """
    Denotes a price expressed in index points, e.g. for a stock index.
    """
    LOG_NORMAL_VOLATILITY = "LogNormalVolatility"
    """
    Denotes a log normal volatility, expressed in %/month, where the percentage is represented as a decimal. For example, 0.15 means a log-normal volatility of 15% per month.
    """
    SHARE = "Share"
    """
    Denotes the number of units of financial stock shares.
    """
    VALUE_PER_DAY = "ValuePerDay"
    """
    Denotes a value (expressed in currency units) for a one day change in a valuation date, which is typically used for expressing sensitivity to the passage of time, also known as theta risk, or carry, or other names.
    """
    VALUE_PER_PERCENT = "ValuePerPercent"
    """
    Denotes a value (expressed in currency units) per percent change in the underlying rate which is typically used for expressing sensitivity to volatility changes, also known as vega risk.
    """
    WEIGHT = "Weight"
    """
    Denotes a quantity (expressed as a decimal value) represented the weight of a component in a basket.
    """'''
        val expectedTestType5='''class UnitType(BaseDataClass):
    """
    Defines the unit to be used for price, quantity, or other purposes
    """
    capacityUnit: Optional[com.rosetta.test.model.CapacityUnitEnum.CapacityUnitEnum] = Field(None, description="Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.")
    """
    Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.
    """
    weatherUnit: Optional[com.rosetta.test.model.WeatherUnitEnum.WeatherUnitEnum] = Field(None, description="Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.")
    """
    Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.
    """
    financialUnit: Optional[com.rosetta.test.model.FinancialUnitEnum.FinancialUnitEnum] = Field(None, description="Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.")
    """
    Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.
    """
    currency: Optional[AttributeWithMeta[str] | str] = Field(None, description="Defines the currency to be used as a unit for a price, quantity, or other purpose.")
    """
    Defines the currency to be used as a unit for a price, quantity, or other purpose.
    """
    
    @rosetta_condition
    def condition_0_UnitType(self):
        """
        Requires that a unit type must be set.
        """
        item = self
        return rosetta_check_one_of(self, 'capacityUnit', 'weatherUnit', 'financialUnit', 'currency', necessity=True)'''
        
        val expectedTestType6='''class CapacityUnitEnum(Enum):
    """
    Provides enumerated values for capacity units, generally used in the context of defining quantities for commodities.
    """
    ALW = "ALW"
    """
    Denotes Allowances as standard unit.
    """
    BBL = "BBL"
    """
    Denotes a Barrel as a standard unit.
    """
    BCF = "BCF"
    """
    Denotes Billion Cubic Feet as a standard unit.
    """
    BDFT = "BDFT"
    """
    Denotes Board Feet as a standard unit.
    """
    BSH = "BSH"
    """
    Denotes a Bushel as a standard unit of weight (48 lb or 21.7725 kg).
    """
    BTU = "BTU"
    """
    Denotes British Thermal Units as a standard unit.
    """
    CBM = "CBM"
    """
    Denotes Cubic Meters as a standard unit.
    """
    CER = "CER"
    """
    Denotes Certified Emissions Reduction as a standard unit.
    """
    CRT = "CRT"
    """
    Denotes Climate Reserve Tonnes as a standard unit.
    """
    DAG = "DAG"
    """
    Denotes 10 grams as a standard unit used in precious metals contracts (e.g MCX).
    """
    DAY = "DAY"
    """
    Denotes a single day as a standard unit used in time charter trades.
    """
    DMTU = "DMTU"
    """
    Denotes Dry Metric Ton (Tonne) Units - Consists of a metric ton of mass excluding moisture.
    """
    DTH = "DTH"
    """
    Denotes a Dekatherm as a standard unit.
    """
    ENVCRD = "ENVCRD"
    """
    Denotes Environmental Credit as a standard unit.
    """
    ENVOFST = "ENVOFST"
    """
    Denotes Environmental Offset as a standard unit.
    """
    FEU = "FEU"
    """
    Denotes a 40 ft. Equivalent Unit container as a standard unit.
    """
    G = "G"
    """
    Denotes a Gram as a standard unit.
    """
    GBCWT = "GBCWT"
    """
    Denotes a GB Hundredweight unit as standard unit.
    """
    GBGAL = "GBGAL"
    """
    Denotes a GB Gallon unit as standard unit.
    """
    GBT = "GBT"
    """
    Denotes a GB Ton as a standard unit.
    """
    GJ = "GJ"
    """
    Denotes a Gigajoule as a standard unit.
    """
    GW = "GW"
    """
    Denotes a Gigawatt as a standard unit.
    """
    GWH = "GWH"
    """
    Denotes a Gigawatt-hour as a standard unit.
    """
    HL = "HL"
    """
    Denotes a Hectolitre as a standard unit.
    """
    INGOT = "INGOT"
    """
    Denotes an Ingot as a standard unit.
    """
    KG = "KG"
    """
    Denotes a Kilogram as a standard unit.
    """
    KL = "KL"
    """
    Denotes a Kilolitre as a standard unit.
    """
    KW = "KW"
    """
    Denotes a Kilowatt as a standard unit.
    """
    KWDC = "KWDC"
    """
    Denotes a Kilowatt Day Capacity as a standard unit.
    """
    KWH = "KWH"
    """
    Denotes a Kilowatt-hour as a standard unit.
    """
    KWHC = "KWHC"
    """
    Denotes a Kilowatt Hours Capacity as a standard unit.
    """
    KWMC = "KWMC"
    """
    Denotes a Kilowatt Month Capacity as a standard unit.
    """
    KWMINC = "KWMINC"
    """
    Denotes a Kilowatt Minute Capacity as a standard unit.
    """
    KWYC = "KWYC"
    """
    Denotes a Kilowatt Year Capacity as a standard unit.
    """
    L = "L"
    """
    Denotes a Litre as a standard unit.
    """
    LB = "LB"
    """
    Denotes a Pound as a standard unit.
    """
    MB = "MB"
    """
    Denotes a Thousand Barrels as a standard unit.
    """
    MBF = "MBF"
    """
    Denotes a Thousand board feet, which are used in contracts on forestry underlyers as a standard unit.
    """
    MJ = "MJ"
    """
    Denotes a Megajoule as a standard unit.
    """
    MMBBL = "MMBBL"
    """
    Denotes a Million Barrels as a standard unit.
    """
    MMBF = "MMBF"
    """
    Denotes a Million board feet, which are used in contracts on forestry underlyers as a standard unit.
    """
    MMBTU = "MMBTU"
    """
    Denotes a Million British Thermal Units as a standard unit.
    """
    MSF = "MSF"
    """
    Denotes a Thousand square feet as a standard unit.
    """
    MT = "MT"
    """
    Denotes a Metric Ton as a standard unit.
    """
    MW = "MW"
    """
    Denotes a Megawatt as a standard unit.
    """
    MWDC = "MWDC"
    """
    Denotes a Megawatt Day Capacity as a standard unit.
    """
    MWH = "MWH"
    """
    Denotes a Megawatt-hour as a standard unit.
    """
    MWHC = "MWHC"
    """
    Denotes a Megawatt Hours Capacity as a standard unit.
    """
    MWMC = "MWMC"
    """
    Denotes a Megawatt Month Capacity as a standard unit.
    """
    MWMINC = "MWMINC"
    """
    Denotes a Megawatt Minute Capacity as a standard unit.
    """
    MWYC = "MWYC"
    """
    Denotes a Megawatt Year Capacity as a standard unit.
    """
    OZT = "OZT"
    """
    Denotes a Troy Ounce as a standard unit.
    """
    TEU = "TEU"
    """
    Denotes a 20 ft. Equivalent Unit container as a standard unit.
    """
    THERM = "THERM"
    """
    Denotes a Thermal Unit as a standard unit.
    """
    USCWT = "USCWT"
    """
    Denotes US Hundredweight unit as a standard unit.
    """
    USGAL = "USGAL"
    """
    Denotes a US Gallon unit as a standard unit.
    """
    UST = "UST"
    """
    Denotes a US Ton as a standard unit.
    """'''

        assertTrue(python.toString.contains(expectedTestType1))
        assertTrue(python.toString.contains(expectedTestType2))
        assertTrue(python.toString.contains(expectedTestType3))
        assertTrue(python.toString.contains(expectedTestType4))
        assertTrue(python.toString.contains(expectedTestType5))
        assertTrue(python.toString.contains(expectedTestType6))
        
    } 


    @Test
    def void testGenerateTypesChoiceCondition() {
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

        val expected ='''class TestType(BaseDataClass):
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
        item = self
        return rosetta_check_one_of(self, 'field1', 'field2', necessity=True)'''
        assertTrue(types.contains(expected))
    }

    @Test
    def void testGenerateIfThenCondition() {
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

        val expected ='''class TestType(BaseDataClass):
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
        item = self
        def _then_fn0():
            return all_elements(rosetta_resolve_attr(self, "field3"), ">", 0)
        
        def _else_fn0():
            return True
        
        return if_cond_fn(rosetta_attr_exists(rosetta_resolve_attr(self, "field1")), _then_fn0, _else_fn0)'''
        assertTrue(types.contains(expected))
    }

    @Test
    def void testGenerateIfThenElseCondition() {
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

        val expected ='''class TestType(BaseDataClass):
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
        item = self
        def _then_fn0():
            return all_elements(rosetta_resolve_attr(self, "field3"), ">", 0)
        
        def _else_fn0():
            return all_elements(rosetta_resolve_attr(self, "field4"), ">", 0)
        
        return if_cond_fn(rosetta_attr_exists(rosetta_resolve_attr(self, "field1")), _then_fn0, _else_fn0)'''
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

        val expectedCondition = '''class DateRange(BaseDataClass):
    """
    A class defining a contiguous series of calendar dates. The date range is defined as all the dates between and including the start and the end date. The start date must fall on or before the end date.
    """
    startDate: datetime.date = Field(..., description="The first date of a date range.")
    """
    The first date of a date range.
    """
    endDate: datetime.date = Field(..., description="The last date of a date range.")
    """
    The last date of a date range.
    """
    
    @rosetta_condition
    def condition_0_DatesOrdered(self):
        """
        The start date must fall on or before the end date (a date range of only one date is allowed).
        """
        item = self
        return all_elements(rosetta_resolve_attr(self, "startDate"), "<=", rosetta_resolve_attr(self, "endDate"))'''
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
                    aValue->a0 exists
                        or (intValue2 exists and intValue1 exists and intValue1 exists)
                        or (intValue2 exists and intValue1 exists and intValue1 is absent)
            '''.generatePython
        
        val expectedA='''class A(BaseDataClass):
    a0: Optional[int] = Field(None, description="")
    a1: Optional[int] = Field(None, description="")
    
    @rosetta_condition
    def condition_0_(self):
        item = self
        return rosetta_check_one_of(self, 'a0', 'a1', necessity=True)'''

        val expectedB='''class B(BaseDataClass):
    intValue1: Optional[int] = Field(None, description="")
    intValue2: Optional[int] = Field(None, description="")
    aValue: com.rosetta.test.model.A.A = Field(..., description="")
    
    @rosetta_condition
    def condition_0_Rule(self):
        item = self
        return all_elements(rosetta_resolve_attr(self, "intValue1"), "<", 100)
    
    @rosetta_condition
    def condition_1_OneOrTwo(self):
        """
        Choice rule to represent an FpML choice construct.
        """
        item = self
        return rosetta_check_one_of(self, 'intValue1', 'intValue2', necessity=False)
    
    @rosetta_condition
    def condition_2_ReqOneOrTwo(self):
        """
        Choice rule to represent an FpML choice construct.
        """
        item = self
        return rosetta_check_one_of(self, 'intValue1', 'intValue2', necessity=True)
    
    @rosetta_condition
    def condition_3_SecondOneOrTwo(self):
        """
        FpML specifies a choice between adjustedDate and [unadjustedDate (required), dateAdjutsments (required), adjustedDate (optional)].
        """
        item = self
        return ((rosetta_attr_exists(rosetta_resolve_attr(rosetta_resolve_attr(self, "aValue"), "a0")) or ((rosetta_attr_exists(rosetta_resolve_attr(self, "intValue2")) and rosetta_attr_exists(rosetta_resolve_attr(self, "intValue1"))) and rosetta_attr_exists(rosetta_resolve_attr(self, "intValue1")))) or ((rosetta_attr_exists(rosetta_resolve_attr(self, "intValue2")) and rosetta_attr_exists(rosetta_resolve_attr(self, "intValue1"))) and (not rosetta_attr_exists(rosetta_resolve_attr(self, "intValue1")))))'''
        
        assertTrue(python.toString.contains(expectedA))
        assertTrue(python.toString.contains(expectedB))
    }
    
    
    def generatePython(CharSequence model) {
        val m = model.parseRosettaWithNoErrors
        val resourceSet = m.eResource.resourceSet
        val version = m.version
        
        val result = newHashMap
        result.putAll(generator.beforeAllGenerate(resourceSet, #{m}, version))
        result.putAll(generator.beforeGenerate(m.eResource, m, version))
        result.putAll(generator.generate(m.eResource, m, version))
        result.putAll(generator.afterGenerate(m.eResource, m, version))
        result.putAll(generator.afterAllGenerate(resourceSet, #{m}, version))
        
        result
    }
}