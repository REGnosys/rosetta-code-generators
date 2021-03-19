package com.regnosys.rosetta.generator.c_sharp.util

import com.google.inject.Inject
import com.google.inject.Injector
import com.regnosys.rosetta.generator.java.RosettaJavaPackages
import com.regnosys.rosetta.generator.java.RosettaJavaPackages.Package
import com.regnosys.rosetta.generator.java.RosettaJavaPackages.RootPackage
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import com.regnosys.rosetta.generator.object.ExpandedType
import com.regnosys.rosetta.generator.util.RosettaAttributeExtensions
import com.regnosys.rosetta.rosetta.RosettaBasicType
import com.regnosys.rosetta.rosetta.RosettaCalculationType
import com.regnosys.rosetta.rosetta.RosettaCallableWithArgs
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaExternalFunction
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.rosetta.RosettaNamed
import com.regnosys.rosetta.rosetta.RosettaQualifiedType
import com.regnosys.rosetta.rosetta.RosettaRecordType
import com.regnosys.rosetta.rosetta.RosettaRootElement
import com.regnosys.rosetta.rosetta.RosettaType
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.simple.Function
import com.regnosys.rosetta.types.RBuiltinType
import com.regnosys.rosetta.types.RDataType
import com.regnosys.rosetta.types.REnumType
import com.regnosys.rosetta.types.RFeatureCallType
import com.regnosys.rosetta.types.RRecordType
import com.regnosys.rosetta.types.RType
import java.util.List
import org.eclipse.xtend.lib.annotations.Accessors
import org.eclipse.xtend2.lib.StringConcatenationClient
import org.eclipse.xtext.EcoreUtil2
import com.regnosys.rosetta.generator.c_sharp.enums.CSharpEnumGenerator

class CSharpNames {

    @Accessors(PUBLIC_GETTER)
    RosettaJavaPackages packages

    def StringConcatenationClient toListOrSingleCSharpType(Attribute attribute) {
        if (attribute.card.isIsMany) {
            '''«List»<«attribute.type.toCSharpType()»>'''
        } else
            '''«attribute.type.toCSharpType()»'''
    }

    def CSharpType toCSharpType(ExpandedType type) {
        if (type.name == RosettaAttributeExtensions.METAFIELDS_CLASS_NAME || type.name == RosettaAttributeExtensions.META_AND_TEMPLATE_FIELDS_CLASS_NAME) {
            return createCSharpType(packages.basicMetafields, type.name)
        }
        if (type.builtInType) {
            return createForBasicType(type.name)
        }
        createCSharpType(new RootPackage(type.model), type.name)
    }

    def CSharpType toCSharpType(RosettaCallableWithArgs func) {
        switch (func) {
            Function:
                createCSharpType(modelRootPackage(func).functions, func.name)
            RosettaExternalFunction:
                createCSharpType(packages.defaultLibFunctions, func.name)
            default:
                throw new UnsupportedOperationException("Not implemented for type " + func?.class?.name)
        }
    }

    def CSharpType toCSharpType(RosettaType type) {
        switch (type) {
            RosettaBasicType:
                createForBasicType(type.name)
            Data,
            RosettaEnumeration:
                createCSharpType(modelRootPackage(type), CSharpEnumGenerator.toCSharpName(type.name, true))
            RosettaRecordType:
                CSharpType.create(type.name) ?:
                    CSharpType.create(packages.defaultLibRecords.name + '.' + type.name.toFirstUpper)
            RosettaExternalFunction:
                createCSharpType(packages.defaultLibFunctions, type.name)
            RosettaCalculationType,
            RosettaQualifiedType:
                CSharpType.create('java.lang.String')
            default:
                throw new UnsupportedOperationException("Not implemented for type " + type?.class?.name)
        }
    }

    def CSharpType toCSharpType(RType rType) {
        switch (rType) {
            RBuiltinType:
                rType.name.createForBasicType
            REnumType:
                rType.enumeration.toCSharpType
            RDataType:
                rType.data.toCSharpType
            RFeatureCallType:
                rType.featureType.toCSharpType
            RRecordType:
                (rType.record as RosettaType).toCSharpType
            default:
                CSharpType.create(rType.name)
        }
    }

    def createCSharpType(Package pack, String typeName) {
        CSharpType.create(pack.child(typeName).name())
    }
    
    def createMetaType(String parent, String meta) {
        MetaType.create(parent, meta)
    }

    def toMetaType(Attribute ctx, String name) {
        var model = ctx.type.eContainer
        if (model instanceof RosettaModel) {
            var pkg = new RootPackage(model.name).metaField
            return createCSharpType(pkg, name)
        }
        
        if(model instanceof RosettaBasicType) {
            // built-in meta types are defined in metafield package
            return createCSharpType(packages.basicMetafields, name)
        }
    }

    def toMetaType(ExpandedAttribute type, String name) {
        if(type.type.isBuiltInType) {
            // built-in meta types are defined in metafield package
            return createCSharpType(packages.basicMetafields, name)
        }
        var parentPKG = new RootPackage(type.type.model)
        var metaParent = parentPKG.child(type.type.name).name()
        
        var metaPKG = parentPKG.metaField
        var meta = metaPKG.child(name).name()       
        createMetaType(metaParent, meta)
    }

    def private RootPackage modelRootPackage(RosettaNamed namedType) {
        val rootElement = EcoreUtil2.getContainerOfType(namedType, RosettaRootElement)
        val model = rootElement.model
        if (model === null)
            // Faked attributes
            throw new IllegalArgumentException('''Can not compute package name for «namedType.eClass.name» «namedType.name». Element is not attached to a RosettaModel.''')
        return new RootPackage(model)
    }

    private def CSharpType createForBasicType(String typeName) {
        return CSharpType.create(typeName ?: 
        "missing built-in type " + typeName
        )
    }

    static class Factory {
        @Inject Injector injector

        def create(RosettaModel model) {
            create(new RosettaJavaPackages(model))
        }

        private def create(RosettaJavaPackages packages) {
            val result = new CSharpNames
            injector.injectMembers(result)
            result.packages = packages
            return result
        }
    }

    def voidType() {
        CSharpType.create('void')
    }

}
