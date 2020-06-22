package com.regnosys.rosetta.generator.c_sharp.object

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import com.regnosys.rosetta.rosetta.RosettaClass
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Condition
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.HashMap
import java.util.List
import java.util.Map
import java.util.Set

import static com.regnosys.rosetta.generator.c_sharp.util.CSharpModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*

class CSharpModelObjectGenerator {

    @Inject
    extension RosettaExtensions
    @Inject
    extension CSharpModelObjectBoilerPlate
    @Inject
    extension CSharpMetaFieldGenerator
    
    static final String CLASSES_FILENAME = 'Types.cs'
    static final String INTERFACES_FILENAME = 'Interfaces.cs'
    static final String META_FILENAME = 'MetaTypes.cs'

    def dispatch Iterable<ExpandedAttribute> allExpandedAttributes(RosettaClass type) {
        type.allSuperTypes.expandedAttributes
    }

    def dispatch Iterable<ExpandedAttribute> allExpandedAttributes(Data type) {
        type.allSuperTypes.map[it.expandedAttributes].flatten
    }

    def dispatch String definition(RosettaClass element) {
        element.definition
    }

    def dispatch String definition(Data element) {
        element.definition
    }

    def Map<String, ? extends CharSequence> generate(Iterable<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes,
        String version) {
        val result = new HashMap

        val superTypes = rosettaClasses.map[superType].map[allSuperTypes].flatten.toSet

        val interfaces = superTypes.sortBy[name].generateInterfaces(version).replaceTabsWithSpaces
        result.put(com.regnosys.rosetta.generator.c_sharp.object.CSharpModelObjectGenerator.INTERFACES_FILENAME, interfaces)

        val classes = rosettaClasses.sortBy[name].generateClasses(superTypes, version).replaceTabsWithSpaces
        result.put(CLASSES_FILENAME, classes)

        val metaFields = rosettaClasses.sortBy[name].generateMetaFields(metaTypes, version).replaceTabsWithSpaces
        result.put(META_FILENAME, metaFields)

        //val objectMapper = generateObjectMapper(version)
        //result.put(SERIALIZATION_FILENAME, objectMapper)

        result;
    }

    /* 
     * 	private def generateAttribute(Data c, ExpandedAttribute attribute) {
     * 		if (attribute.enum && !attribute.hasMetas) {
     * 			// TODO: Sort out indentation!!!
     * 			if (attribute.singleOptional) {
     * '''@JsonDeserialize(contentAs = classOf[«attribute.type.toEnumAnnotationType».Value])
     *     @JsonCSharpEnumeration(classOf[«attribute.type.toEnumAnnotationType».Class])
     *     «attribute.toType» «attribute.toAttributeName»'''
     *             } else {
     * '''@JsonCSharpEnumeration(classOf[«attribute.type.toEnumAnnotationType».Class])
     *     «attribute.toType» «attribute.toAttributeName»'''
     *             }
     *         } else {
     *             '''«attribute.toType» «attribute.toAttributeName»'''
     *         }
     *     }

     * 	private def generateAttributes(Data c) {
     *         '''«FOR attribute : c.allExpandedAttributes SEPARATOR ',\n    '»«generateAttribute(c, attribute)»«ENDFOR»'''
     * 	}
     */
    private def generateAttributeComment(ExpandedAttribute attribute, Data c, Set<Data> superTypes) {
        '''
            «IF attribute.definition !== null && !attribute.definition.isEmpty»
«««             If attribute was defined in a parent interface, then it should inherit the documentation as well
                «IF attribute.enclosingType != c.name || superTypes.contains(c)»
                    /// <inheritdoc/>
                «ELSE»
                    /// <summary>
                    /// «attribute.definition»
                    /// </summary>
                «ENDIF»
            «ENDIF»
        '''
    }

