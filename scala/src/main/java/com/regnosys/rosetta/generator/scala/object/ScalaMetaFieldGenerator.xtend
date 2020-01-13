package com.regnosys.rosetta.generator.scala.object

import com.regnosys.rosetta.rosetta.RosettaMetaType

import static com.regnosys.rosetta.generator.scala.util.ScalaModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.scala.util.ScalaTranslator.toScalaBasicType
import static extension com.regnosys.rosetta.generator.util.Util.*

class ScalaMetaFieldGenerator {
	
	def generateMetaFields(Iterable<RosettaMetaType> metaTypes, String version) {
		fileComment(version) + metaClasses.toString + metaFields(metaTypes.filter[t|t.name!="id" && t.name!="reference"], version)
	}
	
	private def metaClasses() '''
		package org.isda.cdm.metafields

		case class FieldWithMeta[T](value: Option[T],
				meta: Option[MetaFields]) {
		}

		case class ReferenceWithMeta[T](value: Option[T],
				globalReference: Option[String],
				externalReference: Option[String]) {
		}
		
	'''
	
	def metaFields(Iterable<RosettaMetaType> types, String version) '''				
		case class MetaFields(«FOR type : types.distinctBy(t|t.name.toFirstLower) SEPARATOR '\n		'»«type.name.toFirstLower»: Option[«type.type.name.toScalaBasicType»],«ENDFOR»
				globalKey: Option[String],
				externalKey: Option[String]) {
		}
		
	'''
}
