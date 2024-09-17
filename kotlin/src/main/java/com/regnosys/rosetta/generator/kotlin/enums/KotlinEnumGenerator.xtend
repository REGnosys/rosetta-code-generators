package com.regnosys.rosetta.generator.kotlin.enums

import com.google.inject.Inject
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import com.regnosys.rosetta.generator.kotlin.object.KotlinModelObjectBoilerPlate
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import java.util.ArrayList
import java.util.HashMap
import java.util.List
import java.util.Map

import static com.regnosys.rosetta.generator.kotlin.util.KotlinModelGeneratorUtil.*

class KotlinEnumGenerator {

    @Inject extension KotlinModelObjectBoilerPlate

    static final String FILENAME = 'Enums.kt'

    def Map<String, ? extends CharSequence> generate(Iterable<RosettaEnumeration> rosettaEnums, String version) {
        val result = new HashMap
        val enums = rosettaEnums.sortBy[name].generateEnums(version).replaceTabsWithSpaces
        result.put(FILENAME,enums)
        return result;
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

    private def generateEnums(List<RosettaEnumeration> enums, String version)
		'''
		«fileComment(version)»
		package org.isda.cdm.kotlin
		
		import kotlinx.serialization.*
		
		«FOR e : enums SEPARATOR "\n"»
			«val allEnumValues = allEnumsValues(e)»
			«comment(e.definition)»
			@Serializable
			enum class «e.name» {
				«FOR value: allEnumValues SEPARATOR ','»
					«comment(value.definition)»
					@SerialName("«IF value.display !== null»«value.display»«ELSE»«EnumHelper.convertValue(value)»«ENDIF»")
					«EnumHelper.convertValue(value)»
				«ENDFOR»
				;
			}
		«ENDFOR»
		'''
}