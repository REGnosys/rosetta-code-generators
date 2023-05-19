package com.regnosys.rosetta.generator.typescript.object

import com.regnosys.rosetta.rosetta.RosettaMetaType

import static com.regnosys.rosetta.generator.typescript.util.TypescriptModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.util.Util.*
import static extension com.regnosys.rosetta.generator.typescript.util.TypescriptTranslator.toTSType

class TypescriptMetaFieldGenerator {
	
	def generateMetaFields(Iterable<RosettaMetaType> metaTypes, String version) {
		fileComment(version) + metaClasses.toString + metaFields(metaTypes.filter[name != "id" && name != "reference" && name != "address"], version)
	}
	
		private def metaClasses() '''
		export interface FieldWithMeta<T> {
		  value?: T;
		  meta?: MetaFields;
		}

		export interface ReferenceWithMeta<T> {
		  globalReference?: string;
		  externalReference?: string;
		  address?: Reference;
		  value?: T;
		}
		
	'''
	
	def metaFields(Iterable<RosettaMetaType> types, String version) '''				
		export interface MetaFields {
			«FOR type : types.distinctBy(t|t.name.toFirstLower)»
				«type.name.toFirstLower»?: «type.typeCall.type.name.toTSType»;
			«ENDFOR»
			globalKey?: string;
			externalKey?: string;
			location?: Key[];
		}
		
		export interface MetaAndTemplateFields {
		  «FOR type : types.distinctBy(t|t.name.toFirstLower)»
		  	«type.name.toFirstLower»?: «type.typeCall.type.name.toTSType»;
		  «ENDFOR»
		  globalKey?: string;
		  externalKey?: string;
		  templateGlobalReference?: string;
		  location?: Key[];
		}
		
		export interface Key {
		  scope?: string;
		  value?: string;
		}
		
		export interface Reference {
		  scope?: string;
		  value?: string;
		}
		
	'''
}
