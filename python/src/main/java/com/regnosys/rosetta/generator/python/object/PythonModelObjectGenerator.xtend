package com.regnosys.rosetta.generator.python.object

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import com.regnosys.rosetta.generator.python.util.PythonModelGeneratorUtil
import com.regnosys.rosetta.rosetta.RosettaCallableWithArgs
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumValueReference
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaFeature
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.rosetta.expression.ChoiceOperation
import com.regnosys.rosetta.rosetta.expression.ListLiteral
import com.regnosys.rosetta.rosetta.expression.ModifiableBinaryOperation
import com.regnosys.rosetta.rosetta.expression.Necessity
import com.regnosys.rosetta.rosetta.expression.OneOfOperation
import com.regnosys.rosetta.rosetta.expression.RosettaAbsentExpression
import com.regnosys.rosetta.rosetta.expression.RosettaBinaryOperation
import com.regnosys.rosetta.rosetta.expression.RosettaBooleanLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaConditionalExpression
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
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Condition
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.simple.impl.FunctionImpl
import java.util.ArrayList
import java.util.Arrays
import java.util.Collection
import java.util.HashMap
import java.util.List
import java.util.Map

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*

class PythonModelObjectGenerator {

	@Inject extension RosettaExtensions
	@Inject extension PythonModelObjectBoilerPlate
	
	
	@Inject
	PythonModelGeneratorUtil utils;

	
	var List<String> importsFound = newArrayList
	var if_cond_blocks = new ArrayList<String>()

	static def toPythonBasicType(String typename) {
		switch typename {
			case 'string': 'str'
			case 'time': 'time'
			case 'date': 'date'
			case 'dateTime': 'datetime'
			case 'zonedDateTime': 'datetime'
			case 'number': 'Decimal'
			case 'boolean': 'bool'
			case 'int': 'int'
			case 'calculation',				
			case 'productType',				
			case 'eventType':
				'str'
			default: (typename === null) ? null : typename.toFirstUpper
		}
	}

	static def toPythonType(Data c, ExpandedAttribute attribute) throws Exception {
		var basicType = toPythonBasicType(attribute.type.name);
		if (basicType === null) {
			throw new Exception ("Attribute type is null for " + attribute.name + " for class " + c.name)
		}
		if (attribute.hasMetas) {
			var helper_class = "Attribute";
			var is_ref = false;
			var is_address = false;
			var is_meta = false;
			for (ExpandedAttribute meta : attribute.getMetas()) {
				val mname = meta.getName();
				if (mname == "reference") { // what about location?!?
					is_ref = true;
				} else if (mname == "address") {
					is_address = true;
				} else if (mname == "key" || mname == "id" || 
					mname == "scheme" || mname == "location") { 
					is_meta = true;
				} else {
					helper_class += "---" + mname + "---";
				}
			}
			if (is_meta) {
				helper_class += "WithMeta";
			}
	 		if (is_address) {
				helper_class += "WithAddress";
			}
	 		if (is_ref) {
	 			helper_class += "WithReference";
			}
			if (is_meta || is_address) {
				helper_class += "[" + basicType + "]";
			}

  			basicType = helper_class + " | " + basicType;
		}
	   	return basicType
	}
	
	def Map<String, ? extends CharSequence> generate(
		Iterable<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version, Collection<? extends RosettaModel> models
	) {
		val result = new HashMap
		
		for(Data type: rosettaClasses){
			val model   = type.eContainer as RosettaModel
			val classes = type.generateClasses(version, models).replaceTabsWithSpaces
			result.put(utils.toPyFileName(model.name, type.name), utils.createImports(type.name) + classes)
		}
		
		result;
	}
	
	def boolean checkBasicType(ExpandedAttribute attr) {
		val types = Arrays.asList('int', 'str', 'Decimal', 'date', 'datetime', 'datetime.date', 'datetime.time', 'time', 'bool', 'number')
		if(attr!==null){	
			if(attr.toRawType!==null)
				return types.contains(attr.toRawType.toString())	
			else
				return false
		}
		else{
			return false
		} 
	 }
	 def boolean checkBasicType(String attr) {
		val types = Arrays.asList('int', 'str', 'Decimal', 'date', 'datetime', 'datetime.date', 'datetime.time', 'time', 'bool','number')
		try {
			return types.contains(attr)
		} catch (Exception ex) {
			return false
		}
	 }

