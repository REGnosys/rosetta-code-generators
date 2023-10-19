package com.regnosys.rosetta.generator.python.func

import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Function
import com.regnosys.rosetta.rosetta.simple.Operation
import com.regnosys.rosetta.rosetta.simple.impl.FunctionImpl
import com.regnosys.rosetta.rosetta.expression.RosettaExpression
import com.regnosys.rosetta.rosetta.simple.ShortcutDeclaration
import com.regnosys.rosetta.rosetta.expression.RosettaSymbolReference
import com.regnosys.rosetta.rosetta.expression.RosettaOnlyElement
import com.regnosys.rosetta.rosetta.expression.RosettaFeatureCall
import com.regnosys.rosetta.rosetta.expression.RosettaConditionalExpression
import com.regnosys.rosetta.rosetta.expression.RosettaBinaryOperation
import java.util.ArrayList
import java.util.HashMap
import java.util.List
import java.util.Map
import java.util.Arrays
import com.regnosys.rosetta.rosetta.RosettaModel
import com.google.inject.Inject
import com.regnosys.rosetta.generator.python.util.PythonModelGeneratorUtil
import com.regnosys.rosetta.generator.python.util.PythonTranslator
import org.slf4j.LoggerFactory
import org.slf4j.Logger
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import com.regnosys.rosetta.rosetta.RosettaFeature
import com.regnosys.rosetta.rosetta.expression.RosettaExistsExpression
import com.regnosys.rosetta.rosetta.expression.RosettaAbsentExpression
import com.regnosys.rosetta.rosetta.expression.RosettaReference
import com.regnosys.rosetta.rosetta.expression.RosettaNumberLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaBooleanLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaIntLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaStringLiteral
import com.regnosys.rosetta.rosetta.expression.ListLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaCountOperation
import com.regnosys.rosetta.rosetta.expression.RosettaOnlyExistsExpression
import com.regnosys.rosetta.rosetta.RosettaEnumValueReference
import com.regnosys.rosetta.rosetta.expression.RosettaImplicitVariable
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaCallableWithArgs
import com.regnosys.rosetta.rosetta.expression.ModifiableBinaryOperation
import com.regnosys.rosetta.rosetta.simple.Segment
import com.regnosys.rosetta.rosetta.expression.MapOperation
import com.regnosys.rosetta.rosetta.expression.ReduceOperation
import com.regnosys.rosetta.rosetta.expression.SortOperation
import com.regnosys.rosetta.rosetta.expression.FilterOperation
import com.regnosys.rosetta.rosetta.TypeParameter
import org.eclipse.emf.common.util.EList
import com.regnosys.rosetta.rosetta.simple.Condition

class  PythonFunctionGenerator {
	
	static final Logger LOGGER = LoggerFactory.getLogger(PythonFunctionGenerator);
	
	var List<String> importsFound = newArrayList
	var if_cond_blocks = new ArrayList<String>()
	
	@Inject PythonModelGeneratorUtil utils;
	@Inject PythonTranslator translator
	
	val Object SymbolReference = null
	
	static def toPythonBasicType(String typename) {
		switch typename {
			case 'string':
				'str'
			case 'time':
				'time'
			case 'date':
				'date'
			case 'dateTime':
				'datetime'
			case 'zonedDateTime':
				'datetime'
			case 'number':
				'BigDecimal'
			case 'boolean':
				'bool'
			case 'int':
				'int'
			case 'calculation',
			case 'productType',
			case 'eventType':
				'str'
			default:
				(typename === null) ? null : typename.toFirstUpper
		}
	}
	
	def Map<String, ? extends CharSequence> generate(List<Function> rosettaFunctions, String version) {
		val result = new HashMap
		
		if(rosettaFunctions.size()>0){
			for(Function func: rosettaFunctions){
				val tr = func.eContainer as RosettaModel
				val namespace = tr.name
				try{
					val funcs = func.generateFunctions(version)			
					result.put(utils.toPyFunctionFileName(namespace, func.name), 
						utils.createImportsFunc(func.name) + funcs)
				}
				catch(Exception ex){
					LOGGER.error("Exception occurred generating func {}", func.name, ex)	
				}		
			} 
		}
		
		return result
	}

