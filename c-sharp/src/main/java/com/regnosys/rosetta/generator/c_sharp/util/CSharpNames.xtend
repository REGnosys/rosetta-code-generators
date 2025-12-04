package com.regnosys.rosetta.generator.c_sharp.util

import com.google.inject.Inject
import com.google.inject.Injector
import com.regnosys.rosetta.generator.c_sharp.enums.CSharpEnumGenerator
import com.regnosys.rosetta.generator.java.RosettaJavaPackages
import com.regnosys.rosetta.generator.util.RosettaAttributeExtensions
import com.regnosys.rosetta.rosetta.RosettaBasicType
import com.regnosys.rosetta.rosetta.RosettaCallableWithArgs
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaExternalFunction
import com.regnosys.rosetta.rosetta.RosettaNamed
import com.regnosys.rosetta.rosetta.RosettaRecordType
import com.regnosys.rosetta.rosetta.RosettaRootElement
import com.regnosys.rosetta.rosetta.RosettaType
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.simple.Function
import java.util.List
import org.eclipse.xtend.lib.annotations.Accessors
import org.eclipse.xtend2.lib.StringConcatenationClient
import org.eclipse.xtext.EcoreUtil2
import com.regnosys.rosetta.rosetta.TypeCall
import com.regnosys.rosetta.rosetta.RosettaTypeAlias
import com.rosetta.util.DottedPath
import com.regnosys.rosetta.types.RAttribute

class CSharpNames {

    @Accessors(PUBLIC_GETTER)
    RosettaJavaPackages packages
    
    @Inject
    extension CSharpTranslator
    

    def StringConcatenationClient toListOrSingleCSharpType(RAttribute attribute) {
        if (attribute.multi) {
            '''«List»<«attribute.RMetaAnnotatedType.RType.toCSharpType»>'''
        } else
            '''«attribute.RMetaAnnotatedType.RType.toCSharpType»'''
    }

    def CSharpType toCSharpType(RosettaCallableWithArgs func) {
        switch (func) {
            Function:
                createCSharpType(modelRootPackage(func).child("functions"), func.name)
            RosettaExternalFunction:
                createCSharpType(packages.defaultLibFunctions, func.name)
            default:
                throw new UnsupportedOperationException("Not implemented for type " + func?.class?.name)
        }
    }

	def CSharpType toCSharpType(TypeCall typeCall) {
		typeCall.type.toCSharpType
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
                    CSharpType.create(packages.defaultLib.child("records").withDots + '.' + type.name.toFirstUpper)
            RosettaExternalFunction:
                createCSharpType(packages.defaultLibFunctions, type.name)
            RosettaTypeAlias:
            	type.typeCall.toCSharpType
            default:
                throw new UnsupportedOperationException("Not implemented for type " + type?.class?.name)
        }
    }

    def createCSharpType(DottedPath pack, String typeName) {
        CSharpType.create(pack.child(typeName).withDots)
    }
    
    def createMetaType(String parent, String meta) {
        MetaType.create(parent, meta)
    }

    def toMetaType(Attribute ctx, String name) {
        var model = ctx.typeCall.type.model
        var pkg = DottedPath.splitOnDots(model.name).child("metafields")
        return createCSharpType(pkg, name)
    }

    def private DottedPath modelRootPackage(RosettaNamed namedType) {
        val rootElement = EcoreUtil2.getContainerOfType(namedType, RosettaRootElement)
        val model = rootElement.model
        if (model === null)
            // Faked attributes
            throw new IllegalArgumentException('''Can not compute package name for «namedType.eClass.name» «namedType.name». Element is not attached to a RosettaModel.''')
        return DottedPath.splitOnDots(model.name)
    }

    private def CSharpType createForBasicType(String typeName) {
        return CSharpType.create(typeName ?: 
        "missing built-in type " + typeName
        )
    }

    static class Factory {
        @Inject Injector injector

        def create() {
            create(new RosettaJavaPackages())
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
