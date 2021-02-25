package com.regnosys.rosetta.generator.c_sharp.object

import com.regnosys.rosetta.generator.object.ExpandedType
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.List

import static com.regnosys.rosetta.generator.c_sharp.util.CSharpModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.c_sharp.object.CSharpModelObjectBoilerPlate.*
import static extension com.regnosys.rosetta.generator.c_sharp.util.CSharpTranslator.*
import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*
import static extension com.regnosys.rosetta.generator.util.Util.*

class CSharpMetaFieldGenerator {

    def generateMetaFields(List<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version) {
        val metaFieldsImports = generateMetaFieldsImports.toString

        val refs = rosettaClasses.flatMap[expandedAttributes].filter[hasMetas && metas.exists[name == "reference"]].map [
            type
        ].toSet

        var referenceWithMeta = '';

        for (ref : refs) {
            if (ref.isType)
                referenceWithMeta += generateReferenceWithMeta(ref).toString
            else
                referenceWithMeta += generateBasicReferenceWithMeta(ref).toString
        }

        // Any enumerations with comments currently fails to parse correctly.
        val missing = rosettaClasses.flatMap[expandedAttributes].filter[hasMetas && !metas.exists[name == "reference"] && type.name === null].toSet
        for (m : missing) {
            println("Missing: " + m.name + " enclosed by: " + m.enclosingType + " : " +  m.type)
        }

        val metas = rosettaClasses.flatMap[expandedAttributes].filter[hasMetas && !metas.exists[name == "reference"] && type.name !== null].
            map[type].toSet

        for (meta : metas) {
            referenceWithMeta += generateFieldWithMeta(meta).toString
        }

        val metaFields = genMetaFields(metaTypes.filter[t|t.name != "key" && t.name != "id" && t.name != "reference"], version)

		val metaAndTemplateFields = genMetaAndTemplateFields(metaTypes.filter[t|t.name != "key" && t.name != "id" && t.name != "reference"], version)

        return '''
        «fileComment(version)»
        
        #nullable enable // Allow nullable reference types
        
        «metaFieldsImports»
        «referenceWithMeta»
        «metaFields»
        «metaAndTemplateFields»
        }'''
    }

    private def generateAttribute(ExpandedType type, boolean isOptional) '''
        «IF type.enumeration»[JsonConverter(typeof(StringEnumConverter))]«ELSEIF type.isDate»[JsonConverter(typeof(Rosetta.Lib.LocalDateConverter))]«ENDIF»
        public «IF isOptional»«type.toOptionalCSharpType»«ELSE»«type.toQualifiedCSharpType»«ENDIF» Value { get; }'''

    private def generateInterface(ExpandedType type, boolean isReference) '''
        I«IF type.enumeration»Enum«ELSEIF type.isStruct»Value«ENDIF»«IF isReference»Reference«ELSE»Field«ENDIF»WithMeta<«type.toQualifiedCSharpType»>'''

    private def generateFieldInterface(ExpandedType type) {
        generateInterface(type, false)
    }

    private def generateReferenceInterface(ExpandedType type) {
        generateInterface(type, true)
    }

    private def generateBasicReferenceWithMeta(ExpandedType type) '''
        «""»
            public class BasicReferenceWithMeta«type.toMetaTypeName» : «generateReferenceInterface(type)»
            {
                [JsonConstructor]
                public BasicReferenceWithMeta«type.toMetaTypeName»(«type.toOptionalCSharpType» value, string? globalReference, string? externalReference)
                {
                    Value = value;
                    GlobalReference = globalReference;
                    ExternalReference = externalReference;
                }
                
                «generateAttribute(type, true)»
                
                public string? GlobalReference { get; }
                
                public string? ExternalReference { get; }
            }
            
    '''