	private def generateFunctions(Function function,String version) {
	    
	    importsFound = getImportsFromAttributes(function)
	    //var List<String> updateForwardRefs = newArrayList
	    //updateForwardRefs.add('''«function.name».update_forward_refs()''')
	    
		'''
		«generatesBody(function)»
		
		«FOR dataImport : importsFound SEPARATOR "\n"»«dataImport»«ENDFOR»
					
		'''
		
	}
	
    private def generatesBody(Function function) {
 
    	val output = function.output
    	val defaultClassName = function.name+"Default"
		'''	
		
		class «function.name»(ABC):
			def __init__(self,«generatesInputs(function)»):
				«FOR inp : function.inputs SEPARATOR "\n"»self.«inp.name»=«inp.name»«ENDFOR»
				
			def evaluate(self):
				«IF function.conditions !== null»
					«generateFuncConditions(function,function.conditions)»
				«ENDIF»
				«output.name» = self.doEvaluate()
				«IF function.postConditions !== null»	
					«generateFuncConditions(function,function.postConditions)»	
				«ENDIF»
				return «output.name»
			
			@abstractmethod
			def doEvaluate(self):
				pass
			
			«getAliases(function)»	
			

		class «defaultClassName»(«function.name»):
			def doEvaluate(self):
				«generateOutput(output)»
				return self.assignOutput(«output.name»)
							
			def assignOutput(self,«output.name»):
				«generateConditions(function)»  
				«IF !checkBasicType(function.output) && !isList(function.output)»
				«output.name» = «output.typeCall.type.name»(«createObject(function)»)
				«ENDIF»
				return «output.name»
				
			«IF function.shortcuts !== null»
			«FOR shortcut : function.shortcuts»
			def «shortcut.name»(self):
			«generateAliasCondition(shortcut,function, 0)»
			«ENDFOR»
			«ENDIF»	
		'''
	}
	
	/* ********************************************************************** */
	/* ***	   OUTPUT GENERATION	  										*** */
	/* ********************************************************************** */
	
	private def createObject(Function f) {
		var obj = ""
		for (var i = 0;i < f.operations.size;i++) {
			var attr = f.operations.get(i).path.attribute
			var typeName = attr.name
			var param = attr.typeCall.type instanceof RosettaEnumeration ?
			attr.typeCall.type.name+".returnResult_"+Integer.toString(i)+"()":getObjects(f.operations.get(i).path,i,"",0)
			obj+=typeName+" = "+param
			if (i!=f.operations.size-1) obj+=", "
		}
		'''«obj»'''
	}
	
	//Iterative versionn
	/*/private def getObjects(Operation op,int i) {
		var s = op.path
		var obj = ""
		if (s.next !== null) {
			var parenthesis = 0
			obj+="_get_rosetta_object("+'"'+s.attribute.typeCall.type.name+'"'+","+'"'+
									     s.next.attribute.name+'"'
			while (s.next !== null) {
				if (s.next.next===null) obj+=", returnResult_"+Integer.toString(i)+")"
				else {
					obj+= ", _get_rosetta_object("+'"'+s.attribute.typeCall.type.name+'"'+","+
									         '"'+s.next.attribute.name+'"'
					parenthesis++
				}
				s = s.next
			}
			for (var j = 0;j < parenthesis;j++) obj+=")"
			
		}
		else obj+="returnResult_"+Integer.toString(i)
		'''«obj»'''
	} */
	
	//Recursive version
	private def String getObjects(Segment s,int i,String object,int parenthesis) {
		var obj = object
		if (s.next !== null) {
			obj+="_get_rosetta_object("+'"'+s.attribute.typeCall.type.name+'"'+","+'"'+
									     s.next.attribute.name+'"'
			if (s.next.next===null) {
				obj+=", returnResult_"+Integer.toString(i)+"())"
				for (var j = 0;j < parenthesis;j++) obj+=")"
			}
			else {
				obj+= ", "+getObjects(s.next,i,obj,parenthesis+1)
			}
	
		}
			
		else obj+="returnResult_"+Integer.toString(i)+"()"
		'''«obj»'''
		
	}
	
