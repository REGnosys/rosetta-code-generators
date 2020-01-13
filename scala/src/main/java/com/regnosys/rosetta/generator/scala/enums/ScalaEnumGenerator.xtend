package com.regnosys.rosetta.generator.scala.enums

import com.google.inject.Inject
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import com.regnosys.rosetta.generator.scala.object.ScalaModelObjectBoilerPlate
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import java.util.ArrayList
import java.util.HashMap
import java.util.List
import java.util.Map

import static com.regnosys.rosetta.generator.scala.util.ScalaModelGeneratorUtil.*

class ScalaEnumGenerator {
	
	@Inject extension ScalaModelObjectBoilerPlate
	
	static final String FILENAME = 'Enums.scala'
		
	def Map<String, ? extends CharSequence> generate(Iterable<RosettaEnumeration> rosettaEnums, String version) {
		val result = new HashMap
		val enums = rosettaEnums.sortBy[name].generateEnums(version).replaceTabsWithSpaces
		result.put(FILENAME,enums)
		return result;
	}

	def static toJavaEnumName(RosettaEnumeration enumeration, RosettaEnumValue rosettaEnumValue) {
		return enumeration.name + '.' + EnumHelper.convertValues(rosettaEnumValue)
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

	private def generateEnums(List<RosettaEnumeration> enums, String version)  '''		
		«fileComment(version)»
		package org.isda.cdm
		
		«FOR e : enums»
			«val allEnumValues = allEnumsValues(e)»
			«comment(e.definition)»
			object «e.name» extends Enumeration {
				«FOR value: allEnumValues»
					«comment(value.definition)»
					val «EnumHelper.convertValues(value)» = Value
				«ENDFOR»
			}
			
		«ENDFOR»
	'''
	
	def boolean anyValueHasSynonym(RosettaEnumeration enumeration) {
		enumeration.allEnumsValues.map[enumSynonyms].flatten.size > 0
	}
}
