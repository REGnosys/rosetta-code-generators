package com.regnosys.rosetta.generator.daml.enums

import com.google.inject.Inject
import com.regnosys.rosetta.generator.daml.object.DamlModelObjectBoilerPlate
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import java.util.ArrayList
import java.util.List

import static com.regnosys.rosetta.generator.daml.util.DamlModelGeneratorUtil.*
import java.util.Map
import java.util.HashMap

class DamlEnumGenerator {
	
	@Inject extension DamlModelObjectBoilerPlate
	
	static final String FILENAME = 'Org/Isda/Cdm/Enums.daml'
		
	def Map<String, ? extends CharSequence> generate(Iterable<RosettaEnumeration> rosettaEnums, String version) {
		val result = new HashMap
		val enums = rosettaEnums.sortBy[name].generateEnums(version).replaceTabsWithSpaces
		result.put(FILENAME,enums)
		return result;
	}

	def static toJavaEnumName(RosettaEnumeration enumeration, RosettaEnumValue rosettaEnumValue) {
		return enumeration.name + '.' + convertValues(rosettaEnumValue)
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
		daml 1.2
		
		«fileComment(version)»
		module Org.Isda.Cdm.Enums
		  ( module Org.Isda.Cdm.Enums ) where
		
		«FOR e : enums»
			«val allEnumValues = allEnumsValues(e)»
			«var i = 0»
			«classComment(e.definition)»
			data «e.name» 
			  «FOR value: allEnumValues»
			      «IF i++<1»=«ELSE»|«ENDIF» «e.name»_«convertValues(value)»«IF allEnumValues.size==1»()«ENDIF»
			      «methodComment(value.definition)»
			  «ENDFOR»
			    deriving (Eq, Ord, Show)
			
		«ENDFOR»
	'''
	
	def boolean anyValueHasSynonym(RosettaEnumeration enumeration) {
		enumeration.allEnumsValues.map[enumSynonyms].flatten.size > 0
	}
	
    def static convertValues(RosettaEnumValue enumValue) {
		return formatEnumName(enumValue.name)
	}
	
	def static String formatEnumName(String name) {
		return name
	}
}