package com.regnosys.rosetta.generator.kotlin.object

import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.List

import static com.regnosys.rosetta.generator.kotlin.util.KotlinModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.util.IterableUtil.*
import com.regnosys.rosetta.types.RType
import jakarta.inject.Inject
import com.regnosys.rosetta.types.REnumType
import com.regnosys.rosetta.types.RObjectFactory
import com.regnosys.rosetta.generator.kotlin.util.KotlinTranslator
import com.regnosys.rosetta.types.RDataType

class KotlinMetaFieldGenerator {
	@Inject
	extension KotlinModelObjectBoilerPlate
	@Inject
	extension RObjectFactory
	@Inject
	extension KotlinTranslator

    def generateMetaFields(List<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version) {
        val metaFieldsImports = generateMetaFieldsImports.toString

        val refs = rosettaClasses
                .map[buildRDataType]
                .flatMap[ownAttributes]
                .filter[RMetaAnnotatedType.hasAttributeMeta && RMetaAnnotatedType.metaAttributes.exists[name=="reference" || name=="address"]]
                .map[RMetaAnnotatedType.RType.stripFromTypeAliasesExceptInt]
                .toSet

        var referenceWithMeta = '';

        for (ref:refs) {
            if (ref instanceof RDataType)
                referenceWithMeta += generateReferenceWithMeta(ref).toString
            else
                referenceWithMeta += generateBasicReferenceWithMeta(ref).toString
        }

        val metas = rosettaClasses
                .map[buildRDataType]
                .flatMap[ownAttributes]
                .filter[RMetaAnnotatedType.hasAttributeMeta && !RMetaAnnotatedType.metaAttributes.exists[name=="reference" || name=="address"]]
                .map[RMetaAnnotatedType.RType.stripFromTypeAliasesExceptInt]
                .toSet

        for (meta:metas) {
            referenceWithMeta += generateFieldWithMeta(meta).toString
        }

        val metaFields = genMetaFields(metaTypes.filter[t|t.name!="id" && t.name!="key" && t.name!="reference" && t.name!="address" && t.name!="location"], version)

        return fileComment(version) + metaFieldsImports + referenceWithMeta + metaFields
    }

    private def generateMetaFieldsImports() 
    '''
	package org.isda.cdm.kotlin
	
	import kotlinx.serialization.*
	
	'''

    private def generateFieldWithMeta(RType type) '''
    @Serializable
    open class FieldWithMeta«type.toMetaTypeName» (
    	«generateAttribute(type)»
    	var meta: MetaFields? = null
    )

	'''

    private def generateAttribute(RType rawType) {
        val type = rawType.stripFromTypeAliasesExceptInt
        if (type instanceof REnumType) {
            '''var value: «rawType.toKotlinType»? = null,'''
        } else {
            '''var value: «rawType.toKotlinType»? = null,'''
        }
    }

    private def generateReferenceWithMeta(RType type)
    '''
    @Serializable
    open class ReferenceWithMeta«type.toMetaTypeName» (
    	var value: «type.toKotlinType»? = null,
    	var globalReference: String? = null,
    	var externalReference: String? = null,
    	var address: Reference? = null
    )

	'''
    private def generateBasicReferenceWithMeta(RType type)
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