	/* ********************************************************************** */
	/* ***	              END  OUTPUT GENERATION	  					   *** */
	/* ********************************************************************** */
	
	/* ********************************************************************** */
	/* ***	    Generation of function conditions and postcondition		  *** */
	/* ********************************************************************** */
	
	
	private def generateFuncConditions(Function function,EList<Condition> cond) {
		var n_condition = 0;
		var res = "";
		for (Condition c : cond) {
		    res += generateFuncConditionBoilerplate(c,n_condition)+
		    generateFuncExpressionCondition(function,c.expression,n_condition).toString
		}
		for (Condition c: cond) {
			var msg = c.definition !== null?c.definition:"Error"
			res+="validateCondition("+c.name+"()"+","+'"'+msg+'"'+")\n"
		}
		return res
	}
	
	private def generateFuncConditionBoilerplate(Condition c,int n_condition) {
		'''
		def «c.name»():
		'''
	}
	
	private def generateFuncExpressionCondition(Function function,RosettaExpression exp,int n_condition) {
		if_cond_blocks = new ArrayList<String>()
		var expr = generateExpression(exp,function, 0)
		var blocks = ""
		if (!if_cond_blocks.isEmpty()) {
			blocks = '''	«FOR arg : if_cond_blocks»«arg»«ENDFOR»'''
		}
		'''
		«blocks»	return «expr»
		'''	
		
	}
	
	/* ********************************************************************** */
	/* ***	   END of function conditions and postcondition		  *** */
	/* ********************************************************************** */
	
	
	private def generateConditions(Function function) {
		var n_condition = 0;
		var res = '';
		for (Operation op : function.operations) {
		    res += generateConditionBoilerPlate(op, n_condition)+generateExpressionCondition(function,op,n_condition)
			n_condition += 1;
		}
		return res
	}

	private def generateConditionBoilerPlate(Operation op, int n_condition) {
		'''
		def returnResult_«n_condition»():
		«IF op.definition!==null»
			"""
			«op.definition»
			"""
		«ENDIF»
		'''
	}
	
	/* ********************************************************************** */
	/* ***	   ALIAS GENERATION	  										  *** */
	/* ********************************************************************** */
	
	private def generateAliasCondition(ShortcutDeclaration s,Function function,int n_condition) {
		if_cond_blocks = new ArrayList<String>()
		var expr = generateExpression(s.expression,function, 0)
		var blocks = ""
		if (!if_cond_blocks.isEmpty()) {
			blocks = '''	«FOR arg : if_cond_blocks»«arg»«ENDFOR»'''
		}
		return 
		'''
		«blocks»	return «expr»
		
		'''
	}
	
	private def getAliases(Function function) {
		var out = ""
		for (shortcuts: function.shortcuts) {
			out+=getAlias(function,shortcuts)
		}
		'''
		«out»
		'''
	}
	
	private def getAlias(Function function,ShortcutDeclaration s) {
		'''
		@abstractmethod
		def «s.name»(self):
			pass
		'''
	}
	
	/* ********************************************************************** */
	/* ***	  END ALIAS GENERATION	  										*** */
	/* ********************************************************************** */
	
	private def generateExpressionCondition(Function function, Operation op,int n_condition) {
		if_cond_blocks = new ArrayList<String>()
		var expr = generateExpression(op.expression,function, 0)
		var blocks = ""
		if (!if_cond_blocks.isEmpty()) {
			blocks = '''	«FOR arg : if_cond_blocks»«arg»«ENDFOR»'''
		}
		return 
		'''
		«blocks»	return «expr»
		
		«IF isList(function.output)» 
		«function.output.name».extend(returnResult_«n_condition»)
		«ELSEIF checkBasicType(function.output)»
		«function.output.name» = returnResult_«n_condition»()
		«ENDIF»
		'''
	}
	
	
	

	def addImportsFromConditions(String variable, String namespace) {
		val import = '''from «namespace».«variable» import «variable»'''
		if (!importsFound.contains(import)) {
			importsFound.add(import)
		}
	}
	
