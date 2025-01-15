package com.regnosys.rosetta.generator.python.expression

import com.google.inject.Inject
import com.regnosys.rosetta.generator.python.PythonCodeGenerator
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*
import org.junit.Ignore

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class PythonExpressionGeneratorTest {
    
    @Inject extension ModelHelper
    @Inject PythonCodeGenerator generator;
    
    @Test
    def void testGenerateSwitch() {
            val python = '''type FooTest:
            a int (1..1)
            condition Test:
                a switch
                    1 then True,
                    2 then True,
                    default False
            '''.generatePython()
            val expected = '''class FooTest(BaseDataClass):
    a: int = Field(..., description="")
    
    @rosetta_condition
    def condition_0_Test(self):
        item = self
        def _then_1():
            return True
        def _then_2():
            return True
        def _then_default():
            return False
        match rosetta_resolve_attr(self, "a"):
            case 1: return _then_1()
            case 2: return _then_2()
            case _: return _then_default()'''
            assertTrue(python.toString.contains(expected));
        }

    @Test
    def void testGenerateChoiceCondition() {
        val python = '''type Test1:<"Test choice condition.">
            field1 string (0..1) <"Test string field 1">
            field2 string (0..1) <"Test string field 2">
            field3 string (0..1) <"Test string field 3">
            condition TestChoice: optional choice field1, field2, field3
            '''.generatePython    
        val expected = '''class Test1(BaseDataClass):
    """
    Test choice condition.
    """
    field1: Optional[str] = Field(None, description="Test string field 1")
    """
    Test string field 1
    """
    field2: Optional[str] = Field(None, description="Test string field 2")
    """
    Test string field 2
    """
    field3: Optional[str] = Field(None, description="Test string field 3")
    """
    Test string field 3
    """
    
    @rosetta_condition
    def condition_0_TestChoice(self):
        item = self
        return rosetta_check_one_of(self, 'field1', 'field2', 'field3', necessity=False)'''

        assertTrue(python.toString.contains(expected))
    }
    
    @Test
    def void testGenerateOneOfCondition() {
        val python = '''type Test1:<"Test one-of condition.">
                field1 string (0..1) <"Test string field 1">
                condition OneOf: one-of
            '''.generatePython    

        val expected= '''class Test1(BaseDataClass):
    _CHOICE_ALIAS_MAP ={"field1":[]}
    """
    Test one-of condition.
    """
    field1: Optional[str] = Field(None, description="Test string field 1")
    """
    Test string field 1
    """
    
    @rosetta_condition
    def condition_0_OneOf(self):
        item = self
        return rosetta_check_one_of(self, 'field1', necessity=True)'''
        assertTrue(python.toString.contains(expected))
    }

    @Test
    def void testGenerateIfThenCondition() {
        val python = '''type Test1: <"Test if-then condition.">
                field1 string (0..1) <"Test string field 1">
                field2 number (0..1) <"Test number field 2">
                condition TestCond: <"Test condition">
                    if field1 exists
                        then field2=0
            '''.generatePython    

        val expected = '''class Test1(BaseDataClass):
    """
    Test if-then condition.
    """
    field1: Optional[str] = Field(None, description="Test string field 1")
    """
    Test string field 1
    """
    field2: Optional[Decimal] = Field(None, description="Test number field 2")
    """
    Test number field 2
    """
    
    @rosetta_condition
    def condition_0_TestCond(self):
        """
        Test condition
        """
        item = self
        def _then_fn0():
            return all_elements(rosetta_resolve_attr(self, "field2"), "=", 0)
        
        def _else_fn0():
            return True
        
        return if_cond_fn(rosetta_attr_exists(rosetta_resolve_attr(self, "field1")), _then_fn0, _else_fn0)'''

        assertTrue(python.toString.contains(expected))
    }
    
    @Test
    def void testGenerateIfThenElseCondition() {
        val python = '''type Test1: <"Test if-then-else condition.">
            field1 string (0..1) <"Test string field 1">
            field2 number (0..1) <"Test number field 2">
            condition TestCond: <"Test condition">
                if field1 exists
                    then field2=0
                    else field2=1
        '''.generatePython    
                       
         val expected= '''class Test1(BaseDataClass):
    """
    Test if-then-else condition.
    """
    field1: Optional[str] = Field(None, description="Test string field 1")
    """
    Test string field 1
    """
    field2: Optional[Decimal] = Field(None, description="Test number field 2")
    """
    Test number field 2
    """
    
    @rosetta_condition
    def condition_0_TestCond(self):
        """
        Test condition
        """
        item = self
        def _then_fn0():
            return all_elements(rosetta_resolve_attr(self, "field2"), "=", 0)
        
        def _else_fn0():
            return all_elements(rosetta_resolve_attr(self, "field2"), "=", 1)
        
        return if_cond_fn(rosetta_attr_exists(rosetta_resolve_attr(self, "field1")), _then_fn0, _else_fn0)'''
        assertTrue(python.toString.contains(expected))
    }
    
    @Test
    def void testGenerateBooleanCondition(){
        val python = '''type Test1: <"Test boolean condition.">
            field1 boolean (1..1) <"Test booelan field 1">
            field2 number (0..1) <"Test number field 2">
            condition TestCond: <"Test condition">
                if field1= True
                    then field2=0
                    else field2=5
                '''.generatePython 
        val expected= '''class Test1(BaseDataClass):
    """
    Test boolean condition.
    """
    field1: bool = Field(..., description="Test booelan field 1")
    """
    Test booelan field 1
    """
    field2: Optional[Decimal] = Field(None, description="Test number field 2")
    """
    Test number field 2
    """
    
    @rosetta_condition
    def condition_0_TestCond(self):
        """
        Test condition
        """
        item = self
        def _then_fn0():
            return all_elements(rosetta_resolve_attr(self, "field2"), "=", 0)
        
        def _else_fn0():
            return all_elements(rosetta_resolve_attr(self, "field2"), "=", 5)
        
        return if_cond_fn(all_elements(rosetta_resolve_attr(self, "field1"), "=", True), _then_fn0, _else_fn0)'''
        assertTrue(python.toString.contains(expected))
    }
    
    @Test
    def void testGenerateAbsentCondition(){
        val python = '''type Test1: <"Test absent condition.">
            field1 boolean (1..1) <"Test booelan field 1">
            field2 number (0..1) <"Test number field 2">
            condition TestCond: <"Test condition">
                if field1= True
                    then field2=0
                    else field2 is absent
        '''.generatePython 
        val expected= '''class Test1(BaseDataClass):
    """
    Test absent condition.
    """
    field1: bool = Field(..., description="Test booelan field 1")
    """
    Test booelan field 1
    """
    field2: Optional[Decimal] = Field(None, description="Test number field 2")
    """
    Test number field 2
    """
    
    @rosetta_condition
    def condition_0_TestCond(self):
        """
        Test condition
        """
        item = self
        def _then_fn0():
            return all_elements(rosetta_resolve_attr(self, "field2"), "=", 0)
        
        def _else_fn0():
            return (not rosetta_attr_exists(rosetta_resolve_attr(self, "field2")))
        
        return if_cond_fn(all_elements(rosetta_resolve_attr(self, "field1"), "=", True), _then_fn0, _else_fn0)'''

        assertTrue(python.toString.contains(expected))
    }
    
    @Test
    def void testGenerateOnlyElementCondition(){
        val python = '''enum TestEnum: <"Enum to test">
            TestEnumValue1 <"Test enum value 1">
            TestEnumValue2 <"Test enum value 2">
            type Test1: <"Test only-element condition.">
                field1 TestEnum (0..1) <"Test enum field 1">
                field2 number (0..1) <"Test number field 2">
                condition TestCond: <"Test condition">
                    if field1 only-element= TestEnum->TestEnumValue1 
                        then field2=0
            '''.generatePython 
            
        val expectedEnum= '''class TestEnum(Enum):
    """
    Enum to test
    """
    TEST_ENUM_VALUE_1 = "TestEnumValue1"
    """
    Test enum value 1
    """
    TEST_ENUM_VALUE_2 = "TestEnumValue2"
    """
    Test enum value 2
    """'''
        val expectedTest= '''class Test1(BaseDataClass):
    """
    Test only-element condition.
    """
    field1: Optional[com.rosetta.test.model.TestEnum.TestEnum] = Field(None, description="Test enum field 1")
    """
    Test enum field 1
    """
    field2: Optional[Decimal] = Field(None, description="Test number field 2")
    """
    Test number field 2
    """
    
    @rosetta_condition
    def condition_0_TestCond(self):
        """
        Test condition
        """
        item = self
        def _then_fn0():
            return all_elements(rosetta_resolve_attr(self, "field2"), "=", 0)
        
        def _else_fn0():
            return True
        
        return if_cond_fn(all_elements(get_only_element(rosetta_resolve_attr(self, "field1")), "=", rosetta_resolve_attr(TestEnum, "TEST_ENUM_VALUE_1")), _then_fn0, _else_fn0)'''
        assertTrue(python.toString.contains(expectedEnum))
        assertTrue(python.toString.contains(expectedTest))
    }

    @Test
    def void testGenerateOnlyExistsCondition(){
        val python = '''type A: <"Test type">
            field1 number (0..1) <"Test number field 1">

            type Test: <"Test only exists condition">
                aValue A (1..1) <"Test A type aValue">

                condition TestCond: <"Test condition">
                    if aValue -> field1 exists 
                        then aValue -> field1 only exists
            '''.generatePython

            val expected= '''class Test(BaseDataClass):
    """
    Test only exists condition
    """
    aValue: com.rosetta.test.model.A.A = Field(..., description="Test A type aValue")
    """
    Test A type aValue
    """
    
    @rosetta_condition
    def condition_0_TestCond(self):
        """
        Test condition
        """
        item = self
        def _then_fn0():
            return rosetta_check_one_of(self, rosetta_resolve_attr(rosetta_resolve_attr(self, "aValue"), "field1"))
        
        def _else_fn0():
            return True
        
        return if_cond_fn(rosetta_attr_exists(rosetta_resolve_attr(rosetta_resolve_attr(self, "aValue"), "field1")), _then_fn0, _else_fn0)'''
        val expectedA ='''class A(BaseDataClass):
    """
    Test type
    """
    field1: Optional[Decimal] = Field(None, description="Test number field 1")
    """
    Test number field 1
    """'''

        assertTrue(python.toString.contains(expected))
        assertTrue(python.toString.contains(expectedA))
    }
    
    @Test
    def void testGenerateCountCondition(){
        val python = '''type A: <"Test type">
            field1 int (0..*) <"Test int field 1">
            field2 int (0..*) <"Test int field 2">

            type Test: <"Test count operation condition">
                aValue A (1..*) <"Test A type aValue">
                
                condition TestCond: <"Test condition">
                    if aValue -> field1 count <> aValue -> field2 count 
                        then True
                    else False
            '''.generatePython 

            val expected = '''class Test(BaseDataClass):
    """
    Test count operation condition
    """
    aValue: List[com.rosetta.test.model.A.A] = Field([], description="Test A type aValue")
    """
    Test A type aValue
    """
    @rosetta_condition
    def cardinality_aValue(self):
        return check_cardinality(self.aValue, 1, None)
    
    
    @rosetta_condition
    def condition_0_TestCond(self):
        """
        Test condition
        """
        item = self
        def _then_fn0():
            return True
        
        def _else_fn0():
            return False
        
        return if_cond_fn(any_elements(rosetta_count(rosetta_resolve_attr(rosetta_resolve_attr(self, "aValue"), "field1")), "<>", rosetta_count(rosetta_resolve_attr(rosetta_resolve_attr(self, "aValue"), "field2"))), _then_fn0, _else_fn0)'''
        val expectedA ='''class A(BaseDataClass):
    """
    Test type
    """
    field1: List[int] = Field([], description="Test int field 1")
    """
    Test int field 1
    """
    field2: List[int] = Field([], description="Test int field 2")
    """
    Test int field 2
    """'''

        assertTrue(python.toString.contains(expected))
        assertTrue(python.toString.contains(expectedA))
    }
    
    @Test
    def void testGenerateAnyCondition(){
        val python = '''type Test: <"Test any operation condition">
                field1 string (1..1) <"Test string field1">
                field2 string (1..1) <"Test boolean field2">
                condition TestCond: <"Test condition">
                    if field1="A" 
                    then ["B", "C", "D"] any = field2
            '''.generatePython 
            
            val expected= '''class Test(BaseDataClass):
    """
    Test any operation condition
    """
    field1: str = Field(..., description="Test string field1")
    """
    Test string field1
    """
    field2: str = Field(..., description="Test boolean field2")
    """
    Test boolean field2
    """
    
    @rosetta_condition
    def condition_0_TestCond(self):
        """
        Test condition
        """
        item = self
        def _then_fn0():
            return all_elements(["B", "C", "D"], "=", rosetta_resolve_attr(self, "field2"))
        
        def _else_fn0():
            return True
        
        return if_cond_fn(all_elements(rosetta_resolve_attr(self, "field1"), "=", "A"), _then_fn0, _else_fn0)'''

        assertTrue(python.toString.contains(expected))
    }
    
    @Test
    def void testGenerateDistinctCondition(){
        val python = '''type A: <"Test type">
            field1 int (0..*) <"Test int field 1">
            field2 int (0..*) <"Test int field 2">
                    
            type Test: <"Test distinct operation condition">
            aValue A (1..*) <"Test A type aValue">
                field3 number (1..1)<"Test number field 3">
            condition TestCond: <"Test condition">
                if aValue -> field1 distinct count = 1
                    then field3=0
                else field3=1
                '''.generatePython 

            val expected= '''class Test(BaseDataClass):
    """
    Test distinct operation condition
    """
    aValue: List[com.rosetta.test.model.A.A] = Field([], description="Test A type aValue")
    """
    Test A type aValue
    """
    @rosetta_condition
    def cardinality_aValue(self):
        return check_cardinality(self.aValue, 1, None)
    
    field3: Decimal = Field(..., description="Test number field 3")
    """
    Test number field 3
    """
    
    @rosetta_condition
    def condition_0_TestCond(self):
        """
        Test condition
        """
        item = self
        def _then_fn0():
            return all_elements(rosetta_resolve_attr(self, "field3"), "=", 0)
        
        def _else_fn0():
            return all_elements(rosetta_resolve_attr(self, "field3"), "=", 1)
        
        return if_cond_fn(all_elements(rosetta_count(set(rosetta_resolve_attr(rosetta_resolve_attr(self, "aValue"), "field1"))), "=", 1), _then_fn0, _else_fn0)
            '''
            
            val expectedClassA=  '''
            class A(BaseDataClass):
                """
                Test type
                """
                field1: List[int] = Field([], description="Test int field 1")
                """
                Test int field 1
                """
                field2: List[int] = Field([], description="Test int field 2")
                """
                Test int field 2
                """'''

            assertTrue(python.toString.contains(expected))
            assertTrue(python.toString.contains(expectedClassA))
    }
    def void testGenerateFlattenCondition(){
        val python = '''
              type C: <"Test type C">
                field4 int (1..1) <"Test int field 4">
                  field5 int (0..*) <"Test int field 5">
              type A: <"Test type">
                  field1 int (0..*) <"Test int field 1">
                  cValue C (0..*) <"Test C type cValue">
              type B: <"Test type B">
                  field2 int (0..*) <"Test int field 2">
                  aValue A (0..*) <"Test A type aValue">
               type Test: <"Test filter operation condition">
                bValue B (0..*) <"Test B type bValue">
                field6 boolean (0..1) <"Test boolean type field6">
                
                condition TestCond: <"Test condition">
                    if bValue->field2 exists
                    then bValue flatten
                  '''.generatePython 
                  
            val expected= '''
            class Test(BaseDataClass):
                """
                Test filter operation condition
                """
                aValue: com.rosetta.test.model.A.A = Field(..., description="Test A type aValue")
                """
                Test A type aValue
                """
                
                @rosetta_condition
                def condition_0_TestCond(self):
                    """
                    Test condition
                    """
                    item = self
                    return (lambda item: rosetta_resolve_attr(rosetta_resolve_attr(self, "aValue"), "field2")[0])(rosetta_filter(item, lambda item: rosetta_resolve_attr(rosetta_resolve_attr(self, "aValue"), "field1")))
            '''
            val expectedClassA='''
            class A(BaseDataClass):
                """
                Test type
                """
                field1: bool = Field(..., description="Test int field 1")
                """
                Test int field 1
                """
                field2: List[int] = Field([], description="Test int field 2")
                """
                Test int field 2
                """
            '''
           assertTrue(python.toString.contains(expected))
           assertTrue(python.toString.contains(expectedClassA))         
    }
    
    @Test
    def void testGenerateBinContainsCondition(){
        val python = '''
              enum C: <"Test type C">
                field4 <"Test enum field 4">
                  field5 <"Test enum field 5">
              type A: <"Test type">
                  field1 int (0..*) <"Test int field 1">
                  cValue C (0..*) <"Test C type cValue">
              type B: <"Test type B">
                  field2 int (0..*) <"Test int field 2">
                  aValue A (0..*) <"Test A type aValue">
               type Test: <"Test filter operation condition">
                bValue B (0..*) <"Test B type bValue">
                field3 boolean (0..1) <"Test bool type field3">
                condition TestCond: <"Test condition">
                    if field3=True
                    then bValue->aValue->cValue contains C->field4
                  '''.generatePython 
                  
            val expected= '''
            class Test(BaseDataClass):
                """
                Test filter operation condition
                """
                bValue: List[com.rosetta.test.model.B.B] = Field([], description="Test B type bValue")
                """
                Test B type bValue
                """
                field3: Optional[bool] = Field(None, description="Test bool type field3")
                """
                Test bool type field3
                """
                
                @rosetta_condition
                def condition_0_TestCond(self):
                    """
                    Test condition
                    """
                    item = self
                    def _then_fn0():
                        return contains(rosetta_resolve_attr(rosetta_resolve_attr(rosetta_resolve_attr(self, "bValue"), "aValue"), "cValue"), rosetta_resolve_attr(C, "FIELD_4"))
                    
                    def _else_fn0():
                        return True
                    
                    return if_cond_fn(all_elements(rosetta_resolve_attr(self, "field3"), "=", True), _then_fn0, _else_fn0)
            '''
            val expectedClassA='''
            class A(BaseDataClass):
                """
                Test type
                """
                field1: List[int] = Field([], description="Test int field 1")
                """
                Test int field 1
                """
                cValue: List[com.rosetta.test.model.C.C] = Field([], description="Test C type cValue")
                """
                Test C type cValue
                """
            '''
            val expectedClassB='''
            class B(BaseDataClass):
                """
                Test type B
                """
                field2: List[int] = Field([], description="Test int field 2")
                """
                Test int field 2
                """
                aValue: List[com.rosetta.test.model.A.A] = Field([], description="Test A type aValue")
                """
                Test A type aValue
                """
            '''
            
            val expectedClassC='''
            class C(Enum):
                """
                Test type C
                """
                FIELD_4 = "field4"
                """
                Test enum field 4
                """
                FIELD_5 = "field5"
                """
                Test enum field 5
                """
            '''
            
           assertTrue(python.toString.contains(expected))
           assertTrue(python.toString.contains(expectedClassA))
           assertTrue(python.toString.contains(expectedClassB))    
           assertTrue(python.toString.contains(expectedClassC))             
    }
    
       @Test
    def void testGenerateBinDisjointCondition(){
        val python = '''
              type Test: <"Test disjoint binary expression condition">
                field1 string (1..1) <"Test string field1">
                field2 string (1..1) <"Test string field2">
                field3 boolean (1..1) <"Test boolean field3">
                condition TestCond: <"Test condition">
                    if field3=False 
                    then if ["B", "C", "D"] any = field2 and ["A"] disjoint field1 
                    then field3=True
            '''.generatePython 
            
            val expected= '''
            class Test(BaseDataClass):
                """
                Test disjoint binary expression condition
                """
                field1: str = Field(..., description="Test string field1")
                """
                Test string field1
                """
                field2: str = Field(..., description="Test string field2")
                """
                Test string field2
                """
                field3: bool = Field(..., description="Test boolean field3")
                """
                Test boolean field3
                """
                
                @rosetta_condition
                def condition_0_TestCond(self):
                    """
                    Test condition
                    """
                    item = self
                    def _then_fn1():
                        return all_elements(rosetta_resolve_attr(self, "field3"), "=", True)
                    
                    def _else_fn1():
                        return True
                    
                    def _then_fn0():
                        return if_cond_fn((all_elements(["B", "C", "D"], "=", rosetta_resolve_attr(self, "field2")) and disjoint(["A"], rosetta_resolve_attr(self, "field1"))), _then_fn1, _else_fn1)
                    
                    def _else_fn0():
                        return True
                    
                    return if_cond_fn(all_elements(rosetta_resolve_attr(self, "field3"), "=", False), _then_fn0, _else_fn0)
            '''
         assertTrue(python.toString.contains(expected))
                    
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
    