package com.regnosys.rosetta.generator.python.enums

import com.google.inject.Inject
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import com.regnosys.rosetta.generator.python.object.PythonModelObjectBoilerPlate
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import java.util.ArrayList
import java.util.HashMap
import java.util.List
import java.util.Map


class PythonEnumGenerator {

    @Inject extension PythonModelObjectBoilerPlate

    static final String FILENAME = 'Enums.kt'

    def Map<String, ? extends CharSequence> generate(Iterable<RosettaEnumeration> rosettaEnums, String version) {
        val result = new HashMap
        if(rosettaEnums.size>0){
        	val enums = rosettaEnums.sortBy[name].generateEnums(version).replaceTabsWithSpaces
        	result.put(FILENAME,enums)
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

    private def generateEnums(List<RosettaEnumeration> enums, String version){
        val rosettaClasses = enums.map[name].map["'"+it+"'"]
	    '''
	    from enum import Enum

	    «FOR e : enums SEPARATOR "\n"»
	    «val allEnumValues = allEnumsValues(e)»
	    class «e.name»(Enum):
	        «IF e.definition!==null»
	        """
	        «e.definition»
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
	    «ENDFOR»
	    '''
	}
}