	/* ********************************************************************** */
	/* ***				   BEGIN expression generation				   *** */
	/* ********************************************************************** */

	def String generateExpression(RosettaExpression expr, Function function,int iflvl) {
		switch (expr) {
			RosettaConditionalExpression: {
				// val nslashes = (2**iflvl - 1) as int;
				// val escsec = '\\'.repeat(nslashes) + "'";
				val ifexpr = generateExpression(expr.getIf(), function,iflvl + 1)
				val ifthen = generateExpression(expr.ifthen,function, iflvl + 1)
				var elsethen = expr.elsethen !== null && expr.full ? generateExpression(expr.elsethen,
						function,iflvl + 1) : 'True'

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
				var receiver = generateExpression(expr.receiver,function, iflvl)
				if (receiver === null) {
					'''«right»'''
				} else {
					'''_resolve_rosetta_attr(«receiver», "«right»")'''
				}

			}
			RosettaExistsExpression: {
				val argument = expr.argument as RosettaExpression
				'''((«generateExpression(argument,function, iflvl)») is not None)'''
			}
			RosettaBinaryOperation: {
				binaryExpr(expr, function,iflvl)
			}
			RosettaAbsentExpression: {
				val argument = expr.argument as RosettaExpression
				'''((«generateExpression(argument,function, iflvl)») is None)'''
			}
			RosettaReference: {
				reference(expr, function,iflvl)
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
				'''(«generateExpression(argument,function, iflvl)»)'''
			}
			RosettaEnumValueReference: {
				val value = EnumHelper.convertValues(expr.value)
				'''«expr.enumeration».«value»'''
			}
			RosettaOnlyExistsExpression: {
				var aux = expr as RosettaOnlyExistsExpression;
				'''check_one_of_constraint(self, «generateExpression(aux.getArgs().get(0),function, iflvl)»)'''
			}
			RosettaCountOperation: {
				val argument = expr.argument as RosettaExpression
				'''len(«generateExpression(argument,function, iflvl)»)'''
			}
			ListLiteral: {
				'''[«FOR arg : expr.elements SEPARATOR ', '»«generateExpression(arg,function, iflvl)»«ENDFOR»]'''
			}
			MapOperation: {
				val argument = expr.argument as RosettaExpression
				'''list(map(lambda «generateExpression(argument,function, iflvl)»:«generateExpression(expr.function.body,function, iflvl)»,«generateExpression(argument,function, iflvl)»))'''
			}
			ReduceOperation: {
				
			}
			SortOperation: {
				
			}
			FilterOperation: {
				val argument = expr.argument as RosettaExpression
				'''list(filter(lambda «generateExpression(argument,function, iflvl)»:«generateExpression(expr.function.body,function, iflvl)»,«generateExpression(argument,function, iflvl)»))'''
			}
			default:
				throw new UnsupportedOperationException("Unsupported expression type of " + expr?.class?.simpleName)
		}
	}
	

	protected def String reference(RosettaReference expr,Function function, int iflvl) {
		switch (expr) {
			RosettaImplicitVariable: {
			}
			RosettaSymbolReference: {
				symbolReference(expr,function, iflvl)
			}
		}
	}

	def String symbolReference(RosettaSymbolReference expr,Function function, int iflvl) {
		val s = expr.symbol
		switch (s) {
			Function: {
				'''«s.name»Default(«generatesInputs(s)»).evaluate()'''
			}
			Attribute: {
				'''_resolve_rosetta_attr(self, "«s.name»")'''
			}
			RosettaEnumeration: {
				'''«s.name»'''
			}
			RosettaCallableWithArgs: {
				callableWithArgsCall(s, expr, iflvl,function)
			}
			ShortcutDeclaration: {
				'''self.«s.name»()'''
			}
			default:
				throw new UnsupportedOperationException("Unsupported callable type of " + s.class.simpleName)
		}
	}
	
