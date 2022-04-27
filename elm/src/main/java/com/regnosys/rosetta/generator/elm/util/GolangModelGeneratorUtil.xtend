package com.regnosys.rosetta.generator.elm.util

class GolangModelGeneratorUtil {
	
	static def fileComment(String version) '''
			-- This file is auto-generated from the ISDA Common Domain Model, do not edit.
			-- Version: «version»
	'''
		
	static def classComment(String definition) {
		comment(definition)
	}
	
	static def methodComment(String definition) {
		comment(definition)
	}
	
	private static def comment(String definition) '''
		«IF definition !==null && !definition.isEmpty »
			-- «definition»
		«ENDIF»
	'''
	
}
