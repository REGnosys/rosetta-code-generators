package com.regnosys.rosetta.generator.python.expressions

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import com.regnosys.rosetta.generator.python.object.PythonModelObjectBoilerPlate
import com.regnosys.rosetta.generator.python.util.PythonModelGeneratorUtil
import com.regnosys.rosetta.rosetta.RosettaCallableWithArgs
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumValueReference
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaFeature
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.rosetta.expression.ChoiceOperation
import com.regnosys.rosetta.rosetta.expression.ClosureParameter
import com.regnosys.rosetta.rosetta.expression.DistinctOperation
import com.regnosys.rosetta.rosetta.expression.FilterOperation
import com.regnosys.rosetta.rosetta.expression.FirstOperation
import com.regnosys.rosetta.rosetta.expression.FlattenOperation
import com.regnosys.rosetta.rosetta.expression.InlineFunction
import com.regnosys.rosetta.rosetta.expression.LastOperation
import com.regnosys.rosetta.rosetta.expression.ListLiteral
import com.regnosys.rosetta.rosetta.expression.MapOperation
import com.regnosys.rosetta.rosetta.expression.ModifiableBinaryOperation
import com.regnosys.rosetta.rosetta.expression.Necessity
import com.regnosys.rosetta.rosetta.expression.OneOfOperation
import com.regnosys.rosetta.rosetta.expression.RosettaAbsentExpression
import com.regnosys.rosetta.rosetta.expression.RosettaBinaryOperation
import com.regnosys.rosetta.rosetta.expression.RosettaBooleanLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaConditionalExpression
import com.regnosys.rosetta.rosetta.expression.RosettaConstructorExpression
import com.regnosys.rosetta.rosetta.expression.RosettaCountOperation
import com.regnosys.rosetta.rosetta.expression.RosettaExistsExpression
import com.regnosys.rosetta.rosetta.expression.RosettaExpression
import com.regnosys.rosetta.rosetta.expression.RosettaFeatureCall
import com.regnosys.rosetta.rosetta.expression.RosettaImplicitVariable
import com.regnosys.rosetta.rosetta.expression.RosettaIntLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaNumberLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaOnlyElement
import com.regnosys.rosetta.rosetta.expression.RosettaOnlyExistsExpression
import com.regnosys.rosetta.rosetta.expression.RosettaReference
import com.regnosys.rosetta.rosetta.expression.RosettaStringLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaSymbolReference
import com.regnosys.rosetta.rosetta.expression.SortOperation
import com.regnosys.rosetta.rosetta.expression.SumOperation
import com.regnosys.rosetta.rosetta.expression.ThenOperation
import com.regnosys.rosetta.rosetta.expression.impl.AsKeyOperationImpl
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Condition
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.simple.ShortcutDeclaration
import com.regnosys.rosetta.rosetta.simple.impl.FunctionImpl
import java.util.ArrayList
import java.util.List
import com.regnosys.rosetta.rosetta.simple.Segment
import com.regnosys.rosetta.rosetta.expression.EqualityOperation

class PythonExpressionGenerator {
    
    @Inject extension RosettaExtensions
    @Inject extension PythonModelObjectBoilerPlate

    @Inject
    PythonModelGeneratorUtil utils;
    
    public var List<String> importsFound
    public var if_cond_blocks = new ArrayList<String>()
    
    public def generateConditions(Data cls) {
        // Move your condition and expression-related logic here
        var n_condition = 0;
        var res = '';
        for (Condition cond : cls.conditions) {
            res += generateConditionBoilerPlate(cond, n_condition)
            if (cond.isConstraintCondition)
                res += generateConstraintCondition(cls, cond)
            else
                res += generateExpressionCondition(cond)
            n_condition += 1;
        }        
        return res
    }

    public def generateConditions(List<Condition> conditions) {
        // Move your condition and expression-related logic here
        var n_condition = 0;
        var res = '';
        for (Condition cond : conditions) {
            res += generateConditionBoilerPlate(cond, n_condition)
            if (cond.isConstraintCondition)
                println('A')
                //res += generateConstraintCondition(cls, cond)
            else
                res += generateExpressionCondition(cond)
            n_condition += 1;
        }
        
        return res
    }

    public def generatePostConditions(List<Condition> conditions) {
        // Move your condition and expression-related logic here
        var n_condition = 0;
        var res = '';
        for (Condition cond : conditions) {
            res += generatePostConditionBoilerPlate(cond, n_condition)
            if (cond.isConstraintCondition)
                println('A')
                //res += generateConstraintCondition(cls, cond)
            else
                res += generateExpressionCondition(cond)
            n_condition += 1;
        }
        
        return res
    }

