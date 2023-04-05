package com.regnosys.rosetta.generator.python.rule

import com.google.inject.Inject
import com.google.inject.Provider
import com.regnosys.rosetta.generator.python.PythonCodeGenerator
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import org.eclipse.xtext.resource.XtextResourceSet
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.eclipse.xtext.testing.util.ParseHelper
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)

class DataRuleGeneratorTest {
	
    @Inject extension ModelHelper
    @Inject PythonCodeGenerator generator;

    @Inject extension ParseHelper<RosettaModel>
    @Inject Provider<XtextResourceSet> resourceSetProvider;
	
	@Test
	def void shouldGenerateConditionWithIfElseIf() {
		val python = '''
			type Foo:
				bar string (0..1)
				baz string (0..1)
			
			    condition:
			        if bar="Y" then baz exists
			        else if (bar="I" or bar="N") then baz is absent
		'''.generatePython

		val expected=
		'''
		class Foo(BaseModel):
		    bar: Optional[str] = Field(None,description = "")
		    baz: Optional[str] = Field(None,description = "")
		    
		    @root_validator
		    @classmethod
		    def condition_0_(cls, values):
		        return _if(self.bar == "Y", ((self.baz) is not None), _if((self.bar == "I" or self.bar == "N"), ((self.baz) is None), False))
		'''
		
		//assertTrue(python.toString.contains(expected))
	}

	@Test
	def void shouldGenerateConditionWithNestedIfElseIf() {
		val python = '''
			type Foo:
				bar string (0..1)
				baz string (0..1)
			
			    condition:
			    	if bar exists then
				        if bar="Y" then baz exists
				        else if (bar="I" or bar="N") then baz is absent
		'''.generatePython

		
		val expected=
		'''
		class Foo(BaseDataClass):
		    bar: Optional[str] = Field(None, description="")
		    baz: Optional[str] = Field(None, description="")
		    
		    @cdm_condition
		    def condition_0_(self):
		        return if_cond(((self.bar) is not None), 'if_cond(all_elements(self.bar, "=", "Y"), \'((self.baz) is not None)\', \'if_cond((all_elements(self.bar, "=", "I") or all_elements(self.bar, "=", "N")), \\\'((self.baz) is None)\\\', \\\'True\\\', self)\', self)', 'True', self)
		
		
		Foo.update_forward_refs()
		'''
		
		
		assertTrue(python.get("Types.kt").toString.contains(expected))
	}


	@Test
	def void quoteExists() {
		val python = '''
				type Quote:
					quotePrice QuotePrice (0..1)
					condition Quote_Price:
						if quotePrice exists
						then quotePrice -> bidPrice exists or quotePrice -> offerPrice exists
				
				type QuotePrice:
					bidPrice number (0..1)
					offerPrice number (0..1)
		'''.generatePython

		val expected=
		'''
		class Quote(BaseDataClass):
		    quotePrice: Optional[QuotePrice] = Field(None, description="")
		    
		    @cdm_condition
		    def condition_0_Quote_Price(self):
		        return if_cond(((self.quotePrice) is not None), '(((self.quotePrice.bidPrice) is not None) or ((self.quotePrice.offerPrice) is not None))', 'True', self)
		
		class QuotePrice(BaseDataClass):
		    bidPrice: Optional[float] = Field(None, description="")
		    offerPrice: Optional[float] = Field(None, description="")
		
		
		Quote.update_forward_refs()
		QuotePrice.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.kt").toString.contains(expected))
	}

	@Test
	def void nestedAnds() {
		val python = '''
				type Quote:
					quotePrice QuotePrice (0..1)
					condition Quote_Price:
						if quotePrice exists
						then (
							quotePrice -> price1 exists
							and quotePrice -> price2 exists
							and quotePrice -> price3 exists
						)
				
				type QuotePrice:
					price1 number (0..1)
					price2 number (0..1)
					price3 number (0..1)
				
		'''.generatePython

		
		val expected=
		'''
		class Quote(BaseDataClass):
		    quotePrice: Optional[QuotePrice] = Field(None, description="")
		    
		    @cdm_condition
		    def condition_0_Quote_Price(self):
		        return if_cond(((self.quotePrice) is not None), '((((self.quotePrice.price1) is not None) and ((self.quotePrice.price2) is not None)) and ((self.quotePrice.price3) is not None))', 'True', self)
		
		class QuotePrice(BaseDataClass):
		    price1: Optional[float] = Field(None, description="")
		    price2: Optional[float] = Field(None, description="")
		    price3: Optional[float] = Field(None, description="")
		
		
		Quote.update_forward_refs()
		QuotePrice.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.kt").toString.contains(expected))
	}

