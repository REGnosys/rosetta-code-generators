package com.regnosys.rosetta.generator.kotlin.util

import com.regnosys.rosetta.generator.object.ExpandedAttribute

class KotlinModelGeneratorUtil {
    
    static def fileComment(String version) 
		'''
		/**
		 * This file is auto-generated from the ISDA Common Domain Model, do not edit.
		 * Version: «version»
		 */
		'''

    static def comment(String definition) 
		'''
		«IF definition !==null && !definition.isEmpty »
		/** 
		* «definition» 
		*/
		«ENDIF»
		'''

    static def classComment(String definition, Iterable<ExpandedAttribute> attributes) 
		'''
		«IF definition !==null && !definition.isEmpty »
		/**
		 * «definition»
		 *
		«FOR attribute : attributes»
		 * @param «attribute.name» «attribute.definition»
		«ENDFOR»
		 */
		«ENDIF»
		'''
}