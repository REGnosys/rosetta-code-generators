package com.regnosys.rosetta.generator.c_sharp.rule

import com.google.common.base.CaseFormat
import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.rosetta.simple.Condition
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.simple.Necessity
import java.util.List
import org.eclipse.xtend2.lib.StringConcatenationClient

import static com.regnosys.rosetta.generator.c_sharp.util.CSharpModelGeneratorUtil.*
import com.regnosys.rosetta.generator.c_sharp.expression.ExpressionGenerator
import com.regnosys.rosetta.rosetta.RosettaType

class CSharpChoiceRuleGenerator {
    @Inject ExpressionGenerator expressionHandler
    @Inject extension RosettaExtensions

    def generateChoiceRules(List<Data> rosettaClasses, String version) {
        '''
        «fileComment(version)»
        namespace Org.Isda.Cdm.Validation.ChoiceRule
        {
            using System.Collections.Generic;
            
            using Org.Isda.Cdm;
            
            using Rosetta.Lib.Attributes;
            using Rosetta.Lib.Validation;
            
        «FOR rosettaClass : rosettaClasses»
            «FOR c : rosettaClass.conditions»
                «IF c.isChoiceRuleCondition»«c.choiceRuleClassBody(rosettaClass, version)»«ENDIF»
            «ENDFOR»
        «ENDFOR»
        }
        '''
    }
    
    private def StringConcatenationClient choiceRuleClassBody(Condition rule, Data data /*, JavaNames javaName*/, String version)  {
        val rosettaClass = rule.eContainer as RosettaType
        val clazz = data.name
        val varName = clazz.toFirstLower;
        val ruleName = rule.conditionName(data)
        val className = choiceRuleClassName(rule.conditionName(data))
        val usedAttributes = if(rule.constraint.isOneOf) data.allAttributes else rule.constraint.attributes // TODO multi choice rules? 
        val validationType = if(rule.constraint.isOneOf || rule.constraint.necessity === Necessity.REQUIRED) 'RequiredChoiceRuleValidationMethod' else 'OptionalChoiceRuleValidationMethod'
        '''
            «»
                «comment(rule.definition)»
                [RosettaChoiceRule("«ruleName»")]
                public class «choiceRuleClassName(className)» : AbstractChoiceRule<«rosettaClass.name»>
                {
                    private static readonly string[] choiceFieldNames = { «usedAttributes.join(', ')['"'+name+'"']» };

                    public IValidationResult Validate(«clazz» «varName») {
                        var validationMethod = «validationType».Instance;
                        var populatedFieldNames = new List<string>();

                        «FOR a : usedAttributes»
                            if («varName».«expressionHandler.getPropertyName(a)» != null) populatedFieldNames.Add("«a.name»");
                        «ENDFOR»

                        if (validationMethod.Check(populatedFieldNames.Count))
                        {
                            return ModelValidationResult.Success(Name, ValidationType.CHOICE_RULE, "«clazz»");
                        }
                        return new ChoiceRuleFailure(Name, "«clazz»", choiceFieldNames, populatedFieldNames, validationMethod);
                    }
                }
    '''
    }

    def static String choiceRuleClassName(String choiceRuleName) {
        val allUnderscore = CaseFormat.UPPER_CAMEL.to(CaseFormat.LOWER_UNDERSCORE, choiceRuleName)
        val camel = CaseFormat.LOWER_UNDERSCORE.to(CaseFormat.UPPER_CAMEL, allUnderscore)
        return camel
    }

    def static String oneOfRuleClassName(String className) {
        return className + 'OneOfRule'
    }
    
    def static String oneOfRuleName(String className) {
        return className + '_oneOf'
    }
}

    