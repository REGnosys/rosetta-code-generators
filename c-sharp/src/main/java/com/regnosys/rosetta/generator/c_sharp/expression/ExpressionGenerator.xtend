package com.regnosys.rosetta.generator.c_sharp.expression;

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.generator.c_sharp.util.CSharpNames
import com.regnosys.rosetta.generator.c_sharp.util.CSharpType
import com.regnosys.rosetta.generator.util.RosettaFunctionExtensions
import com.regnosys.rosetta.rosetta.RosettaAbsentExpression
import com.regnosys.rosetta.rosetta.RosettaAlias
import com.regnosys.rosetta.rosetta.RosettaBigDecimalLiteral
import com.regnosys.rosetta.rosetta.RosettaBinaryOperation
import com.regnosys.rosetta.rosetta.RosettaBooleanLiteral
import com.regnosys.rosetta.rosetta.RosettaCallableCall
import com.regnosys.rosetta.rosetta.RosettaCallableWithArgs
import com.regnosys.rosetta.rosetta.RosettaCallableWithArgsCall
import com.regnosys.rosetta.rosetta.RosettaConditionalExpression
import com.regnosys.rosetta.rosetta.RosettaContainsExpression
import com.regnosys.rosetta.rosetta.RosettaCountOperation
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumValueReference
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaExistsExpression
import com.regnosys.rosetta.rosetta.RosettaExpression
import com.regnosys.rosetta.rosetta.RosettaExternalFunction
import com.regnosys.rosetta.rosetta.RosettaFeature
import com.regnosys.rosetta.rosetta.RosettaFeatureCall
import com.regnosys.rosetta.rosetta.RosettaGroupByExpression
import com.regnosys.rosetta.rosetta.RosettaGroupByFeatureCall
import com.regnosys.rosetta.rosetta.RosettaIntLiteral
import com.regnosys.rosetta.rosetta.RosettaLiteral
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.rosetta.RosettaParenthesisCalcExpression
import com.regnosys.rosetta.rosetta.RosettaStringLiteral
import com.regnosys.rosetta.rosetta.RosettaType
import com.regnosys.rosetta.rosetta.RosettaWhenPresentExpression
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.simple.EmptyLiteral
import com.regnosys.rosetta.rosetta.simple.Function
import com.regnosys.rosetta.rosetta.simple.ListLiteral
import com.regnosys.rosetta.rosetta.simple.ShortcutDeclaration
import com.regnosys.rosetta.types.RosettaOperators
import com.regnosys.rosetta.types.RosettaTypeProvider
import com.regnosys.rosetta.utils.ExpressionHelper
import com.rosetta.model.lib.mapper.MapperC
import com.rosetta.model.lib.expression.MapperMaths
import com.rosetta.model.lib.mapper.MapperS
import java.util.HashMap
import org.eclipse.xtend2.lib.StringConcatenationClient
import org.eclipse.xtext.EcoreUtil2
import org.eclipse.xtext.util.Wrapper

import static extension com.regnosys.rosetta.generator.c_sharp.enums.CSharpEnumGenerator.toCSharpEnumName
import static extension com.regnosys.rosetta.generator.c_sharp.util.CSharpTranslator.toCSharpType
import org.eclipse.emf.ecore.EObject

class ExpressionGenerator {

    @Inject
    protected RosettaTypeProvider typeProvider
    @Inject
    RosettaOperators operators
    //@Inject
    //CardinalityProvider cardinalityProvider // TODO: Decide if this should be used in place of isCollection
    @Inject
    CSharpNames.Factory factory
    @Inject
    RosettaFunctionExtensions funcExt
    @Inject
    extension RosettaExtensions
    @Inject
    ExpressionHelper exprHelper
    
    def StringConcatenationClient csharpCode(RosettaExpression expr, ParamMap params) {
        // TODO: Convert expression to C# code via extension!!!
        expr.csharpCode(params, true);
    }

