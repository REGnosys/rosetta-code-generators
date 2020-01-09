package com.regnosys.rosetta.generator.scala.object

import com.regnosys.rosetta.rosetta.RosettaMetaType


import static extension com.regnosys.rosetta.generator.util.Util.*
import static com.regnosys.rosetta.generator.scala.util.ScalaModelGeneratorUtil.*
import static extension com.regnosys.rosetta.generator.scala.util.ScalaTranslator.toTSType

class ScalaMetaFieldGenerator {
	
	def generateMetaFields(Iterable<RosettaMetaType> metaTypes, String version) {
		fileComment(version) + metaClasses.toString + metaFields(metaTypes.filter[name !== "reference"], version)
	}
	
		private def metaClasses() '''
		export interface FieldWithMeta<T> {
		  value: T;
		  meta?: MetaFields;
		}

		export interface ReferenceWithMeta<T> {
		  globalReference: String;
		  externalReference: String;
		  value: T;
		}
				
	'''
	
	def metaFields(Iterable<RosettaMetaType> types, String version) '''				
		export interface MetaFields {
			«FOR type : types.distinctBy(t|t.name.toFirstLower)»
				«type.name.toFirstLower»?: «type.type.name.toTSType»;
			«ENDFOR»
			globalKey?: String;
			externalKey?: String;
		}
		
	'''
}