	def String callableWithArgsCall(RosettaCallableWithArgs s, RosettaSymbolReference expr, int iflvl,Function function) {
		if (s instanceof FunctionImpl)
			addImportsFromConditions(s.getName(), (s.eContainer as RosettaModel).name + "." + "functions")
		else
			addImportsFromConditions(s.name, (s.eContainer as RosettaModel).name)
		var args = '''«FOR arg : expr.args SEPARATOR ', '»«generateExpression(arg,function, iflvl)»«ENDFOR»'''
		'''«s.name»(«args»)'''

	}

	def String binaryExpr(RosettaBinaryOperation expr,Function function,int iflvl) {
		if (expr instanceof ModifiableBinaryOperation) {
			if (expr.cardMod !== null) {
				if (expr.operator == "<>") {
					'''any_elements(«generateExpression(expr.left,function, iflvl)», "«expr.operator»", «generateExpression(expr.right,function, iflvl)»)'''
				} else {
					'''all_elements(«generateExpression(expr.left,function, iflvl)», "«expr.operator»", «generateExpression(expr.right, function,iflvl)»)'''
				}
			}
		} else {
			switch expr.operator {
				case ("="): {
					'''(«generateExpression(expr.left,function, iflvl)» == «generateExpression(expr.right,function, iflvl)»)'''
				}
				case ("<>"): {
					'''(«generateExpression(expr.left,function, iflvl)» != «generateExpression(expr.right,function, iflvl)»)'''
				}
				case ("contains"): {
					'''contains(«generateExpression(expr.left,function, iflvl)», «generateExpression(expr.right,function, iflvl)»)'''

				}
				case ("disjoint"): {
					'''disjoint(«generateExpression(expr.left,function, iflvl)», «generateExpression(expr.right, function,iflvl)»)'''

				}
				case ("join"): {
					'''join(«generateExpression(expr.left,function, iflvl)», «generateExpression(expr.right,function, iflvl)»)'''
				}
				default: {
					'''(«generateExpression(expr.left,function, iflvl)» «expr.operator» «generateExpression(expr.right,function, iflvl)»)'''
				}
			}
		}
	}
	
	/* ********************************************************************** */
	/* ***					  END condition generation				  *** */
	/* ********************************************************************** */

	
	
	private def generateOutput(Attribute output) {
		var out = ""
		val outputName = output.name
		if (output.getCard.unbounded) out = outputName+"=[]"
		else out = outputName+"=None"
		'''
		«out»
		'''
	}
	
	private def boolean isList(Attribute output) {
		return output.getCard.unbounded
	}
	
	
	
	private def getImportsFromAttributes(Function function) {
		var filteredAttributes = new ArrayList
		for (f : function.inputs) if (!checkBasicType(f)) filteredAttributes.add(f)
		if (!checkBasicType(function.output)) filteredAttributes.add(function.output)
		
		val imports = newArrayList
		for (attribute : filteredAttributes) {
			val originalIt = attribute
			val model = function.model
			if (model !== null) {
				val importStatement = '''from «model.name».«translator.toPythonType(originalIt)» import «translator.toPythonType(originalIt)»'''
				imports.add(importStatement)
			}

		}

		// Remove duplicates by converting the list to a set and back to a list
		return imports.toSet.toList
		
	}
	
	
	
	def checkBasicType(Attribute attr) {
		val types = Arrays.asList('int', 'str', 'Decimal', 'date', 'datetime', 'datetime.date', 'datetime.time', 'time',
			'bool', 'number')
		return (attr !== null && translator.toPythonType(attr) !== null) ? types.contains(translator.toPythonType(attr).toString()) : false
	}
	
	
 	
	private def generatesInputs(Function function) {
		
		val inputs = orderInputs(function.inputs)
		
		var result=""
		var count =0
		for(Attribute input: inputs){
			count+=1
			result+=input.name
			if(input.card.inf==0)
				result+="=None"
			if(count<inputs.size())
				result+=", "
		}
		'''«result»'''
	}
	
	private def List<Attribute> orderInputs(List<Attribute> inputs){
		val orderedInputs = new ArrayList<Attribute>();
		
		for(Attribute input: inputs){
			if(input.card.inf!=0)
				orderedInputs.add(input)
		}
		for(Attribute input: inputs){
			if(!orderedInputs.contains(input))
				orderedInputs.add(input)
		}
		orderedInputs
	}
}