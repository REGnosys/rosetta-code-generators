package com.regnosys.rosetta.generator.typescript.enums

import com.google.inject.Inject
import com.regnosys.rosetta.generator.typescript.object.TypescriptModelObjectBoilerPlate
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import java.util.ArrayList
import java.util.HashMap
import java.util.List
import java.util.Map

import static com.regnosys.rosetta.generator.typescript.util.TypescriptModelGeneratorUtil.*
import com.regnosys.rosetta.generator.java.enums.EnumHelper

class TypescriptEnumGenerator {
	
	@Inject extension TypescriptModelObjectBoilerPlate
	
	static final String FILENAME = 'enums.ts'
		
	def Map<String, ? extends CharSequence> generate(Iterable<RosettaEnumeration> rosettaEnums, String version) {
		val result = new HashMap
		val enums = rosettaEnums.sortBy[name].generateEnums(version).replaceTabsWithSpaces
		result.put(FILENAME,enums)
		return result;
	}

	def static toJavaEnumName(RosettaEnumeration enumeration, RosettaEnumValue rosettaEnumValue) {
		return enumeration.name + '.' + EnumHelper.convertValue(rosettaEnumValue)
	}

	private def allEnumsValues(RosettaEnumeration enumeration) {
		val enumValues = new ArrayList
		var e = enumeration;

		while (e !== null) {
			e.enumValues.forEach[enumValues.add(it)]
			e = e.parent
		}
		return enumValues.sortBy[name];
	}

	private def generateEnums(List<RosettaEnumeration> enums, String version)  '''		
		«fileComment(version)»
		
		«FOR e : enums»
			«val allEnumValues = allEnumsValues(e)»
			«classComment(e.definition)»
			export enum «e.name» {
			«FOR value: allEnumValues SEPARATOR ","»
			
				«methodComment(value.definition)»
				«EnumHelper.convertValue(value)»
			«ENDFOR»
			}
		«ENDFOR»
	'''
	
	def boolean anyValueHasSynonym(RosettaEnumeration enumeration) {
		enumeration.allEnumsValues.map[enumSynonyms].flatten.size > 0
	}
}
