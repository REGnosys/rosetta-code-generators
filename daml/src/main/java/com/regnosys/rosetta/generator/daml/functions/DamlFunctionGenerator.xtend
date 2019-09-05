package com.regnosys.rosetta.generator.daml.functions

import com.regnosys.rosetta.generator.daml.object.DamlModelObjectBoilerPlate
import com.regnosys.rosetta.rosetta.RosettaFunction
import com.regnosys.rosetta.rosetta.RosettaFunctionInput
import java.util.HashMap
import java.util.List
import java.util.Map
import javax.inject.Inject

import static com.regnosys.rosetta.generator.daml.util.DamlModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.daml.util.DamlTranslator.toDamlType
import com.regnosys.rosetta.rosetta.RosettaCardinality

class DamlFunctionGenerator {
	@Inject extension DamlModelObjectBoilerPlate
	
	static final String FILENAME = 'Org/Isda/Cdm/EFunctions.daml'
		
	def Map<String, ? extends CharSequence> generate(Iterable<RosettaFunction> rosettaFunctions, String version) {
		val result = new HashMap
		val functions = rosettaFunctions.sortBy[name].generateFunctions(version).replaceTabsWithSpaces
		result.put(FILENAME,functions)
		return result;
	}
	
	private def generateFunctions(List<RosettaFunction> functions, String version)  '''
		daml 1.2
		
		«fileComment(version)»
		module Org.Isda.Cdm.Functions
		  ( module Org.Isda.Cdm.Functions ) where
		
		import Org.Isda.Cdm.Classes
		import Org.Isda.Cdm.Enums
		import Org.Isda.Cdm.ZonedDateTime
		import Org.Isda.Cdm.MetaClasses
		import Org.Isda.Cdm.MetaFields
		import Prelude hiding (Party, exercise, id, product, agreement)
		
		«FOR f : functions»
			«classComment("Function argument object definition for "+f.name)»
			data «f.name.toFirstUpper»Spec = «f.name.toFirstUpper»Spec with
			    «FOR input : f.inputs»
			        «input.name» : «input.toType»
			    «ENDFOR»
			    deriving (Eq, Ord, Show)
			
			fun«f.name»Spec : («f.name» -> «f.output.toType») «f.name» -> «f.output.toType»
			    fun«f.name»Spec impl spec = impl spec
		«ENDFOR»
	'''
	
	private def toType(RosettaFunctionInput input) {
		if (input.card.sup>1)
			'''[«input.toRawType»]'''
		else
			input.toRawType.prefixSingleOptional(input.card)
	}
	
	private def toRawType(RosettaFunctionInput input) {
		input.type.name.toDamlType	
	}
	
	private def prefixSingleOptional(CharSequence type, RosettaCardinality card) {
		if (card.inf<1)
			'''Optional «type»'''
		else
			type
	}
}