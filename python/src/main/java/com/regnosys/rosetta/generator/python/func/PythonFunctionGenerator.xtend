package com.regnosys.rosetta.generator.python.func

import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Function
import java.util.ArrayList
import java.util.HashMap
import java.util.List
import java.util.Map
import com.regnosys.rosetta.rosetta.RosettaModel
import com.google.inject.Inject
import com.regnosys.rosetta.generator.python.util.PythonModelGeneratorUtil

class  PythonFunctionGenerator {
	
	@Inject
	PythonModelGeneratorUtil utils;
	
	
	def Map<String, ? extends CharSequence> generate(List<Function> rosettaFunctions, String version) {
		val result = new HashMap
		
		if(rosettaFunctions.size()>0){
			for(Function func: rosettaFunctions){
				val tr = func.eContainer as RosettaModel
				val namespace = tr.name
				try{
					val funcs = func.generateFunctions(version)				
					result.put(utils.toPyFunctionFileName(namespace, func.name), 
						utils.createImports(func.name) + funcs)
				}
				catch(Exception ex){
					println ('PythonFilesGeneratorTest::Error in... ' + func.name )	
				}		
			} 
		}
		
		return result
	}

	private def generateFunctions(Function function,String version) {
		'''
		def «function.name»«generatesInputs(function)»:
			«generatesBody(function)»
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