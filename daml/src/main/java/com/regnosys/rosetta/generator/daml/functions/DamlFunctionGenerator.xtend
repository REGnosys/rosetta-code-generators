package com.regnosys.rosetta.generator.daml.functions

import com.regnosys.rosetta.generator.daml.object.DamlModelObjectBoilerPlate
import com.regnosys.rosetta.rosetta.RosettaCardinality
import com.regnosys.rosetta.rosetta.RosettaNamed
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Function
import com.regnosys.rosetta.rosetta.simple.FunctionDispatch
import java.util.HashMap
import java.util.List
import java.util.Map
import jakarta.inject.Inject

import static com.regnosys.rosetta.generator.daml.util.DamlModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.daml.util.DamlTranslator.toDamlType

class DamlFunctionGenerator {
	@Inject extension DamlModelObjectBoilerPlate
			
	def Map<String, ? extends CharSequence> generate(Iterable<Function> rosettaFunctions, String version) {
		val functionsByNamespace = rosettaFunctions.groupBy[model.name.split("\\.").first]
		
		val result = new HashMap
		functionsByNamespace.forEach[k,v|
			val namespace = k.toFirstUpper
			val functions = v.sortBy[name].generateFunctions(namespace, version).replaceTabsWithSpaces
			result.put('''Org/Isda/«namespace»/Functions.daml''',functions)
		]
		
		return result;
	}
	
	private def generateFunctions(List<Function> functions, String namespace, String version)  '''
		daml 1.2
		
		«fileComment(version)»
		module Org.Isda.«namespace».Functions
		  ( module Org.Isda.«namespace».Functions ) where
		
		import Org.Isda.«namespace».Classes
		import Org.Isda.«namespace».Enums
		import Com.Regnosys.Meta.DateTime
		import Com.Regnosys.Meta.ZonedDateTime
		import Com.Regnosys.Meta.MetaClasses hiding (Reference)
		import Com.Regnosys.Meta.MetaFields
		«IF namespace=="Cdm"»
			import Org.Isda.Fpml.Classes
			import Org.Isda.Fpml.Enums
		«ENDIF»
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
		input.typeCall.type.toDamlType	
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