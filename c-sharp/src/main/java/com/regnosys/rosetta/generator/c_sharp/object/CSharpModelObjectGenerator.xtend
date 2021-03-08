package com.regnosys.rosetta.generator.c_sharp.object

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import com.regnosys.rosetta.generator.object.ExpandedType
import com.regnosys.rosetta.generator.c_sharp.object.CSharpValidatorsGenerator
import com.regnosys.rosetta.generator.c_sharp.rule.CSharpChoiceRuleGenerator
import com.regnosys.rosetta.generator.c_sharp.rule.CSharpDataRuleGenerator
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.RosettaNamed
import com.regnosys.rosetta.rosetta.simple.Condition
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.Arrays
import java.util.HashMap
import java.util.List
import java.util.Map
import java.util.Set

import static com.regnosys.rosetta.generator.c_sharp.util.CSharpModelGeneratorUtil.*
import static extension com.regnosys.rosetta.generator.c_sharp.util.CSharpTranslator.*

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*

class CSharpModelObjectGenerator {

    @Inject
    extension RosettaExtensions

    @Inject
    extension CSharpModelObjectBoilerPlate

    @Inject
    extension CSharpMetaFieldGenerator

    @Inject
    extension CSharpChoiceRuleGenerator

    @Inject
    extension CSharpDataRuleGenerator
    
    @Inject
    extension CSharpValidatorsGenerator

    static final String ASSEMBLY_INFO_FILENAME = 'Properties/AssemblyInfo.cs'
    static final String CLASSES_FILENAME = 'Types.cs'
    static final String INTERFACES_FILENAME = 'Interfaces.cs'
    static final String META_FILENAME = 'MetaTypes.cs'
    static final String META_FIELD_FILENAME = 'MetaFieldTypes.cs'
    static final String DATA_RULES_FILENAME = "DataRules.cs"
    static final String CHOICE_RULES_FILENAME = "ChoiceRules.cs"
    static final String VALIDATORS_FILENAME = "Validators.cs"

    def Iterable<ExpandedAttribute> allExpandedAttributes(Data type) {
        type.allSuperTypes.map[it.expandedAttributes].flatten
    }

    @org.eclipse.xtend.lib.annotations.Data
    static class ClassRule {
        String className;
        String ruleName;
    }

    private def List<ClassRule> conditionRules(Data d, List<Condition> elements, (Condition)=>boolean filter) {
        return elements.filter(filter).map[new ClassRule((it.eContainer as RosettaNamed).getName, it.conditionName(d))].toList
    }

    def String definition(Data element) {
        element.definition
    }

    def Map<String, ? extends CharSequence> generate(Iterable<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes,
        String version, CSharpCodeInfo cSharpCodeInfo) {
        val result = new HashMap

        val superTypes = rosettaClasses
                    .map[superType]
                    .map[allSuperTypes].flatten
                    .toSet

        val interfaces = superTypes.sortBy[name].generateInterfaces(version).replaceTabsWithSpaces
        result.put(com.regnosys.rosetta.generator.c_sharp.object.CSharpModelObjectGenerator.INTERFACES_FILENAME, interfaces)

        val sortedClasses = rosettaClasses.sortBy[name]
        val classes = sortedClasses.generateClasses(superTypes, version, cSharpCodeInfo.getCSharpVersion).replaceTabsWithSpaces
        result.put(CLASSES_FILENAME, classes)

        val metaClasses = sortedClasses.generateMetaClasses(superTypes, version, cSharpCodeInfo.getCSharpVersion).replaceTabsWithSpaces
        result.put(META_FILENAME, metaClasses)

        val metaFields = sortedClasses.generateMetaFields(metaTypes, version).replaceTabsWithSpaces
        result.put(META_FIELD_FILENAME, metaFields)

        val choiceRules = sortedClasses.generateChoiceRules(version).replaceTabsWithSpaces
        result.put(CHOICE_RULES_FILENAME, choiceRules)
        
        val dataRules = sortedClasses.generateDataRules(version).replaceTabsWithSpaces
        result.put(DATA_RULES_FILENAME, dataRules)

        val validators = sortedClasses.generateValidators(version).replaceTabsWithSpaces
        result.put(VALIDATORS_FILENAME, validators)

        result.put(ASSEMBLY_INFO_FILENAME, generateAssemblyInfo(getAssemblyVersion(version), cSharpCodeInfo.getDotNetVersion))

        result;
    }

    private def generateAssemblyInfo(String version, String dotnetVersion) {
        '''
        using System.Reflection;

        [assembly: AssemblyTitle("Org.Isda.Cdm")]
        [assembly: AssemblyDescription("«dotnetVersion» Implementation of ISDA/CDM")]
        [assembly: AssemblyCompany("ISDA.org")]
        [assembly: AssemblyProduct("CDM")]
        [assembly: AssemblyCopyright("Copyright © ISDA «getYear»")]
        [assembly: AssemblyTrademark("CDM")]

        [assembly: AssemblyVersion("«version»")]
        '''
    }

