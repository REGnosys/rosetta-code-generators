package com.regnosys.rosetta.generator.c_sharp.expression;

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.generator.c_sharp.util.CSharpNames
import com.regnosys.rosetta.generator.c_sharp.util.CSharpType
import com.regnosys.rosetta.generator.util.RosettaFunctionExtensions
import com.regnosys.rosetta.rosetta.expression.RosettaAbsentExpression
import com.regnosys.rosetta.rosetta.expression.RosettaBinaryOperation
import com.regnosys.rosetta.rosetta.expression.RosettaBooleanLiteral
import com.regnosys.rosetta.rosetta.RosettaCallableWithArgs
import com.regnosys.rosetta.rosetta.expression.RosettaConditionalExpression
import com.regnosys.rosetta.rosetta.expression.RosettaCountOperation
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumValueReference
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.expression.RosettaExistsExpression
import com.regnosys.rosetta.rosetta.expression.RosettaExpression
import com.regnosys.rosetta.rosetta.RosettaExternalFunction
import com.regnosys.rosetta.rosetta.RosettaFeature
import com.regnosys.rosetta.rosetta.expression.RosettaFeatureCall
import com.regnosys.rosetta.rosetta.expression.RosettaIntLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaLiteral
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.rosetta.expression.RosettaOnlyExistsExpression
import com.regnosys.rosetta.rosetta.expression.RosettaStringLiteral
import com.regnosys.rosetta.rosetta.RosettaType
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.simple.Function
import com.regnosys.rosetta.rosetta.expression.ListLiteral
import com.regnosys.rosetta.rosetta.simple.ShortcutDeclaration
import com.regnosys.rosetta.types.RosettaOperators
import com.regnosys.rosetta.types.RosettaTypeProvider
import com.regnosys.rosetta.utils.ExpressionHelper
import com.rosetta.model.lib.mapper.MapperC
import java.util.HashMap
import org.eclipse.emf.ecore.EObject
import org.eclipse.xtend2.lib.StringConcatenationClient
import org.eclipse.xtext.EcoreUtil2

import static extension com.regnosys.rosetta.generator.c_sharp.enums.CSharpEnumGenerator.*
import static extension com.regnosys.rosetta.generator.c_sharp.util.CSharpTranslator.*
import com.regnosys.rosetta.rosetta.expression.RosettaOnlyElement
import com.regnosys.rosetta.rosetta.expression.RosettaUnaryOperation
import com.regnosys.rosetta.rosetta.expression.SumOperation
import com.regnosys.rosetta.rosetta.expression.ExistsModifier
import com.regnosys.rosetta.rosetta.expression.RosettaReference
import com.regnosys.rosetta.rosetta.expression.RosettaSymbolReference
import com.regnosys.rosetta.rosetta.expression.RosettaNumberLiteral
import com.regnosys.rosetta.rosetta.TypeCall

class ExpressionGenerator {

