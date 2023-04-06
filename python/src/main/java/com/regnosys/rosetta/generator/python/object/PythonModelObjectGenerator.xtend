package com.regnosys.rosetta.generator.python.object

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.expression.RosettaConditionalExpression
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.simple.Condition
import java.util.List
import java.util.Map
import java.util.Set
import com.regnosys.rosetta.rosetta.expression.RosettaAbsentExpression
import com.regnosys.rosetta.rosetta.expression.RosettaBigDecimalLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaBinaryOperation
import com.regnosys.rosetta.rosetta.expression.RosettaBooleanLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaCountOperation
import com.regnosys.rosetta.rosetta.RosettaEnumValueReference
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaCallableWithArgs
import com.regnosys.rosetta.rosetta.expression.RosettaExistsExpression
import com.regnosys.rosetta.rosetta.expression.RosettaExpression
import com.regnosys.rosetta.rosetta.expression.RosettaFeatureCall
import com.regnosys.rosetta.rosetta.expression.RosettaOnlyElement
import com.regnosys.rosetta.rosetta.expression.RosettaIntLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaOnlyExistsExpression
import com.regnosys.rosetta.rosetta.expression.RosettaStringLiteral
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.expression.ListLiteral
import com.regnosys.rosetta.rosetta.expression.ListOperation
import java.util.HashMap
import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*
import com.regnosys.rosetta.rosetta.expression.Necessity
import java.util.ArrayList
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaFeature
import java.util.Arrays
import com.regnosys.rosetta.types.RQualifiedType
import com.regnosys.rosetta.types.RCalculationType
import com.regnosys.rosetta.rosetta.expression.OneOfOperation
import com.regnosys.rosetta.rosetta.expression.ChoiceOperation
import com.regnosys.rosetta.rosetta.expression.RosettaReference
import com.regnosys.rosetta.rosetta.expression.RosettaImplicitVariable
import com.regnosys.rosetta.rosetta.expression.RosettaSymbolReference
import com.regnosys.rosetta.rosetta.expression.ModifiableBinaryOperation
import com.regnosys.rosetta.rosetta.expression.FilterOperation
import com.regnosys.rosetta.rosetta.expression.SumOperation
import com.regnosys.rosetta.generator.java.enums.EnumHelper

class PythonModelObjectGenerator {

    @Inject extension RosettaExtensions
    @Inject extension PythonModelObjectBoilerPlate
    @Inject extension PythonMetaFieldGenerator

    static final String CLASSES_FILENAME = 'Types.kt'
    static final String META_FILENAME = 'Metatypes.kt'
    
    var importedFromConditions = new ArrayList<String>()

    static def toPythonBasicType(String typename) {
        switch typename {
            case 'string': 'str'
            case 'time': 'time'
            case 'date': 'date'
            case 'dateTime': 'datetime'
            case 'zonedDateTime': 'datetime'
            case 'number': 'float'
            case 'boolean': 'bool'
            case 'int': 'int'
            case RQualifiedType.PRODUCT_TYPE.qualifiedType: 'str'
            case RQualifiedType.EVENT_TYPE.qualifiedType: 'str'
            case RCalculationType.CALCULATION.calculationType: 'str'
        }
    }

     static def toPythonType(ExpandedAttribute attribute) {
    	val type = attribute.type;
         var basicType = toPythonBasicType(type.name);
        if (basicType === null)
             basicType = type.name.toFirstUpper
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
        Iterable<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version, HashMap<String, List<String>> importsVariables
    ) {
        val result = new HashMap
		
        val superTypes = rosettaClasses
                .map[superType]
                .map[allSuperTypes].flatten
                .toSet
		 
		if (rosettaClasses.size() > 0) {
			val classes = rosettaClasses.sortBy[name].generateClasses(superTypes, version, importsVariables).replaceTabsWithSpaces
        	result.put(CLASSES_FILENAME, classes)
		}
        
		if (metaTypes.size > 0) {
			val metaFields = rosettaClasses.sortBy[name].generateMetaFields(metaTypes, version).replaceTabsWithSpaces
        	result.put(META_FILENAME, metaFields)
		}
        result;
    }
    