    private def generateClasses(List<Data> rosettaClasses, Set<Data> superTypes, String version) {
        '''
            «fileComment(version)»
            
            #nullable enable // Allow nullable reference types
            
            namespace Org.Isda.Cdm
            {
                using System.Collections.Generic;
                using System.Linq;

                using Newtonsoft.Json;
                using Newtonsoft.Json.Converters;
                using NodaTime;
                using Org.Isda.Cdm.MetaFields;

            
                «FOR c : rosettaClasses SEPARATOR '\n'»
                    «classComment(c.definition)»
«««                 «IF isOneOf(c)»[OneOf]«ENDIF»
«««                 NB: C# 9: nNormal declaration should change to "public data class" to make immutable
«««                 and also remove the need to declare properties explicitly
                    public «IF isOneOf(c)»sealed «ENDIF»class «c.name»«generateParents(c, superTypes)»
                    {
                        [JsonConstructor]
                        public «c.name»(«FOR attribute : c.allExpandedAttributes SEPARATOR ', '»«attribute.toType» «attribute.toParamName»«ENDFOR»)
                        {
                            «FOR attribute : c.allExpandedAttributes»
                                «attribute.toPropertyName» = «attribute.toParamName»;
                            «ENDFOR»
                        }
                        
                        «FOR attribute : c.allExpandedAttributes SEPARATOR '\n'»
                            «generateAttributeComment(attribute, c, superTypes)»
                            «IF attribute.enum  && !attribute.hasMetas»[JsonConverter(typeof(StringEnumConverter))]«ENDIF»
«««                         NB: This could be converted to use { get; init; } in C# 9 (.NET 5), which would allow us to remove the constructor. 
                            public «attribute.toType» «attribute.toPropertyName» { get; }
                        «ENDFOR»
                        «FOR condition : c.conditions»
                            «generateConditionLogic(c, condition)»
                        «ENDFOR»
                    }
                «ENDFOR»
            }
        '''
    }
    
    private def isOneOf(Data rosettaClass) {
        !rosettaClass.conditions.filter[constraint.oneOf].isEmpty()
    }

    private def generateConditionLogic(Data c, Condition condition) {
        '''
            «IF condition.constraint !== null && condition.constraint.oneOf»«generateOneOfLogic(c)»«ENDIF»
        '''
    }

    private def generateOneOfLogic(Data c) {
        '''
            //val numberOfPopulatedFields = List(«FOR attribute : c.allExpandedAttributes SEPARATOR ', '»«attribute.toAttributeName»«ENDFOR»).flatten.length
            //require(numberOfPopulatedFields == 1)
        '''
    }

    private def generateParents(Data c, Set<Data> superTypes) {
        '''
«««         Implement interfaces associated with:
«««             super type, if it is defined.
«««             this class, if it is a super type.
            «IF c.superType !== null && superTypes.contains(c)» : «getInterfaceName(c)», «getInterfaceName(c.superType)»«ELSEIF c.superType !== null» : «getInterfaceName(c.superType)»«ELSEIF superTypes.contains(c)» : «getInterfaceName(c)»«ENDIF»
        '''
    }

    private def generateInterfaces(List<Data> rosettaClasses, String version) {
        '''
            «fileComment(version)»
            
            #nullable enable // Allow nullable reference types
            
            namespace Org.Isda.Cdm
            {
                using System.Collections.Generic;
                using System.Linq;
            
                using Newtonsoft.Json;
                using Newtonsoft.Json.Converters;
                using NodaTime;
                using Org.Isda.Cdm.MetaFields;
            
                «FOR c : rosettaClasses SEPARATOR '\n'»
                    «comment(c.definition)»
                    interface «getInterfaceName(c)»«IF c.superType !== null» : «getInterfaceName(c.superType)»«ENDIF»
                    {
                        «FOR attribute : c.expandedAttributes SEPARATOR '\n'»
                            «comment(attribute.definition)»
                            «attribute.toType» «attribute.toPropertyName» { get; }
                        «ENDFOR»
                    }
                «ENDFOR»
            }
        '''
    }

    private def getInterfaceName(Data c) {
        '''I«c.name»'''
    }
}
