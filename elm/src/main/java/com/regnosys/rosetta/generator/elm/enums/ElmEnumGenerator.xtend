package com.regnosys.rosetta.generator.elm.enums

import com.google.inject.Inject
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import java.util.ArrayList
import java.util.HashMap
import java.util.List
import java.util.Map

import com.regnosys.rosetta.generator.java.enums.EnumHelper
import java.nio.file.Files
import java.nio.file.Paths
import com.regnosys.rosetta.generator.elm.object.ElmModelObjectBoilerPlate
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
import java.util.Enumeration
import static com.regnosys.rosetta.generator.elm.util.ElmModelGeneratorUtil.*

class ElmEnumGenerator {
	
	
	@Inject extension RosettaExtensions
	@Inject extension ElmModelObjectBoilerPlate

	def Map<String, ? extends CharSequence> generate(String namespace, Iterable<RosettaEnumeration> enums, String version) {
		val result = new HashMap		
		
		val elm = enums.sortBy[name].generateElm(namespace, version).replaceTabsWithSpaces
		
		val folder = namespace.split("\\.").map[it.toFirstUpper].join('/')
		val fileName =  "Enum.elm"
		
		result.put(folder + '/' + fileName, elm)

		result;
	}
	
	private def generateElm(List<RosettaEnumeration> rosettaEnums, String namespace, String version) {
	'''	
	
	module «namespace.split("\\.").map[it.toFirstUpper].join(".")».Enum exposing (..)
	
	
	«fileComment(version)»	
	
	
	«FOR c : rosettaEnums»
		«classComment(c.definition)»
	type «c.name»
	    «FOR enumValue : c.allEnumValues»
	    «IF c.allEnumValues.toList.indexOf(enumValue) === 0»= «ELSE»| «ENDIF»	«enumValue.name.toFirstUpper»
	    «ENDFOR»
	
	«ENDFOR»
	'''}
		
	
	def Iterable<ExpandedAttribute> allExpandedAttributes(Data type){
		type.allSuperTypes.map[it.expandedAttributes].flatten
	}
	
	def String definition(Data element){
		element.definition
	}
}
