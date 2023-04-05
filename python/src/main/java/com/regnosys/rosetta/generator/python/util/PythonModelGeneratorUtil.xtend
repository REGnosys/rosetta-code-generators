package com.regnosys.rosetta.generator.python.util

import com.regnosys.rosetta.generator.object.ExpandedAttribute
import java.util.List
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.simple.Function
import java.util.ArrayList
import java.util.Map
import java.util.HashMap
import java.util.stream.Stream
import java.util.Collection
import java.util.stream.Collectors

class PythonModelGeneratorUtil {
    
    static def fileComment(String version) 
		'''
		 # This file is auto-generated from the ISDA Common Domain Model, do not edit.
		 # Version: «version»

		'''

    static def comment(String definition) 
		'''
		«IF definition !==null && !definition.isEmpty »
		# 
		# «definition»
		#
		«ENDIF»
		'''

    static def classComment(String definition, Iterable<ExpandedAttribute> attributes) 
		'''
		«IF definition !==null && !definition.isEmpty »
		#
		# «definition»
		#
		 «FOR attribute : attributes»
		# @param «attribute.name» «attribute.definition»
		 «ENDFOR»
		#
		«ENDIF»
		'''
		
	def Map<String, ? extends CharSequence> createImports(List<Data> classes, List<RosettaEnumeration> enums, List<Function> functions, HashMap<String, List<String>> importsVariables){
		
		val result = new HashMap
		val List<String> classesNames = classes.map[name]
		val List<String> enumsNames = enums.map[name]
		val List<String> functionsNames = functions.map[name]
		
		
		val unitedList = new ArrayList<String>();
		
		unitedList.addAll(classesNames)
		unitedList.addAll(enumsNames)
		unitedList.addAll(functionsNames)
		
		
		
		val all = unitedList.map["'"+it+"'"]
		var simpleNameSpace = "";
		try{
			val fullNameSpace = importsVariables.get(unitedList.get(0)).get(0)
			simpleNameSpace = fullNameSpace.split("\\.").get(0)
		}catch(Exception ex){
			simpleNameSpace = null;
		}
		
		val imports=
		'''
		from __future__ import annotations
		from typing import List, Optional
		from datetime import date
		from datetime import time
		from datetime import datetime
		from pydantic import Field
		«IF simpleNameSpace!==null»from «simpleNameSpace».utils import *«ENDIF»
		
		__all__ = «all»
		
		'''
		
		result.put('Imports.kt', imports)
		
		result
		
		
		
	}
}