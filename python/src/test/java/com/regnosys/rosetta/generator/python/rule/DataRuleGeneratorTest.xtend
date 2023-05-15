package com.regnosys.rosetta.generator.python.rule

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

class DataRuleGeneratorTest {
	
    @Inject extension ModelHelper
    @Inject PythonCodeGenerator generator;

    
	
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
		class Foo(BaseDataClass):
		  bar: Optional[str] = Field(None, description="")
		  baz: Optional[str] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_(self):
		    def _then_fn1():
		      return ((self.baz) is None)
		    
		    def _else_fn1():
		      return True
		    
		    def _then_fn0():
		      return ((self.baz) is not None)
		    
		    def _else_fn0():
		      return if_cond_fn((all_elements(self.bar, "=", "I") or all_elements(self.bar, "=", "N")), _then_fn1, _else_fn1)
		    
		    return if_cond_fn(all_elements(self.bar, "=", "Y"), _then_fn0, _else_fn0)
		'''
		
		assertTrue(python.toString.contains(expected))
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
		  
		  @rosetta_condition
		  def condition_0_(self):
		    def _then_fn2():
		      return ((self.baz) is None)
		    
		    def _else_fn2():
		      return True
		    
		    def _then_fn1():
		      return ((self.baz) is not None)
		    
		    def _else_fn1():
		      return if_cond_fn((all_elements(self.bar, "=", "I") or all_elements(self.bar, "=", "N")), _then_fn2, _else_fn2)
		    
		    def _then_fn0():
		      return if_cond_fn(all_elements(self.bar, "=", "Y"), _then_fn1, _else_fn1)
		    
		    def _else_fn0():
		      return True
		    
		    return if_cond_fn(((self.bar) is not None), _then_fn0, _else_fn0)
		'''
		
		
		assertTrue(python.toString.contains(expected))
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
		
		val expectedQuote=
		'''
		class Quote(BaseDataClass):
		  quotePrice: Optional[QuotePrice] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_Quote_Price(self):
		    def _then_fn0():
		      return (((self.quotePrice.bidPrice) is not None) or ((self.quotePrice.offerPrice) is not None))
		    
		    def _else_fn0():
		      return True
		    
		    return if_cond_fn(((self.quotePrice) is not None), _then_fn0, _else_fn0)
		'''
		
		val expectedQuotePrice=
		'''
		class QuotePrice(BaseDataClass):
		  bidPrice: Optional[Decimal] = Field(None, description="")
		  offerPrice: Optional[Decimal] = Field(None, description="")
		'''
		
		assertTrue(python.toString.contains(expectedQuote))
		assertTrue(python.toString.contains(expectedQuotePrice))
		
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

		
		val expectedQuote=
		'''
		class Quote(BaseDataClass):
		  quotePrice: Optional[QuotePrice] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_Quote_Price(self):
		    def _then_fn0():
		      return ((((self.quotePrice.price1) is not None) and ((self.quotePrice.price2) is not None)) and ((self.quotePrice.price3) is not None))
		    
		    def _else_fn0():
		      return True
		    
		    return if_cond_fn(((self.quotePrice) is not None), _then_fn0, _else_fn0)
		'''
		val expectedQuotePrice=
		'''
		class QuotePrice(BaseDataClass):
		  price1: Optional[Decimal] = Field(None, description="")
		  price2: Optional[Decimal] = Field(None, description="")
		  price3: Optional[Decimal] = Field(None, description="")
		'''
		
		assertTrue(python.toString.contains(expectedQuote))
		assertTrue(python.toString.contains(expectedQuotePrice))
		
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

	
		
		val expectedQuote=
		'''
		class Quote(BaseDataClass):
		  quotePrice: Optional[QuotePrice] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_Quote_Price(self):
		    def _then_fn0():
		      return all_elements(self.quotePrice.bidPrice, "=", 0.0)
		    
		    def _else_fn0():
		      return True
		    
		    return if_cond_fn(((self.quotePrice) is not None), _then_fn0, _else_fn0)
		'''
		
