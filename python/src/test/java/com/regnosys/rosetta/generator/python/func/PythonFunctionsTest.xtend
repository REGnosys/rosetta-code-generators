package com.regnosys.rosetta.generator.python.func

import com.google.inject.Inject
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper

import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith
import com.regnosys.rosetta.generator.python.PythonCodeGenerator
import static org.junit.jupiter.api.Assertions.*

/*
 * Test Principal
 */
@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class PythonFunctionsTest {
    
     @Inject extension ModelHelper
     @Inject PythonCodeGenerator generator;
    

    @Test
    def void testSimpleSet() {
        val python = 
        '''
        func Abs: <"Returns the absolute value of a number. If the argument is not negative, the argument is returned. If the argument is negative, the negation of the argument is returned.">
            inputs:
                arg number (1..1)
            output:
                result number (1..1)
            set result:
                if arg < 0 then -1 * arg else arg
        '''.generatePython
        
        val expected = 
        '''
        @replaceable
        def Abs(arg: Decimal) -> Decimal:
            """
            Returns the absolute value of a number. If the argument is not negative, the argument is returned. If the argument is negative, the negation of the argument is returned.
            
            Parameters 
            ----------
            arg : number
            
            Returns
            -------
            result : number
            
            """
            self = inspect.currentframe()
            
            
            def _then_fn0():
                return (-1 * rosetta_resolve_attr(self, "arg"))
            
            def _else_fn0():
                return rosetta_resolve_attr(self, "arg")
            
            result =  if_cond_fn(all_elements(rosetta_resolve_attr(self, "arg"), "<", 0), _then_fn0, _else_fn0)
            
            
            return result
        '''
        assertTrue(python.toString.contains(expected))
    
        
    }
    
    
    @Test
    def void testSimpleAdd() {
        val python = 
        '''
        func AppendToVector: <"Append a single value to a vector (list of numbers).">
            inputs:
                vector number (0..*) <"Input vector.">
                value number (1..1) <"Value to add to the vector.">
            output:
                resultVector number (0..*) <"Resulting vector.">
        
            add resultVector: vector
            add resultVector: value
        '''.generatePython
        
        val expected =
        '''
        @replaceable
        def AppendToVector(vector: list[Decimal] | None, value: Decimal) -> Decimal:
            """
            Append a single value to a vector (list of numbers).
            
            Parameters 
            ----------
            vector : number
            Input vector.
            
            value : number
            Value to add to the vector.
            
            Returns
            -------
            resultVector : number
            
            """
            self = inspect.currentframe()
            
            
            resultVector = rosetta_resolve_attr(self, "vector")
            resultVector.add_rosetta_attr(self, rosetta_resolve_attr(self, "value"))
            
            
            return resultVector
        
        sys.modules[__name__].__class__ = create_module_attr_guardian(sys.modules[__name__].__class__)
        '''
        assertTrue(python.toString.contains(expected))
          
    }
    
    //Test set with a basemodel output
    @Test
    def void testSetWithBasemodel() {
        val python =  
        '''
        func Create_UnitType: <"Create UnitType with given currency or financial unit.">
            inputs:
                currency string (0..1)
                    [metadata scheme]
                financialUnit FinancialUnitEnum (0..1)
            output:
                unitType UnitType (1..1)
        
            condition CurrencyOrFinancialUnitExists:
                currency exists or financialUnit exists
        
            set unitType -> currency: currency
            set unitType -> financialUnit: financialUnit
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
        enum CapacityUnitEnum: <"Provides enumerated values for capacity units, generally used in the context of defining quantities for commodities.">
            ALW <"Denotes Allowances as standard unit.">
            BBL <"Denotes a Barrel as a standard unit.">
            BCF <"Denotes Billion Cubic Feet as a standard unit.">
            BDFT <"Denotes Board Feet as a standard unit.">
            CBM <"Denotes Cubic Meters as a standard unit.">
            CER <"Denotes Certified Emissions Reduction as a standard unit.">
            CRT <"Denotes Climate Reserve Tonnes as a standard unit.">
            DAG <"Denotes 10 grams as a standard unit used in precious metals contracts (e.g MCX).">
            DAY <"Denotes a single day as a standard unit used in time charter trades.">
            DMTU <"Denotes Dry Metric Ton (Tonne) Units - Consists of a metric ton of mass excluding moisture.">
            ENVCRD <"Denotes Environmental Credit as a standard unit.">
            ENVOFST <"Denotes Environmental Offset as a standard unit.">
            FEU <"Denotes a 40 ft. Equivalent Unit container as a standard unit.">
            G <"Denotes a Gram as a standard unit.">
            GBBSH <"Denotes a GB Bushel as a standard unit.">
            GBBTU <"Denotes a GB British Thermal Unit as a standard unit.">
            GBCWT <"Denotes a GB Hundredweight unit as standard unit.">
            GBGAL <"Denotes a GB Gallon unit as standard unit.">
            GBMBTU <"Denotes a Thousand GB British Thermal Units as a standard unit.">
            GBMMBTU <"Denotes a Million GB British Thermal Units as a standard unit.">
            GBT <"Denotes a GB Ton as a standard unit.">
            GBTHM <"Denotes a GB Thermal Unit as a standard unit.">
            GJ <"Denotes a Gigajoule as a standard unit.">
            GW <"Denotes a Gigawatt as a standard unit.">
            GWH <"Denotes a Gigawatt-hour as a standard unit.">
            HL <"Denotes a Hectolitre as a standard unit.">
            HOGB <"Denotes a 100-troy ounces Gold Bar as a standard unit.">
            ISOBTU <"Denotes an ISO British Thermal Unit as a standard unit.">
            ISOMBTU <"Denotes a Thousand ISO British Thermal Unit as a standard unit.">
            ISOMMBTU <"Denotes a Million ISO British Thermal Unit as a standard unit.">
            ISOTHM <"Denotes an ISO Thermal Unit as a standard unit.">
            KG <"Denotes a Kilogram as a standard unit.">
            KL <"Denotes a Kilolitre as a standard unit.">
            KW <"Denotes a Kilowatt as a standard unit.">
            KWD <"Denotes a Kilowatt-day as a standard unit.">
            KWH <"Denotes a Kilowatt-hour as a standard unit.">
            KWM <"Denotes a Kilowatt-month as a standard unit.">
            KWMIN <"Denotes a Kilowatt-minute as a standard unit.">
            KWY <"Denotes a Kilowatt-year as a standard unit.">
            L <"Denotes a Litre as a standard unit.">
            LB <"Denotes a Pound as a standard unit.">
            MB <"Denotes a Thousand Barrels as a standard unit.">
            MBF <"Denotes a Thousand board feet, which are used in contracts on forestry underlyers as a standard unit.">
            MJ <"Denotes a Megajoule as a standard unit.">
            MMBF <"Denotes a Million board feet, which are used in contracts on forestry underlyers as a standard unit.">
            MMBBL <"Denotes a Million Barrels as a standard unit.">
            MSF <"Denotes a Thousand square feet as a standard unit.">
            MT <"Denotes a Metric Ton as a standard unit.">
            MW <"Denotes a Megawatt as a standard unit.">
            MWD <"Denotes a Megawatt-day as a standard unit.">
            MWH <"Denotes a Megawatt-hour as a standard unit.">
            MWM <"Denotes a Megawatt-month as a standard unit.">
            MWMIN <"Denotes a Megawatt-minute as a standard unit.">
            MWY <"Denotes a Megawatt-year as a standard unit.">
            OZT <"Denotes a Troy Ounce as a standard unit.">
            SGB <"Denotes a Standard Gold Bar as a standard unit.">
            TEU <"Denotes a 20 ft. Equivalent Unit container as a standard unit.">
            USBSH <"Denotes a US Bushel as a standard unit.">
            USBTU <"Denotes a US British Thermal Unit as a standard unit.">
            USCWT <"Denotes US Hundredweight unit as a standard unit.">
            USGAL <"Denotes a US Gallon unit as a standard unit.">
            USMBTU <"Denotes a Thousand US British Thermal Units as a standard unit.">
            USMMBTU <"Denotes a Million US British Thermal Units as a standard unit.">
            UST <"Denotes a US Ton as a standard unit.">
            USTHM <"Denotes a US Thermal Unit as a standard unit.">
        enum WeatherUnitEnum: <"Provides enumerated values for weather units, generally used in the context of defining quantities for commodities.">
            CDD <"Denotes Cooling Degree Days as a standard unit.">
            CPD <"Denotes Critical Precipitation Day as a standard unit.">
            HDD <"Heating Degree Day as a standard unit.">
        '''.generatePython
        
        val expected =
        '''
        @replaceable
        def Create_UnitType(currency: str | None, financialUnit: FinancialUnitEnum | None) -> UnitType:
            """
            Create UnitType with given currency or financial unit.
            
            Parameters 
            ----------
            currency : string
            
            financialUnit : FinancialUnitEnum
            
            Returns
            -------
            unitType : UnitType
            
            """
            _pre_registry = {}
            self = inspect.currentframe()
            
            # conditions
            
            @rosetta_local_condition(_pre_registry)
            def condition_0_CurrencyOrFinancialUnitExists(self):
                return (rosetta_attr_exists(rosetta_resolve_attr(self, "currency")) or rosetta_attr_exists(rosetta_resolve_attr(self, "financialUnit")))
            # Execute all registered conditions
            execute_local_conditions(_pre_registry, 'Pre-condition')
            
            unitType = _get_rosetta_object('UnitType', 'currency', rosetta_resolve_attr(self, "currency"))
            unitType = set_rosetta_attr(rosetta_resolve_attr(self, 'unitType'), 'financialUnit', rosetta_resolve_attr(self, "financialUnit"))
            
            
            return unitType
        
        sys.modules[__name__].__class__ = create_module_attr_guardian(sys.modules[__name__].__class__)
        '''
        assertTrue(python.toString.contains(expected))
    }
    
    //Test add and set in the same function with basemodel output
    @Test
    def void testAddAndSet() {
        val python = 
        '''
        func ResolvePerformanceReset: <"Defines how to resolve the reset value for a performance payout.">
            inputs:
                observation Observation (1..1) <"Represents the observation that will be used to compute the reset value.">
                date date (1..1) <"Specifies the date of the reset.">
            output:
                reset Reset (1..1)
            set reset -> resetValue: <"Assigns the observed value to the reset value.">
                observation -> observedValue
            set reset -> resetDate:
                date
            add reset -> observations: <"Assigns the observation required to compute the rest value as audit.">
                observation
        type Reset: <"Defines the reset value or fixing value produced in cashflow calculations, during the life-cycle of a financial instrument. The reset process defined in Create_Reset function joins product definition details with observations to compute the reset value.">
            [metadata key]
            resetValue Price (1..1) <"Specifies the reset or fixing value. The fixing value could be a cash price, interest rate, or other value.">
            resetDate date (1..1) <"Specifies the date on which the reset occurred.">
            observations Observation (1..*)
        type Price : 
            price int(1..1)
        
        type Observation: <"Defines a single, numerical value that was observed in the marketplace. Observations of market data are made independently to business events or trade life-cycle events, so data instances of Observation can be created independently of any other model type, hence it is annotated as a root type. Observations will be broadly reused in many situations, so references to Observation are supported via the 'key' annotation.">
            [rootType]
            [metadata key]
            observedValue Price (1..1) <"Specifies the observed value as a number.">
        '''.generatePython
        
        val expected = 
        '''
        @replaceable
        def ResolvePerformanceReset(observation: Observation, date: datetime.date) -> Reset:
            """
            Defines how to resolve the reset value for a performance payout.
            
            Parameters 
            ----------
            observation : Observation
            Represents the observation that will be used to compute the reset value.
            
            date : date
            Specifies the date of the reset.
            
            Returns
            -------
            reset : Reset
            
            """
            self = inspect.currentframe()
            
            
            reset = _get_rosetta_object('Reset', 'resetValue', rosetta_resolve_attr(rosetta_resolve_attr(self, "observation"), "observedValue"))
            reset = set_rosetta_attr(rosetta_resolve_attr(self, 'reset'), 'resetDate', rosetta_resolve_attr(self, "date"))
            reset.add_rosetta_attr(rosetta_resolve_attr(rosetta_resolve_attr(self, reset), 'observations'), rosetta_resolve_attr(self, "observation"))
            
            
            return reset
        
        sys.modules[__name__].__class__ = create_module_attr_guardian(sys.modules[__name__].__class__)
        '''
        assertTrue(python.toString.contains(expected))
        
    }
    
    @Test
    def void testFilterOperation() {
        val python =
        '''
        func FilterQuantity: <"Filter list of quantities based on unit type.">
                    inputs:
                        quantities Quantity (0..*) <"List of quantities to filter.">
                        unit UnitType (1..1) <"Currency unit type.">
                    output:
                        filteredQuantities Quantity (0..*)
                
                    add filteredQuantities:
                        quantities
                            filter quantities -> unit = unit
                type Quantity: <"Specifies a quantity as a single value to be associated to a financial product, for example a transfer amount resulting from a trade. This data type extends QuantitySchedule and requires that only the single amount value exists.">
                    value number (0..1) <"Specifies the value of the measure as a number. Optional because in a measure vector or schedule, this single value may be omitted.">
                    unit UnitType (0..1) <"Qualifies the unit by which the amount is measured. Optional because a measure may be unit-less (e.g. when representing a ratio between amounts in the same unit).">
                  type UnitType: <"Defines the unit to be used for price, quantity, or other purposes">
                      value int (1..1)
        '''.generatePython
        
        val expected =
        '''
        @replaceable
        def FilterQuantity(quantities: list[Quantity] | None, unit: UnitType) -> Quantity:
            """
            Filter list of quantities based on unit type.
            
            Parameters 
            ----------
            quantities : Quantity
            List of quantities to filter.
            
            unit : UnitType
            Currency unit type.
            
            Returns
            -------
            filteredQuantities : Quantity
            
            """
            self = inspect.currentframe()
            
            
            filteredQuantities = rosetta_filter(rosetta_resolve_attr(self, "quantities"), lambda item: all_elements(rosetta_resolve_attr(rosetta_resolve_attr(self, "quantities"), "unit"), "=", rosetta_resolve_attr(self, "unit")))
            
            
            return filteredQuantities
        
        sys.modules[__name__].__class__ = create_module_attr_guardian(sys.modules[__name__].__class__)
        '''
        assertTrue(python.toString.contains(expected))
        
    }
    
    //Test generation with an enum
    @Test
    def void testWithEnumAttr() {
        
        val python =
        '''
        enum ArithmeticOperationEnum: <"An arithmetic operator that can be passed to a function">
            Add <"Addition">
            Subtract <"Subtraction">
            Multiply <"Multiplication">
            Divide <"Division">
            Max <"Max of 2 values">
            Min <"Min of 2 values">
        
        func ArithmeticOperation:
            inputs:
                n1 number (1..1)
                op ArithmeticOperationEnum (1..1)
                n2 number (1..1)
            output:
                result number (1..1)
        
            set result:
                if op = ArithmeticOperationEnum -> Add then
                    n1 + n2
                else if op = ArithmeticOperationEnum -> Subtract then
                    n1 - n2
                else if op = ArithmeticOperationEnum -> Multiply then
                    n1 * n2
                else if op = ArithmeticOperationEnum -> Divide then
                    n1 / n2
                else if op = ArithmeticOperationEnum -> Max then
                    Max( n1, n2 )
                else if op = ArithmeticOperationEnum -> Min then
                    Min( n1, n2 )
        '''.generatePython

        val expected =
        '''
        @replaceable
        def ArithmeticOperation(n1: Decimal, op: ArithmeticOperationEnum, n2: Decimal) -> Decimal:
            """
            
            Parameters 
            ----------
            n1 : number
            
            op : ArithmeticOperationEnum
            
            n2 : number
            
            Returns
            -------
            result : number
            
            """
            self = inspect.currentframe()
            
            
            def _then_fn5():
                return Min(rosetta_resolve_attr(self, "n1"), rosetta_resolve_attr(self, "n2"))
            
            def _else_fn5():
                return True
            
            def _then_fn4():
                return Max(rosetta_resolve_attr(self, "n1"), rosetta_resolve_attr(self, "n2"))
            
            def _else_fn4():
                return if_cond_fn(all_elements(rosetta_resolve_attr(self, "op"), "=", rosetta_resolve_attr(ArithmeticOperationEnum, "MIN")), _then_fn5, _else_fn5)
            
            def _then_fn3():
                return (rosetta_resolve_attr(self, "n1") / rosetta_resolve_attr(self, "n2"))
            
            def _else_fn3():
                return if_cond_fn(all_elements(rosetta_resolve_attr(self, "op"), "=", rosetta_resolve_attr(ArithmeticOperationEnum, "MAX")), _then_fn4, _else_fn4)
            
            def _then_fn2():
                return (rosetta_resolve_attr(self, "n1") * rosetta_resolve_attr(self, "n2"))
            
            def _else_fn2():
                return if_cond_fn(all_elements(rosetta_resolve_attr(self, "op"), "=", rosetta_resolve_attr(ArithmeticOperationEnum, "DIVIDE")), _then_fn3, _else_fn3)
            
            def _then_fn1():
                return (rosetta_resolve_attr(self, "n1") - rosetta_resolve_attr(self, "n2"))
            
            def _else_fn1():
                return if_cond_fn(all_elements(rosetta_resolve_attr(self, "op"), "=", rosetta_resolve_attr(ArithmeticOperationEnum, "MULTIPLY")), _then_fn2, _else_fn2)
            
            def _then_fn0():
                return (rosetta_resolve_attr(self, "n1") + rosetta_resolve_attr(self, "n2"))
            
            def _else_fn0():
                return if_cond_fn(all_elements(rosetta_resolve_attr(self, "op"), "=", rosetta_resolve_attr(ArithmeticOperationEnum, "SUBTRACT")), _then_fn1, _else_fn1)
            
            result =  if_cond_fn(all_elements(rosetta_resolve_attr(self, "op"), "=", rosetta_resolve_attr(ArithmeticOperationEnum, "ADD")), _then_fn0, _else_fn0)
            
            
            return result
        
        sys.modules[__name__].__class__ = create_module_attr_guardian(sys.modules[__name__].__class__)
        '''
        assertTrue(python.toString.contains(expected))
    }
     
    @Test
    def void testFilterOperation2() {
        val python =
        '''
        func FilterQuantityByCurrencyExists: <"Filter list of quantities based on unit type.">
            inputs:
                quantities QuantitySchedule (0..*) <"List of quantities to filter.">
            output:
                filteredQuantities QuantitySchedule (0..*)
        
            add filteredQuantities:
                quantities
                    filter item -> unit -> currency exists
        type QuantitySchedule: <"Specifies a quantity as a single value to be associated to a financial product, for example a transfer amount resulting from a trade. This data type extends QuantitySchedule and requires that only the single amount value exists.">
                value number (0..1) <"Specifies the value of the measure as a number. Optional because in a measure vector or schedule, this single value may be omitted.">
                unit UnitType (0..1) <"Qualifies the unit by which the amount is measured. Optional because a measure may be unit-less (e.g. when representing a ratio between amounts in the same unit).">
        type UnitType: <"Defines the unit to be used for price, quantity, or other purposes">
                  currency string(0..1)
        '''.generatePython
        
        
        val expected =
        '''
        @replaceable
        def FilterQuantityByCurrencyExists(quantities: list[QuantitySchedule] | None) -> QuantitySchedule:
            """
            Filter list of quantities based on unit type.
            
            Parameters 
            ----------
            quantities : QuantitySchedule
            List of quantities to filter.
            
            Returns
            -------
            filteredQuantities : QuantitySchedule
            
            """
            self = inspect.currentframe()
            
            
            filteredQuantities = rosetta_filter(rosetta_resolve_attr(self, "quantities"), lambda item: rosetta_attr_exists(rosetta_resolve_attr(rosetta_resolve_attr(item, "unit"), "currency")))
            
            
            return filteredQuantities
        
        sys.modules[__name__].__class__ = create_module_attr_guardian(sys.modules[__name__].__class__)
        '''
        assertTrue(python.toString.contains(expected))
        
    }
    
    
    @Test 
    def void testAlias1() {
        
        val python =
        '''
        func testAlias:
            inputs:
                inp1 number(1..1)
                inp2 number(1..1)
            output:
                result number(1..1)
            alias Alias:
                if inp1 < 0 then inp1
                
            set result:
                Alias
        '''.generatePython
 
        val expected =
        '''
        @replaceable
        def testAlias(inp1: Decimal, inp2: Decimal) -> Decimal:
            """
            
            Parameters 
            ----------
            inp1 : number
            
            inp2 : number
            
            Returns
            -------
            result : number
            
            """
            self = inspect.currentframe()
            
            
            def _then_fn0():
                return rosetta_resolve_attr(self, "inp1")
            
            def _else_fn0():
                return True
            
            Alias = if_cond_fn(all_elements(rosetta_resolve_attr(self, "inp1"), "<", 0), _then_fn0, _else_fn0)
            result =  rosetta_resolve_attr(self, "Alias")
            
            
            return result
        
        sys.modules[__name__].__class__ = create_module_attr_guardian(sys.modules[__name__].__class__)
        '''
        assertTrue(python.toString.contains(expected))
        
    }
    
    //Test alias with basemodels inputs
    @Test
    def void testAlias2() {

        val python =
        '''
        type A:
            valueA number(1..1)
            
        type B:
            valueB number(1..1)
            
        type C:
            valueC number(1..1)
            
        func testAlias:
            inputs:
                a A (1..1)
                b B (1..1)
            output:
                c C (1..1)
            alias Alias1:
                a->valueA
            alias Alias2:
                b->valueB
            set c->valueC:
                Alias1*Alias2
        '''.generatePython
        
        val expected = 
        '''
        @replaceable
        def testAlias(a: A, b: B) -> C:
            """
            
            Parameters 
            ----------
            a : A
            
            b : B
            
            Returns
            -------
            c : C
            
            """
            self = inspect.currentframe()
            
            
            Alias1 = rosetta_resolve_attr(rosetta_resolve_attr(self, "a"), "valueA")
            Alias2 = rosetta_resolve_attr(rosetta_resolve_attr(self, "b"), "valueB")
            c = _get_rosetta_object('C', 'valueC', (rosetta_resolve_attr(self, "Alias1") * rosetta_resolve_attr(self, "Alias2")))
            
            
            return c
        
        sys.modules[__name__].__class__ = create_module_attr_guardian(sys.modules[__name__].__class__)
        '''
        
        assertTrue(python.toString.contains(expected))
        
    }
    
    @Test
    def void testComplexSetConstructors() {
        
        val python =
        '''
        type InterestRatePayout: <" A class to specify all of the terms necessary to define and calculate a cash flow based on a fixed, a floating or an inflation index rate. The interest rate payout can be applied to interest rate swaps and FRA (which both have two associated interest rate payouts), credit default swaps (to represent the fee leg when subject to periodic payments) and equity swaps (to represent the funding leg). The associated globalKey denotes the ability to associate a hash value to the InterestRatePayout instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage.">
            [metadata key]
            rateSpecification RateSpecification (0..1) <"The specification of the rate value(s) applicable to the contract using either a floating rate calculation, a single fixed rate, a fixed rate schedule, or an inflation rate calculation.">
        
        type RateSpecification: <" A class to specify the fixed interest rate, floating interest rate or inflation rate.">
            floatingRate FloatingRateSpecification (0..1) <"The floating interest rate specification, which includes the definition of the floating rate index. the tenor, the initial value, and, when applicable, the spread, the rounding convention, the averaging method and the negative interest rate treatment.">
        
        type FloatingRateSpecification: <"A class defining a floating interest rate through the specification of the floating rate index, the tenor, the multiplier schedule, the spread, the qualification of whether a specific rate treatment and/or a cap or floor apply.">
            [metadata key]
        
            rateOption FloatingRateOption (0..1)
        
        type FloatingRateOption: <"Specification of a floating rate option as a floating rate index and tenor.">
            value int(1..1)
        
        type ObservationIdentifier: <"Defines the parameters needed to uniquely identify a piece of data among the population of all available market data.">
            observable Observable (1..1) <"Represents the asset or rate to which the observation relates.">
            observationDate date (1..1) <"Specifies the date value to use when resolving the market data.">
        
        type Observable: <"Specifies the object to be observed for a price, it could be an asset or a reference.">
            [metadata key]
        
            rateOption FloatingRateOption (0..1) <"Specifies a floating rate index and tenor.">
            
        func ResolveInterestRateObservationIdentifiers: <"Defines which attributes on the InterestRatePayout should be used to locate and resolve the underlier's price, for example for the reset process.">
            inputs:
                payout InterestRatePayout (1..1)
                date date (1..1)
            output:
                identifiers ObservationIdentifier (1..1)
        
            set identifiers -> observable -> rateOption:
                payout -> rateSpecification -> floatingRate -> rateOption
            set identifiers -> observationDate:
                date
        '''.generatePython
        

        val expected = 
        '''
        @replaceable
        def ResolveInterestRateObservationIdentifiers(payout: InterestRatePayout, date: datetime.date) -> ObservationIdentifier:
            """
            Defines which attributes on the InterestRatePayout should be used to locate and resolve the underlier's price, for example for the reset process.
            
            Parameters 
            ----------
            payout : InterestRatePayout
            
            date : date
            
            Returns
            -------
            identifiers : ObservationIdentifier
            
            """
            self = inspect.currentframe()
            
            
            identifiers = _get_rosetta_object('ObservationIdentifier', 'observable', _get_rosetta_object('Observable', 'rateOption', rosetta_resolve_attr(rosetta_resolve_attr(rosetta_resolve_attr(rosetta_resolve_attr(self, "payout"), "rateSpecification"), "floatingRate"), "rateOption")))
            identifiers = set_rosetta_attr(rosetta_resolve_attr(self, 'identifiers'), 'observationDate', rosetta_resolve_attr(self, "date"))
            
            
            return identifiers
        
        sys.modules[__name__].__class__ = create_module_attr_guardian(sys.modules[__name__].__class__)
        '''
        assertTrue(python.toString.contains(expected))
        
    }
    
    @Test
    def void testCondition() {
        val python =
        '''
        func RoundToNearest:
            inputs:
                value number (1..1)
                nearest number (1..1)
                roundingMode RoundingModeEnum (1..1)
            output:
                roundedValue number (1..1)
            condition PositiveNearest:
                nearest > 0
        enum RoundingModeEnum:
            Down
            Up
        '''.generatePython

        val expected = 
        '''
        @replaceable
        def RoundToNearest(value: Decimal, nearest: Decimal, roundingMode: RoundingModeEnum) -> Decimal:
            """
            
            Parameters 
            ----------
            value : number
            
            nearest : number
            
            roundingMode : RoundingModeEnum
            
            Returns
            -------
            roundedValue : number
            
            """
            _pre_registry = {}
            self = inspect.currentframe()
            
            # conditions
            
            @rosetta_local_condition(_pre_registry)
            def condition_0_PositiveNearest(self):
                return all_elements(rosetta_resolve_attr(self, "nearest"), ">", 0)
            # Execute all registered conditions
            execute_local_conditions(_pre_registry, 'Pre-condition')
            
            roundedValue = rosetta_resolve_attr(self, "roundedValue")
            
            
            return roundedValue
        
        sys.modules[__name__].__class__ = create_module_attr_guardian(sys.modules[__name__].__class__)
        '''
        assertTrue(python.toString.contains(expected))
    }
    
    @Test
    def void testMultipleConditions() {
        val python =
        '''
        func RoundToNearest:
            inputs:
                value number (1..1)
                nearest number (1..1)
                roundingMode RoundingModeEnum (1..1)
            output:
                roundedValue number (1..1)
            condition PositiveNearest:
                nearest > 0
            condition valueNegative:
                value < 0
        enum RoundingModeEnum:
            Down
            Up
        '''.generatePython
        
        val expected =
        '''
        @replaceable
        def RoundToNearest(value: Decimal, nearest: Decimal, roundingMode: RoundingModeEnum) -> Decimal:
            """
            
            Parameters 
            ----------
            value : number
            
            nearest : number
            
            roundingMode : RoundingModeEnum
            
            Returns
            -------
            roundedValue : number
            
            """
            _pre_registry = {}
            self = inspect.currentframe()
            
            # conditions
            
            @rosetta_local_condition(_pre_registry)
            def condition_0_PositiveNearest(self):
                return all_elements(rosetta_resolve_attr(self, "nearest"), ">", 0)
            
            @rosetta_local_condition(_pre_registry)
            def condition_1_valueNegative(self):
                return all_elements(rosetta_resolve_attr(self, "value"), "<", 0)
            # Execute all registered conditions
            execute_local_conditions(_pre_registry, 'Pre-condition')
            
            roundedValue = rosetta_resolve_attr(self, "roundedValue")
            
            
            return roundedValue
        
        sys.modules[__name__].__class__ = create_module_attr_guardian(sys.modules[__name__].__class__)
        '''
        assertTrue(python.toString.contains(expected))
    }
    
    @Test
    def void testPostCondition() {
        val python =
        '''
        func NewFloatingPayout: <"Function specification to create the interest rate (floating) payout part of an Equity Swap according to the 2018 ISDA CDM Equity Confirmation template.">
            inputs: masterConfirmation EquitySwapMasterConfirmation2018 (0..1)
            output: interestRatePayout InterestRatePayout (1..1)
        
            post-condition InterestRatePayoutTerms: <"Interest rate payout must inherit terms from the Master Confirmation Agreement when it exists.">
                if masterConfirmation exists then 
                //interestRatePayout -> calculationPeriodDates = masterConfirmation -> equityCalculationPeriod and 
                interestRatePayout -> paymentDates = masterConfirmation -> equityCashSettlementDates
        type EquitySwapMasterConfirmation2018:
            equityCashSettlementDates PaymentDates (1..1) 
        type PaymentDates:
            date date(0..1)
        type InterestRatePayout:
            paymentDates PaymentDates(0..1)
        '''.generatePython

        val expected =
        '''
        @replaceable
        def NewFloatingPayout(masterConfirmation: EquitySwapMasterConfirmation2018 | None) -> InterestRatePayout:
            """
            Function specification to create the interest rate (floating) payout part of an Equity Swap according to the 2018 ISDA CDM Equity Confirmation template.
            
            Parameters 
            ----------
            masterConfirmation : EquitySwapMasterConfirmation2018
            
            Returns
            -------
            interestRatePayout : InterestRatePayout
            
            """
            _post_registry = {}
            self = inspect.currentframe()
            
            
            interestRatePayout = rosetta_resolve_attr(self, "interestRatePayout")
            
            # post-conditions
            
            @rosetta_local_condition(_post_registry)
            def condition_0_InterestRatePayoutTerms(self):
                """
                Interest rate payout must inherit terms from the Master Confirmation Agreement when it exists.
                """
                def _then_fn0():
                    return all_elements(rosetta_resolve_attr(rosetta_resolve_attr(self, "interestRatePayout"), "paymentDates"), "=", rosetta_resolve_attr(rosetta_resolve_attr(self, "masterConfirmation"), "equityCashSettlementDates"))
                
                def _else_fn0():
                    return True
                
                return if_cond_fn(rosetta_attr_exists(rosetta_resolve_attr(self, "masterConfirmation")), _then_fn0, _else_fn0)
            # Execute all registered post-conditions
            execute_local_conditions(_post_registry, 'Post-condition')
            
            return interestRatePayout
        
        sys.modules[__name__].__class__ = create_module_attr_guardian(sys.modules[__name__].__class__)
        '''
        assertTrue(python.toString.contains(expected))
        
    }
    
    @Test
    def void functionCallTest() {
        val python = 
        '''
        type InterestRatePayout: <" A class to specify all of the terms necessary to define and calculate a cash flow based on a fixed, a floating or an inflation index rate. The interest rate payout can be applied to interest rate swaps and FRA (which both have two associated interest rate payouts), credit default swaps (to represent the fee leg when subject to periodic payments) and equity swaps (to represent the funding leg). The associated globalKey denotes the ability to associate a hash value to the InterestRatePayout instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage.">
                            [metadata key]
                            rateSpecification RateSpecification (0..1) <"The specification of the rate value(s) applicable to the contract using either a floating rate calculation, a single fixed rate, a fixed rate schedule, or an inflation rate calculation.">
                        
                        type RateSpecification: <" A class to specify the fixed interest rate, floating interest rate or inflation rate.">
                            floatingRate FloatingRateSpecification (0..1) <"The floating interest rate specification, which includes the definition of the floating rate index. the tenor, the initial value, and, when applicable, the spread, the rounding convention, the averaging method and the negative interest rate treatment.">
                        
                        type FloatingRateSpecification: <"A class defining a floating interest rate through the specification of the floating rate index, the tenor, the multiplier schedule, the spread, the qualification of whether a specific rate treatment and/or a cap or floor apply.">
                            [metadata key]
                        
                            rateOption FloatingRateOption (0..1)
                        
                        type FloatingRateOption: <"Specification of a floating rate option as a floating rate index and tenor.">
                            value int(1..1)
                func FixedAmount:
                  [calculation]
                  inputs:
                    interestRatePayout InterestRatePayout (1..1)
                    date date (1..1)
                  output:
                    fixedAmount number (1..1)
        
                  alias dayCountFraction: DayCountFraction(interestRatePayout, date)
                func DayCountFraction:
                     inputs:
                         interestRatePayout InterestRatePayout (1..1)
                         date date(1..1)
                     output:
                         a number(1..1)
        '''.generatePython
        
        val expected = 
        '''@replaceable
def DayCountFraction(interestRatePayout: InterestRatePayout, date: datetime.date) -> Decimal:
    """
    
    Parameters 
    ----------
    interestRatePayout : InterestRatePayout
    
    date : date
    
    Returns
    -------
    a : number
    
    """
    self = inspect.currentframe()
    
    
    a = rosetta_resolve_attr(self, "a")
    
    
    return a'''

        assertTrue(python.toString.contains(expected))
    }
    

    def generatePython(CharSequence model) {
        val m = model.parseRosetta
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