    def boolean isConstraintCondition(Condition cond) {
        return cond.isOneOf || cond.isChoice
    }

    private def boolean isOneOf(Condition cond) {
        return cond.expression instanceof OneOfOperation
    }

    private def boolean isChoice(Condition cond) {
        return cond.expression instanceof ChoiceOperation
    }

    private def generateConditionBoilerPlate(Condition cond, int n_condition) {
        '''
            
            @rosetta_condition
            def condition_«n_condition»_«cond.name»(self):
                «IF cond.definition!==null»
                    """
                    «cond.definition»
                    """
                «ENDIF»
                item = self
        '''
    }

    private def generatePostConditionBoilerPlate(Condition cond, int n_condition) {
        '''
            
            @rosetta_condition
            def post_condition_«n_condition»_«cond.name»(self):
                «IF cond.definition!==null»
                    """
                    «cond.definition»
                    """
                «ENDIF»
        '''
    }

    private def generateConstraintCondition(Data cls, Condition cond) {
        val expression = cond.expression
        var attributes = cls.attributes
        var necessity = "necessity=True"

        if (expression instanceof ChoiceOperation) {
            attributes = expression.attributes
            if (expression.necessity == Necessity.OPTIONAL) {
                necessity = "necessity=False"
            }
        }
        '''    return self.check_one_of_constraint(«FOR a : attributes SEPARATOR ", "»'«a.name»'«ENDFOR», «necessity»)
        '''
    }

    private def generateExpressionCondition(Condition c) {
        if_cond_blocks = new ArrayList<String>()
        var expr = generateExpression(c.expression, 0)
        var blocks = ""
        if (!if_cond_blocks.isEmpty()) {
            blocks = '''    «FOR arg : if_cond_blocks»«arg»«ENDFOR»'''
        }
        return '''«blocks»    return «expr»
        '''
    }

    def generateExpressionThenElse(RosettaExpression expr, List<Integer> iflvl) {
        if_cond_blocks = new ArrayList<String>()
        val expression = generateExpression(expr, iflvl.get(0))
    
        var blocks = ""
        if (!if_cond_blocks.isEmpty()) {
            iflvl.set(0, iflvl.get(0) + 1)
            blocks = '''    «FOR arg : if_cond_blocks»«arg»«ENDFOR»'''
        }
        return '''«blocks»'''
    }

