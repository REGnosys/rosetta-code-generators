package com.regnosys.rosetta.generator.c_sharp.object

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import com.regnosys.rosetta.generator.c_sharp.serialization.CSharpObjectMapperGenerator
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
    @Inject
    extension CSharpObjectMapperGenerator

    static final String CLASSES_FILENAME = 'Types.cs'
    static final String TRAITS_FILENAME = 'Traits.cs'
    static final String META_FILENAME = 'MetaTypes.cs'
    static final String SERIALIZATION_FILENAME = 'Serialization.cs'

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

        val traits = superTypes.sortBy[name].generateTraits(version).replaceTabsWithSpaces
        result.put(TRAITS_FILENAME, traits)

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
                using NodaTime;
                using Org.Isda.Cdm.MetaFields;

            
                «FOR c : rosettaClasses SEPARATOR '\n'»
                    «classComment(c.definition)»
«««                    «IF isOneOf(c)»[OneOf]«ENDIF»
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
«««         Implement traits associated with:
«««             super type, if it is defined.
«««             this class, if it is a super type.
            «IF c.superType !== null && superTypes.contains(c)» : «getTraitName(c)», «getTraitName(c.superType)»«ELSEIF c.superType !== null» : «getTraitName(c.superType)»«ELSEIF superTypes.contains(c)» : «getTraitName(c)»«ENDIF»
        '''
    }

    private def generateTraits(List<Data> rosettaClasses, String version) {
        '''
            «fileComment(version)»
            
            #nullable enable // Allow nullable reference types
            
            namespace Org.Isda.Cdm
            {
                using System.Collections.Generic;
                using System.Linq;
            
                using Newtonsoft.Json;
                using NodaTime;
                using Org.Isda.Cdm.MetaFields;
            
                «FOR c : rosettaClasses SEPARATOR '\n'»
                    «comment(c.definition)»
                    interface «getTraitName(c)»«IF c.superType !== null» : «getTraitName(c.superType)»«ENDIF»
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

    private def getTraitName(Data c) {
        '''I«c.name»Trait'''
    }
}
