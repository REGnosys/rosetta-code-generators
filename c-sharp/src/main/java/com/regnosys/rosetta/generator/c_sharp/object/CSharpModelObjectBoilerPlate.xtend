package com.regnosys.rosetta.generator.c_sharp.object

import com.regnosys.rosetta.generator.object.ExpandedAttribute

import static extension com.regnosys.rosetta.generator.c_sharp.util.CSharpTranslator.toCSharpType
import com.regnosys.rosetta.generator.object.ExpandedType

class CSharpModelObjectBoilerPlate {

    def replaceTabsWithSpaces(CharSequence code) {
        // Visual Studio default is 4-spaces
        code.toString.replace('\t', '    ')
    }

    def toAttributeName(ExpandedAttribute attribute) {
        attribute.name
    }

    def toBasicReferenceWithMetaTypeName(ExpandedType type) {
        '''BasicReferenceWithMeta«type.toMetaTypeName»'''
    }

    def toEnumAnnotationType(ExpandedType type) {
        '''«type.name»'''
    }

    def toFieldWithMetaTypeName(ExpandedType type) {
        '''FieldWithMeta«type.toMetaTypeName»'''
    }

    static def toMetaTypeName(ExpandedType type) {
        val name = type.toCSharpType

        removePackage(name).toFirstUpper
    }

    static def removePackage(String name) {
        if (name.contains(".")) {
            // Remove any packages from basic types e.g. NodaTime.LocalTime
            return name.substring(name.lastIndexOf(".") + 1)
        }
        return name
    }

    def toParamName(ExpandedAttribute attribute) {
        attribute.name.toFirstLower
    }

    def toPropertyName(ExpandedAttribute attribute) {
        attribute.name.toFirstUpper
    }

    private def toRawType(ExpandedAttribute attribute) {
        if (!attribute.hasMetas)
            removePackage(attribute.type.toCSharpType)
        else if (attribute.refIndex >= 0) {
            if (attribute.type.isType)
                attribute.type.toReferenceWithMetaTypeName
            else
                attribute.type.toBasicReferenceWithMetaTypeName
        } else
            attribute.type.toFieldWithMetaTypeName
    }

    def toReferenceWithMetaTypeName(ExpandedType type) {
        '''ReferenceWithMeta«type.toMetaTypeName»'''
    }

    def toType(ExpandedAttribute attribute) {
        val typeName = attribute.toRawType
        if (attribute.multiple)
            '''IEnumerable<«typeName»>'''
        else if (attribute.singleOptional)
            '''«typeName»?'''
        else
            '''«typeName»'''
    }
}