    def String generateExpression(RosettaExpression expr, int iflvl) {
        switch (expr) {
            RosettaConditionalExpression: {
                // val nslashes = (2**iflvl - 1) as int;
                // val escsec = '\\'.repeat(nslashes) + "'";
                val ifexpr = generateExpression(expr.getIf(), iflvl + 1)
                val ifthen = generateExpression(expr.ifthen, iflvl + 1)
                var elsethen = expr.elsethen !== null && expr.full ? generateExpression(expr.elsethen,
                        iflvl + 1) : 'True'

                val if_blocks = '''
                    def _then_fn«iflvl»():
                        return «ifthen»

                    def _else_fn«iflvl»():
                        return «elsethen»

                '''
                if_cond_blocks.add(if_blocks)

                // '''if_cond(«ifexpr», «escsec»«ifthen»«escsec», «escsec»«elsethen»«escsec», self)'''
                '''if_cond_fn(«ifexpr», _then_fn«iflvl», _else_fn«iflvl»)'''
            }
            RosettaFeatureCall: {
                var right = switch (expr.feature) {
                    Attribute: {
                        expr.feature.name
                    }
                    RosettaMetaType: {
                        expr.feature.name
                    }
                    RosettaEnumValue: {
                        val rosettaValue = expr.feature as RosettaEnumValue
                        val value = EnumHelper.convertValues(rosettaValue)

                        val symbol = (expr.receiver as RosettaSymbolReference).symbol
                        val model = symbol.eContainer as RosettaModel
                        addImportsFromConditions(symbol.name, model.name)

                        value
                    }
                    // TODO: RosettaFeature: '''.Select(x => x.«feature.name.toFirstUpper»)'''
                    RosettaFeature: {
                        expr.feature.name
                    }
                    default:
                        throw new UnsupportedOperationException("Unsupported expression type of " +
                            expr.feature.eClass.name)
                }

                if (right == "None")
                    right = "NONE"
                var receiver = generateExpression(expr.receiver, iflvl)
                if (receiver === null) {
                    '''«right»'''
                } else {
                    '''_resolve_rosetta_attr(«receiver», "«right»")'''
                }
            }
            RosettaExistsExpression: {
                val argument = expr.argument as RosettaExpression
                '''((«generateExpression(argument, iflvl)») is not None)'''
            }
            RosettaBinaryOperation: {
                binaryExpr(expr, iflvl)
            }
            RosettaAbsentExpression: {
                val argument = expr.argument as RosettaExpression
                '''((«generateExpression(argument, iflvl)») is None)'''
            }
            RosettaReference: {
                reference(expr, iflvl)
            }
            RosettaNumberLiteral: {
                '''«expr.value»'''
            }
            RosettaBooleanLiteral: {
                if (expr.value == "true")
                    '''True'''
                else
                    '''False'''
            }
            RosettaIntLiteral: {
                '''«expr.value»'''
            }
            RosettaStringLiteral: {
                '''"«expr.value»"'''
            }
            RosettaOnlyElement: {
                val argument = expr.argument as RosettaExpression
                '''get_only_element(«generateExpression(argument, iflvl)»)'''
            }
            RosettaEnumValueReference: {
                val value = EnumHelper.convertValues(expr.value)
                '''«expr.enumeration».«value»'''
            }
            RosettaOnlyExistsExpression: {
                var aux = expr as RosettaOnlyExistsExpression;
                '''self.check_one_of_constraint(self, «generateExpression(aux.getArgs().get(0), iflvl)»)'''
            }
            RosettaCountOperation: {
                val argument = expr.argument as RosettaExpression
                '''rosetta_count(«generateExpression(argument, iflvl)»)'''
            }
            ListLiteral: {
                '''[«FOR arg : expr.elements SEPARATOR ', '»«generateExpression(arg, iflvl)»«ENDFOR»]'''
            }

            DistinctOperation: {
            // Implement the logic for DistinctOperation
            // Example: return '''set(«generateExpression(expr.argument, iflvl)»)'''
                val argument = generateExpression(expr.argument, iflvl);
                return '''set(«argument»)''';
            }
            
            SortOperation: {
                val argument = generateExpression(expr.argument, iflvl);
                return '''sorted(«argument»)''';
            // Implement the logic for DistinctOperation
            // Example: return '''set(«generateExpression(expr.argument, iflvl)»)'''
            }
            ThenOperation: {
                val funcExpr = expr.function
                val argExpr = generateExpression(expr.argument, iflvl)
                val body = generateExpression(funcExpr.body, iflvl)
                val funcParams = funcExpr.parameters.map[it.name].join(", ")
            
                // Handling the case where funcParams is empty
                val lambdaFunction = if (funcParams.empty) {
                    '''(lambda item: «body»)'''
                } else {
                    '''(lambda «funcParams»: «body»)'''
                }
            
                // Using the lambda function. If there are no parameters, argExpr will not be used.
                return '''«lambdaFunction»(«argExpr»)'''
            }
            LastOperation: {
                // Implement the logic for LastOperation
                // Example: return '''«generateExpression(expr.argument, iflvl)»[-1]'''
                val argument = generateExpression(expr.argument, iflvl);
                // Assuming argument is a list from which we want the last item
                return '''«argument»[-1]''';
            }
            SumOperation: {
                // Implement the logic for SumOperation
                // Example: return '''sum(«generateExpression(expr.argument, iflvl)»)'''
                val argument = generateExpression(expr.argument, iflvl);
                // Assuming argument is a list of numbers we want to sum
                return '''sum(«argument»)''';
            }
            FirstOperation: {
                // Implement the logic for FirstOperation
                // Example: return '''«generateExpression(expr.argument, iflvl)»[0]'''
                val argument = generateExpression(expr.argument, iflvl);
                // Assuming argument is a list from which we want the first item
                return '''«argument»[0]''';
            }
            FilterOperation: {
                // Generate the expression for the list to be filtered
                val argument = generateExpression(expr.argument, iflvl);
            
                // Generate the boolean expression for filtering
                val filterExpression = generateExpression(expr.function.body, iflvl);
            
                // Construct the call to the rosetta_filter function in Python
                // Assuming rosetta_filter is defined in your Python environment
                val filterCall = "rosetta_filter(" + argument + ", lambda item: " + filterExpression + ")";
            
                // Return the filter function call
                return filterCall;
            }

            MapOperation: {
                val inlineFunc = expr.function as InlineFunction;
                val funcParameters = inlineFunc.parameters.map[it.name].join(", ");
                val funcBody = generateExpression(inlineFunc.body, iflvl);
                // Construct the Python lambda function
                val lambdaFunction = "lambda item: " + funcBody;
                
                val argument = generateExpression(expr.argument, iflvl);
                // Using map function with the lambda
                val pythonMapOperation = "map(" + lambdaFunction + ", " + argument + ")";
                
                return pythonMapOperation;
            }
            AsKeyOperationImpl: {
                // Assuming AsKeyOperationImpl has a 'key' (possibly the 'operator' attribute) and an 'argument' property
                val key = expr.operator // or another property representing the key
                val argument = generateExpression(expr.argument, iflvl)
    
                return '''{«key»: «argument»}''' // Example: creating a dictionary entry in Python
            }
            FlattenOperation: {
                val nestedListExpr = generateExpression(expr.argument, iflvl)
                // Using the custom flatten_list method
                return '''flatten_list(«nestedListExpr»)'''
            }
            RosettaConstructorExpression: {
                val type = expr.typeCall?.type?.name // Get the type name, if available
                val keyValuePairs = expr.values // Get the key-value pairs from the constructor expression
            
                val pythonConstructor = if (type !== null) {
                    // If a type name is available, assume a custom Python class with a constructor
                    '''«type»(«FOR pair : keyValuePairs SEPARATOR ', '»«pair.key.name»=«generateExpression(pair.value, iflvl)»«ENDFOR»)'''
                } else {
                    // If no type name is available, assume a dictionary
                    '''{«FOR pair : keyValuePairs SEPARATOR ', '»'«pair.key.name»': «generateExpression(pair.value, iflvl)»«ENDFOR»}'''
                }
            
                return pythonConstructor
            }
            
            default:
                throw new UnsupportedOperationException("Unsupported expression type of " + expr?.class?.simpleName)
        }
    }