    @Inject
    protected RosettaTypeProvider typeProvider
    @Inject
    RosettaOperators operators
//    @Inject
//    CardinalityProvider cardinalityProvider // TODO: Decide if this should be used in place of isCollection
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
            RosettaOnlyExistsExpression : {
				onlyExistsExpr(expr, params)
			}
            RosettaExistsExpression: {
                existsExpr(expr, params)
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
            RosettaReference: {
				reference(expr, params, isLast)
			}
            RosettaNumberLiteral: {
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
                    «expr.ifthen.csharpCode(params)»«IF !expr.elsethen.isEmpty»,
                    «expr.elsethen.csharpCode(params)»«ENDIF»)'''
            }
            ListLiteral: {
                '''«MapperC».of(«FOR ele : expr.elements SEPARATOR ', '»«ele.csharpCode(params)»«ENDFOR»)'''
            }
			RosettaOnlyElement: {
				onlyElement(expr, params)
			}
            RosettaUnaryOperation : {
				listOperation(expr, params)
			}
            default:
                throw new UnsupportedOperationException("Unsupported expression type of " + expr?.class?.simpleName)
        }
    }

    private def String doIfName(RosettaConditionalExpression expr) {
        //if (expr.ifthen.evalulatesToMapper) "DoIf" else "ResultDoIf"
        "IfThen"
    }
    
    private def boolean isEmpty(RosettaExpression e) {
    	if (e instanceof ListLiteral) {
    		return e.elements.size === 0;
    	}
    	return false;
    }

    def StringConcatenationClient callableWithArgs(RosettaSymbolReference expr, ParamMap params) {
        val callable = expr.symbol

        return switch (callable) {
            Function: {
                funcExt.getOutput(callable).card.isMany
                '''«callable.name».Evaluate(«args(expr, params)»)'''
            }
            RosettaExternalFunction: 
            	'''(new «factory.create().toCSharpType(callable as RosettaCallableWithArgs)»().Execute(«args(expr, params)»))'''
            default:
                throw new UnsupportedOperationException("Unsupported callable with args type of " + expr.eClass.name)
        }

    }

    private def StringConcatenationClient args(RosettaSymbolReference expr, ParamMap params) {
        '''«FOR arg : expr.args SEPARATOR ', '»«arg.csharpCode(params)»«ENDFOR»'''
    }

	def StringConcatenationClient onlyExistsExpr(RosettaOnlyExistsExpression onlyExists, ParamMap params) {
		val paths = onlyExists.args.map[arg | 
			if (arg.isOptional || (arg.isMetaType && arg.isReference)) {
		        var code = '''«arg.csharpCode(params)»'''
			    // Need to split 'parent.param' into: OnlyExists(parent, "param")
			    // Removing trailing .Value for meta fields
			    val suffix = ".Value"
		        return code.endsWith(suffix) ? 
	            	code.substring(0, code.length - suffix.length).removeOptionalChar :
	            	code
	        }]
		 if (!paths.empty) {
		 	// list of attribute names
			 val fields = paths
			 	.map[path | path.substring(path.lastIndexOf(".") + 1)]
			 	.toSet
			 // common parent
			 val parents = paths
			 	.map[path | path.substring(0, path.lastIndexOf(".")).removeOptionalChar]
			 	.toSet
			 if (parents.size !== 1) {
			 	throw new IllegalArgumentException("Only exists expression with different parents " + parents.join(", "))
			 }
			'''OnlyExists(«parents.get(0)», new HashSet<string> {«fields.map['''"«it»"'''].join(", ")»})'''
		 
		}
		else '''ComparisonResult.Success()'''
    }

    def StringConcatenationClient existsExpr(RosettaExistsExpression exists, ParamMap params) {
        val arg = exists.argument
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
            '''«IF exists.modifier == ExistsModifier.SINGLE»Single«ELSEIF exists.modifier == ExistsModifier.MULTIPLE»Multiple«ENDIF»Exists(«arg.csharpCode(params)»)'''
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
        val arg = argument
        val binary = arg.findBinaryOperation
        if (binary !== null) {
                // if the arg is binary then the operator needs to be pushed down
                binary.binaryExpr(absent, params)
        } else {
            '''«doAbsentExpr(absent, arg, params)»'''
        }
    }
    
    protected def StringConcatenationClient reference(RosettaReference expr, ParamMap params, boolean isLast) {
		switch (expr) {
			RosettaSymbolReference: {
				val s = expr.symbol
				switch (s)  {
					Data: {
						'''«params.getClass(s)»'''
					}
					Attribute: {
						// Data Attributes can only be called from their conditions
		                // The current container (Data) is stored in Params, but we need also look for superTypes
		                // so we could also do: (call.eContainer as Data).allSuperTypes.map[it|params.getClass(it)].filterNull.head
		                if (s.eContainer instanceof Data) {
		                    val variableName = EcoreUtil2.getContainerOfType(expr, Data).getName.toFirstLower
		                    '''«variableName»«buildMapFunc(s, false, true)»'''
		                }
		                else
		                    '''«s.name»'''
					}
					ShortcutDeclaration: {
		                '''«s.name»(«aliasCallArgs(s)»).«IF exprHelper.usesOutputParameter(s.expression)»build()«ELSE»get()«ENDIF»'''
		            }
					RosettaEnumeration: '''Enums.«s.toCSharpType»'''
					RosettaCallableWithArgs: {
						callableWithArgs(expr, params)
					}
					default: 
						throw new UnsupportedOperationException("Unsupported symbol type of " + s?.class?.name)
				}
			}
			default: 
				throw new UnsupportedOperationException("Unsupported reference type of " + expr?.class?.name)
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
        
        if (!call.receiver.isCollection) {
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
            RosettaSymbolReference: {
                isMetaType(expr.symbol)
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
            RosettaSymbolReference: {
                isReference(expr.symbol)
            }
            RosettaFeatureCall: {
                return isReference(expr.feature)
            }
            Attribute: {
                return !expr.metaAnnotations.nullOrEmpty && expr.metaAnnotations.exists[attribute.name == "reference" || attribute.name == "address"]
            }
            default: false
        }    
    }
    
    def private boolean isCollection(EObject expr) {
        switch (expr) {
            RosettaSymbolReference: {
                expr.symbol.isCollection
            }
            RosettaFeatureCall: {
                expr.feature.isCollection || expr.receiver.isCollection
            }
            Attribute: {
                expr.card.isIsMany
            }
            Function: {
            	expr.output.isCollection
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
            RosettaSymbolReference: {
                expr.symbol.isOptional
            }
            RosettaFeatureCall: {
                expr.feature.isOptional || expr.receiver.isOptional
            }
            Function: {
                expr.output.isOptional
            }
            Attribute: {
                expr.card.optional
            }
            default: false
        } 
    }
    def private boolean isOptional(RosettaFeature feature) {
        switch (feature) {
            Attribute:
                feature.card.inf == 0
            default:
                false
        }
    }

    def StringConcatenationClient countExpr(RosettaCountOperation expr, RosettaExpression test, ParamMap params) {
        '''«expr.argument.csharpCode(params)».Count()'''
    }

    def StringConcatenationClient binaryExpr(RosettaBinaryOperation expr, RosettaExpression test, ParamMap params) {
        val left = expr.left
        val right = expr.right
        val leftRtype = typeProvider.getRType(expr.left)
        val rightRtype = typeProvider.getRType(expr.right)
        val resultType = operators.resultType(expr.operator, leftRtype, rightRtype)
        val leftType = '''«leftRtype.name.toCSharpType»'''
        val rightType = '''«rightRtype.name.toCSharpType»'''

        switch expr.operator {
            case ("and"): {
                '''
                And(«left.csharpCode(params)»,
                    «right.csharpCode(params)»)'''
            }
            case ("or"): {
                    '''
                    Or(«left.csharpCode(params)»,
                        «right.csharpCode(params)»)'''
            }
            case ("+"): {
                '''«expr.left.csharpCode(params)» + «expr.right.csharpCode(params)»'''
            }
            case ("-"): {
                '''«expr.left.csharpCode(params)» - «expr.right.csharpCode(params)»'''
            }
            case ("*"): {
                '''«expr.left.csharpCode(params)» * «expr.right.csharpCode(params)»'''
            }
            case ("/"): {
                '''«expr.left.csharpCode(params)» / «expr.right.csharpCode(params)»'''
            }
            default: {
                // Comparisons
                // FIXME isProduct isEvent stuff in QualifyFunctionGenerator. Should be removed after alias migration
                val leftExpr = expr.left.csharpCode(params)
                val rightExpr = expr.right.csharpCode(params)
                
                if (expr.left.isCollection || expr.right.isCollection) {
                    '''«leftExpr».«toComparisonFuncName(expr.operator)»(«rightExpr»)'''
                } else {
                    // TODO: Produce error message?
                    '''ComparisonResult.FromBoolean(«expr.left.csharpCode(params)» «toComparisonOp(expr.operator)» «expr.right.csharpCode(params)»)'''
                }
            }
        }
    }

    private def boolean isLogicalOperation(RosettaExpression expr) {
        if (expr instanceof RosettaBinaryOperation) return expr.operator == "and" || expr.operator == "or"
        return false
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
            '''.«attribute.propertyName»«IF isLast && attribute.isMetaType && autoValue».EmptyIfNull().Select(«attribute.name.toFirstLower» => «attribute.name.toFirstLower».Value)«ENDIF»'''
        } else {
            val memberCall = '''«IF attribute.override»(«attribute.typeCall.toCSharpType») «ENDIF»«IF !(attribute.card.eContainer instanceof Attribute)»«attribute.attributeTypeVariableName»«ENDIF».«attribute.propertyName»'''
            if (!attribute.isMetaType || !autoValue) {
                '''«memberCall»'''
            } else {// FieldWithMeta
                '''«memberCall»«IF attribute.isOptional»?«ENDIF».Value'''
            }
        }
    }

	private def CSharpType toCSharpType(TypeCall typeCall) {
        typeCall.type.toCSharpType
    }
    private def CSharpType toCSharpType(RosettaType rosType) {
        val model = rosType.model
        if (model === null)
            throw new IllegalArgumentException('''Can not create type reference. «rosType.eClass?.name» «rosType.name» is not attached to a «RosettaModel.simpleName»''')
        factory.create().toCSharpType(rosType)
    }

    private def csharpNames(Attribute attr) {
        val model = EcoreUtil2.getContainerOfType(attr, RosettaModel)
        if (model === null)
            throw new IllegalArgumentException('''Can not create type reference. «attr.eClass?.name» «attr.name» is not attached to a «RosettaModel.simpleName»''')
        factory.create()
    }

    def CSharpType metaClass(Attribute attribute) {
        val names = attribute.csharpNames
        val name = if (attribute.annotations.exists [ a |
                a.annotation?.name == "metadata" && a.attribute?.name == "reference"
            ])
                "ReferenceWithMeta" + attribute.typeCall.type.name.toFirstUpper
            else
                "FieldWithMeta" + attribute.typeCall.type.name.toFirstUpper
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
    
    private def typeName(Attribute attribute)
        // TODO: Handle Meta types
        '''«attribute.typeCall.type.toCSharpType»'''

    private def attributeTypeVariableName(Attribute attribute)
         '''«(attribute.eContainer as Data).toCSharpType.simpleName.toFirstLower»'''

	def StringConcatenationClient listOperation(RosettaUnaryOperation op, ParamMap params) {
		switch (op) {
			case SumOperation: {
				'''
				«op.argument.csharpCode(params)»
					.Sum()'''	
			}
			default:
				'''/* Unsupported list operation «op.class» */'''
		}
	}
	
	def StringConcatenationClient onlyElement(RosettaOnlyElement expr, ParamMap params) {
		'''«expr.argument.csharpCode(params)».FirstOrDefault()?'''
	}

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
            RosettaOnlyExistsExpression: {
                '''«IF expr.args.size > 1»(«ENDIF»«expr.args.map[toNodeLabel].join(", ")»«IF expr.args.size > 1»)«ENDIF» only exists'''
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
            RosettaReference: '''''' // (receiver.callable as RosettaClass).name
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
