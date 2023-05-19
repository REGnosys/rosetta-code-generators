package com.regnosys.rosetta.generators.test

import java.util.List
import java.io.File
import java.nio.file.Files
import com.google.inject.Inject
import com.google.inject.Provider
import org.eclipse.xtext.resource.XtextResourceSet
import com.regnosys.rosetta.tests.util.ModelHelper
import com.regnosys.rosetta.rosetta.RosettaModel

class TestUtil {
	
	@Inject
    Provider<XtextResourceSet> resourceSetProvider
    
    @Inject
    extension ModelHelper
	
	def getRosettaFileContents(List<String> srcPaths) {
        return srcPaths
        	.map[new File(it)]
        	.flatMap[listFiles[it.name.endsWith('.rosetta')].toList]
        	.map[Files.readAllBytes(toPath)]
        	.map[new String(it)]
        	.toList
	}
	
	def parseAllRosettaFiles(List<String> srcPaths) {
        srcPaths.rosettaFileContents.parseRosetta

        return resourceSetProvider.get.resources
        	.flatMap[contents.filter(RosettaModel)]
        	.toList
	}
}