    /**
     * convert a rosetta expression to code
     * ParamMpa params  - a map keyed by classname or positional index that provides variable names for expression parameters
     */
    def StringConcatenationClient csharpCode(RosettaExpression expr, ParamMap params, boolean isLast) {
        switch (expr) {
            RosettaFeatureCall: {
                var autoValue = true // if the attribute being referenced is WithMeta and we aren't accessing the meta fields then access the value by default
                if (expr.eContainer !== null && expr.eContainer instanceof RosettaFeatureCall &&
                    (expr.eContainer as RosettaFeatureCall).feature instanceof RosettaMetaType) {
                    autoValue = false;
                }
                featureCall(expr, params, isLast, autoValue)
            }
            RosettaExistsExpression: {
                existsExpr(expr, expr.argument, params)
            }
            RosettaBinaryOperation: {
                binaryExpr(expr, null, params)
            }
            RosettaCountOperation: {
                countExpr(expr, null, params)
            }
            RosettaAbsentExpression: {
                absentExpr(expr, expr.argument, params)
            }
            RosettaWhenPresentExpression: {
                whenPresentExpr(expr, expr.left, params)
            }
            RosettaCallableCall: {
                callableCall(expr, params)
            }
            RosettaCallableWithArgsCall: {
                callableWithArgs(expr, params)
            }
            RosettaBigDecimalLiteral: {
                '''Convert.ToDecimal(«expr.value»)'''
            }
            RosettaBooleanLiteral: {
                '''«expr.value»'''
            }
            RosettaIntLiteral: {
                '''«expr.value»'''
            }
            RosettaStringLiteral: {
                '''"«expr.value»"'''
            }
            RosettaEnumValueReference: {
                '''Enums.XX«expr.enumeration.toCSharpType».YY«expr.value.toCSharpEnumName»'''
            }
            RosettaConditionalExpression: {
                '''
                «expr.doIfName»(«expr.^if.csharpCode(params)»,
                    «expr.ifthen.csharpCode(params)»«IF expr.elsethen !== null»,
                    «expr.elsethen.csharpCode(params)»«ENDIF»)'''
            }
            RosettaContainsExpression: {
                '''«expr.container.csharpCode(params)».Includes(«expr.contained.csharpCode(params)»)'''
            }
            RosettaParenthesisCalcExpression: {
                expr.expression.csharpCode(params, isLast)
            }
            EmptyLiteral: {
                '''null'''
            }
            ListLiteral: {
                '''«MapperC».of(«FOR ele : expr.elements SEPARATOR ', '»«ele.csharpCode(params)»«ENDFOR»)'''
            }
            default:
                throw new UnsupportedOperationException("Unsupported expression type of " + expr?.class?.simpleName)
        }
    }

    private def String doIfName(RosettaConditionalExpression expr) {
        //if (expr.ifthen.evalulatesToMapper) "DoIf" else "ResultDoIf"
        "IfThen"
    }

    def StringConcatenationClient callableWithArgs(RosettaCallableWithArgsCall expr, ParamMap params) {
        val callable = expr.callable

        return switch (callable) {
            Function: {
                funcExt.getOutput(callable).card.isMany
                val implicitArg = funcExt.implicitFirstArgument(expr)
                '''«callable.name».Evaluate(«IF implicitArg !== null»«implicitArg.name.toFirstLower»«ENDIF»«args(expr, params)»)'''
            }
            RosettaExternalFunction: '''(new «factory.create(callable.model).toCSharpType(callable as RosettaCallableWithArgs)»().Execute(«args(expr, params)»))'''
            default:
                throw new UnsupportedOperationException("Unsupported callable with args type of " + expr.eClass.name)
        }

    }

    private def StringConcatenationClient args(RosettaCallableWithArgsCall expr, ParamMap params) {
        '''«FOR arg : expr.args SEPARATOR ', '»«arg.csharpCode(params)»«IF !(arg instanceof EmptyLiteral)»«ENDIF»«ENDFOR»'''
    }

    def StringConcatenationClient existsExpr(RosettaExistsExpression exists, RosettaExpression argument,
        ParamMap params) {
        val arg = getAliasExpressionIfPresent(argument)
        val binary = arg.findBinaryOperation
        if (binary !== null) {
                // if the argument is a binary expression then the exists needs to be pushed down into it
                binary.binaryExpr(exists, params)
        } else {
            '''«doExistsExpr(exists, arg, params)»'''
        }
    }

    def RosettaBinaryOperation findBinaryOperation(RosettaExpression expression) {
        switch (expression) {
            RosettaBinaryOperation: expression
            RosettaParenthesisCalcExpression: expression.expression.findBinaryOperation
            default: null
        }
    }
    
    private def removeOptionalChar(String str) {
        var length = str.length
        val char optional = '?'
        if (length > 1 && str.charAt(length - 1) == optional) length -= 1
        return str.substring(0, length)
    }

