package com.regnosys.rosetta.generator.c_sharp.object

import java.util.HashSet
import java.util.Arrays
import com.regnosys.rosetta.types.RType
import com.regnosys.rosetta.types.RAttribute
import jakarta.inject.Inject
import com.regnosys.rosetta.types.REnumType
import com.regnosys.rosetta.generator.c_sharp.util.CSharpTranslator
import com.regnosys.rosetta.types.RDataType

class CSharpModelObjectBoilerPlate {
    @Inject
    extension CSharpTranslator
    static val keywords = new HashSet<String>(Arrays.asList("string", "int", "decimal", "bool", "event"));

    def isKeyWord(String name) {
        keywords.contains(name)        
    }

    def isMissingType(RAttribute attribute) {
        // TODO: Check for FieldWithMeta??
        val t = attribute.RMetaAnnotatedType
        attribute.toRawType === null || (t.hasAttributeMeta && !(t.hasMetaAttribute("reference") || t.hasMetaAttribute("address")) && t.RType.name === null)
    }

    def matchesEnclosingType(RAttribute attribute) {
        attribute.name.toFirstUpper == attribute.enclosingType?.name
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

    def toAttributeName(RAttribute attribute) {
        attribute.name
    }

    def toBasicReferenceWithMetaTypeName(RType type) {
        '''BasicReferenceWithMeta«type.toMetaTypeName»'''
    }

    def toEnumAnnotationType(RType type) {
        '''«type.name»'''
    }

    def toFieldWithMetaTypeName(RType type) {
        '''FieldWithMeta«type.toMetaTypeName»'''
    }

    def toJsonName(RAttribute attribute) {
        return attribute.name.toFirstLower
    }

    def toMetaTypeName(RType rawType) {
        removePackage(rawType.toCSharpType).toFirstUpper
    }

    def toQualifiedMetaTypeName(RType rawType) {
        val type = rawType.stripFromTypeAliasesExceptInt
        '''«IF type instanceof REnumType»Enums.«ENDIF»«removePackage(rawType.toCSharpType)»'''
    }

    def toParamName(RAttribute attribute) {
        var name = attribute.name.toFirstLower
        // Ensure parameter name does not match C# keyWords
        if (isKeyWord(name)) {
            name += "Value"
        }
        return name
    }

    def toPropertyName(RAttribute attribute) {
        var name = attribute.name.toFirstUpper
        // Ensure property name does not match enclosing type
        if (name == attribute.enclosingType.name) {
            name += "Value"
        }
        return name
    }

    def toRawType(RAttribute attribute) {
        val t = attribute.originalAttribute.RMetaAnnotatedType
        if (!t.hasAttributeMeta) {
            val type = t.RType.stripFromTypeAliasesExceptInt
            if (type instanceof REnumType) {
                t.RType.toQualifiedCSharpType
            }
            else
                removePackage(t.RType.toCSharpType)
        }
        else if (t.hasMetaAttribute("reference") || t.hasMetaAttribute("address")) {
            if (t.RType instanceof RDataType)
                t.RType.toReferenceWithMetaTypeName
            else
                t.RType.toBasicReferenceWithMetaTypeName
        } else
            t.RType.toFieldWithMetaTypeName
    }

    def toReferenceWithMetaTypeName(RType type) {
        '''ReferenceWithMeta«type.toMetaTypeName»'''
    }

    def toType(RAttribute rawAttr) {
    	val attribute = rawAttr.originalAttribute
        val typeName = attribute.toRawType
        if (attribute.multi) {
            // All fields of one-of have to be nullable.
            '''IEnumerable<«typeName»>'''
        }
        else if (attribute.cardinality.optional)
            '''«typeName»?'''
        else
            '''«typeName»'''
    }
    
    private def RAttribute originalAttribute(RAttribute attr) {
    	var curr = attr
    	while (curr.parentAttribute !== null) {
    		curr = curr.parentAttribute
    	}
    	return curr
    }
}
