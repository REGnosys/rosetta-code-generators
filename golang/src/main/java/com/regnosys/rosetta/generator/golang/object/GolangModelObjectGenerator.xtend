package com.regnosys.rosetta.generator.golang.object

import com.google.inject.Inject
import com.regnosys.rosetta.rosetta.RosettaMetaType
import java.util.List

import static com.regnosys.rosetta.generator.golang.util.GolangModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*
import java.util.Map
import java.util.HashMap
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import java.util.Set
import com.google.common.collect.Lists
import com.regnosys.rosetta.RosettaEcoreUtil

class GolangModelObjectGenerator {

	@Inject extension RosettaEcoreUtil
	@Inject extension GolangModelObjectBoilerPlate
	@Inject extension GolangMetaFieldGenerator
	
	static final String CLASSES_FILENAME = 'types.go'
	static final String META_FILENAME = 'metatypes.go'
	static final String CLASSES_FOLDERNAME = 'org_isda_cdm'
	static final String META_FOLDERNAME = 'org_isda_cdm_metafields'
	
	def Map<String, ? extends CharSequence> generate(Iterable<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version) {
		val result = new HashMap		
		val enumImports = rosettaClasses
				.map[allExpandedAttributes].flatten
				.map[type]
				.filter[isEnumeration]
				.map[name]
				.toSet
		
		val classes = rosettaClasses.sortBy[name].generateClasses(enumImports, version).replaceTabsWithSpaces
		result.put(CLASSES_FOLDERNAME+"/"+ CLASSES_FILENAME, classes)
		val metaFields = generateMetaFields(metaTypes, version).replaceTabsWithSpaces
		result.put(META_FOLDERNAME +"/"+ META_FILENAME, metaFields)
		result;
	}
	
	
	private def generateClasses(List<Data> rosettaClasses, Set<String> importedEnums,  String version) {
	'''	
	package org_isda_cdm
	
	«fileComment(version)»	
	
	import "time"
	import . "org_isda_cdm_metafields";
		
	
	«FOR c : rosettaClasses»
		«classComment(c.definition)»
		type «c.name» struct {
			«FOR attribute : c.allExpandedAttributes»				
				«methodComment(attribute.definition)»
				«IF (c.name.toString == "Pric" && attribute.toType.toString == "Pric") || (c.name.toString == "New" && attribute.toType.toString == "Tx")»
				«attribute.toAttributeName» *«attribute.toType»;
				«ELSE»
				«attribute.toAttributeName» «attribute.toType»;
				«ENDIF»
			«ENDFOR»
		}
			
	«ENDFOR»
	'''}
	
	
	
	def Iterable<ExpandedAttribute> allExpandedAttributes(Data type){
		type.allSuperTypes.map[it.expandedAttributes].flatten
	}
	
	def String definition(Data element){
		element.definition
	}

}
