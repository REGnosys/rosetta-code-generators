package com.regnosys.rosetta.generator.elm.object

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.rosetta.RosettaMetaType
import java.util.List


import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*
import java.util.Map
import java.util.HashMap
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import java.util.Set
import com.google.common.collect.Lists
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaModel
import static com.regnosys.rosetta.generator.elm.util.ElmModelGeneratorUtil.*

class ElmModelObjectGenerator {

	@Inject extension RosettaExtensions
	@Inject extension ElmModelObjectBoilerPlate

	def Map<String, ? extends CharSequence> generate(String namespace, Iterable<Data> data, String version) {
		val result = new HashMap		
		
		val enumsToImport = data.map[attributes]
			.flatten
			.map[type]
			.filter(RosettaEnumeration).toList
		
		val elm = data.sortBy[name].generateElm(enumsToImport, namespace, version).replaceTabsWithSpaces
		
		val folder = namespace.split("\\.").map[it.toFirstUpper].join('/')
		val fileName =  "Type.elm"
		
		result.put(folder + '/' + fileName, elm)

		result;
	}
	
	
	private def generateElm(List<Data> rosettaClasses, List<RosettaEnumeration> enumsToImport, String namespace, String version) {
	'''	
	
	module «namespace.split("\\.").map[it.toFirstUpper].join(".")».Type exposing (..)
	
	import Morphir.SDK.LocalDate exposing (LocalDate)
	import Morphir.SDK.LocalTime exposing (LocalTime)
	import Com.Rosetta.Model.Type exposing (ZonedDateTime)
	import Com.Rosetta.Model.Type exposing (Date)
	
	«FOR enumImport : enumsToImport»
		import «(enumImport.eContainer as RosettaModel).name.split("\\.").map[it.toFirstUpper].join(".")».Enum exposing («enumImport.name»)
	«ENDFOR»
	
	
	«fileComment(version)»	
	
	
	«FOR c : rosettaClasses»
		«classComment(c.definition)»
	type alias «c.name» =
	    «FOR attribute : c.attributes»
	    «IF c.attributes.indexOf(attribute) === 0»{ «ELSE», «ENDIF»	«attribute.toAttributeName» : «attribute.toType» «methodComment(attribute.definition)»
	    «ENDFOR»
	    }
	«ENDFOR»
	'''}
		
	
	def Iterable<ExpandedAttribute> allExpandedAttributes(Data type){
		type.allSuperTypes.map[it.expandedAttributes].flatten
	}
	
	def String definition(Data element){
		element.definition
	}

}