		val expectedQuotePrice=
		'''
		class QuotePrice(BaseDataClass):
		  bidPrice: Optional[Decimal] = Field(None, description="")
		'''
		
		assertTrue(python.toString.contains(expectedQuote))
		assertTrue(python.toString.contains(expectedQuotePrice))
		
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

		val expectedFoo=
		'''
		def Foo(price=None):
			pass
		'''
		val expectedQuote='''
		class Quote(BaseDataClass):
		  price: Optional[Decimal] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_(self):
		    def _then_fn0():
		      return all_elements(Foo(self.price), "=", 5.0)
		    
		    def _else_fn0():
		      return True
		    
		    return if_cond_fn(((self.price) is not None), _then_fn0, _else_fn0)
		'''
		
		
		assertTrue(python.toString.contains(expectedQuote))
		assertTrue(python.toString.contains(expectedFoo))
		
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

		
		val expectedQuoute=
		'''
		class Quote(BaseDataClass):
		  price: Optional[Decimal] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_(self):
		    def _then_fn0():
		      return all_elements(Foo(self.price), "=", 5.0)
		    
		    def _else_fn0():
		      return False
		    
		    return if_cond_fn(((self.price) is not None), _then_fn0, _else_fn0)
		'''
		
		val expectedFoo=
		'''
		def Foo(price=None):
			pass
		'''
		
		
		assertTrue(python.toString.contains(expectedFoo))
		assertTrue(python.toString.contains(expectedQuoute))
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
		  
		  @rosetta_condition
		  def condition_0_CoinHeadRule(self):
		    def _then_fn0():
		      return all_elements(self.tail, "=", False)
		    
		    def _else_fn0():
		      return True
		    
		    return if_cond_fn(all_elements(self.head, "=", False), _then_fn0, _else_fn0)
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
		  
		  @rosetta_condition
		  def condition_0_CoinTailRule(self):
		    def _then_fn0():
		      return all_elements(self.head, "=", False)
		    
		    def _else_fn0():
		      return True
		    
		    return if_cond_fn(all_elements(self.tail, "=", False), _then_fn0, _else_fn0)
		'''
		
		assertTrue(python.toString.contains(expected))
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
		  
		  @rosetta_condition
		  def condition_0_EdgeRule(self):
		    def _then_fn0():
		      return all_elements(self.head, "=", False)
		    
		    def _else_fn0():
		      return True
		    
		    return if_cond_fn(all_elements(self.tail, "=", False), _then_fn0, _else_fn0)
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
		  multiAttr: List[Decimal] = Field([], description="")
		  
		  @rosetta_condition
		  def condition_0_(self):
		    return all_elements(len(self.multiAttr), ">=", 0)
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

		val expectedFoo=
		'''
		class Foo(BaseDataClass):
		  x: Optional[str] = Field(None, description="")
		  y: Optional[str] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_(self):
		    return ((self.x) is not None)

		'''
		
		val expectedBar=
		'''
		class Bar(Foo):
		  z: Optional[str] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_(self):
		    return ((self.y) is not None)
		'''
		
		assertTrue(python.toString.contains(expectedFoo))
		assertTrue(python.toString.contains(expectedBar))
		
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
		
		val expectedFoo=
		'''
		class Foo(BaseDataClass):
		  x: Optional[str] = Field(None, description="")
		  y: Optional[str] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_(self):
		    return ((self.x) is not None)
		'''
		
		val expectedBar=
		'''
		class Bar(Foo):
		  z: Optional[str] = Field(None, description="")
		  
		  @rosetta_condition
		  def condition_0_(self):
		    return ((self.y) is not None)
		'''
		
		assertTrue(python.toString.contains(expectedFoo))
		assertTrue(python.toString.contains(expectedBar))	
	}
		
	
	
	def generatePython(CharSequence model) {
    	val eResource = model.parseRosettaWithNoErrors.eResource
    	generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
    	
    }

	
}