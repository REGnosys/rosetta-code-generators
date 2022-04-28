package com.regnosys.rosetta.generator.elm.rule

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.generator.elm.object.ElmModelObjectBoilerPlate
import com.regnosys.rosetta.generator.java.expression.ExpressionGenerator.ParamMap
import com.regnosys.rosetta.rosetta.BlueprintNodeExp
import com.regnosys.rosetta.rosetta.RosettaAbsentExpression
import com.regnosys.rosetta.rosetta.RosettaBigDecimalLiteral
import com.regnosys.rosetta.rosetta.RosettaBinaryOperation
import com.regnosys.rosetta.rosetta.RosettaBlueprintReport
import com.regnosys.rosetta.rosetta.RosettaBooleanLiteral
import com.regnosys.rosetta.rosetta.RosettaCallableCall
import com.regnosys.rosetta.rosetta.RosettaCallableWithArgsCall
import com.regnosys.rosetta.rosetta.RosettaConditionalExpression
import com.regnosys.rosetta.rosetta.RosettaContainsExpression
import com.regnosys.rosetta.rosetta.RosettaCountOperation
import com.regnosys.rosetta.rosetta.RosettaDisjointExpression
import com.regnosys.rosetta.rosetta.RosettaEnumValueReference
import com.regnosys.rosetta.rosetta.RosettaExistsExpression
import com.regnosys.rosetta.rosetta.RosettaExpression
import com.regnosys.rosetta.rosetta.RosettaFactory
import com.regnosys.rosetta.rosetta.RosettaFeatureCall
import com.regnosys.rosetta.rosetta.RosettaIntLiteral
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.RosettaOnlyExistsExpression
import com.regnosys.rosetta.rosetta.RosettaParenthesisCalcExpression
import com.regnosys.rosetta.rosetta.RosettaStringLiteral
import com.regnosys.rosetta.rosetta.simple.EmptyLiteral
import com.regnosys.rosetta.rosetta.simple.ListLiteral
import com.regnosys.rosetta.rosetta.simple.ListOperation
import com.regnosys.rosetta.validation.RosettaBlueprintTypeResolver
import com.regnosys.rosetta.validation.TypedBPNode
import com.rosetta.model.lib.expression.ExpressionOperators
import com.rosetta.model.lib.mapper.MapperC
import com.rosetta.model.lib.mapper.MapperS
import java.math.BigDecimal
import java.util.HashMap
import java.util.List
import java.util.Map

import static com.regnosys.rosetta.generator.elm.util.ElmModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.elm.util.ElmTranslator.toElmType

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*


import com.regnosys.rosetta.rosetta.impl.BlueprintExtractImpl
import com.regnosys.rosetta.rosetta.BlueprintExtract
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaFeature
import com.regnosys.rosetta.rosetta.simple.Data
import org.eclipse.xtext.EcoreUtil2
import com.regnosys.rosetta.rosetta.simple.ShortcutDeclaration
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.simple.ClosureParameter
import com.regnosys.rosetta.generator.java.function.CardinalityProvider
import com.regnosys.rosetta.rosetta.RosettaModel
import org.eclipse.emf.ecore.EObject
import com.regnosys.rosetta.rosetta.RosettaMapPathValue
import com.regnosys.rosetta.rosetta.RosettaRootElement
import com.regnosys.rosetta.rosetta.RosettaSynonymValueBase
import com.regnosys.rosetta.rosetta.RosettaTypedFeature
import com.regnosys.rosetta.rosetta.RosettaLiteral
import com.regnosys.rosetta.rosetta.simple.Function
import com.regnosys.rosetta.rosetta.WithCardinality
import com.regnosys.rosetta.rosetta.RosettaBlueprint
import java.util.Set
import org.eclipse.xtext.util.Tuples

class ReportRuleGenerator {
	
	@Inject extension RosettaExtensions
	@Inject extension RosettaBlueprintTypeResolver
	@Inject extension ElmModelObjectBoilerPlate
//		@Inject extension ExpressionGenerator
		@Inject extension com.regnosys.rosetta.generator.util.Util
			@Inject CardinalityProvider cardinalityProvider
		
	

