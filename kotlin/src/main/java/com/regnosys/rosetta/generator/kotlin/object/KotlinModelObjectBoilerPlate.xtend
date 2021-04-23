package com.regnosys.rosetta.generator.kotlin.object

import com.regnosys.rosetta.generator.object.ExpandedAttribute

import static extension com.regnosys.rosetta.generator.kotlin.util.KotlinTranslator.toKotlinType
import com.regnosys.rosetta.generator.object.ExpandedType

class KotlinModelObjectBoilerPlate {

    def toAttributeName(ExpandedAttribute attribute) {
        if (attribute.name == "val")
        '''`val`'''
		else
        attribute.name.toFirstLower
    }

    def replaceTabsWithSpaces(CharSequence code) {
        code.toString.replace('\t', '  ')
    }

    def toEnumAnnotationType(ExpandedType type) {
        '''«type.name»'''
    }

    def toType(ExpandedAttribute attribute) {
        if (attribute.multiple)
            '''MutableList<«attribute.toRawType»>'''
		else if (attribute.singleOptional)
            '''«attribute.toRawType»'''
		else
        '''«attribute.toRawType»'''
    }

    private def toRawType(ExpandedAttribute attribute) {
        if (!attribute.hasMetas)
            attribute.type.toKotlinType
        else if (attribute.refIndex >= 0) {
            if (attribute.type.isType)
                attribute.type.toReferenceWithMetaTypeName
            else
                attribute.type.toBasicReferenceWithMetaTypeName
        }
        else
            attribute.type.toFieldWithMetaTypeName
    }

    def toReferenceWithMetaTypeName(ExpandedType type) {
        '''ReferenceWithMeta«type.toMetaTypeName»'''
    }

    def toBasicReferenceWithMetaTypeName(ExpandedType type) {
        '''BasicReferenceWithMeta«type.toMetaTypeName»'''
    }

    def toFieldWithMetaTypeName(ExpandedType type) {
        '''FieldWithMeta«type.toMetaTypeName»'''
    }

    static def toMetaTypeName(ExpandedType type) {
        val name = type.toKotlinType

        if (type.enumeration) {
            return name
        } else if (name.contains(".")) {
            return name.substring(name.lastIndexOf(".") + 1).toFirstUpper
        }

        return name.toFirstUpper
    }
}