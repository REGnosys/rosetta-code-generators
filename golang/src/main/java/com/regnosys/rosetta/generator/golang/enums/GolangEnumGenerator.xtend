package com.regnosys.rosetta.generator.golang.enums

import com.google.inject.Inject
import com.regnosys.rosetta.generator.golang.object.GolangModelObjectBoilerPlate
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import java.util.ArrayList
import java.util.HashMap
import java.util.List
import java.util.Map

import static com.regnosys.rosetta.generator.golang.util.GolangModelGeneratorUtil.*
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import java.nio.file.Files
import java.nio.file.Paths

class GolangEnumGenerator {
	
	@Inject extension GolangModelObjectBoilerPlate
	
	static final String FILENAME = 'enums.go'
	static final String FOLDERNAME = 'org_isda_cdm'
		
	
	def Map<String, ? extends CharSequence>generate(Iterable<RosettaEnumeration> rosettaEnums, String version) {
		val result = new HashMap
		val enumTypes = rosettaEnums.sortBy[name].generateEnumTypes(version)
		result.put(FOLDERNAME+"/"+FILENAME,enumTypes)
		result.putAll(generateEnumVals(rosettaEnums.sortBy[name], version))
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

	
	private def generateEnumTypes(List<RosettaEnumeration> enums, String version){
		return '''		
		package org_isda_cdm
		
		«fileComment(version)»			
		
		«FOR e : enums»			
			«classComment(e.definition)»
			type «e.name» int			
		«ENDFOR»
	'''
		
	}
	
	private def generateEnumVals(List<RosettaEnumeration> enums, String version){
		val dictionary = new HashMap<String, String>
		for (e: enums){
			val eString = '''		
		«fileComment(version)»			
			package «e.name»
			import . "org_isda_cdm"
			«val allEnumValues = allEnumsValues(e)»
			«classComment(e.definition)»
			
			const (
			«FOR value: allEnumValues»
				«methodComment(value.definition)»
				«EnumHelper.convertValue(value)» «e.name» = iota + 1
			«ENDFOR»
			)		
		'''.replaceTabsWithSpaces
		val enumName = FOLDERNAME+"/"+ e.name+"/"+e.name+".go"		
		dictionary.put(enumName, eString)
		}		
		return dictionary		
	}
	
	
	def boolean anyValueHasSynonym(RosettaEnumeration enumeration) {
		enumeration.allEnumsValues.map[enumSynonyms].flatten.size > 0
	}
}