    private def StringConcatenationClient doExistsExpr(RosettaExistsExpression exists, RosettaExpression arg, ParamMap params) {
        if (arg.isOptional || (arg.isMetaType && arg.isReference)) {
            if (exists.only) {
                var code = '''«arg.csharpCode(params)»'''
                // Need to split 'parent.param' into: OnlyExists(parent, "param")
                // Removing trailing .Value for meta fields
                val suffix = ".Value"
                if (code.endsWith(suffix)) {
                    code = code.substring(0, code.length - suffix.length).removeOptionalChar
                }
                val ordinal = code.lastIndexOf(".")
                val param = code.substring(ordinal + 1)
                val parent = code.substring(0, ordinal).removeOptionalChar
                '''OnlyExists(«parent», "«param»")'''
            }
            else {
                '''«IF exists.single»Single«ELSEIF exists.multiple»Multiple«ENDIF»Exists(«arg.csharpCode(params)»)'''
            }
        }
        else '''ComparisonResult.Success()'''
    }

    private def StringConcatenationClient doAbsentExpr(RosettaAbsentExpression absent, RosettaExpression arg, ParamMap params) {
        if (arg.isOptional) {
            '''NotExists(«arg.csharpCode(params)»)'''
        }
        else '''ComparisonResult.Failure("Field is not optional and must exist")'''
    }

    def StringConcatenationClient absentExpr(RosettaAbsentExpression absent, RosettaExpression argument,
        ParamMap params) {
        val arg = getAliasExpressionIfPresent(argument)
        val binary = arg.findBinaryOperation
        if (binary !== null) {
                // if the arg is binary then the operator needs to be pushed down
                binary.binaryExpr(absent, params)
        } else {
            '''«doAbsentExpr(absent, arg, params)»'''
        }
    }

    protected def StringConcatenationClient callableCall(RosettaCallableCall expr, ParamMap params) {
        val call = expr.callable
        switch (call) {
            Data: {
                '''«params.getClass(call)»'''
            }
            RosettaAlias: {
                call.expression.csharpCode(params)
            }
            Attribute: {
                // Data Attributes can only be called from their conditions
                // The current container (Data) is stored in Params, but we need also look for superTypes
                // so we could also do: (call.eContainer as Data).allSuperTypes.map[it|params.getClass(it)].filterNull.head
                if (call.eContainer instanceof Data) {
                    val variableName = EcoreUtil2.getContainerOfType(expr, Data).getName.toFirstLower
                    '''«variableName»«buildMapFunc(call, false, true)»'''
                }
                else
                    '''«call.name»'''
            }
            ShortcutDeclaration: {
                '''«call.name»(«aliasCallArgs(call)»).«IF exprHelper.usesOutputParameter(call.expression)»build()«ELSE»get()«ENDIF»'''
            }
            RosettaEnumeration: '''Enums.«call.toCSharpType»'''
            default:
                throw new UnsupportedOperationException("Unsupported callable type of " + call.class.simpleName)
        }
    }

    def aliasCallArgs(ShortcutDeclaration alias) {
        val func = EcoreUtil2.getContainerOfType(alias, Function)
        val attrs = <String>newArrayList
        attrs.addAll(funcExt.getInputs(func).map[name].toList)
        if (exprHelper.usesOutputParameter(alias.expression)) {
            attrs.add(0, funcExt.getOutput(func)?.name + '.toBuilder()')
        }
        attrs.join(', ')
    }

    /**
     * feature call is a call to get an attribute of an object e.g. Quote->amount
     * 
     */
    private def StringConcatenationClient featureCall(RosettaFeatureCall call, ParamMap params, boolean isLast,
        boolean autoValue) {
        val feature = call.feature
        val StringConcatenationClient right = switch (feature) {
            Attribute: feature.buildMapFunc(isLast, autoValue)
            RosettaMetaType: feature.buildMapFunc(isLast)
            RosettaEnumValue: '''.«feature.toCSharpEnumName»'''
            //TODO: RosettaFeature: '''.Select(x => x.«feature.name.toFirstUpper»)'''
            default:
                throw new UnsupportedOperationException("Unsupported expression type of " + feature.eClass.name)
        }
        
        // NB: Reference MetaTypes always have optional Value properties
        val isMetaType = call.receiver.isMetaType
        val isReference = call.receiver.isReference
        val receiver = '''«csharpCode(call.receiver, params, false)»'''
        
        if (call.toOne || !call.receiver.isCollection) {
            return '''«receiver»«IF call.receiver.isOptional || isReference»?«ENDIF»«right»'''
        }
        else if (feature instanceof Attribute) {
            // Use Select if receiver is a collection, but SelectMany if feature is also a collection
            // Assume collections are never null, possibly empty and could contain optional values
            val variableName = feature.getVariableName
            val isCollection = feature.isCollection
            val qualifier = '''«IF isMetaType».Value«ENDIF»«IF isReference || call.receiver.isElementOptional»?«ENDIF»'''
            return '''
                «receiver»«IF call.receiver instanceof RosettaFeatureCall»
                    «ENDIF».Select«IF isCollection»Many«ENDIF»(«variableName» => «IF isCollection»(«ENDIF»«variableName»«qualifier»«right»«IF isCollection»).EmptyIfNull()«ENDIF»)'''
        } else
            return '''«receiver».All(TODO => «right»'''
    }

