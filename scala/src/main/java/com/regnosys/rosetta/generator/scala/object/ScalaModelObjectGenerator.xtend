package com.regnosys.rosetta.generator.scala.object

import com.google.inject.Inject
import com.regnosys.rosetta.generator.scala.serialization.ScalaObjectMapperGenerator
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Condition
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.HashMap
import java.util.List
import java.util.Map
import java.util.Set

import static com.regnosys.rosetta.generator.scala.util.ScalaModelGeneratorUtil.*

import com.regnosys.rosetta.RosettaEcoreUtil
import com.regnosys.rosetta.types.RObjectFactory
import com.regnosys.rosetta.types.RDataType
import com.regnosys.rosetta.types.RAttribute
import com.regnosys.rosetta.types.REnumType
import com.regnosys.rosetta.generator.scala.util.ScalaTranslator

class ScalaModelObjectGenerator {

	@Inject extension RosettaEcoreUtil
	@Inject extension ScalaModelObjectBoilerPlate
	@Inject extension ScalaMetaFieldGenerator
	@Inject extension ScalaObjectMapperGenerator
	@Inject extension RObjectFactory
	@Inject extension ScalaTranslator
	
	static final String CLASSES_FILENAME = 'Types.scala'
	static final String TRAITS_FILENAME = 'Traits.scala'
	static final String META_FILENAME = 'MetaTypes.scala'
	static final String SERIALIZATION_FILENAME = 'Serialization.scala'
	
	def Map<String, ? extends CharSequence> generate(Iterable<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version) {
		val result = new HashMap		
		
		val superTypes = rosettaClasses
				.filter[superType !== null]
                .map[superType]
                .flatMap[allSuperTypes]
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
		«val t = c.buildRDataType»
		«classComment(c.definition, t.allAttributes)»
		case class «c.name»(«generateAttributes(t)»)«IF c.superType === null && !superTypes.contains(c)» {«ENDIF»
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
		«val t = c.buildRDataType»
		«comment(c.definition)»
		trait «c.name»Trait «IF c.superType !== null»extends «c.superType.name»Trait «ENDIF»{
			«generateTraitAttributes(t)»
		}

	«ENDFOR»
	'''
	}
	
	private def generateAttributes(RDataType t) {
		'''
		«FOR attribute : t.allAttributes SEPARATOR ',\n		'»«generateAttribute(t, attribute)»«ENDFOR»«IF t.requiresMetaFields»,
				meta: Option[MetaFields]«ENDIF»'''
	}
	
	private def generateAttribute(RDataType t, RAttribute attribute) {
		val metaType = attribute.RMetaAnnotatedType
		val type = metaType.RType.stripFromTypeAliasesExceptInt
		if (type instanceof REnumType && !metaType.hasAttributeMeta) {
			if (!attribute.multi && attribute.cardinality.optional) {
			'''@JsonDeserialize(contentAs = classOf[«type.toEnumAnnotationType».Value])
		@JsonScalaEnumeration(classOf[«type.toEnumAnnotationType».Class])
		«attribute.toAttributeName»: «attribute.toType»'''
			} else {
				'''@JsonScalaEnumeration(classOf[«type.toEnumAnnotationType».Class])
		«attribute.toAttributeName»: «attribute.toType»'''
			}
		} else {
			'''«attribute.toAttributeName»: «attribute.toType»'''
		}
	}
	
	private def generateTraitAttributes(RDataType t) {
		'''
		«FOR attribute : t.ownAttributes»
			«generateTraitAttribute(t, attribute)»
		«ENDFOR»
		«IF t.requiresMetaFields»val meta: Option[MetaFields]«ENDIF»'''
	}
	
	private def generateTraitAttribute(RDataType t, RAttribute attribute) {
		'''
		«comment(attribute.definition)»
		val «attribute.toAttributeName»: «attribute.toType»
		'''
	}
	
	private def generateConditionLogic(Data c, Condition condition) {
		'''
		'''
	}
	
	def String definition(Data element){
		element.definition
	}
}