    private def generateAttributeComment(ExpandedAttribute attribute, Data c, Set<Data> superTypes) {
        '''
            «IF attribute.definition !== null && !attribute.definition.isEmpty»
«««             If attribute was defined in a parent interface, then it should inherit the documentation as well
                «IF attribute.enclosingType != c.name || superTypes.contains(c)»
                    /// <inheritdoc/>
                «ELSE»
                    «comment(attribute.definition)»
                «ENDIF»
            «ENDIF»
        '''
    }

    private def generateClasses(List<Data> rosettaClasses, Set<Data> superTypes, String version, int cSharpVersion) {
        '''
            «fileComment(version)»
            [assembly: Rosetta.Lib.Attributes.CdmVersion("«version»")]
            
            #nullable enable // Allow nullable reference types
            
            namespace Org.Isda.Cdm
            {
                using System.Collections.Generic;

                using Newtonsoft.Json;
                using Newtonsoft.Json.Converters;
            
                using NodaTime;
            
                using Rosetta.Lib;
                using Rosetta.Lib.Attributes;
                using Rosetta.Lib.Meta;
                using Rosetta.Lib.Validation;
            
                using Org.Isda.Cdm.Meta;
                using Org.Isda.Cdm.MetaFields;
                using _MetaFields = Org.Isda.Cdm.MetaFields.MetaFields;
                
                «FOR c : rosettaClasses SEPARATOR '\n'»
                    «val allExpandedAttributes = c.allExpandedAttributes»
«««                     Filter out invalid types to prevent compilation errors
                    «val expandedAttributes = allExpandedAttributes.filter[!isMissingType]»
«««                 Discriminated unions are not scheduled to be added until C# 10, so use a sealed class with all optional fields for the moment.
«««                 Use of one-of condtion on a derived class is not properly defined, so mark it as an error and ignore. 
                    «val isChild = c.superType !== null»
                    «val isOneOf = isOneOf(c) && !isChild»
                    «var properties = if (isOneOf) getOneOfProperty(cSharpVersion) else " { get; }"»
                    «classComment(c.definition)»
                    «IF isOneOf»[OneOf]«ELSEIF isOneOf(c)»// ERROR: [OneOf] cannot be used on a derived class«ENDIF»
                    «val metaType = 'IRosettaMetaData<' + c.name +'>'»
                    public «IF isOneOf»«getOneOfType(cSharpVersion)»«ELSE»class«ENDIF» «c.name» : «generateParents(c, superTypes, cSharpVersion)»
                    {
                        private static readonly «metaType» metaData = new «c.name»Meta();
                        
                        «IF !isOneOf»
                        [JsonConstructor]
                        public «c.name»(«FOR attribute : expandedAttributes SEPARATOR ', '»«attribute.toType» «attribute.toParamName»«ENDFOR»)
                        {
                            «FOR attribute : expandedAttributes»
                                «attribute.toPropertyName» = «attribute.toParamName»;
                            «ENDFOR»
                        }
                        
                        «ENDIF»
                        /// <inheritdoc />
                        [JsonIgnore]
                        public override «metaType» MetaData => metaData;
                        
                        «FOR attribute : allExpandedAttributes SEPARATOR '\n'»
                            «generateAttributeComment(attribute, c, superTypes)»
                            «IF attribute.enum  && !attribute.hasMetas»[JsonConverter(typeof(StringEnumConverter))]«ELSEIF attribute.getType.isDate && !attribute.hasMetas»[JsonConverter(typeof(Rosetta.Lib.LocalDateConverter))]«ENDIF»
                            «IF attribute.matchesEnclosingType»[JsonProperty(PropertyName = "«attribute.toJsonName»")]«ENDIF»
«««                         NB: This property definition could be converted to use { get; init; } in C# 9 (.NET 5), which would allow us to remove the constructor.
«««                         During testing many types are not parsed correctly by Rosetta, so comment them out to create compilable code
                            «IF attribute.isMissingType»// MISSING «ENDIF»public «attribute.toType(isOneOf)» «attribute.toPropertyName»«properties»
                        «ENDFOR»
                        «FOR condition : c.conditions»
                            «generateConditionLogic(c, condition)»
                        «ENDFOR»
                    }
                «ENDFOR»
            }
        '''
    }
    