	/**
	 * Generate the classes
	 */
	 // TODO remove Date implementation in beginning
	 // TODO removed one-of condition due to limitations after instantiation of objects
   private def generateClasses(Data rosettaClass, String version, Collection<? extends RosettaModel> models) {
		var List<String> enumImports = newArrayList
		var List<String> dataImports = newArrayList
		var List<String> classDefinitions = newArrayList
		var List<String> updateForwardRefs = newArrayList
		var superType = rosettaClass.superType
		if(superType!== null && superType.name === null){
			throw new Exception ("SuperType is null for " + rosettaClass.name)
        }
		importsFound = getImportsFromAttributes(rosettaClass)
		
		val classDefinition = generateClassDefinition(rosettaClass)
		classDefinitions.add(classDefinition)	  
		updateForwardRefs.add('''«rosettaClass.name».update_forward_refs()''')
		
	
		// Remove duplicates
		enumImports = enumImports.toSet().toList()
		dataImports = dataImports.toSet().toList()
	
		// Return generated classes
		return '''
	«IF superType!==null»from «(superType.eContainer as RosettaModel).name».«superType.name» import «superType.name»«ENDIF»
	
	«classDefinition»
	
	«FOR dataImport : importsFound SEPARATOR "\n"»«dataImport»«ENDFOR»
	
	«FOR updateForwardRef : updateForwardRefs SEPARATOR "\n"»«updateForwardRef»«ENDFOR»
	'''
	}
	
