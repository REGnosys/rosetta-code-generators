package com.regnosys.rosetta.generator.python.util

import com.regnosys.rosetta.generator.object.ExpandedAttribute
import java.util.List
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.simple.Function
import java.util.ArrayList
import java.util.Map
import java.util.HashMap

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
		
	def String createImports(String name){			
		val imports=
		'''
		# pylint: disable=line-too-long, invalid-name, missing-function-docstring, missing-module-docstring, superfluous-parens
		# pylint: disable=wrong-import-position, unused-import, unused-wildcard-import, wildcard-import, wrong-import-order, missing-class-docstring
		from __future__ import annotations
		from typing import List, Optional
		from datetime import date
		from datetime import time
		from datetime import datetime
		from decimal import Decimal
		from pydantic import Field
		from rosetta.runtime.utils import *
		
		__all__ = [«"'"+name+"'"»]
		
		'''
		
		imports
		
		
		
	}
}