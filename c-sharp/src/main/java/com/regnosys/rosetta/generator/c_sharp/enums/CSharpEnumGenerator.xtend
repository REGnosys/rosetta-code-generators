package com.regnosys.rosetta.generator.c_sharp.enums

import com.google.inject.Inject
import com.regnosys.rosetta.generator.c_sharp.object.CSharpModelObjectBoilerPlate
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import java.util.ArrayList
import java.util.HashMap
import java.util.List
import java.util.Map

import static com.regnosys.rosetta.generator.c_sharp.util.CSharpModelGeneratorUtil.*

class CSharpEnumGenerator {

    @Inject
    extension CSharpModelObjectBoilerPlate

    static final String FILENAME = 'Enums.cs'
    public static final String ENUM_SUFFIX = "Enum"

    /*  NB: Synonyms at enumeration level are not supported by Rosetta  
     *  private def addAttributes(RosettaEnumeration e) '''
     *     «FOR synonym : e.synonyms»
     *         «FOR source : synonym.sources»
     *             [RosettaSynonym(Value = "«synonym.getBody.getValues»", Source = "«source.getName»")]
     *         «ENDFOR»
     *     «ENDFOR»
     '''*/

    private def addAttributes(RosettaEnumValue e) '''
        «FOR synonym : e.enumSynonyms»
            «FOR source : synonym.sources»
                [RosettaSynonym(Value = "«synonym.synonymValue»", Source = "«source.getName»")]
            «ENDFOR»
        «ENDFOR»
«««     Output JSON and description which matches display name if specified, else Java format
        «val javaName = EnumHelper.formatEnumName(e.name)»
        «IF e.display !== null»[EnumMember(Value = "«e.display»")]«ELSEIF javaName != toCSharpEnumName(e)»[EnumMember(Value = "«javaName»")]«ENDIF»
    '''

    private def allEnumsValues(RosettaEnumeration enumeration) {
        val enumValues = new ArrayList
        var e = enumeration;

        while (e !== null) {
            e.enumValues.forEach[enumValues.add(it)]
            e = e.parent
        }
        return enumValues.sortBy[name];
    }

    private static def toCSharpName(RosettaEnumeration e) {
        toCSharpName(e.name, false)
    }

    static def toCSharpName(String name, boolean qualify) {
        var enumName = name

        if (name.endsWith(ENUM_SUFFIX)) {
            enumName = name.substring(0, name.length - ENUM_SUFFIX.length)
        }
        if (qualify) {
            enumName = "Enums." + enumName
        }
        return enumName
    }

    static def toCSharpMetaName(String name) {
        return name
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
        result.put(FILENAME, enums)
        return result;
    }
    

    private def generateEnums(List<RosettaEnumeration> enums, String version) // TODO: Handle synonyms via attribute??
    '''        
        «fileComment(version)»
        namespace Org.Isda.Cdm.Enums
        {
            «IF enums.anyValueHasSynonym»
                using System.Runtime.Serialization;
                using Rosetta.Lib.Attributes;
                
            «ENDIF»
            «FOR e : enums SEPARATOR '\n'»
            «val allEnumValues = allEnumsValues(e)»
            «comment(e.definition)»
            [CdmName("«e.name»")]
«««             TODO: These seem to be ignored in Java version «e.addAttributes»
            public enum «e.toCSharpName»
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
                    public static string GetDisplayName(this «e.toCSharpName» value)
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

    def static toCSharpEnumName(RosettaEnumValue rosettaEnumValue) {
        return rosettaEnumValue.name.toFirstUpper
    }

    def static toCSharpEnumName(RosettaEnumeration enumeration, RosettaEnumValue rosettaEnumValue) {
        return enumeration.toCSharpName + '.' + toCSharpEnumName(rosettaEnumValue)
    }

}
