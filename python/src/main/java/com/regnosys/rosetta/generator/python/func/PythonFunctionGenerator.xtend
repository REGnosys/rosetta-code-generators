package com.regnosys.rosetta.generator.python.func

import com.google.inject.Inject
import com.regnosys.rosetta.generator.util.Util
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumValueReference
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaFeature
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.RosettaNamed
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Condition
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.simple.Function
import java.util.ArrayList
import java.util.HashMap
import java.util.List
import java.util.Map

class  PythonFunctionGenerator {

	
	static final String FUNCTIONS_FILENAME = 'Funcs.kt'
	
	def Map<String, ? extends CharSequence> generate(List<Function> rosettaFunctions, String version) {
		val result = new HashMap
		
		
		
		if(rosettaFunctions.size()>0){
			
			
			
			val funcs = rosettaFunctions.sortBy[name].generateFunctions(version)
			result.put(FUNCTIONS_FILENAME, funcs)	
		}
		
		result;
		
		
	}
	
	private def generateFunctions(List<Function> rosettaFunctions,String version) {
		
		val existingFunctions = new ArrayList<RosettaNamed>();
		
		
		for(Function func: rosettaFunctions){

			if(!existingFunctions.contains(func)){
				val sharedFunctions = rosettaFunctions.filter[name==func.name]
				
			}
			
			
		}
		
		'''
		«FOR function : rosettaFunctions SEPARATOR "\n"»
		def «function.name»«generatesInputs(function)»:
			«generatesBody(function)»
		
		«ENDFOR»
		'''
		
    }
    private def generatesBody(Function function) {
			'''
			pass
			'''

	}
	
	
	
	private def generatesInputs(Function function) {
		
		val inputs = orderInputs(function.inputs)
		
		var result="("
		var count =0
		for(Attribute input: inputs){
			count+=1
			result+=input.name
			if(input.card.inf==0)
				result+="=None"
			if(count<inputs.size())
				result+=", "
		}
		result+=")"
		'''«result»'''
	}
	
	private def List<Attribute> orderInputs(List<Attribute> inputs){
		val orderedInputs = new ArrayList<Attribute>();
		
		for(Attribute input: inputs){
			if(input.card.inf!=0)
				orderedInputs.add(input)
		}
		for(Attribute input: inputs){
			if(!orderedInputs.contains(input))
				orderedInputs.add(input)
		}
		orderedInputs
		
		
	}
	

	
}