    def private boolean isMetaType(EObject expr) {
        switch (expr) {
            RosettaCallableCall: {
                isMetaType(expr.callable)
            }
            RosettaFeatureCall: {
                return isMetaType(expr.feature)
            }
            Attribute: {
                return !expr.metaAnnotations.nullOrEmpty
            }
            default: false
        }    
    }

    def private boolean isReference(EObject expr) {
        switch (expr) {
            RosettaCallableCall: {
                isReference(expr.callable)
            }
            RosettaFeatureCall: {
                return isReference(expr.feature)
            }
            Attribute: {
                return !expr.metaAnnotations.nullOrEmpty && expr.metaAnnotations.exists[attribute.name == "reference"]
            }
            default: false
        }    
    }
    
    def private boolean isCollection(EObject expr) {
        switch (expr) {
            RosettaCallableCall: {
                expr.callable.isCollection
            }
            RosettaCallableWithArgsCall: {
                expr.callable.isCollection
            }
            RosettaFeatureCall: {
                expr.feature.isCollection || expr.receiver.isCollection
            }
            Attribute: {
                expr.card.isIsMany
            }
            default: false
        } 
    }

    def private boolean isCollection(RosettaFeature feature) {
        switch (feature) {
            Attribute:
                feature.card.isIsMany
            default:
                false
        }
    }

    def private boolean isElementOptional(EObject expr) {
        switch (expr) {
            RosettaFeatureCall: {
                expr.isOptional
            }
            default: false
        } 
    }

    def private boolean isOptional(EObject expr) {
        switch (expr) {
            RosettaCallableCall: {
                expr.callable.isOptional
            }
            RosettaCallableWithArgsCall: {
                expr.callable.isOptional
            }
            RosettaFeatureCall: {
                expr.feature.isOptional || expr.receiver.isOptional
            }
            Function: {
                expr.output.isOptional
            }
            Attribute: {
                expr.card.isIsOptional && !expr.card.isIsMany
            }
            default: false
        } 
    }
    def private boolean isOptional(RosettaFeature feature) {
        switch (feature) {
            Attribute:
                feature.card.isIsOptional
            default:
                false
        }
    }

    def StringConcatenationClient countExpr(RosettaCountOperation expr, RosettaExpression test, ParamMap params) {
        '''«expr.argument.csharpCode(params)».Count()'''
    }

    def StringConcatenationClient whenPresentExpr(RosettaWhenPresentExpression expr, RosettaExpression left, ParamMap params) {
        '''DoWhenPresent(«left.csharpCode(params)», «toComparisonFunc(expr.left.csharpCode(params), expr.operator, expr.right.csharpCode(params))»)'''
    }