	def Map<String, ? extends CharSequence> generate(String namespace, List<RosettaBlueprintReport> reports, List<Data> dataImports, List<RosettaEnumeration> enumImports, String version) {
		val result = new HashMap		
		
		val elm = reports.generateElm(dataImports, enumImports, namespace, version)
		
		val folder = namespace.split("\\.").map[it.toFirstUpper].join('/')
		val fileName =  "Rule.elm"
		
		result.put(folder + '/' + fileName, elm)

		result;
	}
	
	
	def String generateElm(List<RosettaBlueprintReport> reports, List<Data> dataImports, List<RosettaEnumeration> enumImports, String namespace, String version) 
	'''	
	module «namespace.split("\\.").map[it.toFirstUpper].join(".")».Rule exposing (..)
	
	import Morphir.SDK.LocalDate exposing (LocalDate)
	import Morphir.SDK.LocalTime exposing (LocalTime)
	import Com.Rosetta.Model.Type exposing (ZonedDateTime)
	import Com.Rosetta.Model.Type exposing (Date)

	«FOR enumImport : enumImports»
		import «(enumImport.eContainer as RosettaModel).name.split("\\.").map[it.toFirstUpper].join(".")».Enum exposing («enumImport.name»)
	«ENDFOR»
	«FOR dataImport : dataImports»
		import «(dataImport.eContainer as RosettaModel).name.split("\\.").map[it.toFirstUpper].join(".")».Type exposing («dataImport.name»)
	«ENDFOR»
	«fileComment(version)»
	
	«FOR c : reports»
	«val typeGraph = buildTypeGraph(c.firstNodeExpression, null)»
	«c.reportOutputTypeName.toFirstLower» : «typeGraph.inputTypeName» -> «c.reportOutputTypeName»
	«c.reportOutputTypeName.toFirstLower» «typeGraph.inputTypeName.toFirstLower» =
		«FOR attribute : c.reportType.attributes»
			«IF c.reportType.attributes.indexOf(attribute) === 0»{ «ELSE», «ENDIF»	«attribute.toAttributeName» = «attribute.ruleReference.reportingRule.name.toFirstLower» «typeGraph.inputTypeName.toFirstLower»
		«ENDFOR»
		}
	
	«FOR ruleTuple : c.allReportingRules»
	«val ruleTypeGraph = buildTypeGraph(ruleTuple.first.nodes, null)»
	«ruleTuple.first.name.toFirstLower» : «ruleTypeGraph.inputTypeName» -> «IF ruleTuple.second»Maybe «ENDIF»«ruleTypeGraph.output.type.name.toElmType»
	«ruleTuple.first.name.toFirstLower» «ruleTypeGraph.inputTypeName.toFirstLower» =
		«(ruleTuple.first.nodes.node as BlueprintExtract).call.elmCode(new ParamMap(ruleTypeGraph.input.type))»

	«ENDFOR»

	«ENDFOR»
	
	
	onlyElement : List a -> Maybe a
	onlyElement list =
	    case list of
	        [ a ] ->
	            Just a
	
	        _ ->
	            Nothing
	'''
	
	protected def String inputTypeName(TypedBPNode typeGraph) {
		typeGraph.input.type.name
	}
	
	def String reportOutputTypeName(RosettaBlueprintReport report){
		report.reportType.name
	}
	
