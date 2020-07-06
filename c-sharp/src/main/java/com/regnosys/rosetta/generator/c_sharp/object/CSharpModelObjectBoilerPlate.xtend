package com.regnosys.rosetta.generator.c_sharp.object

import com.regnosys.rosetta.generator.object.ExpandedAttribute

import static extension com.regnosys.rosetta.generator.c_sharp.util.CSharpTranslator.*
import com.regnosys.rosetta.generator.object.ExpandedType
import java.util.HashSet
import java.util.Arrays

class CSharpModelObjectBoilerPlate {
    static val keywords = new HashSet<String>(Arrays.asList("string", "int", "decimal", "bool", "event"));

    def isKeyWord(String name) {
        keywords.contains(name)        
    }

    def isMissingType(ExpandedAttribute attribute) {
        // TODO: Check for FieldWithMeta??
        attribute.toRawType === null || (attribute.hasMetas && attribute.refIndex < 0 && attribute.type.name === null)
    }

    def matchesEnclosingType(ExpandedAttribute attribute) {
        attribute.name.toFirstUpper == attribute.enclosingType
    }

    static def removePackage(String name) {
        if (name !== null && name.contains(".")) {
            // Remove any packages from basic types e.g. NodaTime.LocalTime
            return name.substring(name.lastIndexOf(".") + 1)
        }
        return name
    }

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

    def toJsonName(ExpandedAttribute attribute) {
        return attribute.name.toFirstLower
    }

    static def toMetaTypeName(ExpandedType type) {
        removePackage(type.toCSharpType).toFirstUpper
    }
    

    def toParamName(ExpandedAttribute attribute) {
        var name = attribute.name.toFirstLower
        // Ensure parameter name does not match C# keyWords
        if (isKeyWord(name)) {
            name += "Value"
        }
        return name
    }

    def toPropertyName(ExpandedAttribute attribute) {
        var name = attribute.name.toFirstUpper
        // Ensure property name does not match enclosing type
        if (name == attribute.enclosingType) {
            name += "Value"
        }
        return name
    }

    def toRawType(ExpandedAttribute attribute) {
        if (!attribute.hasMetas) {
            if (attribute.enum) {
                val type = attribute.type
                type.toQualifiedCSharpType
                
            }
            else
                removePackage(attribute.type.toCSharpType)
        }
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
