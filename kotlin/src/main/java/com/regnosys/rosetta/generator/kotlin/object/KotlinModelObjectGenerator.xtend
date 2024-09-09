package com.regnosys.rosetta.generator.kotlin.object

import com.google.inject.Inject
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.HashMap
import java.util.List
import java.util.Map
import java.util.Set

import static com.regnosys.rosetta.generator.kotlin.util.KotlinModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*
import com.regnosys.rosetta.RosettaEcoreUtil

class KotlinModelObjectGenerator {

    @Inject extension RosettaEcoreUtil
    @Inject extension KotlinModelObjectBoilerPlate
    @Inject extension KotlinMetaFieldGenerator

    static final String CLASSES_FILENAME = 'Types.kt'
    static final String META_FILENAME = 'Metatypes.kt'


    def Map<String, ? extends CharSequence> generate(Iterable<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version) {
        val result = new HashMap

        val superTypes = rosettaClasses
				.filter[superType !== null]
                .map[superType]
                .map[allSuperTypes].flatten
                .toSet

        val classes = rosettaClasses.sortBy[name].generateClasses(superTypes, version).replaceTabsWithSpaces
        result.put(CLASSES_FILENAME, classes)

        val metaFields = rosettaClasses.sortBy[name].generateMetaFields(metaTypes, version).replaceTabsWithSpaces
        result.put(META_FILENAME, metaFields)


        result;
    }

	/**
	 * Generate the classes
	 */
	 // TODO remove Date implementation in beginning
	 // TODO removed one-of condition due to limitations after instantiation of objects
    private def generateClasses(List<Data> rosettaClasses, Set<Data> superTypes, String version) {
		'''
		«fileComment(version)»
		package org.isda.cdm.kotlin
		
		import kotlinx.serialization.*

		/**
		* Basic Date implementation
		*/
		@Serializable
		class Date (
			val year: Int,
			val month: Int,
			val day: Int
		)

		«FOR c : rosettaClasses SEPARATOR "\n"»
		«classComment(c.definition, c.allExpandedAttributes)»
		@Serializable
		open class «c.name»«IF c.superType === null && !superTypes.contains(c)»«ENDIF» (
			«generateAttributes(c)»
		)
		«IF c.superType !== null && superTypes.contains(c)»: «c.superType.name»()«ELSEIF c.superType !== null»: «c.superType.name»()«ENDIF»
		«IF c.conditions.size !== 0»
«««		{
«««			«FOR condition : c.conditions»
«««			«generateConditionLogic(c, condition)»
«««			«ENDFOR»
«««		}
		«ENDIF»
		«ENDFOR»
		'''
    }

    private def generateAttributes(Data c) {
        '''«FOR attribute : c.allExpandedAttributes.filter[enclosingType == c.name] SEPARATOR ","»«generateExpandedAttribute(c, attribute)»«ENDFOR»'''
    }

    private def generateExpandedAttribute(Data c, ExpandedAttribute attribute) {
	    '''
	    var «attribute.toAttributeName»: «attribute.toType»? = null
	    '''
    }

//    private def generateConditionLogic(Data c, Condition condition) {
//        '''
//		«IF condition.constraint !== null && condition.constraint.oneOf»«generateOneOfLogic(c)»«ENDIF»
//        '''
//    }

//    private def generateOneOfLogic(Data c) {
//        '''
//	        init {
//	        	require(listOfNotNull(«FOR attribute : c.allExpandedAttributes SEPARATOR ', '»«attribute.toAttributeName»«ENDFOR»).size == 1)
//	        }
//        '''
//    }

    def Iterable<ExpandedAttribute> allExpandedAttributes(Data type){
        type.allSuperTypes.map[it.expandedAttributes].flatten
    }
    
    def String definition(Data element){
        element.definition
    }
}