	@Test
	def void numberAttributeisHandled() {
		val python = '''
				type Quote:
					quotePrice QuotePrice (0..1)
					condition Quote_Price:
						if quotePrice exists
						then quotePrice -> bidPrice = 0.0
				
				type QuotePrice:
					bidPrice number (0..1)
		'''.generatePython

		
		val expected=
		'''
		class Quote(BaseDataClass):
		    quotePrice: Optional[QuotePrice] = Field(None, description="")
		    
		    @cdm_condition
		    def condition_0_Quote_Price(self):
		        return if_cond(((self.quotePrice) is not None), 'all_elements(self.quotePrice.bidPrice, "=", 0.0)', 'True', self)
		
		class QuotePrice(BaseDataClass):
		    bidPrice: Optional[float] = Field(None, description="")
		
		
		Quote.update_forward_refs()
		QuotePrice.update_forward_refs()
		'''
		
		
		assertTrue(python.get("Types.kt").toString.contains(expected))
	}
	
	@Test
	def void dataRuleWithDoIfAndFunction() {
		val python = '''
				func Foo:
					inputs:
						price number (0..1)
					output:
						something number (1..1)
				
				type Quote:
					price number (0..1)
					
					condition:
						if price exists
						then Foo( price ) = 5.0
		'''.generatePython

		val expectedFunc=
		'''
		def Foo(price=None):
			pass
		'''
		val expectedType='''
		
		class Quote(BaseDataClass):
		    price: Optional[float] = Field(None, description="")
		    
		    @cdm_condition
		    def condition_0_(self):
		        return if_cond(((self.price) is not None), 'all_elements(Foo(self.price), "=", 5.0)', 'True', self)
		
		
		Quote.update_forward_refs()
		'''
		
		
		assertTrue(python.get("Types.kt").toString.contains(expectedType))
		assertTrue(python.get("Funcs.kt").toString.contains(expectedFunc))
		
	}
	
	@Test
	def void dataRuleWithDoIfAndFunctionAndElse() {
		val python = '''
				func Foo:
					inputs:
						price number (0..1)
					output:
						something number (1..1)
				
				type Quote:
					price number (0..1)
					
					condition:
						if price exists
						then Foo( price ) = 5.0
						else True
		'''.generatePython

		val expected1=
		'''
		class Quote(BaseDataClass):
		    price: Optional[float] = Field(None, description="")
		    
		    @cdm_condition
		    def condition_0_(self):
		        return if_cond(((self.price) is not None), 'all_elements(Foo(self.price), "=", 5.0)', 'False', self)
		
		
		Quote.update_forward_refs()
		'''
		
		
		assertTrue(python.toString.contains(expected1))
	}
	
	@Test
	def void dataRuleCoinHead() {
		val python = '''
			type Coin:
				head boolean (0..1)
				tail boolean (0..1)
				
				condition CoinHeadRule:
					if head = True
					then tail = False

		'''.generatePython
		
		val expected=
		'''
		class Coin(BaseDataClass):
		    head: Optional[bool] = Field(None, description="")
		    tail: Optional[bool] = Field(None, description="")
		    
		    @cdm_condition
		    def condition_0_CoinHeadRule(self):
		        return if_cond(all_elements(self.head, "=", False), 'all_elements(self.tail, "=", False)', 'True', self)
		
		
		Coin.update_forward_refs()
		'''
		
		assertTrue(python.toString.contains(expected))
	}

