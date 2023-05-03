package com.regnosys.rosetta.generator.python.util

import com.regnosys.rosetta.generator.java.RosettaJavaPackages

class PythonModelGeneratorUtil {
	
	def generateVersion(String version) {
		'''__version__ = "«version»"'''
	}
	
	def generatePyProjectToml(String version) '''
		[build-system]
		requires = ["setuptools>=62.0"]
		build-backend = "setuptools.build_meta"
		
		[project]
		name = "rosetta.runtime"
		version = "«version»"
		requires-python = ">= 3.10"
		dependencies = [
		    "pydantic"
		]
		
		[tool.setuptools.packages.find]
		where = ["src"]
		'''

    def String toPyFileName(RosettaJavaPackages packages, String fileName) {
       '''«packages.model.withForwardSlashes»/«fileName».py''';
    }
}