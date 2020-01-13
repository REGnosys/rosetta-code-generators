package com.regnosys.rosetta.generator.scala.object

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import com.regnosys.rosetta.rosetta.RosettaClass
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.HashMap
import java.util.List
import java.util.Map
import java.util.Set

import static com.regnosys.rosetta.generator.scala.util.ScalaModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*

class ScalaModelObjectGenerator {

	@Inject extension RosettaExtensions
	@Inject extension ScalaModelObjectBoilerPlate
	@Inject extension ScalaMetaFieldGenerator
	
	static final String CLASSES_FILENAME = 'Types.scala'
	static final String META_FILENAME = 'MetaTypes.scala'
	
	def Map<String, ? extends CharSequence> generate(Iterable<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version) {
		val result = new HashMap		
		val enumImports = rosettaClasses
				.map[allExpandedAttributes].flatten
				.map[type]
				.filter[isEnumeration]
				.map[name]
				.toSet
		
		val classes = rosettaClasses.sortBy[name].generateClasses(enumImports, version).replaceTabsWithSpaces
		result.put(CLASSES_FILENAME, classes)
		val metaFields = generateMetaFields(metaTypes, version).replaceTabsWithSpaces
		result.put(META_FILENAME, metaFields)
		result;
	}
	
	private def generateClasses(List<Data> rosettaClasses, Set<String> importedEnums,  String version) {
	'''
	«fileComment(version)»
	package org.isda.cdm
	
	import org.isda.cdm.metafields.{ ReferenceWithMeta, FieldWithMeta, MetaFields }
	
	«FOR c : rosettaClasses»
		«classComment(c.definition, c.allExpandedAttributes)»
		case class «c.name»(«generateAttributes(c, false)»)«IF c.superType === null» {«ENDIF»
			«IF c.superType !== null»extends «c.superType.name»(«generateAttributes(c.superType, true)») {«ENDIF»
		}

	«ENDFOR»
	'''
	}
	
	private def generateAttributes(Data c, boolean extendsContructor) {
		'''«FOR attribute : c.allExpandedAttributes SEPARATOR ',\n		'»«generateAttribute(c, attribute, extendsContructor)»«ENDFOR»'''
	}
	
	private def generateAttribute(Data c, ExpandedAttribute attribute, boolean extendsContructor) {
		'''«IF !extendsContructor && !c.expandedAttributes.contains(attribute)»override val «ENDIF»«attribute.toAttributeName»«IF !extendsContructor»: «attribute.toType»«ENDIF»'''
	}
	
	def dispatch Iterable<ExpandedAttribute> allExpandedAttributes(RosettaClass type) {
		type.allSuperTypes.expandedAttributes
	}
	
	def dispatch Iterable<ExpandedAttribute> allExpandedAttributes(Data type){
		type.allSuperTypes.map[it.expandedAttributes].flatten
	}
	
	def dispatch String definition(RosettaClass element) {
		element.definition
	}
	def dispatch String definition(Data element){
		element.definition
	}
}
