package com.regnosys.rosetta.generator.scala.object

import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.List

import static com.regnosys.rosetta.generator.scala.util.ScalaModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.scala.util.ScalaTranslator.*
import static extension com.regnosys.rosetta.generator.util.IterableUtil.*
import com.regnosys.rosetta.types.RType
import jakarta.inject.Inject
import com.regnosys.rosetta.types.REnumType
import com.regnosys.rosetta.types.RObjectFactory
import com.regnosys.rosetta.generator.scala.util.ScalaTranslator

class ScalaMetaFieldGenerator {
	@Inject
	extension ScalaModelObjectBoilerPlate
	@Inject
	extension RObjectFactory
	@Inject
	extension ScalaTranslator
	
	def generateMetaFields(List<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version) {
		val metaFieldsImports = generateMetaFieldsImports.toString
		
		val refs = rosettaClasses
			.map[buildRDataType]
			.flatMap[ownAttributes]
			.filter[RMetaAnnotatedType.hasAttributeMeta && RMetaAnnotatedType.metaAttributes.exists[name=="reference" || name =="address"]]
			.map[RMetaAnnotatedType.RType.stripFromTypeAliasesExceptInt]
			.toSet
		
		var referenceWithMeta = '';
		
		for (ref:refs) {
				referenceWithMeta += generateReferenceWithMeta(ref).toString
		}
		
		val metas = rosettaClasses
			.map[buildRDataType]
			.flatMap[ownAttributes]
			.filter[RMetaAnnotatedType.hasAttributeMeta && !RMetaAnnotatedType.metaAttributes.exists[name=="reference" || name =="address"]]
			.map[RMetaAnnotatedType.RType.stripFromTypeAliasesExceptInt]
			.toSet

		for (meta:metas) {
			referenceWithMeta += generateFieldWithMeta(meta).toString
		}
		
		val metaFields = genMetaFields(metaTypes.filter[t|t.name!="key" && t.name!="id" && t.name!="reference" && t.name!="address" && t.name!="location"], version)
		
		return fileComment(version) + metaFieldsImports + keyRef.toString + referenceWithMeta + metaFields
	}
	
	private def generateMetaFieldsImports() '''
		package org.isda.cdm.metafields

		import com.fasterxml.jackson.core.`type`.TypeReference
		import com.fasterxml.jackson.module.scala.JsonScalaEnumeration
		import com.fasterxml.jackson.databind.annotation.JsonDeserialize

		import org.isda.cdm._
		
	'''
	
	private def keyRef() '''
		case class Key(
			value: String,
			scope: Option[String]) {}
			
		case class Reference(
			value: String,
			scope: Option[String]) {}
		
	'''
	
	private def generateFieldWithMeta(RType type) '''
		case class FieldWithMeta«type.toMetaTypeName»(«generateAttribute(type)»,
				meta: Option[MetaFields]) {}
		
	'''
	
	private def generateAttribute(RType rawType) {
		val type = rawType.stripFromTypeAliasesExceptInt
		if (type instanceof REnumType) {
			'''@JsonDeserialize(contentAs = classOf[«type.name».Value])
		@JsonScalaEnumeration(classOf[«type.name».Class])
		value: Option[«type.toScalaType»]'''
		} else {
			'''value: Option[«type.toScalaType»]'''
		}
	}
	
	private def generateReferenceWithMeta(RType type) '''
		case class ReferenceWithMeta«type.toMetaTypeName»(value: Option[«type.toScalaType»],
				globalReference: Option[String],
				externalReference: Option[String],
				address: Option[Reference]) {}
		
	'''
	
	private def genMetaFields(Iterable<RosettaMetaType> types, String version) '''				
		case class MetaFields(«FOR type : types.distinctBy(t|t.name.toFirstLower) SEPARATOR '\n		'»«type.name.toFirstLower»: Option[«type.typeCall.type.name.toScalaBasicType»],«ENDFOR»
				globalKey: Option[String],
				externalKey: Option[String],
				location: List[Key]) {}
		
		case class MetaAndTemplateFields(«FOR type : types.distinctBy(t|t.name.toFirstLower) SEPARATOR '\n		'»«type.name.toFirstLower»: Option[«type.typeCall.type.name.toScalaBasicType»],«ENDFOR»
				globalKey: Option[String],
				externalKey: Option[String],
				templateGlobalReference: Option[String],
				location: List[Key]) {}
	'''
}
