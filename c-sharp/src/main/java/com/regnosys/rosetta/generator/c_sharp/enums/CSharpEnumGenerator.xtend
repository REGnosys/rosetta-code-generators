package com.regnosys.rosetta.generator.c_sharp.enums

import com.google.inject.Inject
//import com.regnosys.rosetta.generator.java.enums.EnumHelper
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

    def boolean anyValueHasSynonym(List<RosettaEnumeration> enums) {
        !enums.filter[allEnumsValues.map[enumSynonyms].flatten.size > 0].isEmpty
    }

    def boolean anyValueHasDisplayName(RosettaEnumeration enumeration) {
        enumeration.allEnumsValues.exists[display !== null]
    }
    

    def Map<String, ? extends CharSequence> generate(Iterable<RosettaEnumeration> rosettaEnums, String version) {
        val result = new HashMap
        val enums = rosettaEnums.sortBy[name].generateEnums(version).replaceTabsWithSpaces
        result.put(FILENAME,enums)
        return result;
    }

    def static toCSharpEnumName(RosettaEnumValue rosettaEnumValue) {
        
        return rosettaEnumValue.name.prefixWithUnderscoreIfStartsWithNumber()
    }

    def static toCSharpEnumName(RosettaEnumeration enumeration, RosettaEnumValue rosettaEnumValue) {
        return enumeration.name + '.' + toCSharpEnumName(rosettaEnumValue)
    }

    private def generateEnums(List<RosettaEnumeration> enums, String version)
        // TODO: Handle synonyms via attribute??
        // TODO: Handle serialization to/from java style names via [EnumMember(Value = "<javaName>")]
        '''        
        «fileComment(version)»
        namespace Org.Isda.Cdm
        {
            «IF enums.anyValueHasSynonym»
                using Rosetta.Lib.Attributes;
                
            «ENDIF»
            «FOR e : enums SEPARATOR '\n'»
                «val allEnumValues = allEnumsValues(e)»
                «comment(e.definition)»
«««             TODO: These seem to be ignored in Java version «e.addAttributes»
                public enum «e.name»
                {
                    «FOR enumValue: allEnumValues SEPARATOR ",\n"»
                        «comment(enumValue.definition)»
                        «enumValue.addAttributes»
                        «toCSharpEnumName(enumValue)»
                    «ENDFOR»
                }
                «IF anyValueHasDisplayName(e)»
                
                public static partial class Extension
                {
                    public static string GetDisplayName(this «e.name» value)
                    {
                        return value switch
                        {
                        «FOR enumValue: allEnumValues»
                            «IF enumValue.display !== null»    «toCSharpEnumName(e, enumValue)» => "«enumValue.display»",«ENDIF»
                        «ENDFOR»
                            _ => nameof(value)
                        };
                    }
                }
                «ENDIF»
            «ENDFOR»
        }
    '''
    
    private def static String prefixWithUnderscoreIfStartsWithNumber(String name) {
        if (Character.isDigit(name.charAt(0)))
            return "_" + name
        else
            return name
    }

/*    private def addAttributes(RosettaEnumeration e) '''
    «FOR synonym : e.synonyms»
        «FOR source : synonym.sources»
            [RosettaSynonym(Value = "«synonym.getBody.getValues»", Source = "«source.getName»")]
        «ENDFOR»
    «ENDFOR»
    '''*/
    
    private def addAttributes(RosettaEnumValue e) '''
    «FOR synonym : e.enumSynonyms»
        «FOR source : synonym.sources»
            [RosettaSynonym(Value = "«synonym.synonymValue»", Source = "«source.getName»")]
        «ENDFOR»
    «ENDFOR»
    '''
}
