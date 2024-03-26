package com.regnosys.rosetta.generator.python.util

import com.regnosys.rosetta.generator.object.ExpandedAttribute
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

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
        
    static def String createImports(String name){			
        val imports=
        '''
        # pylint: disable=line-too-long, invalid-name, missing-function-docstring
        # pylint: disable=bad-indentation, trailing-whitespace, superfluous-parens
        # pylint: disable=wrong-import-position, unused-import, unused-wildcard-import
        # pylint: disable=wildcard-import, wrong-import-order, missing-class-docstring
        # pylint: disable=missing-module-docstring
        from __future__ import annotations
        from typing import List, Optional
        import datetime
        import inspect
        from decimal import Decimal
        from pydantic import Field
        from rosetta.runtime.utils import (
            BaseDataClass, rosetta_condition, _resolve_rosetta_attr
        )
        from rosetta.runtime.utils import *
        
        __all__ = [«"'"+name+"'"»]
        
        '''
        imports
    }
        
    static def String createImportsFunc(String name) {			
        val imports=
        '''
        # pylint: disable=line-too-long, invalid-name, missing-function-docstring, missing-module-docstring, superfluous-parens
        # pylint: disable=wrong-import-position, unused-import, unused-wildcard-import, wildcard-import, wrong-import-order, missing-class-docstring
        from __future__ import annotations
        import sys
        import datetime
        import inspect
        from decimal import Decimal
        from abc import ABC, abstractmethod
        from rosetta.runtime.utils import *
        from rosetta.runtime.func_proxy import replaceable, create_module_attr_guardian
        '''
        imports
    }

    static def String toFileName(String namespace, String fileName) {
        '''src/«namespace.replace(".", "/")»/«fileName»''';
    }
    
    static def String toPyFileName(String namespace, String fileName) {
        '''«toFileName(namespace, fileName)».py''';
    }

    static def String toPyFunctionFileName(String namespace, String fileName) {
        '''src/«namespace.replace(".", "/")»/functions/«fileName».py''';
    }
    
    static def String createTopLevelInitFile (String version) {
        return "from .version import __version__"
    }

    static def String createVersionFile (String version) {
        val versionComma	 = version.replace ('.', ',')
        return "version = ("+versionComma+",0)\n"+
                "version_str = '"+version+"-0'\n"+
                "__version__ = '"+version+"'\n"+
                "__build_time__ = '"+LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_DATE_TIME)+"'"		 	
    }

    static def String createPYProjectTomlFile (String namespace, String version) {
        return "[build-system]\n" + 
               "requires = [\"setuptools>=62.0\"]\n" +
               "build-backend = \"setuptools.build_meta\"\n\n" +
               "[project]\n" + 
               "name = \"python-" + namespace + "\"\n" + 
               "version = \"" + version + "\"\n" + 
               "requires-python = \">= 3.10\"\n" +
               "dependencies = [\n" + 
               "   \"pydantic>=2.6.1\",\n" +
               "   \"rosetta.runtime==2.0.0\"\n" +
               "]\n" +
               "[tool.setuptools.packages.find]\n" +
               "where = [\"src\"]"
    }
}