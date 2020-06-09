package com.regnosys.rosetta.generator.c_sharp.enums

import com.google.inject.Inject
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import com.regnosys.rosetta.generator.c_sharp.object.CSharpModelObjectBoilerPlate
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import java.util.ArrayList
import java.util.HashMap
import java.util.List
import java.util.Map

import static com.regnosys.rosetta.generator.c_sharp.util.CSharpModelGeneratorUtil.*

class CSharpEnumGenerator {
    
    @Inject extension CSharpModelObjectBoilerPlate
    
    static final String FILENAME = 'Enums.cs'
        
    private def allEnumsValues(RosettaEnumeration enumeration) {
        val enumValues = new ArrayList
        var e = enumeration;

        while (e !== null) {
            e.enumValues.forEach[enumValues.add(it)]
            e = e.superType
        }
        return enumValues.sortBy[name];
    }

    def boolean anyValueHasSynonym(RosettaEnumeration enumeration) {
        enumeration.allEnumsValues.map[enumSynonyms].flatten.size > 0
    }

    def Map<String, ? extends CharSequence> generate(Iterable<RosettaEnumeration> rosettaEnums, String version) {
        val result = new HashMap
        val enums = rosettaEnums.sortBy[name].generateEnums(version).replaceTabsWithSpaces
        result.put(FILENAME,enums)
        return result;
    }

    def static toJavaEnumName(RosettaEnumeration enumeration, RosettaEnumValue rosettaEnumValue) {
        return enumeration.name + '.' + EnumHelper.convertValues(rosettaEnumValue)
    }

    // TODO: What is value.display????
    private def generateEnums(List<RosettaEnumeration> enums, String version)  '''        
        «fileComment(version)»
        namespace Org.Isda.Cdm
        {
            «FOR e : enums SEPARATOR '\n'»
                «val allEnumValues = allEnumsValues(e)»
                «comment(e.definition)»
                public enum «e.name»
                {
                    «FOR value: allEnumValues SEPARATOR ",\n"»
                        «comment(value.definition)»
                        «EnumHelper.convertValues(value)»«IF value.display !== null»("«value.display»")«ENDIF»
                    «ENDFOR»
                }
            «ENDFOR»
        }
    '''
}