	@Test
	def void dataRuleCoinTail() {
		val python = '''
			type Coin:
				head boolean (0..1)
				tail boolean (0..1)
				
				condition CoinTailRule:
					if tail = True
					then head = False
		'''.generatePython

		val expected=
		'''
		class Coin(BaseDataClass):
		    head: Optional[bool] = Field(None, description="")
		    tail: Optional[bool] = Field(None, description="")
		    
		    @cdm_condition
		    def condition_0_CoinTailRule(self):
		        return if_cond(all_elements(self.tail, "=", False), 'all_elements(self.head, "=", False)', 'True', self)
		
		
		Coin.update_forward_refs()
		'''
		
		assertTrue(python.get("Types.kt").toString.contains(expected))
	}
	
	@Test
	def void dataRuleCoinEdge() {
		val python = '''
			type Coin:
				head boolean (0..1)
				tail boolean (0..1)
				
				condition EdgeRule:
					if tail = False
					then head = False
		'''.generatePython

		val expected=
		'''
		class Coin(BaseDataClass):
		    head: Optional[bool] = Field(None, description="")
		    tail: Optional[bool] = Field(None, description="")
		    
		    @cdm_condition
		    def condition_0_EdgeRule(self):
		        return if_cond(all_elements(self.tail, "=", False), 'all_elements(self.head, "=", False)', 'True', self)
		
		
		Coin.update_forward_refs()
		'''
		
		assertTrue(python.toString.contains(expected))
	}

	
	@Test
	def void conditionCount() {
		val python = '''
			type CondTest:
				multiAttr number (0..*)
				
				condition:
					multiAttr count >= 0
		'''.generatePython

		
		val expected=
		'''
		class CondTest(BaseDataClass):
		    multiAttr: Optional[List[float]] = Field(None, description="")
		    
		    @cdm_condition
		    def condition_0_(self):
		        return all_elements(len(self.multiAttr), ">=", 0)
		
		
		CondTest.update_forward_refs()
		'''
		
		
		assertTrue(python.toString.contains(expected))
	}
	
	@Test
	def void shouldCheckConditionWithInheritedAttribute() {
		val python = '''
			type Foo:
				x string (0..1)
				y string (0..1)
				
				condition:
					x exists
			
			type Bar extends Foo:
				z string (0..1)
				
				condition:
					y exists
		'''.generatePython

		val expected=
		'''
		class Foo(BaseDataClass):
		    x: Optional[str] = Field(None, description="")
		    y: Optional[str] = Field(None, description="")
		    
		    @cdm_condition
		    def condition_0_(self):
		        return ((self.x) is not None)
		
		class Bar(Foo):
		    z: Optional[str] = Field(None, description="")
		    
		    @cdm_condition
		    def condition_0_(self):
		        return ((self.y) is not None)
		
		
		Foo.update_forward_refs()
		Bar.update_forward_refs()
		'''
		
		assertTrue(python.toString.contains(expected))
	}
	
	
	@Test
	def void shouldCheckInheritedCondition() {
		val python = '''
			type Foo:
				x string (0..1)
				y string (0..1)
				
				condition:
					x exists
			
			type Bar extends Foo:
				z string (0..1)
				
				condition:
					y exists
		'''.generatePython

		val expected=
		'''
		class Foo(BaseDataClass):
		    x: Optional[str] = Field(None, description="")
		    y: Optional[str] = Field(None, description="")
		    
		    @cdm_condition
		    def condition_0_(self):
		        return ((self.x) is not None)
		
		class Bar(Foo):
		    z: Optional[str] = Field(None, description="")
		    
		    @cdm_condition
		    def condition_0_(self):
		        return ((self.y) is not None)
		
		
		Foo.update_forward_refs()
		Bar.update_forward_refs()
		'''
		
		assertTrue(python.toString.contains(expected))
	}
		
	
	
	def generatePython(CharSequence model) {
    	val eResource = model.parseRosettaWithNoErrors.eResource
    	generator.afterGenerateTest(eResource.contents.filter(RosettaModel).toList)
    	
    }

	
}