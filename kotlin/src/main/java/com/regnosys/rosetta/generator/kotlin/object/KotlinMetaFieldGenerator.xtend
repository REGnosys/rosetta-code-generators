package com.regnosys.rosetta.generator.kotlin.object

import com.regnosys.rosetta.generator.object.ExpandedType
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.List

import static com.regnosys.rosetta.generator.kotlin.util.KotlinModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.kotlin.object.KotlinModelObjectBoilerPlate.*
import static extension com.regnosys.rosetta.generator.kotlin.util.KotlinTranslator.*
import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*
import static extension com.regnosys.rosetta.generator.util.Util.*

class KotlinMetaFieldGenerator {

    def generateMetaFields(List<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version) {
        val metaFieldsImports = generateMetaFieldsImports.toString

        val refs = rosettaClasses
                .flatMap[expandedAttributes]
 				.filter[hasMetas && metas.exists[name=="reference" || name=="address"]]
                .map[type]
                .toSet

        var referenceWithMeta = '';

        for (ref:refs) {
            if (ref.isType)
                referenceWithMeta += generateReferenceWithMeta(ref).toString
            else
                referenceWithMeta += generateBasicReferenceWithMeta(ref).toString
        }

        val metas =  rosettaClasses
                .flatMap[expandedAttributes]
                .filter[hasMetas && !metas.exists[name=="reference" || name=="address"]]
                .map[type]
                .toSet

        for (meta:metas) {
            referenceWithMeta += generateFieldWithMeta(meta).toString
        }

        val metaFields = genMetaFields(metaTypes.filter[t|t.name!="id" && t.name!="key" && t.name!="reference" && t.name!="address"], version)

        return fileComment(version) + metaFieldsImports + referenceWithMeta + metaFields
    }

    private def generateMetaFieldsImports() 
    '''
	package org.isda.cdm.kotlin
	
	import kotlinx.serialization.*
	
	'''

    private def generateFieldWithMeta(ExpandedType type) '''
    @Serializable
    open class FieldWithMeta«type.toMetaTypeName» (
    	«generateAttribute(type)»
    	var meta: MetaFields? = null
    )

	'''

    private def generateAttribute(ExpandedType type) {
        if (type.enumeration) {
            '''var value: «type.toKotlinType»? = null,'''
        } else {
            '''var value: «type.toKotlinType»? = null,'''
        }
    }

    private def generateReferenceWithMeta(ExpandedType type)
    '''
    @Serializable
    open class ReferenceWithMeta«type.toMetaTypeName» (
    	var value: «type.toKotlinType»? = null,
    	var globalReference: String? = null,
    	var externalReference: String? = null,
    	var address: Reference? = null
    )
    
	'''
    private def generateBasicReferenceWithMeta(ExpandedType type) 
    '''
    @Serializable
    open class BasicReferenceWithMeta«type.toMetaTypeName» (
    	var value: «type.toKotlinType»? = null,
    	var globalReference: String? = null,
    	var externalReference: String? = null,
    	var address: Reference? = null
    )

	'''

    private def genMetaFields(Iterable<RosettaMetaType> types, String version) 
    '''
    @Serializable
    open class MetaFields (
    	«FOR type : types.distinctBy(t|t.name.toFirstLower) SEPARATOR '\n'»var «type.name.toFirstLower»: «type.typeCall.type.name.toKotlinBasicType»? = null,«ENDFOR»
    	var globalKey: String? = null,
    	var externalKey: String? = null,
    	var location: MutableList<Key>? = null
    )

    @Serializable
    open class MetaAndTemplateFields (
    	«FOR type : types.distinctBy(t|t.name.toFirstLower) SEPARATOR '\n'»var «type.name.toFirstLower»: «type.typeCall.type.name.toKotlinBasicType»? = null,«ENDFOR»
    	var globalKey: String? = null,
    	var externalKey: String? = null,
    	var templateGlobalReference: String? = null,
    	var location: MutableList<Key>? = null
    )

    @Serializable
    open class Key (
    	var scope: String? = null,
    	var value: String? = null
    )
    
    @Serializable
    open class Reference (
    	var scope: String? = null,
    	var value: String? = null
    )
    
	'''
}