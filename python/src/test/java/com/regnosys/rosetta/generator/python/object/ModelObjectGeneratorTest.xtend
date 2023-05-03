package com.regnosys.rosetta.generator.python.object

import com.google.inject.Inject
import com.regnosys.rosetta.generator.python.PythonCodeGenerator
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Disabled
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)

class ModelObjectGeneratorTest {

    @Inject extension ModelHelper
    @Inject PythonCodeGenerator generator;
	
	@Test
	def void generateStringBasicType() {
		val python = '''
			type Tester:
				one string (0..1)
				list string (0..*)
		'''.generatePython

		
		val expected=
		'''
		class Tester(BaseDataClass):
		    list: List[str] = Field([], description="")
		    one: Optional[str] = Field(None, description="")
		
		
		Tester.update_forward_refs()
		'''
		
		assertTrue(python.toString.contains(expected))
	}

	@Test
	def void generateIntBasicType() {
		val python = '''
			type Tester:
				one int (0..1)
				list int (0..*)
		'''.generatePython

		val expected=
		'''
		class Tester(BaseDataClass):
		    list: List[int] = Field([], description="")
		    one: Optional[int] = Field(None, description="")
		
		
		Tester.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.py").toString.contains(expected))

	}

	@Test
	def void generateNumberBasicType() {
		val python = '''
			type Tester:
				one number (0..1)
				list number (0..*)
		'''.generatePython

		
		
		val expected=
		'''
		class Tester(BaseDataClass):
		    list: List[Decimal] = Field([], description="")
		    one: Optional[Decimal] = Field(None, description="")
		
		
		Tester.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.py").toString.contains(expected))

	}

	@Test
	def void generateBooleanBasicType() {
		val python = '''
			type Tester:
				one boolean (0..1)
				list boolean (0..*)
		'''.generatePython

		
		
		val expected=
		'''
		class Tester(BaseDataClass):
		    list: List[bool] = Field([], description="")
		    one: Optional[bool] = Field(None, description="")
		
		
		Tester.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.py").toString.contains(expected))
	}

	@Test
	def void generateDateBasicType() {
		val python = '''
			type Tester:
				one date (0..1)
				list date (0..*)
		'''.generatePython

		
		
		val expected=
		'''
		class Tester(BaseDataClass):
		    list: List[date] = Field([], description="")
		    one: Optional[date] = Field(None, description="")
		
		
		Tester.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.py").toString.contains(expected))
	}

	@Test
	def void generateDateTimeBasicType() {
		val python = '''
			type Tester:
				one date (0..1)
				list date (0..*)
				zoned zonedDateTime (0..1)
		'''.generatePython

		val expected=
		'''
		class Tester(BaseDataClass):
		    list: List[date] = Field([], description="")
		    one: Optional[date] = Field(None, description="")
		    zoned: Optional[datetime] = Field(None, description="")
		
		
		Tester.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.py").toString.contains(expected))
	}

	@Test
	def void generateTimeBasicType() {
		val python = '''
			type Tester:
				one time (0..1)
				list time (0..*)
		'''.generatePython
	
		val expected=
		'''
		class Tester(BaseDataClass):
		    list: List[time] = Field([], description="")
		    one: Optional[time] = Field(None, description="")
		
		
		Tester.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.py").toString.contains(expected))
	}



	@Test
	@Disabled
	def void shouldGenerateMetadFieldWhenAttributeSchemePresent() {
		'''
			type TestObject: <"">
				fieldOne string (0..1) [metadata scheme]
		'''.generatePython

		
	}
	
	@Test
	@Disabled
	def void shouldGenerateRosettaReferenceField() {
		'''
			type TestObject: <"">
				fieldOne Test2 (0..1) [metadata reference]
			
			type Test2:
		'''.generatePython

		
	}
	
	@Test
	@Disabled
	def void shouldGenerateBasicReferenceField() {
		val namespace = 'test.ns.basicref'
		'''
			namespace "«namespace»"
			
			// import basic types
			import com.rosetta.test.model.*
			
			type TestObject: <"">
				fieldOne date (0..1) [metadata reference]
		'''.generatePython

		
	}

	@Test
	@Disabled
	def void shouldCreateFieldWithReferenceTypeWhenAttributeIsReference() {
		'''
			
			type ComplexObject:
			
			type TestObject: <"">
				fieldOne ComplexObject (0..1) [metadata reference]
		'''.generatePython

		
	}

	@Test
	@Disabled
    def void shouldGenerateTypeWithMetaFieldImport() {
    	val namespace = 'test.ns.metafield'
        '''
            namespace "«namespace»"
            version "test"
            
            // import basic types
            import com.rosetta.test.model.*
            
            type Foo:
                [metadata key]
                
                attr string (0..1)
        '''.generatePython

		
	}

	@Test
	@Disabled
	def void shouldImplementGlobalKeyWhenDefined() {
		'''
			type WithGlobalKey:
				[metadata key]
				bar string (1..1)
		'''.generatePython

		
	}