    def boolean checkBasicType(ExpandedAttribute attr){    	
    	val types = Arrays.asList('int', 'str', 'float', 'date', 'datetime', 'datetime.date', 'datetime.time','time', 'bool')
    	var attrType = ""
    	try{
    		 attrType = attr.toRawType.toString()	
    	}
    	catch(Exception ex){
    		return true
    	}
    	
    	if(types.contains(attrType)){
    		return true
    	}
    	else
    		return false
    }
    
    private def sortClassesByHierarchy(List<Data> rosettaClasses) {
	    val sortedClasses = newArrayList
	
	    while (!rosettaClasses.isEmpty) {
	        val independentClasses = rosettaClasses.filter[c | c.superType === null || !rosettaClasses.contains(c.superType)].toList
	        sortedClasses.addAll(independentClasses)
	        rosettaClasses.removeAll(independentClasses)
	    }
	
	    return sortedClasses
	}

	/**
	 * Generate the classes
	 */
	 // TODO remove Date implementation in beginning
	 // TODO removed one-of condition due to limitations after instantiation of objects
   private def generateClasses(List<Data> rosettaClasses, Set<Data> superTypes, String version, HashMap<String,List<String>> importsVariables) {
	    val sortedRosettaClasses = sortClassesByHierarchy(rosettaClasses)
	    var List<String> enumImports = newArrayList
	    var List<String> dataImports = newArrayList
	    var List<String> superTypeImports = newArrayList
	    var List<String> classDefinitions = newArrayList
	    var List<String> updateForwardRefs = newArrayList
	    var List<String> importFromConditions = newArrayList
	
	    for (Data rosettaClass : sortedRosettaClasses) {
	        try {
	            enumImports += rosettaClass.allExpandedAttributes.filter[enclosingType == rosettaClass.name].filter[(it.name!=="reference") && (it.name!=="meta") && (it.name!=="scheme")].filter[!checkBasicType(it)].filter[importsVariables.get(it.toRawType.toString).get(1)==='ENUM'].map[it.toRawType].toSet().toList().map[attribute | '''from «importsVariables.get(attribute).get(0)».«attribute» import «attribute»''']
	            dataImports += rosettaClass.allExpandedAttributes.filter[enclosingType == rosettaClass.name].filter[(it.name!=="reference") && (it.name!=="meta") && (it.name!=="scheme")].filter[!checkBasicType(it)].filter[importsVariables.get(it.toRawType.toString).get(1)==='DATA'].map[it.toRawType].toSet().toList().map[attribute | '''from «importsVariables.get(attribute).get(0)».«attribute» import «attribute»''']
	        } catch (Exception ex) {
	        }
	
	        if (rosettaClass.superType !== null && importsVariables.containsKey(rosettaClass.superType.name)) {
	            superTypeImports.add('''from «importsVariables.get(rosettaClass.superType.name).get(0)».«rosettaClass.superType.name» import «rosettaClass.superType.name»''')
	        }
	
	        val classDefinition = '''
	            class «rosettaClass.name»«IF rosettaClass.superType === null && !superTypes.contains(rosettaClass)»«ENDIF»«IF rosettaClass.superType !== null && superTypes.contains(rosettaClass)»(«rosettaClass.superType.name»):«ELSEIF rosettaClass.superType !== null»(«rosettaClass.superType.name»):«ELSE»(BaseDataClass):«ENDIF»
	                «IF rosettaClass.definition!==null»
	                """
	                «rosettaClass.definition»
	                """
	                «ENDIF»
	                «generateAttributes(rosettaClass)»
	                «generateConditions(rosettaClass)»
	        '''
	        classDefinitions.add(classDefinition)
	       	importFromConditions += importedFromConditions.filter[importsVariables.containsKey(it)].toSet().toList().map[attribute | '''from «importsVariables.get(attribute).get(0)».«attribute» import «attribute»''']
	        
	
	        updateForwardRefs.add('''«rosettaClass.name».update_forward_refs()''')
	    }
	    	
	    enumImports = enumImports.toSet().toList()
	    dataImports = dataImports.toSet().toList()
	
	    return 
	    '''
	«FOR enumImport : enumImports SEPARATOR "\n"»«enumImport»«ENDFOR»
	«FOR superTypeImport : superTypeImports SEPARATOR "\n"»«superTypeImport»«ENDFOR»
	
	«FOR classDefinition : classDefinitions SEPARATOR "\n"»«classDefinition»«ENDFOR»
	
	«FOR dataImport : dataImports SEPARATOR "\n"»«dataImport»«ENDFOR»
	«FOR conditionImport : importFromConditions SEPARATOR "\n"»«conditionImport»«ENDFOR»
	
	«FOR updateForwardRef : updateForwardRefs SEPARATOR "\n"»«updateForwardRef»«ENDFOR»
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
    /* ***                   BEGIN condition generation                   *** */    
    /* ********************************************************************** */
    private def generateConditions(Data cls) {
    	importedFromConditions.clear()
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
        
        @cdm_condition
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
        '''    return self.check_one_of_constraint(«FOR a : attributes SEPARATOR ", "»'«a.name»'«ENDFOR», «necessity»)
        '''
               
    }

    private def generateExpressionCondition(Data cls, Condition c) {
        return '''    return «generateExpression(c.expression, 0)»
               '''
    }
    
    def addImportsFromConditions(String value){
    	if(!importedFromConditions.contains(value)){
    		importedFromConditions.add(value)
    	}
    }

    def String generateExpression(RosettaExpression expr, int iflvl) {
        switch (expr) {
            RosettaConditionalExpression: {
            	val nslashes = (2**iflvl - 1) as int;
            	val escsec = '\\'.repeat(nslashes) + "'";
                val ifexpr = generateExpression(expr.getIf(), iflvl+1)
                val ifthen = generateExpression(expr.ifthen, iflvl+1)
                var elsethen = expr.elsethen !== null && expr.full? generateExpression(expr.elsethen, iflvl+1): 'True'
                '''if_cond(«ifexpr», «escsec»«ifthen»«escsec», «escsec»«elsethen»«escsec», self)'''
            }
            RosettaFeatureCall: {
                var right = switch (expr.feature) {
                    Attribute: expr.feature.name
                    RosettaMetaType: expr.feature.name
                    RosettaEnumValue:{
                    	val rosettaValue = expr.feature as RosettaEnumValue
                    	val value = EnumHelper.convertValues(rosettaValue)
                    	value
                    } 
                    //TODO: RosettaFeature: '''.Select(x => x.«feature.name.toFirstUpper»)'''
                    RosettaFeature: expr.feature.name
                    default:
                        throw new UnsupportedOperationException("Unsupported expression type of " + expr.feature.eClass.name)
                }
                if(right=="None")
                	right="NONE"
                val receiver = generateExpression(expr.receiver, iflvl)
                
                if(receiver===null){
                	addImportsFromConditions(right.toString)
                	'''«right»'''
                }
                else{
                	addImportsFromConditions(receiver.toString)
                	'''«receiver».«right»'''
                }
                	
            }
            RosettaExistsExpression: {
                '''((«generateExpression(expr.argument, iflvl)») is not None)'''
            }
            RosettaBinaryOperation: {
                binaryExpr(expr, iflvl)
            }
            RosettaAbsentExpression: {
                '''((«generateExpression(expr.argument, iflvl)») is None)'''
            }

            RosettaReference: {
            	reference(expr, iflvl)
            }
            
            RosettaBigDecimalLiteral: {
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
            	'''(«generateExpression(expr.argument, iflvl)»)'''
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
                '''len(«generateExpression(expr.argument, iflvl)»)'''
            }
                           
            ListLiteral: {
            	'''[«FOR arg : expr.elements SEPARATOR ', '»«generateExpression(arg, iflvl)»«ENDFOR»]'''
            }
            
            FilterOperation : {
            	/* 
				var body = generateExpression(expr.body, iflvl)
            	val reciver = generateExpression(expr.receiver, iflvl)
            	return '''return(filter(«body», «reciver»))'''
            	* 
            	*/
			}
			SumOperation : {
            	/* 
				return '''sum(«generateExpression(expr.getReceiver(), iflvl)»)'''
				* 
				*/
            }
            
                        
            ListOperation : {
            	/* 
            	val operation = expr.getOperationKind()
                switch(operation) {
                    case ListOperationKind.SUM: {
                        return '''sum(«generateExpression(expr.getReceiver(), iflvl)»)'''
                    }
                    case ListOperationKind.FILTER:{
                    	var body = generateExpression(expr.body, iflvl)
                    	val reciver = generateExpression(expr.receiver, iflvl)
                    	return '''return(filter(«body», «reciver»))'''
                    }
                    	
                    default:
                        throw new UnsupportedOperationException("Unsupported ListOperation")                        
                } 
                 * 
            */              
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
            	addImportsFromConditions(s.name.toString)
                '''«s.name»'''
            }
            Attribute: {
            	addImportsFromConditions(s.name.toString)
                '''self.«s.name»'''
            }
            //ShortcutDeclaration: {
                 //'''«call.name»(«aliasCallArgs(call)»).«IF exprHelper.usesOutputParameter(call.expression)»build()«ELSE»get()«ENDIF»'''
            //}
            
            //RosettaEnumeration: '''«call».«call.name»'''
            RosettaEnumeration: {
            	addImportsFromConditions(s.name.toString)
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
        addImportsFromConditions(s.name.toString)

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
	            	'''«generateExpression(expr.left, iflvl)».contains(«generateExpression(expr.right, iflvl)»)'''
	            	
	            }
	            case("disjoint"):{
	            	'''«generateExpression(expr.left, iflvl)».isdisjoint(«generateExpression(expr.right, iflvl)»)'''
	            	
	            }
	            case("join"):{
	            	'''«generateExpression(expr.left, iflvl)».join(«generateExpression(expr.right, iflvl)»)'''
	            }
	            default: {
	                '''(«generateExpression(expr.left, iflvl)» «expr.operator» «generateExpression(expr.right, iflvl)»)'''
	            }
	        }
        }   
    }
    /* ********************************************************************** */
    /* ***                      END condition generation                  *** */
    /* ********************************************************************** */
    
     private def generateAttributes(Data c) {
    	val attr = c.allExpandedAttributes.filter[enclosingType == c.name].filter[(it.name!=="reference") && (it.name!=="meta") && (it.name!=="scheme")]
    	val attrSize = attr.size()
    	val conditionsSize = c.conditions.size()
        '''«IF attrSize === 0 && conditionsSize===0»pass«ELSE»«FOR attribute : attr SEPARATOR ""»«generateExpandedAttribute(c, attribute)»«ENDFOR»«ENDIF»'''
    }

     private def generateExpandedAttribute(Data c, ExpandedAttribute attribute) {
		var att = ""
		if (attribute.inf == 0) {
			att += "Optional"
		}
		if (attribute.sup != 1) {
			if (attribute.inf == 0) {
				att += "[List[" + toPythonType(attribute) + "]]"
			}
			else {
				att += "List[" + toPythonType(attribute) + "]"
			}
		}
		else {
 			if (attribute.inf == 0) {
				att += "[" + toPythonType(attribute) + "]"	
			}
			else {
				att += toPythonType(attribute)
			}
		}

  		var field_default = 'None'
 		if (attribute.inf == 1 && attribute.sup == 1)
			field_default = '...' // mandatory field -> cardinality (1..1)

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
		@cdm_condition
		def cardinality_«attrName»(self):
		    return check_cardinality(self.«attrName», «attribute.inf», «sup_str»)

		«ENDIF»
		'''
		

		/* 
		'''
		«attrName»: «att» = Field(None,description = "«attribute.definition»")
		«IF attribute.definition!==null»
		"""
		«attribute.definition»
		"""
		«ENDIF»
		'''
		*/
    }

    

    def Iterable<ExpandedAttribute> allExpandedAttributes(Data type){
        type.allSuperTypes.map[it.expandedAttributes].flatten
    }
    
    def String definition(Data element){
        element.definition
    }
}