    protected def String reference(RosettaReference expr, int iflvl) {
        switch (expr) {
            RosettaImplicitVariable: {
                '''«expr.name»'''	
            }
            RosettaSymbolReference: {
                symbolReference(expr, iflvl)
            }
        }
    }

    def String symbolReference(RosettaSymbolReference expr, int iflvl) {
        val s = expr.symbol
        
        switch (s) {
            Data: {
                '''«s.name»'''
            }
            Attribute: {
                '''_resolve_rosetta_attr(self, "«s.name»")'''
            }
            RosettaEnumeration: {
                '''«s.name»'''
            }
            RosettaCallableWithArgs: {
                callableWithArgsCall(s, expr, iflvl)
            }
            ShortcutDeclaration:{
                '''_resolve_rosetta_attr(self, "«s.name»")'''
            }			
            ClosureParameter:{
                '''_resolve_rosetta_attr(self, "«s.name»")'''
            }
            
            default:
                throw new UnsupportedOperationException("Unsupported callable type of " + s.class.simpleName)
        }
    }

    def String callableWithArgsCall(RosettaCallableWithArgs s, RosettaSymbolReference expr, int iflvl) {
        if (s instanceof FunctionImpl)
            addImportsFromConditions(s.getName(), (s.eContainer as RosettaModel).name + "." + "functions")
        else
            addImportsFromConditions(s.name, (s.eContainer as RosettaModel).name)
        var args = '''«FOR arg : expr.args SEPARATOR ', '»«generateExpression(arg, iflvl)»«ENDFOR»'''
        '''«s.name»(«args»)'''

    }

    def String binaryExpr(RosettaBinaryOperation expr, int iflvl) {
        if (expr instanceof ModifiableBinaryOperation) {
            if (expr.cardMod !== null) {
                if (expr.operator == "<>") {
                    '''any_elements(«generateExpression(expr.left, iflvl)», "«expr.operator»", «generateExpression(expr.right, iflvl)»)'''
                } else {
                    '''all_elements(«generateExpression(expr.left, iflvl)», "«expr.operator»", «generateExpression(expr.right, iflvl)»)'''
                }
            }
        } else {
            switch expr.operator {
                case ("="): {
                    '''(«generateExpression(expr.left, iflvl)» == «generateExpression(expr.right, iflvl)»)'''
                }
                case ("<>"): {
                    '''(«generateExpression(expr.left, iflvl)» != «generateExpression(expr.right, iflvl)»)'''
                }
                case ("contains"): {
                    '''contains(«generateExpression(expr.left, iflvl)», «generateExpression(expr.right, iflvl)»)'''

                }
                case ("disjoint"): {
                    '''disjoint(«generateExpression(expr.left, iflvl)», «generateExpression(expr.right, iflvl)»)'''

                }
                case ("join"): {
                    '''join(«generateExpression(expr.left, iflvl)», «generateExpression(expr.right, iflvl)»)'''
                }
                default: {
                    '''(«generateExpression(expr.left, iflvl)» «expr.operator» «generateExpression(expr.right, iflvl)»)'''
                }
            }
        }
    }

    def addImportsFromConditions(String variable, String namespace) {
        val import = '''from «namespace».«variable» import «variable»'''
        if(importsFound!=null){
            if (!importsFound.contains(import)) {
                importsFound.add(import)
            }
        }
    }
}