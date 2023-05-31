package com.regnosys.rosetta.generator.python.object

import com.regnosys.rosetta.generator.object.ExpandedType
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.List

import static com.regnosys.rosetta.generator.python.util.PythonModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.python.object.PythonModelObjectBoilerPlate.*
import static extension com.regnosys.rosetta.generator.python.util.PythonTranslator.*
import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*
import static extension com.regnosys.rosetta.generator.util.Util.*

class PythonMetaFieldGenerator {

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
	'''

    private def generateFieldWithMeta(ExpandedType type) '''
    class FieldWithMeta«type.toMetaTypeName»:
        «generateAttribute(type)»
        meta = MetaFields()

	'''

    private def generateAttribute(ExpandedType type) {
        if (type.enumeration) {
            '''value = «type.toPythonType»'''
        } else {
            '''value = None'''
        }
    }

    private def generateReferenceWithMeta(ExpandedType type)
    '''
    class ReferenceWithMeta«type.toMetaTypeName»:
        value = «type.name»()
        globalReference = None
        externalReference = None
        address = Reference()

	'''
    private def generateBasicReferenceWithMeta(ExpandedType type)
    '''
    class BasicReferenceWithMeta«type.toMetaTypeName»:
        value = None
        globalReference = None
        externalReference = None
        address = Reference()

	'''

    private def genMetaFields(Iterable<RosettaMetaType> types, String version) 
    '''
    class MetaFields:
        «FOR type : types.distinctBy(t|t.name.toFirstLower) SEPARATOR '\n'»«type.name.toFirstLower» = None«ENDFOR»
        globalKey = None
        externalKey = None
        location = []


    class MetaAndTemplateFields:
        «FOR type : types.distinctBy(t|t.name.toFirstLower) SEPARATOR '\n'»«type.name.toFirstLower» = None«ENDFOR»
        globalKey = None
        externalKey = None
        templateGlobalReference = None
        location = []


    class Key:
        scope = None
        value = None

    
    class Reference:
        scope = None
        value = None

	'''
}