    private def generateFieldWithMeta(ExpandedType type) {
        val metaTypeName = type.toMetaTypeName
    '''
        «IF type === null || metaTypeName?.length == 0»
«««        Handle types which aren't converted correctly.
            // MISSING: FieldWithMeta for «type.name»
        «ELSE»
            «""»
                public class FieldWithMeta«metaTypeName» : «generateFieldInterface(type)»
                {
                    [JsonConstructor]
                    public FieldWithMeta«metaTypeName»(«type.toQualifiedCSharpType» value, MetaFields? meta)
                    {
                        Value = value;
                        Meta = meta;
                    }
                    
                    «generateAttribute(type, false)»
                    
                    public MetaFields? Meta { get; }
                }
        «ENDIF»
            
    '''
    }

    private def genMetaFields(Iterable<RosettaMetaType> types, String version) {
        val typesDistinct = types.distinct()
        '''
            «""»
                public class MetaFields
                {
                    [JsonConstructor]
                    public MetaFields(«IF !typesDistinct.empty»«FOR t : typesDistinct SEPARATOR ', '»«t.type.name.toCSharpBasicType»? «t.name.toFirstLower»«ENDFOR», «ENDIF»string? globalKey, string? externalKey)
                    {
                        «FOR t : typesDistinct SEPARATOR ';'»«t.name.toFirstUpper» = «t.name.toFirstLower»;«ENDFOR»
                        GlobalKey = globalKey;
                        ExternalKey = externalKey;
                    }
                    
                    «FOR t : typesDistinct SEPARATOR '\n\n        '»public «t.type.name.toCSharpBasicType»? «t.name.toFirstUpper» { get; }«ENDFOR»
                    
                    public string? GlobalKey { get; }
                    
                    public string? ExternalKey { get; }
                }
                
        '''
    }
    
    private def genMetaAndTemplateFields(Iterable<RosettaMetaType> types, String version) {
        val typesDistinct = types.distinct()
        '''
            «""»
                public class MetaAndTemplateFields
                {
                    [JsonConstructor]
                    public MetaAndTemplateFields(«IF !typesDistinct.empty»«FOR t : typesDistinct SEPARATOR ', '»«t.type.name.toCSharpBasicType»? «t.name.toFirstLower»«ENDFOR», «ENDIF»string? globalKey, string? externalKey, string? templateGlobalReference)
                    {
                        «FOR t : typesDistinct SEPARATOR ';'»«t.name.toFirstUpper» = «t.name.toFirstLower»;«ENDFOR»
                        GlobalKey = globalKey;
                        ExternalKey = externalKey;
                        TemplateGlobalReference = templateGlobalReference;
                    }
                    
                    «FOR t : typesDistinct SEPARATOR '\n\n        '»public «t.type.name.toCSharpBasicType»? «t.name.toFirstUpper» { get; }«ENDFOR»
                    
                    public string? GlobalKey { get; }
                    
                    public string? ExternalKey { get; }
                    
                    public string? TemplateGlobalReference { get; }
                }
                
        '''
    }
    

    private def generateMetaFieldsImports() '''
        namespace Org.Isda.Cdm.MetaFields
        {
            using System.Collections.Generic;
        
            using Newtonsoft.Json;
            using Newtonsoft.Json.Converters;
        
            using NodaTime;
        
            using Rosetta.Lib.Meta;
        
    '''

    private def generateReferenceWithMeta(ExpandedType type) '''
        «""»
            public class ReferenceWithMeta«type.toMetaTypeName»«IF type.enumeration»Enum«ENDIF» : «generateReferenceInterface(type)»
            {
                [JsonConstructor]
                public ReferenceWithMeta«type.toMetaTypeName»(«type.toOptionalCSharpType» value, string? globalReference, string? externalReference)
                {
                    Value = value;
                    GlobalReference = globalReference;
                    ExternalReference = externalReference;
                }
                
                «generateAttribute(type, true)»
                
                public string? GlobalReference { get; }
                
                public string? ExternalReference { get; }
            }
            
    '''
}