	def getAllReportingRules(RosettaBlueprintReport report) {
		val rules = newHashSet
		report.reportType.collectReportingRules([a,b|rules.add(Tuples.create(a, b))], newHashSet)
		return rules
	}
	
	
	/**
	 * get first node expression
	 */
	def firstNodeExpression(RosettaBlueprintReport report) {
		var BlueprintNodeExp currentNodeExpr = null
		var BlueprintNodeExp firstNodeExpr = null
		
		for (eligibilityRule : report.eligibilityRules) {
			val ref = RosettaFactory.eINSTANCE.createBlueprintRef
			ref.blueprint = eligibilityRule
			ref.name = eligibilityRule.name
			
			var newNodeExpr = RosettaFactory.eINSTANCE.createBlueprintNodeExp
			newNodeExpr.node = ref
			newNodeExpr.node.name = ref.name
						
			if (null === currentNodeExpr) firstNodeExpr = newNodeExpr
			else currentNodeExpr.next = newNodeExpr
				
			currentNodeExpr = newNodeExpr
		}
		
		val node = RosettaFactory.eINSTANCE.createBlueprintAnd
		node.name = report.name
		
		report.allReportingRules.sortBy[first.name].forEach[
			val ref = RosettaFactory.eINSTANCE.createBlueprintRef
			ref.blueprint = it.first
			ref.name = it.first.name
			val rule = RosettaFactory.eINSTANCE.createBlueprintNodeExp
			rule.node = ref
			rule.node.name = ref.name
			node.bps.add(rule)
		]
		
		if (!node.bps.empty) {
			val andNodeExpr = RosettaFactory.eINSTANCE.createBlueprintNodeExp
			andNodeExpr.node = node
			currentNodeExpr.next = andNodeExpr			
		}
			
		return firstNodeExpr
	}
	
	
	def String elmCode(RosettaExpression expr, ParamMap params) {
		switch (expr) {
			RosettaFeatureCall : {
				featureCall(expr, params, false)
			}
			RosettaOnlyExistsExpression : {
				//onlyExistsExpr(expr, params)
				'RosettaOnlyExistsExpression:not supported:' + expr
			}
			RosettaExistsExpression : {
				//existsExpr(expr, params)
				'RosettaExistsExpression:not supported:' + expr
			}
			RosettaBinaryOperation : {
				//binaryExpr(expr, null, params)
				'RosettaBinaryOperation:not supported:' + expr
			}
			RosettaCountOperation : {
				//countExpr(expr, null, params)
				'RosettaCountOperation:not supported:' + expr
			}
			RosettaAbsentExpression : {
				//absentExpr(expr, expr.argument, params)
				'RosettaAbsentExpression:not supported:' + expr
			}
			RosettaCallableCall : {
				callableCall(expr, params) 
//				'RosettaCallableCall:not supported:' + expr
			}
			RosettaCallableWithArgsCall: {
				//callableWithArgs(expr, params)
				'RosettaCallableWithArgsCall:not supported:' + expr
			}
			RosettaBigDecimalLiteral : {
				//'''«MapperS».of(«BigDecimal».valueOf(«expr.value»))'''
				'RosettaBigDecimalLiteral:not supported:' + expr
			}
			RosettaBooleanLiteral : {
				//'''«MapperS».of(Boolean.valueOf(«expr.value»))'''
				'RosettaBooleanLiteral:not supported:' + expr
			}
			RosettaIntLiteral : {
				//'''«MapperS».of(Integer.valueOf(«expr.value»))'''
				'RosettaIntLiteral:not supported:' + expr
			}
			RosettaStringLiteral : {
				//'''«MapperS».of("«expr.value»")'''
				'RosettaStringLiteral:not supported:' + expr
			}
			RosettaEnumValueReference : {
				//'''«MapperS».of(«expr.enumeration.toJavaType».«expr.value.convertValues»)'''
				'RosettaEnumValueReference:not supported:' + expr
			}
			RosettaConditionalExpression : {
				//'''«expr.genConditionalMapper(params)»'''
				'RosettaConditionalExpression:not supported:' + expr
			}
			RosettaContainsExpression : {
				//'''«importMethod(ExpressionOperators,"contains")»(«expr.container.javaCode(params)», «expr.contained.javaCode(params)»)'''
				'RosettaContainsExpression:not supported:' + expr
			}
			RosettaDisjointExpression : {
				//'''«importMethod(ExpressionOperators,"disjoint")»(«expr.container.javaCode(params)», «expr.disjoint.javaCode(params)»)'''
				'RosettaDisjointExpression:not supported:' + expr
			}
			RosettaParenthesisCalcExpression : {
				//expr.expression.javaCode(params)
				'RosettaParenthesisCalcExpression:not supported:' + expr
			}
			EmptyLiteral : {
				'''null'''
			}
			ListLiteral : {
				//'''«MapperC».of(«FOR ele: expr.elements SEPARATOR ', '»«ele.javaCode(params)»«ENDFOR»)'''
				'ListLiteral:not supported:' + expr
			}
			ListOperation : {
				//listOperation(expr, params)
				'ListOperation:not supported:' + expr
			}
			default: 
				throw new UnsupportedOperationException("Unsupported expression type of " + expr?.class?.simpleName)
		}
	}
	
	private def String featureCall(RosettaFeatureCall call, ParamMap params, boolean autoValue) {
		val feature = call.feature
		val String right = switch (feature) {
			Attribute:
				feature.buildMapFunc(cardinalityProvider.isMulti(call.receiver))
			RosettaEnumValue: 
				return '''«feature.enumeration.name»'''
			RosettaFeature: 
				'''.«feature.name.toFirstUpper»'''
			default:
				throw new UnsupportedOperationException("Unsupported expression type of " + feature.eClass.name)
		}
		
		return distinctOrOnlyElement('''«elmCode(call.receiver, params)»«right»''', false, call.onlyElement)
	}
	
