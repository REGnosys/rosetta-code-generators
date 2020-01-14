package com.regnosys.rosetta.generator.scala.object

import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.List

import static com.regnosys.rosetta.generator.scala.util.ScalaModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.scala.util.ScalaTranslator.*
import static extension com.regnosys.rosetta.generator.util.Util.*

import static extension com.regnosys.rosetta.generator.scala.object.ScalaModelObjectBoilerPlate.*

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*
import com.regnosys.rosetta.generator.object.ExpandedType

class ScalaMetaFieldGenerator {
	
	def generateMetaFields(List<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version) {
		val metaFieldsImports = generateMetaFieldsImports.toString
		
		val refs = rosettaClasses
			.flatMap[expandedAttributes]
			.filter[hasMetas && metas.exists[name=="reference"]]
			.map[type]
			.toSet
		
		var referenceWithMeta = '';
		
		for (ref:refs) {
			if (ref.isType)
				referenceWithMeta += generateReferenceWithMeta(ref).toString
			else
				referenceWithMeta += generateBasicReferenceWithMeta(ref).toString
		}
		
//		val metas =  rosettaClasses
//			.flatMap[expandedAttributes]
//			.filter[hasMetas && !metas.exists[name=="reference"]]
//			.map[type]
//			.toSet

//		for (meta:metas) {
//			referenceWithMeta += generateFieldWithMeta(meta).toString
//		}
		
		referenceWithMeta += generateFieldWithMeta.toString
		
		val metaFields = genMetaFields(metaTypes.filter[t|t.name!="id" && t.name!="reference"], version)
		
		return fileComment(version) + metaFieldsImports + referenceWithMeta + metaFields
	}
	
	private def generateMetaFieldsImports() '''
		package org.isda.cdm.metafields

		import org.isda.cdm._
		
		import scala.reflect.ClassTag
		import com.fasterxml.jackson.databind.annotation.JsonDeserialize
		
	'''
	
//	private def generateFieldWithMeta(ExpandedType type) '''
//		case class FieldWithMeta«type.toMetaType»(value: Option[«type.toScalaType»],
//				meta: Option[MetaFields]) {}
//		
//	'''
	
	private def generateFieldWithMeta() '''
		case class FieldWithMeta[T: ClassTag](value: Option[T],
				meta: Option[MetaFields]) {}
		
	'''
	
	private def generateReferenceWithMeta(ExpandedType type) '''
		case class ReferenceWithMeta«type.toMetaType»(value: Option[«type.toScalaType»],
				globalReference: Option[String],
				externalReference: Option[String]) {}
		
	'''

	private def generateBasicReferenceWithMeta(ExpandedType type) '''
		case class BasicReferenceWithMeta«type.toMetaType»(value: Option[«type.toScalaType»],
				globalReference: Option[String],
				externalReference: Option[String]) {}
		
	'''
	
	private def genMetaFields(Iterable<RosettaMetaType> types, String version) '''				
		case class MetaFields(«FOR type : types.distinctBy(t|t.name.toFirstLower) SEPARATOR '\n		'»«type.name.toFirstLower»: Option[«type.type.name.toScalaBasicType»],«ENDFOR»
				globalKey: Option[String],
				externalKey: Option[String]) {}
		
	'''
}
