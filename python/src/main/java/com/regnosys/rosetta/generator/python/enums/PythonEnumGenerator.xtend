package com.regnosys.rosetta.generator.python.enums

import com.google.inject.Inject
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import com.regnosys.rosetta.generator.python.object.PythonModelObjectBoilerPlate
import com.regnosys.rosetta.generator.python.util.PythonModelGeneratorUtil
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaModel
import java.util.ArrayList
import java.util.HashMap
import java.util.Map

class PythonEnumGenerator {

	@Inject extension PythonModelObjectBoilerPlate
	
	@Inject
	PythonModelGeneratorUtil utils;
	
	

	def Map<String, ? extends CharSequence> generate(Iterable<RosettaEnumeration> rosettaEnums, String version) {
		val result = new HashMap
		for(RosettaEnumeration enum: rosettaEnums){
			val tr = enum.eContainer as RosettaModel
			val namespace = tr.name
			val enums = enum.generateEnums(version).replaceTabsWithSpaces
		
			val all = 
			'''
			from enum import Enum
			
			all = ['«enum.name»']
			  
			'''
			result.put(utils.toPyFileName(namespace, enum.name), all +enums)
		}
		return result;
	}

	private def allEnumsValues(RosettaEnumeration enumeration) {
		val enumValues = new ArrayList
		var e = enumeration;

		while (e !== null) {
			e.enumValues.forEach[enumValues.add(it)]
			e = e.superType
		}
		return enumValues.sortBy[name];
	}

	private def generateEnums(RosettaEnumeration enume, String version){

		'''
		«val allEnumValues = allEnumsValues(enume)»
		class «enume.name»(Enum):
			«IF enume.definition!==null»
			"""
			«enume.definition»
			"""
			«ENDIF»
			«IF allEnumValues.size()===0»
			pass
			«ELSE»
			«FOR value: allEnumValues SEPARATOR ''»
			«EnumHelper.convertValues(value)» = "«IF value.display !== null»«value.display»«ELSE»«EnumHelper.convertValues(value)»«ENDIF»"
			«IF value.definition!==null»
			"""
			«value.definition»
			"""
			«ENDIF»
			«ENDFOR»
			«ENDIF»
		'''
	}
}