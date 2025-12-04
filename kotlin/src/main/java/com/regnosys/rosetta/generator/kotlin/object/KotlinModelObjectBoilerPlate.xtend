package com.regnosys.rosetta.generator.kotlin.object

import com.regnosys.rosetta.types.RType
import com.regnosys.rosetta.types.RAttribute
import jakarta.inject.Inject
import com.regnosys.rosetta.types.REnumType
import com.regnosys.rosetta.generator.kotlin.util.KotlinTranslator
import com.regnosys.rosetta.types.RDataType

class KotlinModelObjectBoilerPlate {
	@Inject
	extension KotlinTranslator

    def toAttributeName(RAttribute attribute) {
        if (attribute.name == "val")
        '''`val`'''
		else
        attribute.name.toFirstLower
    }

    def replaceTabsWithSpaces(CharSequence code) {
        code.toString.replace('\t', '  ')
    }

    def toEnumAnnotationType(RType type) {
        '''«type.name»'''
    }

    def toType(RAttribute rawAttribute) {
        val attribute = rawAttribute.originalAttribute
        if (attribute.multi)
            '''MutableList<«attribute.toRawType»>'''
		else if (attribute.cardinality.optional)
            '''«attribute.toRawType»'''
		else
        '''«attribute.toRawType»'''
    }

    private def originalAttribute(RAttribute attribute) {
    	var current = attribute
    	while (current.parentAttribute !== null) {
    		current = current.parentAttribute
    	}
    	return current
    }

    private def toRawType(RAttribute attribute) {
        val t = attribute.RMetaAnnotatedType
        val type = t.RType.stripFromTypeAliasesExceptInt
        if (!t.hasAttributeMeta)
            type.toKotlinType
        else if (t.hasMetaAttribute("reference") || t.hasMetaAttribute("address")) {
           if (type instanceof RDataType)
                type.toReferenceWithMetaTypeName
            else
                type.toBasicReferenceWithMetaTypeName
        }
        else
            type.toFieldWithMetaTypeName
    }

    def toReferenceWithMetaTypeName(RType type) {
        '''ReferenceWithMeta«type.toMetaTypeName»'''
    }

    def toBasicReferenceWithMetaTypeName(RType type) {
        '''BasicReferenceWithMeta«type.toMetaTypeName»'''
    }

    def toFieldWithMetaTypeName(RType type) {
        '''FieldWithMeta«type.toMetaTypeName»'''
    }

    def toMetaTypeName(RType rawType) {
        val type = rawType.stripFromTypeAliasesExceptInt
        val name = rawType.toKotlinType

        if (type instanceof REnumType) {
            return name
        } else if (name.contains(".")) {
            return name.substring(name.lastIndexOf(".") + 1).toFirstUpper
        }

        return name.toFirstUpper
    }
}