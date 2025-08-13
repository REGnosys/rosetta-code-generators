package com.regnosys.rosetta.generator.daml.functions

import com.regnosys.rosetta.generator.daml.object.DamlModelObjectBoilerPlate
import com.regnosys.rosetta.rosetta.RosettaCardinality
import com.regnosys.rosetta.rosetta.RosettaNamed
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Function
import com.regnosys.rosetta.rosetta.simple.FunctionDispatch
import jakarta.inject.Inject
import java.util.HashMap
import java.util.List
import java.util.Map

import static com.regnosys.rosetta.generator.daml.util.DamlModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.daml.util.DamlTranslator.toDamlType
import com.google.common.collect.SetMultimap

class DamlFunctionGenerator {
	@Inject extension DamlModelObjectBoilerPlate
	
	
	def Map<String, ? extends CharSequence> generate(Iterable<Function> rosettaFunctions, SetMultimap<String, String> imports, String version) {
		val functionsByNamespace = rosettaFunctions.groupBy[model.name.split("\\.").map[toFirstUpper].join(".")]
		
		val result = new HashMap
		functionsByNamespace.forEach[k,v|
			val namespace = k
			val folderPart = namespace.split("\\.").join("/")
			val functions = v.sortBy[name].generateFunctions(namespace, imports, version).replaceTabsWithSpaces
			result.put('''Org/Isda/«folderPart»/Functions.daml''',functions)
		]
		
		return result;
	}
	
	private def generateFunctions(List<Function> functions, String namespace, SetMultimap<String, String> imports, String version)  '''
		daml 1.2
		
		«fileComment(version)»
		module Org.Isda.«namespace».Functions
		  ( module Org.Isda.«namespace».Functions ) where
		
		«FOR i : imports.get(namespace)»
			«IF !i.endsWith(".Functions")»import «i»«ENDIF»
		«ENDFOR»
		import Prelude hiding (Party, exercise, id, product, agreement)
		
		«FOR f : functions»
			«writeFunction(f)»
			
		«ENDFOR»
	'''
	
	private def dispatch writeFunction(RosettaNamed f)''''''
	
	private def dispatch writeFunction(Function f)
	'''
		«classComment("Function argument object definition for "+f.name)»
		data «f.name.toFirstUpper»Spec = «f.name.toFirstUpper»Spec with
		  «FOR input : f.inputs»
		  «input.name» : «input.toType»
		  «ENDFOR»
		    deriving (Eq, Ord, Show)
		
		«classComment("Function definition for "+f.name)»
		«f.name.toFirstLower»Func : («f.name»Spec -> «f.output.toType») -> «f.name»Spec -> «f.output.toType»
		«f.name.toFirstLower»Func impl spec = impl spec
	'''
	
	private def dispatch writeFunction(FunctionDispatch f)
	''''''
	
	private def toType(Attribute att) {
		if (att.isMultiple)
			'''[«att.toRawType»]'''
		else
			att.toRawType.prefixSingleOptional(att.card)
	}
	
	private def toRawType(Attribute input) {
		input.typeCall.type.name.toDamlType	
	}
	
	private def prefixSingleOptional(CharSequence type, RosettaCardinality card) {
		if (card!==null && card.inf<1)
			'''Optional «type»'''
		else
			type
	}
	
	private def isMultiple(Attribute att) {
		val card = att.card
		if (card===null) return false;
		return ((card.isUnbounded || (card.inf > 1)) || (card.sup != 1));
  }
}