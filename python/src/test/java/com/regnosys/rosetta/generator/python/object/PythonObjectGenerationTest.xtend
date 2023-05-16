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
    def void shouldGenerateTypes() {
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
		    capacityUnit: Optional[null] = Field(None, description="Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.")
		    """
		    Provides an enumerated value for a capacity unit, generally used in the context of defining quantities for commodities.
		    """
		    currency: Optional[AttributeWithMeta[str] | str] = Field(None, description="Defines the currency to be used as a unit for a price, quantity, or other purpose.")
		    """
		    Defines the currency to be used as a unit for a price, quantity, or other purpose.
		    """
		    financialUnit: Optional[null] = Field(None, description="Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.")
		    """
		    Provides an enumerated value for financial units, generally used in the context of defining quantities for securities.
		    """
		    weatherUnit: Optional[null] = Field(None, description="Provides an enumerated values for a weather unit, generally used in the context of defining quantities for commodities.")
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
    	type PortfolioState: <"State-full representation of a Portfolio that describes all the positions held at a given time, in various states which can be either traded, settled, etc., with lineage information to the previous state">
    		[metadata key]
    	
    		positions Position (0..*) <"The list of positions, each containing a Quantity and a Product.">
    		lineage Lineage (1..1) <"Pointer to the previous PortfolioState and new Event(s) leading to the current (new) state. Previous PortfolioState in the Lineage can be Null in case this is the start of the chain of Events.">
    	
    		condition Initialisation: <"When the PortfolioState is the starting state of the Portfolio, as identified by a Null state in the Lineage, Positions must be empty and the reference to the latest Event is also empty. This is how a Portfolio gets initialised.">
    			if lineage -> portfolioStateReference is absent
    			then positions is absent
    				and lineage -> eventReference is absent
    	'''.generatePython
    	val expectedTestType = 
    	'''
    	class PortfolioState(BaseDataClass):
    	    """
    	    State-full representation of a Portfolio that describes all the positions held at a given time, in various states which can be either traded, settled, etc., with lineage information to the previous state
    	    """
    	    lineage: null = Field(..., description="Pointer to the previous PortfolioState and new Event(s) leading to the current (new) state. Previous PortfolioState in the Lineage can be Null in case this is the start of the chain of Events.")
    	    """
    	    Pointer to the previous PortfolioState and new Event(s) leading to the current (new) state. Previous PortfolioState in the Lineage can be Null in case this is the start of the chain of Events.
    	    """
    	    positions: List[null] = Field([], description="The list of positions, each containing a Quantity and a Product.")
    	    """
    	    The list of positions, each containing a Quantity and a Product.
    	    """
    	    
    	    @rosetta_condition
    	    def condition_0_Initialisation(self):
    	        """
    	        When the PortfolioState is the starting state of the Portfolio, as identified by a Null state in the Lineage, Positions must be empty and the reference to the latest Event is also empty. This is how a Portfolio gets initialised.
    	        """
    	        def _then_fn0():
    	            return (((self.positions) is None) and ((self.lineage.) is None))
    	        
    	        def _else_fn0():
    	            return True
    	        
    	        return if_cond_fn(((self.lineage.) is None), _then_fn0, _else_fn0)
    	'''
    	assertTrue(python.toString.contains(expectedTestType))
    	
    }
    
    @Test
    def void shouldGenerateTypes4() {
    	val python = 
    	'''
    	type AssignedIdentifier: <"A class to specify the identifier value and its associated version.">
    	
    		identifier string (1..1) <"The identifier value.">
    			[metadata scheme]
    		identifierType TradeIdentifierTypeEnum (0..1) <"The enumerated classification of the identifier.">
    		version int (0..1) <"The identifier version, which is specified as an integer and is meant to be incremented each time the transaction terms (whether contract or event) change. This version is made option to support the use case where the identifier is referenced without the version. The constraint that a contract and a lifecycle event need to have an associated version is enforced through data rules.">
    	
    	type Identifier: <"A class to specify a generic identifier, applicable to CDM artefacts such as executions, contracts, lifecycle events and legal documents. An issuer can be associated with the actual identifier value as a way to properly qualify it.">
    		[metadata key]
    	
    		issuerReference Party (0..1) <"The identifier issuer, when specified by reference to a party specified as part of the transaction.">
    			[metadata reference]
    		issuer string (0..1) <"The identifier issuer, when specified explicitly alongside the identifier value (instead of being specified by reference to a party).">
    			[metadata scheme]
    		assignedIdentifier AssignedIdentifier (1..*) <"The identifier value. This level of indirection between the issuer and the identifier and its version provides the ability to associate multiple identifiers to one issuer, consistently with the FpML PartyTradeIdentifier.">
    	
    		condition IssuerChoice: <"The identifier issuer is specified either explicitly or by reference to one of the parties.">
    			required choice issuerReference, issuer
    	
    	type IdentifiedList: <"Attaches an identifier to a collection of objects, when those objects themselves can each be represented by an identifier. One use case is the representation of package transactions, where each component is a separate trade with its own identifier, and those trades are linked together as a package with its own identifier. The data type has been named generically rather than referring to 'packages' as it may have a number of other uses.">
    		[metadata key]
    	
    		listId Identifier (1..1) <"The identifier for the list. In the case of a package transaction, this would be the package identifier. This attribute is mandatory to allow the list itself to be identified.">
    		componentId Identifier (2..*) <"Identifiers for each component of the list. Since the data type is used to link multiple identified objects together, at least 2 components are required in the list. Creating an identified list with only 1 identified component has been deemed unnecessary, because it would just create a redundant identifier.">
    		price Price (0..1) <"The price of the package.">
    	'''.generatePython
    	val expectedType1 = 
    	'''
    	class AssignedIdentifier(BaseDataClass):
    	    """
    	    A class to specify the identifier value and its associated version.
    	    """
    	    identifier: AttributeWithMeta[str] | str = Field(..., description="The identifier value.")
    	    """
    	    The identifier value.
    	    """
    	    identifierType: Optional[null] = Field(None, description="The enumerated classification of the identifier.")
    	    """
    	    The enumerated classification of the identifier.
    	    """
    	    version: Optional[int] = Field(None, description="The identifier version, which is specified as an integer and is meant to be incremented each time the transaction terms (whether contract or event) change. This version is made option to support the use case where the identifier is referenced without the version. The constraint that a contract and a lifecycle event need to have an associated version is enforced through data rules.")
    	    """
    	    The identifier version, which is specified as an integer and is meant to be incremented each time the transaction terms (whether contract or event) change. This version is made option to support the use case where the identifier is referenced without the version. The constraint that a contract and a lifecycle event need to have an associated version is enforced through data rules.
    	    """
    	'''
    	val expectedType2 = 
    	'''
    	class Identifier(BaseDataClass):
    	    """
    	    A class to specify a generic identifier, applicable to CDM artefacts such as executions, contracts, lifecycle events and legal documents. An issuer can be associated with the actual identifier value as a way to properly qualify it.
    	    """
    	    assignedIdentifier: List[AssignedIdentifier] = Field([], description="The identifier value. This level of indirection between the issuer and the identifier and its version provides the ability to associate multiple identifiers to one issuer, consistently with the FpML PartyTradeIdentifier.")
    	    """
    	    The identifier value. This level of indirection between the issuer and the identifier and its version provides the ability to associate multiple identifiers to one issuer, consistently with the FpML PartyTradeIdentifier.
    	    """
    	    @rosetta_condition
    	    def cardinality_assignedIdentifier(self):
    	        return check_cardinality(self.assignedIdentifier, 1, None)
    	    
    	    issuer: Optional[AttributeWithMeta[str] | str] = Field(None, description="The identifier issuer, when specified explicitly alongside the identifier value (instead of being specified by reference to a party).")
    	    """
    	    The identifier issuer, when specified explicitly alongside the identifier value (instead of being specified by reference to a party).
    	    """
    	    issuerReference: Optional[AttributeWithReference | null] = Field(None, description="The identifier issuer, when specified by reference to a party specified as part of the transaction.")
    	    """
    	    The identifier issuer, when specified by reference to a party specified as part of the transaction.
    	    """
    	    
    	    @rosetta_condition
    	    def condition_0_IssuerChoice(self):
    	        """
    	        The identifier issuer is specified either explicitly or by reference to one of the parties.
    	        """
    	        return self.check_one_of_constraint('issuerReference', 'issuer', necessity=True)
    	'''
    	val expectedType3 = 
    	'''
    	class IdentifiedList(BaseDataClass):
    	    """
    	    Attaches an identifier to a collection of objects, when those objects themselves can each be represented by an identifier. One use case is the representation of package transactions, where each component is a separate trade with its own identifier, and those trades are linked together as a package with its own identifier. The data type has been named generically rather than referring to 'packages' as it may have a number of other uses.
    	    """
    	    componentId: List[Identifier] = Field([], description="Identifiers for each component of the list. Since the data type is used to link multiple identified objects together, at least 2 components are required in the list. Creating an identified list with only 1 identified component has been deemed unnecessary, because it would just create a redundant identifier.")
    	    """
    	    Identifiers for each component of the list. Since the data type is used to link multiple identified objects together, at least 2 components are required in the list. Creating an identified list with only 1 identified component has been deemed unnecessary, because it would just create a redundant identifier.
    	    """
    	    @rosetta_condition
    	    def cardinality_componentId(self):
    	        return check_cardinality(self.componentId, 2, None)
    	    
    	    listId: Identifier = Field(..., description="The identifier for the list. In the case of a package transaction, this would be the package identifier. This attribute is mandatory to allow the list itself to be identified.")
    	    """
    	    The identifier for the list. In the case of a package transaction, this would be the package identifier. This attribute is mandatory to allow the list itself to be identified.
    	    """
    	    price: Optional[null] = Field(None, description="The price of the package.")
    	    """
    	    The price of the package.
    	    """
    	'''
    	assertTrue(python.toString.contains(expectedType1))
    	assertTrue(python.toString.contains(expectedType2))
    	assertTrue(python.toString.contains(expectedType3))
    	
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

<<<<<<< HEAD
        
        val expected = 
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
           
           class UnitType(BaseDataClass):
               """
               Defines the unit to be used for price, quantity, or other purposes
               """
               currency: Optional[str] = Field(None, description="Defines the currency to be used as a unit for a price, quantity, or other purpose.")
               """
               Defines the currency to be used as a unit for a price, quantity, or other purpose.
               """
           
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
           
           
           MeasureBase.update_forward_refs()
           UnitType.update_forward_refs()
           Quantity.update_forward_refs()
            '''
        
=======
>>>>>>> 575e05cc4923dc33fdc85e4ad4557929f9a8cbaa
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
    def void shouldGenerateTypesExtends() {
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
    def void testConditionsGeneration() {
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
    
    
    
    
    def generatePython(CharSequence model) {
         val eResource = model.parseRosetta.eResource
         generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
    }
	
}