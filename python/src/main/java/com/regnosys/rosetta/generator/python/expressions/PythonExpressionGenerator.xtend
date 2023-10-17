package com.regnosys.rosetta.generator.python.expressions


import com.regnosys.rosetta.rosetta.simple.Condition
import com.regnosys.rosetta.rosetta.simple.Data


import java.util.Map
import java.util.ArrayList
import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.generator.python.object.PythonModelObjectBoilerPlate
import com.regnosys.rosetta.generator.python.util.PythonModelGeneratorUtil
import com.regnosys.rosetta.rosetta.expression.ChoiceOperation
import com.regnosys.rosetta.rosetta.expression.Necessity
import com.regnosys.rosetta.rosetta.expression.RosettaExpression
import com.regnosys.rosetta.rosetta.expression.RosettaConditionalExpression
import com.regnosys.rosetta.rosetta.expression.RosettaFeatureCall
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import com.regnosys.rosetta.rosetta.expression.RosettaSymbolReference
import com.regnosys.rosetta.rosetta.RosettaModel
import java.util.List
import com.regnosys.rosetta.rosetta.RosettaFeature
import com.regnosys.rosetta.rosetta.expression.RosettaExistsExpression
import com.regnosys.rosetta.rosetta.expression.RosettaBinaryOperation
import com.regnosys.rosetta.rosetta.expression.RosettaAbsentExpression
import com.regnosys.rosetta.rosetta.expression.RosettaReference
import com.regnosys.rosetta.rosetta.expression.RosettaNumberLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaBooleanLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaIntLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaStringLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaOnlyElement
import com.regnosys.rosetta.rosetta.RosettaEnumValueReference
import com.regnosys.rosetta.rosetta.expression.RosettaOnlyExistsExpression
import com.regnosys.rosetta.rosetta.expression.RosettaCountOperation
import com.regnosys.rosetta.rosetta.expression.ListLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaImplicitVariable
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaCallableWithArgs
import com.regnosys.rosetta.rosetta.simple.impl.FunctionImpl
import com.regnosys.rosetta.rosetta.expression.ModifiableBinaryOperation
import com.regnosys.rosetta.rosetta.expression.OneOfOperation

class PythonExpressionGenerator {
	
	@Inject extension RosettaExtensions
	@Inject extension PythonModelObjectBoilerPlate

	@Inject
	PythonModelGeneratorUtil utils;
	
	public var List<String> importsFound
	var if_cond_blocks = new ArrayList<String>()
	
	public def generateConditions(Data cls) {
        // Move your condition and expression-related logic here
        var n_condition = 0;
        var res = '';
        for (Condition cond : cls.conditions) {
            res += generateConditionBoilerPlate(cond, n_condition)
            if (cond.isConstraintCondition)
                res += generateConstraintCondition(cls, cond)
            else
                res += generateExpressionCondition(cls, cond)
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
		'''	return self.check_one_of_constraint(«FOR a : attributes SEPARATOR ", "»'«a.name»'«ENDFOR», «necessity»)
		'''

	}
	
	private def generateExpressionCondition(Data cls, Condition c) {
		if_cond_blocks = new ArrayList<String>()
		var expr = generateExpression(c.expression, 0)
		var blocks = ""
		if (!if_cond_blocks.isEmpty()) {
			blocks = '''	«FOR arg : if_cond_blocks»«arg»«ENDFOR»'''
		}
		return '''«blocks»	return «expr»
		'''
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
				'''(«generateExpression(argument, iflvl)»)'''
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
				'''len(«generateExpression(argument, iflvl)»)'''
			}
			ListLiteral: {
				'''[«FOR arg : expr.elements SEPARATOR ', '»«generateExpression(arg, iflvl)»«ENDFOR»]'''
			}
			default:
				throw new UnsupportedOperationException("Unsupported expression type of " + expr?.class?.simpleName)
		}
	}

	protected def String reference(RosettaReference expr, int iflvl) {
		switch (expr) {
			RosettaImplicitVariable: {
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
		if (!importsFound.contains(import)) {
			importsFound.add(import)
		}
	}
	
	
}