package com.regnosys.rosetta.generator.golang.functions

import com.regnosys.rosetta.generator.golang.object.GolangModelObjectBoilerPlate
import com.regnosys.rosetta.rosetta.RosettaCardinality
import com.regnosys.rosetta.rosetta.RosettaNamed
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Function
import com.regnosys.rosetta.rosetta.simple.FunctionDispatch
import java.util.HashMap
import java.util.List
import java.util.Map
import javax.inject.Inject

import static com.regnosys.rosetta.generator.golang.util.GolangModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.golang.util.GolangTranslator.toGOType

class GolangFunctionGenerator {
	@Inject extension GolangModelObjectBoilerPlate
	
	static final String FILENAME = 'functions.go'
	static final String FOLDERNAME = 'org_isda_cdm_functions'
		
	def Map<String, ? extends CharSequence> generate(Iterable<RosettaNamed> rosettaFunctions, String version) {
		val result = new HashMap
		val functions = rosettaFunctions.sortBy[name].generateFunctions(version).replaceTabsWithSpaces
		result.put(FOLDERNAME+"/"+ FILENAME,functions)
		return result;
	}
	
	private def generateFunctions(List<RosettaNamed> functions, String version)  '''
		
		«fileComment(version)»
		package org_isda_cdm_functions	
		
		import "time"
		import . "org_isda_cdm"		
		
		//Pointer type args used when the latter are optional
		«FOR f : functions»
			«writeFunction(f)»			
		«ENDFOR»
	'''
	
	private def dispatch writeFunction(RosettaNamed f)''''''
	
	private def dispatch writeFunction(Function f)
	'''		
		func «f.name.toFirstUpper»(«FOR input : f.inputs SEPARATOR ","»«input.name» «input.toType» «ENDFOR») «f.output.toType» {		
		«classComment("Function definition for "+f.name)»			
		return «f.output.toZeroValOfGoType»
		}
		
	'''
	
	private def dispatch writeFunction(FunctionDispatch f)
	''''''
	
	private def toZeroValOfGoType(Attribute att) {
		switch att.toRawType.toString{
			case "bool": '''false'''
			case "int": '''0'''
			case "float64": '''0'''			
			default : '''«att.toReturnType»{}'''			
		}
			
		
	}
	
	private def toType(Attribute att) {
		if (att.card!==null && att.card.sup>1)
			'''[]«att.toRawType»'''
		else
			att.toRawType.prefixSingleOptional(att.card)
	}
	
	private def toReturnType(Attribute att) {
		if (att.card!==null && att.card.sup>1)
			'''[]«att.toRawType»'''
		else
			att.toRawType.prefixSingleOptionalReturn(att.card)
	}
	
	private def toRawType(Attribute input) {
		input.typeCall.type.name.toGOType	
	}
	
	
	//optional parameters are made into pointer types so that nil can be passed when the option is absent
	//perhaps a better approach is to pass lists as is done in Java CDM
	private def prefixSingleOptional(CharSequence type, RosettaCardinality card) {
		if (card!==null && card.inf<1)
			'''*«type»'''
		else
			type
	}
	
	private def prefixSingleOptionalReturn(CharSequence type, RosettaCardinality card) {
		if (card!==null && card.inf<1)
			'''&«type»'''
		else
			type
	}
}