	@Test
	def void shouldOmmitGlobalKeyAnnotationWhenNotDefined() {
		val python = '''
			type AttributeGlobalKeyTest:
				withoutGlobalKey string (1..1)
		'''.generatePython

		
		
		val expected=
		'''
		class AttributeGlobalKeyTest(BaseDataClass):
		    withoutGlobalKey: str = Field(..., description="")
		
		
		AttributeGlobalKeyTest.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.py").toString.contains(expected))
	}

	@Test
	@Disabled
	def void shouldGenerateReferenceAttributeAsReference() {
		'''
			type Foo:
				[metadata key]
				bar string (1..1)
			
			type AttributeGlobalKeyTest:
				withGlobalKey Foo (1..1) [metadata reference]
		'''.generatePython

		
	}

	@Test
	def void testGenerateClassList() {
		val python = '''
			type A extends B:
				c C (1..*)
			
			type B:
			
			type C :
				one int (0..1)
				list int (0..*)
			
			
			type D:
				s string (1..*)
		'''.generatePython

		
		val expected=
		'''
		class B(BaseDataClass):
		    pass
		
		class C(BaseDataClass):
		    list: List[int] = Field([], description="")
		    one: Optional[int] = Field(None, description="")
		
		class D(BaseDataClass):
		    s: List[str] = Field([], description="")
		    @rosetta_condition
		    def cardinality_s(self):
		        return check_cardinality(self.s, 1, None)
		
		    
		class A(B):
		    c: List[C] = Field([], description="")
		    @rosetta_condition
		    def cardinality_c(self):
		        return check_cardinality(self.c, 1, None)
		    
		
		
		B.update_forward_refs()
		C.update_forward_refs()
		D.update_forward_refs()
		A.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.py").toString.contains(expected))
	}

	@Test
	def void shouldExtendATypeWithSameAttribute() {
		val python = '''
			type Foo:
				a string (0..1)
				b string (0..1)
			
			type Bar extends Foo:
				a string (0..1)
		'''.generatePython

		
		
		val expected=
		'''
		class Foo(BaseDataClass):
		    a: Optional[str] = Field(None, description="")
		    b: Optional[str] = Field(None, description="")
		
		class Bar(Foo):
		    a: Optional[str] = Field(None, description="")
		
		
		Foo.update_forward_refs()
		Bar.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.py").toString.contains(expected))
	}

	@Test
	def shouldGenerateRosettaCalculationTypeAsString() {
		val python = '''
			type Foo:
				bar calculation (0..1)
		'''.generatePython

		
		val expected=
		'''
		class Foo(BaseDataClass):
		    bar: Optional[str] = Field(None, description="")
		
		
		Foo.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.py").toString.contains(expected))
	}

	@Test
	def void shouldSetAttributesOnEmptyClassWithInheritance() {
		val python = '''
			type Foo:
				attr string (0..1)
			
			type Bar extends Foo:
		'''.generatePython

		
		val expected=
		'''
		class Foo(BaseDataClass):
		    attr: Optional[str] = Field(None, description="")
		
		class Bar(Foo):
		    pass
		
		
		Foo.update_forward_refs()
		Bar.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.py").toString.contains(expected))
	}
	
	@Test
	@Disabled
	def void isProductWithEnumValueRef() {
		'''
			isProduct root Foo;
			
			enum Enum: 
				A
				B
			
			type Foo:
				attr Enum (0..1)
			
			func Qualify_FooProd:
				[qualification Product]
				inputs: foo Foo (1..1)
				output: is_product boolean (1..1)
				set is_product:
					foo -> attr = Enum -> A
		'''.generatePython

	}
	
	@Test
	@Disabled
	def void internalReferenceTest() {
		'''

			type Foo:
				foo string (1..1) 
					[metadata location]
			
			type Bar:
				bar string (1..1)
					[metadata address "pointsTo"=Foo->foo]
			
		'''.generatePython
		
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
                    if B exists
                    then aValue->a0 exists
                        or (intValue2 exists and intValue1 exists and intValue1 exists)
                        or (intValue2 exists and intValue1 exists and intValue1 is absent)
            '''.generatePython

        val expected =
        '''
        class A(BaseDataClass):
            a0: Optional[int] = Field(None, description="")
            a1: Optional[int] = Field(None, description="")
            
            @rosetta_condition
            def condition_0_(self):
                return self.check_one_of_constraint('a0', 'a1', necessity=True)
        
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
        
        
        A.update_forward_refs()
        B.update_forward_refs()
        '''
        assertTrue(python.get("Types.py").toString.contains(expected))
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

        
        val expected = 
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
           
           
           TestType.update_forward_refs()
           TestType2.update_forward_refs()
            '''
            
            assertTrue(python.get("Types.py").toString.contains(expected))
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
        assertTrue(python.get("Types.py").toString.contains(expected))
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


        val types = python.get('Types.py').toString
        val expected =
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
        
            
        class TestType2(TestType3):
            TestType2Value1: Optional[Decimal] = Field(None, description="Test number")
            """
            Test number
            """
            TestType2Value2: List[date] = Field([], description="Test date")
            """
            Test date
            """
        
        class TestType(TestType2):
            TestTypeValue1: str = Field(..., description="Test string")
            """
            Test string
            """
            TestTypeValue2: Optional[int] = Field(None, description="Test int")
            """
            Test int
            """
        
        
        TestType3.update_forward_refs()
        TestType2.update_forward_refs()
        TestType.update_forward_refs()
        '''
        assertTrue(types.contains(expected))        
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

            val types = python.get('Types.py').toString

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
            
            
            TestType.update_forward_refs()
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

            val types = python.get('Types.py').toString

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
            
            
            TestType.update_forward_refs()
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

        val expected =
        '''
        class A(BaseDataClass):
            a0: Optional[int] = Field(None, description="")
            a1: Optional[int] = Field(None, description="")
            
            @rosetta_condition
            def condition_0_(self):
                return self.check_one_of_constraint('a0', 'a1', necessity=True)
        
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
        
        
        A.update_forward_refs()
        B.update_forward_refs()
        '''
        assertTrue(python.get('Types.py').toString.contains(expected))
    }
	
	
	
	def generatePython(CharSequence model) {
    	val eResource = model.parseRosetta.eResource
    	generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
    	
    }
}