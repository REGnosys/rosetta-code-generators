package com.regnosys.rosetta.generator.python.object

import com.regnosys.rosetta.types.RAttribute
import com.regnosys.rosetta.types.RType
import com.regnosys.rosetta.types.REnumType
import static extension com.regnosys.rosetta.generator.python.util.PythonTranslator.toPythonType

class PythonModelObjectBoilerPlate {

    def toAttributeName(RAttribute attribute) {
        return (attribute.name == "val")
            ? '''`val`''' : attribute.name.toFirstLower
    }

    def replaceTabsWithSpaces(CharSequence code) {
        code.toString.replace('\t', '  ')
    }

    def toEnumAnnotationType(RType type) {
        return '''«type.name»''';
    }

    def toType(RAttribute ra) {
        return (ra.isMulti)
            ? '''MutableList<«ra.toRawType»>''' : '''«ra.toRawType»'''
    }

    def toRawType(RAttribute ra) {
        ra.getRMetaAnnotatedType.getRType.toPythonType
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

    static def toMetaTypeName(RType type) {
        val name = type.toPythonType
        if (name === null) {
            return "null-name"
        }
        if (type instanceof REnumType) {
            return name
        }
        if (name.contains(".")) {
            return name.substring(name.lastIndexOf(".") + 1).toFirstUpper
        }
        return name.toFirstUpper
    }
}
