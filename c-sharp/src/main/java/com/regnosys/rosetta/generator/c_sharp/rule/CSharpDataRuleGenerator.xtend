package com.regnosys.rosetta.generator.c_sharp.rule

import com.google.common.base.CaseFormat
import com.google.inject.Inject
import java.util.List

import com.regnosys.rosetta.generator.c_sharp.expression.ExpressionGenerator
import com.regnosys.rosetta.generator.c_sharp.expression.ExpressionGenerator.ParamMap
//import com.regnosys.rosetta.generator.java.function.RosettaFunctionDependencyProvider
import com.regnosys.rosetta.generator.java.util.RosettaGrammarUtil
import com.regnosys.rosetta.rosetta.expression.RosettaConditionalExpression
import com.regnosys.rosetta.rosetta.RosettaType

import com.regnosys.rosetta.rosetta.simple.Condition
import com.regnosys.rosetta.rosetta.simple.Data

import org.eclipse.xtend2.lib.StringConcatenationClient
import static com.regnosys.rosetta.generator.c_sharp.util.CSharpModelGeneratorUtil.*
import static com.regnosys.rosetta.rosetta.simple.SimplePackage.Literals.CONDITION__EXPRESSION
import com.regnosys.rosetta.RosettaEcoreUtil
import java.util.Collection
import com.regnosys.rosetta.rosetta.expression.OneOfOperation
import com.regnosys.rosetta.rosetta.expression.ChoiceOperation

class CSharpDataRuleGenerator {
    @Inject ExpressionGenerator expressionHandler
    @Inject extension RosettaEcoreUtil
    //@Inject RosettaFunctionDependencyProvider funcDependencies
    
    def generateDataRules(List<Data> rosettaClasses, String version) {
        '''
        «fileComment(version)»
        
        #nullable enable // Allow nullable reference types
        
        namespace Org.Isda.Cdm.Validation.DataRule
        {
            using System.Collections.Generic;
            using System;
            using System.Linq;
            
            using Org.Isda.Cdm;
            using Org.Isda.Cdm.Functions;
            
            using Rosetta.Lib.Attributes;
            using Rosetta.Lib.Functions;
            using Rosetta.Lib.Validation;
            
        «FOR rosettaClass : rosettaClasses»
            «FOR c : rosettaClass.conditions»
                «c.dataRuleClassBody(rosettaClass, version)»
            «ENDFOR»
        «ENDFOR»
        }
        '''
    }

    def static String dataRuleClassName(String dataRuleName) {
        val allUnderscore = CaseFormat.UPPER_CAMEL.to(CaseFormat.LOWER_UNDERSCORE, dataRuleName)
        val camel = CaseFormat.LOWER_UNDERSCORE.to(CaseFormat.UPPER_CAMEL, allUnderscore)
        return camel
    }
    
    def  String dataRuleClassName(Condition cond, Data data) {
        dataRuleClassName(cond.conditionName(data))
    }

    @Deprecated
    private def String conditionName(Condition cond, Data data) {
        return cond.conditionName(data.name, data.conditions)
    }

    //Name convention: <type name>(<condition name>|<condition type><#>) where condition type should be 'choice' or 'oneof'.
    private def String conditionName(Condition cond, String containerName, Collection<Condition> conditions) {
        val name = if (!cond.name.nullOrEmpty)
                cond.name
            else {
                val idx = conditions.filter[name.nullOrEmpty].toList.indexOf(cond)
                val type = if (cond.isOneOf) {
                        'OneOf'
                    } else if (cond.isChoice) {
                         'Choice'
                    } else 'DataRule'
                '''«type»«idx»'''
            }
        return '''«containerName»«name»'''
    }
    
    private def boolean isOneOf(Condition cond) {
        return cond.expression instanceof OneOfOperation
    }

    private def boolean isChoice(Condition cond) {
        return cond.expression instanceof ChoiceOperation
    }
    
    private def StringConcatenationClient dataRuleClassBody(Condition rule, Data data, String version)  {
        val rosettaClass = rule.eContainer as RosettaType
        val expression = rule.expression
        
        val ruleWhen = if(expression instanceof RosettaConditionalExpression ) expression.^if
        val ruleThen = if(expression instanceof RosettaConditionalExpression ) expression.ifthen else expression
        
        val definition = RosettaGrammarUtil.quote(RosettaGrammarUtil.extractNodeText(rule, CONDITION__EXPRESSION))
        val ruleName = rule.conditionName(data)
        //val funcDeps = funcDependencies.functionDependencies(#[ruleWhen , ruleThen])
        '''
        «""»
            «comment(rule.definition)»
            [RosettaDataRule("«ruleName»")]
            public class «dataRuleClassName(ruleName)» : AbstractDataRule<«rosettaClass.name»>
            {
                protected override string Definition => «definition»;
««« TODO: Work out dependencies????
«««                «FOR dep : funcDeps»
«««                    @«Inject» protected «javaName.toJavaType(dep)» «dep.name.toFirstLower»;
«««                «ENDFOR»
                
                protected override IComparisonResult? RuleIsApplicable(«rosettaClass.name» «rosettaClass.name.toFirstLower»)
                {
                    «IF ruleWhen === null»
                        return ComparisonResult.Success();
                    «ELSE»
                    try
                    {
                        return «expressionHandler.csharpCode(ruleWhen, new ParamMap(rosettaClass))»;
                    }
                    catch (Exception ex)
                    {
                        return ComparisonResult.Failure(ex.Message);
                    }
                    «ENDIF»
                }
                
                protected override IComparisonResult? EvaluateThenExpression(«rosettaClass.name» «rosettaClass.name.toFirstLower»)
                {
                    try
                    {
                        return «expressionHandler.csharpCode(ruleThen, new ParamMap(rosettaClass))»;
                    }
                    catch (Exception ex)
                    {
                        return ComparisonResult.Failure(ex.Message);
                    }
                }
            }
        
        '''
    }
}

