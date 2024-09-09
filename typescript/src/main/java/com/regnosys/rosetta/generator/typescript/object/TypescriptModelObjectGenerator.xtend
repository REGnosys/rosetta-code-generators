package com.regnosys.rosetta.generator.typescript.object

import com.google.inject.Inject
import com.regnosys.rosetta.rosetta.RosettaMetaType
import java.util.List

import static com.regnosys.rosetta.generator.typescript.util.TypescriptModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*
import java.util.Map
import java.util.HashMap
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import java.util.Set
import com.google.common.collect.Lists
import com.regnosys.rosetta.RosettaEcoreUtil

class TypescriptModelObjectGenerator {

	@Inject extension RosettaEcoreUtil
	@Inject extension TypescriptModelObjectBoilerPlate
	@Inject extension TypescriptMetaFieldGenerator
	
	static final String CLASSES_FILENAME = 'types.ts'
	static final String META_FILENAME = 'metatypes.ts'
	
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
	
	import { ReferenceWithMeta, FieldWithMeta, MetaFields } from './metatypes';
	import {
		«FOR importLine : Lists.partition(importedEnums.toList, 10) SEPARATOR ","»
			«FOR imported : importLine SEPARATOR ", "»«imported»«ENDFOR»
		«ENDFOR»
			} from './enums';
	
	«FOR c : rosettaClasses»
		«classComment(c.definition)»
		export interface «c.name» «IF c.superType !== null»extends «c.superType.name» «ENDIF»{
			«FOR attribute : c.allExpandedAttributes»
				«methodComment(attribute.definition)»
				«attribute.toAttributeName»?: «attribute.toType»;
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