    def StringConcatenationClient binaryExpr(RosettaBinaryOperation expr, RosettaExpression test, ParamMap params) {
        val left = getAliasExpressionIfPresent(expr.left)
        val right = getAliasExpressionIfPresent(expr.right)
        val leftRtype = typeProvider.getRType(expr.left)
        val rightRtype = typeProvider.getRType(expr.right)
        val resultType = operators.resultType(expr.operator, leftRtype, rightRtype)
        val leftType = '''«leftRtype.name.toCSharpType»'''
        val rightType = '''«rightRtype.name.toCSharpType»'''

        switch expr.operator {
            case ("and"): {
                if (evalulatesToMapper(left)) {
                    // Mappers
//                    if (isComparableTypes(expr))
                        '''
                        And(«left.booleanize(test, params)»,
                            «right.booleanize(test, params)»)'''
//                    else
//                        '''
//                        «left.booleanize(test, params)» && «right.booleanize(test, params)»'''
                } else {
                    // ComparisonResults
                    '''
                    And(«left.csharpCode(params)»,
                        «right.csharpCode(params)»)'''
                }
            }
            case ("or"): {
                if (evalulatesToMapper(left)) {
                    // Mappers
//                    if (isComparableTypes(expr))
                        '''
                        Or(«left.booleanize(test, params)»,
                            «right.booleanize(test, params)»)'''
//                    else
//                        '''
//                        «left.booleanize(test, params)» || «right.booleanize(test, params)»'''
                } else {
                    // ComparisonResult
                    '''
                    Or(«left.csharpCode(params)»,
                        «right.csharpCode(params)»)'''
                }
            }
            case ("+"): {
                '''«MapperMaths».<«resultType.name.toCSharpType», «leftType», «rightType»>Add(«expr.left.csharpCode(params)», «expr.right.csharpCode(params)»)'''
            }
            case ("-"): {
                '''«MapperMaths».<«resultType.name.toCSharpType», «leftType», «rightType»>Subtract(«expr.left.csharpCode(params)», «expr.right.csharpCode(params)»)'''
            }
            case ("*"): {
                '''«MapperMaths».<«resultType.name.toCSharpType», «leftType», «rightType»>Multiply(«expr.left.csharpCode(params)», «expr.right.csharpCode(params)»)'''
            }
            case ("/"): {
                '''«MapperMaths».<«resultType.name.toCSharpType», «leftType», «rightType»>Divide(«expr.left.csharpCode(params)», «expr.right.csharpCode(params)»)'''
            }
            default: {
                // Comparisons
                // FIXME isProduct isEvent stuff in QualifyFunctionGenerator. Should be removed after alias migration
                val leftExpr = expr.left.csharpCode(params)
                val rightExpr = expr.right.csharpCode(params)
                
                if (left.needsMapperTree && !right.needsMapperTree) {
                    toComparisonFunc('''«leftExpr»''', expr.operator, '''«toMapperTree(rightExpr)»''')
                } else if (!left.needsMapperTree && right.needsMapperTree) {
                    toComparisonFunc('''«toMapperTree(leftExpr)»''', expr.operator, '''«rightExpr»''')
                } else if (expr.left.isCollection || expr.right.isCollection) {
                    '''«leftExpr».«toComparisonFuncName(expr.operator)»(«rightExpr»)'''
                } else {
                    // TODO: Produce error message?
                    '''ComparisonResult.FromBoolean(«expr.left.csharpCode(params)» «toComparisonOp(expr.operator)» «expr.right.csharpCode(params)»)'''
                }
            }
        }
    }

    private def boolean needsMapperTree(RosettaExpression expr) {
        if (expr instanceof RosettaGroupByFeatureCall) {
            val call = expr.call
            switch (call) {
                RosettaCallableCall: {
                    val callable = call.callable
                    if (callable instanceof RosettaAlias) {
                        return callable.expression.isLogicalOperation
                    }
                }
                RosettaBinaryOperation:
                    return call.isLogicalOperation
            }
        }
        return expr.isLogicalOperation
    }

    private def boolean isLogicalOperation(RosettaExpression expr) {
        if (expr instanceof RosettaBinaryOperation) return expr.operator == "and" || expr.operator == "or"
        return false
    }

    /**
     * Inspect expression and return alias expression if present.  Currently, nested aliases are not supported.
     */
    private def getAliasExpressionIfPresent(RosettaExpression expr) {
        if (expr instanceof RosettaCallableCall) {
            val callable = expr.callable
            if (callable instanceof RosettaAlias) {
                return callable.expression
            }
        }
        return expr
    }

    /**
     * Collects all expressions down the tree, and checks that they're all either FeatureCalls or CallableCalls (or anything that resolves to a Mapper)
     */
    private def boolean evalulatesToMapper(RosettaExpression expr) {
        val exprs = newHashSet
        collectExpressions(expr, [exprs.add(it)])

        return !exprs.empty && exprs.stream.allMatch [
            it instanceof RosettaGroupByFeatureCall || it instanceof RosettaFeatureCall ||
                it instanceof RosettaCallableCall || it instanceof RosettaFeatureCall ||
                it instanceof RosettaCallableWithArgsCall || it instanceof RosettaLiteral
        ]
    }