    private def generateMetaClasses(List<Data> rosettaClasses, Set<Data> superTypes, String version, int cSharpVersion) {
        '''
            «fileComment(version)»
            namespace Org.Isda.Cdm.Meta
            {
                using System.Collections.Generic;

                using Rosetta.Lib;
                using Rosetta.Lib.Attributes;
                using Rosetta.Lib.Meta;
                using Rosetta.Lib.Validation;
                
                using Org.Isda.Cdm.Validation.ChoiceRule;
                using Org.Isda.Cdm.Validation.DataRule;
                
                «FOR c : rosettaClasses SEPARATOR '\n'»
                    /// <summary>
                    /// MetaData definition for «c.name»
                    /// </summary>
                    [RosettaMeta(typeof(«c.name»))]
                    public class «c.name»Meta : IRosettaMetaData<«c.name»>
                    {
                        public IEnumerable<IValidator<«c.name»>> DataRules {
                            get {
                                «FOR r : conditionRules(c, c.conditions)[!isChoiceRuleCondition]»
                                    yield return new «CSharpDataRuleGenerator.dataRuleClassName(r.ruleName)»();
«««                             TODO: Sort out package
«««                             yield return new «javaNames.packages.model.dataRule.name».«CSharpDataRuleGenerator.dataRuleClassName(r.ruleName)»();
                                «ENDFOR»
                                yield break;
                            }
                        }
                    
                        public IEnumerable<IValidator<«c.name»>> ChoiceRuleValidators {
                            get {
                                «FOR r : conditionRules(c, c.conditions)[isChoiceRuleCondition]»
                                    yield return new «CSharpChoiceRuleGenerator.choiceRuleClassName(r.ruleName)»();
«««                             TODO: Sort out package
«««                                    yield return new «javaNames.packages.model.choiceRule.name».«CSharpChoiceRuleGenerator.choiceRuleClassName(r.ruleName)»();
                                «ENDFOR»
                                yield break;
                            }
                        }
                        
                        public IValidatorWithArg<«c.name», string> OnlyExistsValidator => new «c.name»OnlyExistsValidator();

                        public IValidator<«c.name»> Validator => new «c.name»Validator();
                    }
                «ENDFOR»
            }
        '''
    }

    static def getAssemblyVersion(String version) {
        // Take the first three numbers from the version string, which could be "0.0.0.master".
        return String.join(".", Arrays.copyOfRange(version.split("\\."), 0, 3))
    }

    private def getOneOfProperty(int cSharpVersion) '''
            «IF cSharpVersion >= 9» { get; init; }«ELSE» { get; set; }«ENDIF»'''

    private def getOneOfType(int cSharpVersion) '''
            «IF cSharpVersion >= 9»sealed record«ELSE»sealed class«ENDIF»'''

    private def isOneOf(Data rosettaClass) {
        rosettaClass.conditions !== null && !rosettaClass.conditions.filter[constraint?.oneOf].isEmpty()
    }

    private def generateConditionLogic(Data c, Condition condition) {
        /*
        '''
            «IF condition.constraint !== null && condition.constraint.oneOf»«generateOneOfLogic(c)»«ENDIF»
        ''' */
    }

    private def generateParents(Data c, Set<Data> superTypes, int cSharpVersion) {
        '''
«««         Implement interfaces associated with:
«««             super type, if it is defined.
«««             this class, if it is a super type.
«««         Abstract base class has a different name if oneOf, since they are implemented as records instead of classes.
            «val isChild = c.superType !== null»
            «val isOneOf = isOneOf(c) && !isChild»        «»
            AbstractRosettaModel«IF isOneOf && cSharpVersion >= 9»Record«ELSE»Object«ENDIF»<«c.name»>«IF superTypes.contains(c)», «getInterfaceName(c)»«ENDIF»«IF isChild», «getInterfaceName(c.superType)»«ENDIF»
        '''
    }

    private def generateInterfaces(List<Data> rosettaClasses, String version) {
        '''
            «fileComment(version)»
            
            #nullable enable // Allow nullable reference types
            
            namespace Org.Isda.Cdm
            {
                using System.Collections.Generic;
            
                using Newtonsoft.Json;
                using Newtonsoft.Json.Converters;
            
                using NodaTime;
            
                using Org.Isda.Cdm.Meta;
                using Org.Isda.Cdm.MetaFields;
                using _MetaFields = Org.Isda.Cdm.MetaFields.MetaFields;
            
                «FOR c : rosettaClasses SEPARATOR '\n'»
                    «comment(c.definition)»
                    interface «getInterfaceName(c)»«IF c.superType !== null» : «getInterfaceName(c.superType)»«ENDIF»
                    {
                        «FOR attribute : c.expandedAttributes SEPARATOR '\n'»
                            «comment(attribute.definition)»
«««                         During testing many types are not parsed correctly by Rosetta, so comment them out to create compilable code
                            «IF attribute.isMissingType»// MISSING «ENDIF»«attribute.toType» «attribute.toPropertyName» { get; }
                        «ENDFOR»
                    }
                «ENDFOR»
            }
        '''
    }

    private def getInterfaceName(Data c) {
        '''I«c.name»'''
    }

    private def getYear() {
        java.time.Year.now().getValue()
    }
}