	private def getImportsFromAttributes(Data rosettaClass) {
		val filteredAttributes = rosettaClass.allExpandedAttributes
			.filter[enclosingType == rosettaClass.name]
			.filter[(it.name!=="reference") && (it.name!=="meta") && (it.name!=="scheme")]
			.filter[!checkBasicType(it)]
	
		val imports = newArrayList
		for (attribute : filteredAttributes) {
			val originalIt = attribute
			val model = attribute.type.model
			if(model!==null){
				 val importStatement = '''from «model.name».«originalIt.toRawType» import «originalIt.toRawType»'''
				imports.add(importStatement)
			}
		   
		}
	
		// Remove duplicates by converting the list to a set and back to a list
		return imports.toSet.toList
	}


	
	private def generateClassDefinition(Data rosettaClass) {
		return '''
		class «rosettaClass.name»«IF rosettaClass.superType === null»«ENDIF»«IF rosettaClass.superType !== null»(«rosettaClass.superType.name»):«ELSE»(BaseDataClass):«ENDIF»
			«IF rosettaClass.definition !== null»
			"""
			«rosettaClass.definition»
			"""
			«ENDIF»
			«generateAttributes(rosettaClass)»
			«generateConditions(rosettaClass)»
		'''
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
	
	/* ********************************************************************** */
	/* ***				   BEGIN condition generation				   *** */	
	/* ********************************************************************** */
	private def generateConditions(Data cls) {
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
		
 		if(expression instanceof ChoiceOperation){
 			attributes = expression.attributes
 			if(expression.necessity == Necessity.OPTIONAL){
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
		return 
		'''«blocks»	return «expr»
		'''
	}
	
	def addImportsFromConditions(String variable, String namespace){
		val import = '''from «namespace».«variable» import «variable»'''
		if(!importsFound.contains(import)){
			importsFound.add(import)
		}
	}

	def String generateExpression(RosettaExpression expr, int iflvl) {
		switch (expr) {
			RosettaConditionalExpression: {
				// val nslashes = (2**iflvl - 1) as int;
				// val escsec = '\\'.repeat(nslashes) + "'";
				val ifexpr = generateExpression(expr.getIf(), iflvl+1)
				val ifthen = generateExpression(expr.ifthen, iflvl+1)
				var elsethen = expr.elsethen !== null && expr.full? generateExpression(expr.elsethen, iflvl+1): 'True'
				
				val if_blocks = 
				'''
				def _then_fn«iflvl»():
					return «ifthen»

				def _else_fn«iflvl»():
					return «elsethen»

				'''
				if_cond_blocks.add(if_blocks)

				//'''if_cond(«ifexpr», «escsec»«ifthen»«escsec», «escsec»«elsethen»«escsec», self)'''
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
					RosettaEnumValue:{
						val rosettaValue = expr.feature as RosettaEnumValue
						val value = EnumHelper.convertValues(rosettaValue)
						
						val symbol = (expr.receiver as RosettaSymbolReference).symbol
						val model = symbol.eContainer as RosettaModel
						addImportsFromConditions(symbol.name, model.name)
						
						value
					} 
					//TODO: RosettaFeature: '''.Select(x => x.«feature.name.toFirstUpper»)'''
					RosettaFeature:{
						expr.feature.name
					} 
					default:
						throw new UnsupportedOperationException("Unsupported expression type of " + expr.feature.eClass.name)
				}
										   
				if(right=="None")
					right="NONE"
				var receiver = generateExpression(expr.receiver, iflvl)				
				if(receiver===null){
					'''«right»'''
				}
				else{								
					'''«receiver».«right»'''
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
				if(expr.value=="true")
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
			RosettaOnlyElement:{
				val argument = expr.argument as RosettaExpression		   	
				'''(«generateExpression(argument, iflvl)»)'''
			}
			RosettaEnumValueReference: {			
				val value = EnumHelper.convertValues(expr.value)			  
				'''«expr.enumeration».«value»'''
			}

			RosettaOnlyExistsExpression : {
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
			RosettaSymbolReference:{
				symbolReference(expr, iflvl)
			}
		}   
	}
	
	def String symbolReference(RosettaSymbolReference expr, int iflvl){
		val s = expr.symbol
		switch (s)  {
			Data: {   								
				'''«s.name»'''
			}
			Attribute: {
				'''self.«s.name»'''
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
	
	def String callableWithArgsCall(RosettaCallableWithArgs s, RosettaSymbolReference expr, int iflvl){
		if(s instanceof FunctionImpl)
			addImportsFromConditions(s.getName (), (s.eContainer as RosettaModel).name+"."+"functions")
		else
			addImportsFromConditions(s.name, (s.eContainer as RosettaModel).name)
		var args = '''«FOR arg : expr.args SEPARATOR ', '»«generateExpression(arg, iflvl)»«ENDFOR»'''
		'''«s.name»(«args»)'''
		
		
	}


	def String binaryExpr(RosettaBinaryOperation expr, int iflvl) {
		 if(expr instanceof ModifiableBinaryOperation){
		 	if(expr.cardMod!==null){ 	
		 		if(expr.operator=="<>"){
		 		'''any_elements(«generateExpression(expr.left, iflvl)», "«expr.operator»", «generateExpression(expr.right, iflvl)»)'''   	 	
		 		}
		 		else{
		 		'''all_elements(«generateExpression(expr.left, iflvl)», "«expr.operator»", «generateExpression(expr.right, iflvl)»)'''   	 	   	 
		 		}
		 	}
		 }
		else {
			switch expr.operator {
				case ("="): {
					'''(«generateExpression(expr.left, iflvl)» == «generateExpression(expr.right, iflvl)»)'''
				}
				case ("<>"): {
					'''(«generateExpression(expr.left, iflvl)» != «generateExpression(expr.right, iflvl)»)'''
				}
				case("contains"):{
					'''contains(«generateExpression(expr.left, iflvl)», «generateExpression(expr.right, iflvl)»)'''
					
				}
				case("disjoint"):{
					'''disjoint(«generateExpression(expr.left, iflvl)», «generateExpression(expr.right, iflvl)»)'''
					
				}
				case("join"):{
					'''join(«generateExpression(expr.left, iflvl)», «generateExpression(expr.right, iflvl)»)'''
				}
				default: {
					'''(«generateExpression(expr.left, iflvl)» «expr.operator» «generateExpression(expr.right, iflvl)»)'''
				}
			}
		}   
	}
	/* ********************************************************************** */
	/* ***					  END condition generation				  *** */
	/* ********************************************************************** */
	
	 private def generateAttributes(Data c) {
		val attr = c.allExpandedAttributes.filter[enclosingType == c.name].filter[(it.name!=="reference") && (it.name!=="meta") && (it.name!=="scheme")]
		val attrSize = attr.size()
		val conditionsSize = c.conditions.size()
		'''«IF attrSize === 0 && conditionsSize===0»pass«ELSE»«FOR attribute : attr SEPARATOR ""»«generateExpandedAttribute(c, attribute)»«ENDFOR»«ENDIF»'''
	}

	 private def generateExpandedAttribute(Data c, ExpandedAttribute attribute) {
		var att = ""
		if (attribute.sup > 1 || attribute.unbound) {
			att += "List[" + toPythonType(c, attribute) + "]"
		}
		else {
 			if (attribute.inf == 0) { // edge case (0..0) will come here
				att += "Optional[" + toPythonType(c, attribute) + "]"	
			}
			else {
				att += toPythonType(c, attribute) // cardinality (1..1)
			}
		}

  		var field_default = 'None'
 		if (attribute.inf == 1 && attribute.sup == 1)
			field_default = '...' // mandatory field -> cardinality (1..1)
		else if (attribute.sup > 1 || attribute.unbound) { // List filed of cardinality (m..n)
			field_default = '[]'
		}

  		var attrName = ""
 		if (attribute.name == "global")
			attrName = "_global"
		else
			attrName = attribute.name

		var need_card_check = true;
		if ((attribute.inf == 0 && attribute.sup == 1) || 
			(attribute.inf == 1 && attribute.sup == 1) ||
			(attribute.inf == 0 && attribute.unbound)
		) {
			need_card_check = false;
		}
  		var sup_str = attribute.sup.toString();
		if (attribute.unbound) {
			sup_str = 'None';
		}
		'''
		«attrName»: «att» = Field(«field_default», description="«attribute.definition»")
		«IF attribute.definition !== null»
		"""
		«attribute.definition»
		"""
		«ENDIF»
		«IF need_card_check»
		@rosetta_condition
		def cardinality_«attrName»(self):
			return check_cardinality(self.«attrName», «attribute.inf», «sup_str»)
		
		«ENDIF»
		'''
				
	}

	

	def Iterable<ExpandedAttribute> allExpandedAttributes(Data type){
		type.allSuperTypes.map[it.expandedAttributes].flatten
	}
	
	def String definition(Data element){
		element.definition
	}
}