    /**
     * Search leaf node objects to determine whether this is a comparison of matching objects types
     */
    private def isComparableTypes(RosettaBinaryOperation binaryExpr) {
        // get list of the object type at each leaf node
        val rosettaTypes = newHashSet
        collectLeafTypes(binaryExpr, [rosettaTypes.add(it)])

        // check whether they're all the same type
        val type = rosettaTypes.stream.findAny
        return type.isPresent && rosettaTypes.stream.allMatch[it.equals(type.get)]
    }

    private def StringConcatenationClient toComparisonFunc(StringConcatenationClient left, String operator,  StringConcatenationClient right) {
        // NB: Based on https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-value-types#lifted-operators
        // we can use normal operators for nullable value types, which will return false if the parameter is null
        return '''«toComparisonFuncName(operator)»(«left», «right»)'''
    }

    private def String toComparisonFuncName(String operator) {
        switch operator {
            case ("="): "IsEqual"
            case ("<>"): "NotEquals"
            case ("<"): "LessThan"
            case ("<="): "LessThanEquals"
            case (">"): "GreaterThan"
            case (">="): "GreaterThanEquals"
            default:
                throw new UnsupportedOperationException("Unsupported binary operation of " + operator)
        }
    }

    private def String toComparisonOp(String operator) {
        switch operator {
            case ("="): "=="
            case ("<>"): "!="
            default: operator
        }
    }

    /**
     * converts an expression into a boolean result using the test expression pushed down (see exists etc)
     */
    def StringConcatenationClient booleanize(RosettaExpression expr, RosettaExpression test, ParamMap params) {
        switch (expr) {
            RosettaBinaryOperation: {
                binaryExpr(expr, test, params)
            }
            default: {
                switch test {
                    RosettaExistsExpression: {
                        '''«doExistsExpr(test, expr, params)»'''
                    }
                    RosettaAbsentExpression: {
                        '''«doAbsentExpr(test, expr, params)»'''
                    }
                    case null: {
                        expr.csharpCode(params).toMapperTree
                    }
                    default:
                        throw new UnsupportedOperationException(
                            "Unsupported expression type of " + test.class.simpleName)
                }
            }
        }
    }

    def StringConcatenationClient getPropertyName(Attribute attribute) {
        val name = attribute.name.toFirstUpper
        val containerName = (attribute.eContainer as Data).name
        // If property name matches container name, we need to append "Value"
        return '''«name»«IF name == containerName»Value«ENDIF»'''
    }

    def StringConcatenationClient getVariableName(Attribute attribute) {
        '''«attribute.attributeTypeVariableName»'''
    }

    def matchesEnclosingType(Attribute attribute) {
        attribute.name.toFirstUpper == attribute.eContainer
    }

    /**
     * Builds the expression of mapping functions to extract a path of attributes
     */
    def StringConcatenationClient buildMapFunc(Attribute attribute, boolean isLast, boolean autoValue) {
        if (attribute.card.isIsMany) {
            '''.«attribute.getPropertyName»'''
        } else {
            val memberCall = '''«IF attribute.override»(«attribute.type.toCSharpType») «ENDIF»«IF !(attribute.card.eContainer instanceof Attribute)»«attribute.attributeTypeVariableName»«ENDIF».«attribute.getPropertyName»'''
            if (!attribute.isMetaType || !autoValue) {
                '''«memberCall»'''
            } else {// FieldWithMeta
                '''«memberCall»«IF attribute.isOptional»?«ENDIF».Value'''
            }
        }
    }

    private def CSharpType toCSharpType(RosettaType rosType) {
        val model = rosType.model
        if (model === null)
            throw new IllegalArgumentException('''Can not create type reference. «rosType.eClass?.name» «rosType.name» is not attached to a «RosettaModel.simpleName»''')
        factory.create(model).toCSharpType(rosType)
    }

    private def csharpNames(Attribute attr) {
        val model = EcoreUtil2.getContainerOfType(attr, RosettaModel)
        if (model === null)
            throw new IllegalArgumentException('''Can not create type reference. «attr.eClass?.name» «attr.name» is not attached to a «RosettaModel.simpleName»''')
        factory.create(model)
    }