	private def String distinctOrOnlyElement(String code, boolean distinct, boolean onlyElement) {
		return '''«code»«IF onlyElement»
			|> onlyElement
		«ENDIF»'''
	}

	def String buildMapFunc(Attribute attribute, boolean inListStream) {
		val mapFunc = attribute.buildMapFuncAttribute
//		if (attribute.card.isIsMany) {
//				'''
//				
//				|> List.map
//					(\ item -> item.«attribute.name»
//					)''' // flattern if inListStream
//      
//		}
//		else 
		if (inListStream) 
		{
//							'''
//				
//				|> List.«IF attribute.card.isIsMany»flatMap«ELSE»map«ENDIF»
//					(\ item -> item.«attribute.name»
//					'''
				'''
				
				|> List.map
					(\ item -> item.«attribute.name»
					)«IF attribute.card.isIsMany»
						|> List.flatten
					«ENDIF»
					'''
					
		} else {
				'''.«attribute.name»'''
			
		}
	}	
	
	private def String buildMapFuncAttribute(Attribute attribute) {
		'''«attribute.name.toFirstUpper»'''
//		if(attribute.eContainer instanceof Data) 
//			'''"get«attribute.name.toFirstUpper»", «attribute.attributeTypeVariableName» -> «IF attribute.override»(«attribute.type.toJavaType») «ENDIF»«attribute.attributeTypeVariableName».get«attribute.name.toFirstUpper»()'''
	}
	
	protected def String callableCall(RosettaCallableCall expr, ParamMap params) {
		if (expr.implicitReceiver) {
			return '''«EcoreUtil2.getContainerOfType(expr, ListOperation).firstOrImplicit.getNameOrDefault.toDecoratedName»'''
		}
		val call = expr.callable
		switch (call)  {
			Data : {
				'''«params.getClass(call)»'''
			}
//			Attribute : {
//				// Data Attributes can only be called from their conditions
//				// The current container (Data) is stored in Params, but we need also look for superTypes
//				// so we could also do: (call.eContainer as Data).allSuperTypes.map[it|params.getClass(it)].filterNull.head
//				if(call.eContainer instanceof Data)
//					'''«MapperS».of(«EcoreUtil2.getContainerOfType(expr, Data).getName.toFirstLower»)«buildMapFunc(call, true)»'''
//				else
//					distinctOrOnlyElement('''«if (call.card.isIsMany) MapperC else MapperS».of(«call.name»)''', false, expr.onlyElement)
//			}
//			ShortcutDeclaration : {
//				val multi = cardinalityProvider.isMulti(call)
//				distinctOrOnlyElement('''«IF multi»«MapperC»«ELSE»«MapperS»«ENDIF».of(«call.name»(«aliasCallArgs(call)»).«IF exprHelper.usesOutputParameter(call.expression)»build()«ELSE»«IF multi»getMulti()«ELSE»get()«ENDIF»«ENDIF»)''', false, expr.onlyElement)
//			}
			RosettaEnumeration: '''«call.name.toElmType»'''
			ClosureParameter: '''«call.getNameOrDefault.toDecoratedName»'''
			default: 
				throw new UnsupportedOperationException("Unsupported callable type of " + call?.class?.simpleName)
		}
	}
	
	
	
	
	def void collectReportingRules(Data dataType, (RosettaBlueprint, boolean) => void visitor, Set<Data> collectedTypes) {
		dataType.allNonOverridesAttributes.forEach[attr|
			val attrType = attr.type
			val attrEx = attr.toExpandedAttribute
			if (attrEx.builtInType || attrEx.enum) {
				val rule = attr.ruleReference?.reportingRule
				if (rule !== null) {
					visitor.apply(rule, attr.card.optional)
				}
			} else if (attrType instanceof Data) {
				if (!collectedTypes.contains(attrType)) {
					collectedTypes.add(attrType)
					val attrRule = attr.ruleReference?.reportingRule
					// only collect rules from nested type if no rule exists at the top level
					// e.g. nested reporting rules are not supported (except for repeatable rules where only the top level rule should be collected) 
					if (attrRule === null)
						attrType.collectReportingRules(visitor, collectedTypes)
					else 
						visitor.apply(attrRule, attr.card.optional)
				}
			} else {
				throw new IllegalArgumentException("Did not collect reporting rules from type " + attrType)
			}
		]	
	}
	}









