package com.regnosys.rosetta.generator.scala.object

import com.google.inject.Inject
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import com.regnosys.rosetta.generator.scala.serialization.ScalaObjectMapperGenerator
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Condition
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.HashMap
import java.util.List
import java.util.Map
import java.util.Set

import static com.regnosys.rosetta.generator.scala.util.ScalaModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*
import com.regnosys.rosetta.RosettaEcoreUtil

class ScalaModelObjectGenerator {

	@Inject extension RosettaEcoreUtil
	@Inject extension ScalaModelObjectBoilerPlate
	@Inject extension ScalaMetaFieldGenerator
	@Inject extension ScalaObjectMapperGenerator
	
	static final String CLASSES_FILENAME = 'Types.scala'
	static final String TRAITS_FILENAME = 'Traits.scala'
	static final String META_FILENAME = 'MetaTypes.scala'
	static final String SERIALIZATION_FILENAME = 'Serialization.scala'
	
	def Map<String, ? extends CharSequence> generate(Iterable<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version) {
		val result = new HashMap		
		
		val superTypes = rosettaClasses
				.filter[superType !== null]
                .map[superType]
                .map[allSuperTypes].flatten
                .toSet
		
		val classes = rosettaClasses.sortBy[name].generateClasses(superTypes, version).replaceTabsWithSpaces
		result.put(CLASSES_FILENAME, classes)
		
		val traits = superTypes.sortBy[name].generateTraits(version).replaceTabsWithSpaces
		result.put(TRAITS_FILENAME, traits)
				
		val metaFields = rosettaClasses.sortBy[name].generateMetaFields(metaTypes, version).replaceTabsWithSpaces
		result.put(META_FILENAME, metaFields)
		
		val objectMapper = generateObjectMapper(version)
		result.put(SERIALIZATION_FILENAME, objectMapper)
		
		result;
	}
	
	private def generateClasses(List<Data> rosettaClasses, Set<Data> superTypes, String version) {
	'''
	«fileComment(version)»
	package org.isda.cdm
	
	import com.fasterxml.jackson.core.`type`.TypeReference
	import com.fasterxml.jackson.module.scala.JsonScalaEnumeration
	import com.fasterxml.jackson.databind.annotation.JsonDeserialize
	
	import org.isda.cdm.metafields._
	
	«FOR c : rosettaClasses»
		«classComment(c.definition, c.allExpandedAttributes)»
		case class «c.name»(«generateAttributes(c)»)«IF c.superType === null && !superTypes.contains(c)» {«ENDIF»
			«IF c.superType !== null && superTypes.contains(c)»extends «c.name»Trait with «c.superType.name»Trait {
			«ELSEIF c.superType !== null»extends «c.superType.name»Trait {
			«ELSEIF superTypes.contains(c)»extends «c.name»Trait {«ENDIF»
			«FOR condition : c.conditions»
				«generateConditionLogic(c, condition)»
			«ENDFOR»
		}
		
	«ENDFOR»
	'''
	}
	
	private def generateTraits(List<Data> rosettaClasses, String version) {
	'''
	«fileComment(version)»
	package org.isda.cdm
	
	import org.isda.cdm.metafields._
	
	«FOR c : rosettaClasses»
		«comment(c.definition)»
		trait «c.name»Trait «IF c.superType !== null»extends «c.superType.name»Trait «ENDIF»{
			«generateTraitAttributes(c)»
		}

	«ENDFOR»
	'''
	}
	
	private def generateAttributes(Data c) {
		'''«FOR attribute : c.allExpandedAttributes SEPARATOR ',\n		'»«generateAttribute(c, attribute)»«ENDFOR»'''
	}
	
	private def generateAttribute(Data c, ExpandedAttribute attribute) {
		if (attribute.enum && !attribute.hasMetas) {
			if (attribute.singleOptional) {
			'''@JsonDeserialize(contentAs = classOf[«attribute.type.toEnumAnnotationType».Value])
		@JsonScalaEnumeration(classOf[«attribute.type.toEnumAnnotationType».Class])
		«attribute.toAttributeName»: «attribute.toType»'''
			} else {
				'''@JsonScalaEnumeration(classOf[«attribute.type.toEnumAnnotationType».Class])
		«attribute.toAttributeName»: «attribute.toType»'''
			}
		} else {
			'''«attribute.toAttributeName»: «attribute.toType»'''
		}
	}
	
	private def generateTraitAttributes(Data c) {
		'''
		«FOR attribute : c.expandedAttributes»
			«generateTraitAttribute(c, attribute)»
		«ENDFOR»
		'''
	}
	
	private def generateTraitAttribute(Data c, ExpandedAttribute attribute) {
		'''
		«comment(attribute.definition)»
		val «attribute.toAttributeName»: «attribute.toType»
		'''
	}
	
	private def generateConditionLogic(Data c, Condition condition) {
		'''
		'''
	}

	def Iterable<ExpandedAttribute> allExpandedAttributes(Data type){
		type.allSuperTypes.reverse.map[it.expandedAttributes].flatten
	}
	
	def String definition(Data element){
		element.definition
	}
}