    def CSharpType metaClass(Attribute attribute) {
        val names = attribute.csharpNames
        val name = if (attribute.annotations.exists [ a |
                a.annotation?.name == "metadata" && a.attribute?.name == "reference"
            ])
                "ReferenceWithMeta" + attribute.type.name.toFirstUpper
            else
                "FieldWithMeta" + attribute.type.name.toFirstUpper
        return names.toMetaType(attribute, name)
    }

    def static StringConcatenationClient buildMapFunc(RosettaMetaType meta, boolean isLast) {
        if (meta.name == "reference") {
            '''.GlobalReference'''
//            '''.Select(a => a.GlobalReference)'''
        } else {
            '''.Meta.«meta.name.toFirstUpper»)'''
//            '''.Select(a => a.Meta.«meta.name.toFirstUpper»)'''
        }
    }

    def StringConcatenationClient buildGroupBy(RosettaGroupByExpression expression, boolean isLast) {
        val exprs = newArrayList
        val expr = Wrapper.wrap(expression)
        exprs.add(expr.get)
        while (expr.get.right !== null) {
            expr.set(expr.get.right)
            exprs.add(expr.get)
        }
        '''.<«expr.get.attribute.type.name.toCSharpType»>GroupBy(g->new «MapperS»<>(g)«FOR ex : exprs»«buildMapFunc(ex.attribute as Attribute, isLast, true)»«ENDFOR»)'''
    }

    private def typeName(Attribute attribute)
        // TODO: Handle Meta types
        '''«attribute.type.toCSharpType»'''

    private def attributeTypeVariableName(Attribute attribute)
         '''«(attribute.eContainer as Data).toCSharpType.simpleName.toFirstLower»'''

    /**
     * The id for a parameter - either a Class name or a positional index
     */
    @org.eclipse.xtend.lib.annotations.Data
    static class ParamID {
        RosettaType c
        int index
        String name;
    }

    // Class mapping from class name or positional index to the name of a variable defined in the containing code
    static class ParamMap extends HashMap<ParamID, String> {
        new(RosettaType c) {
            if (null !== c)
                put(new ParamID(c, -1, null), c.name.toFirstLower);
        }

        new(RosettaType c, String name) {
            put(new ParamID(c, -1, null), name);
        }

        new() {
        }

        def getClass(RosettaType c) {
            return get(new ParamID(c, -1, null));
        }
    }

    /**
     * Create a string representation of a rosetta function  
     * mainly used to give human readable names to the mapping functions used to extract attributes
     */
    def StringConcatenationClient toNodeLabel(RosettaExpression expr) {
        switch (expr) {
            RosettaGroupByFeatureCall: {
                toNodeLabel(expr.call)
            }
            RosettaFeatureCall: {
                toNodeLabel(expr)
            }
            RosettaBinaryOperation: {
                toNodeLabel(expr)
            }
            RosettaStringLiteral: {
                '''\"«expr.value»\"'''
            }
            RosettaConditionalExpression: {
                '''choice'''
            }
            RosettaExistsExpression: {
                '''«toNodeLabel(expr.argument)» exists'''
            }
            RosettaEnumValueReference: {
                '''«expr.enumeration.name»'''
            }
            RosettaEnumValue: {
                '''«expr.name»'''
            }
            RosettaLiteral: {
                '''«expr.stringValue»'''
            }
            RosettaCountOperation: {
                '''«toNodeLabel(expr.argument)» count'''
            }
            default:
                throw new UnsupportedOperationException("Unsupported expression type of " + expr.class.simpleName)
        }
    }

    def StringConcatenationClient toNodeLabel(RosettaFeatureCall call) {
        val feature = call.feature
        val right = switch feature {
            RosettaMetaType,
            Attribute,
            RosettaEnumValue: feature.name
            default: throw new UnsupportedOperationException("Unsupported expression type " + feature.getClass)
        }

        val receiver = call.receiver
        val left = switch receiver {
            RosettaCallableCall: '''''' // (receiver.callable as RosettaClass).name
            RosettaFeatureCall:
                toNodeLabel(receiver)
            default:
                throw new UnsupportedOperationException("Unsupported expression type")
        }

        '''«left»->«right»'''
    }

    def StringConcatenationClient toNodeLabel(RosettaBinaryOperation binOp) {
        '''«binOp.left.toNodeLabel»«binOp.operator»«binOp.right.toNodeLabel»'''
    }

    private def StringConcatenationClient toMapperTree(StringConcatenationClient code) {
        return '''«code»''' // '''«MapperTree».of(«code»)'''
    }

}
