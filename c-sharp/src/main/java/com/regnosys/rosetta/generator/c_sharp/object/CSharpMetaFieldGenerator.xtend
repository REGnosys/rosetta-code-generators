package com.regnosys.rosetta.generator.c_sharp.object

import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.List

import static com.regnosys.rosetta.generator.c_sharp.util.CSharpModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.util.IterableUtil.*
import com.regnosys.rosetta.types.RType
import jakarta.inject.Inject
import com.regnosys.rosetta.types.REnumType
import com.regnosys.rosetta.types.RObjectFactory
import com.regnosys.rosetta.generator.c_sharp.util.CSharpTranslator
import com.regnosys.rosetta.types.RDataType

class CSharpMetaFieldGenerator {
	@Inject
	extension CSharpModelObjectBoilerPlate
	@Inject
	extension RObjectFactory
	@Inject
	extension CSharpTranslator

    def generateMetaFields(List<Data> rosettaClasses, Iterable<RosettaMetaType> metaTypes, String version) {
        val metaFieldsImports = generateMetaFieldsImports.toString

        val refs = rosettaClasses
            .map[buildRDataType]
            .flatMap[ownAttributes]
            .filter[RMetaAnnotatedType.hasAttributeMeta && RMetaAnnotatedType.metaAttributes.exists[name=="reference" || name =="address"]]
            .map[RMetaAnnotatedType.RType.stripFromTypeAliasesExceptInt]
            .toSet

        var referenceWithMeta = '';

        for (ref : refs) {
            if (ref instanceof RDataType)
                referenceWithMeta += generateReferenceWithMeta(ref).toString
            else
                referenceWithMeta += generateBasicReferenceWithMeta(ref).toString
        }

        // Any enumerations with comments currently fails to parse correctly.
        val missing = rosettaClasses
            .map[buildRDataType]
            .flatMap[ownAttributes]
            .filter[RMetaAnnotatedType.hasAttributeMeta && !RMetaAnnotatedType.metaAttributes.exists[name == "reference" || name =="address"] && RMetaAnnotatedType.RType.name === null]
            .toSet
        for (m : missing) {
            println("Missing: " + m.name + " enclosed by: " + m.RMetaAnnotatedType.RType + " : " +  m.RMetaAnnotatedType.RType)
        }

        val metas = rosettaClasses
            .map[buildRDataType]
            .flatMap[ownAttributes]
            .filter[RMetaAnnotatedType.hasAttributeMeta && !RMetaAnnotatedType.metaAttributes.exists[name == "reference" || name =="address"] && RMetaAnnotatedType.RType.name !== null]
            .map[RMetaAnnotatedType.RType.stripFromTypeAliasesExceptInt]
            .toSet

        for (meta : metas) {
            referenceWithMeta += generateFieldWithMeta(meta).toString
        }

        val metaFields = genMetaFields(metaTypes.filter[t|t.name != "key" && t.name != "id" && t.name != "reference" && t.name !="address" && t.name != "location"], version)

		val metaAndTemplateFields = genMetaAndTemplateFields(metaTypes.filter[t|t.name != "key" && t.name != "id" && t.name != "reference" && t.name !="address" && t.name != "location"], version)

        return '''
        «fileComment(version)»
        
        #nullable enable // Allow nullable reference types
        
        «metaFieldsImports»
        
        public class Key
        {
        	[JsonConstructor]
        	public Key(string keyValue, string? scope)
        	{
        		Scope = scope;
        		KeyValue = keyValue;
        	}
        	
            [JsonProperty("value")]
        	public string KeyValue { get; }
        	public string? Scope { get; }
        }
        
        public class Reference
        {
        	[JsonConstructor]
        	public Reference(string? reference, string? scope)
        	{
        		Scope = scope;
        		ReferenceValue = reference;
        	}
        	[JsonProperty("value")]
        	public string? ReferenceValue { get; }
        	public string? Scope { get; }
        }
        
        «referenceWithMeta»
        «metaFields»
        «metaAndTemplateFields»
        }'''
    }

    private def generateAttribute(RType rawType, boolean isOptional) {
        val type = rawType.stripFromTypeAliasesExceptInt
        '''
        «IF type instanceof REnumType»[JsonConverter(typeof(StringEnumConverter))]«ELSEIF rawType.isDate»[JsonConverter(typeof(Rosetta.Lib.LocalDateConverter))]«ENDIF»
        public «IF isOptional»«rawType.toOptionalCSharpType»«ELSE»«rawType.toQualifiedCSharpType»«ENDIF» Value { get; }'''
    }

    private def generateInterface(RType rawType, boolean isReference) {
        val type = rawType.stripFromTypeAliasesExceptInt
        '''I«IF type instanceof REnumType»Enum«ELSEIF rawType.isStruct»Value«ENDIF»«IF isReference»Reference«ELSE»Field«ENDIF»WithMeta<«rawType.toQualifiedCSharpType»>'''
    }

    private def generateFieldInterface(RType type) {
        generateInterface(type, false)
    }

    private def generateReferenceInterface(RType type) {
        generateInterface(type, true)
    }

    private def generateBasicReferenceWithMeta(RType type) '''
        «""»
            public class BasicReferenceWithMeta«type.toMetaTypeName» : «generateReferenceInterface(type)»
            {
                [JsonConstructor]
                public BasicReferenceWithMeta«type.toMetaTypeName»(«type.toOptionalCSharpType» value, string? globalReference, string? externalReference, Reference? address)
                {
                    Value = value;
                    GlobalReference = globalReference;
                    ExternalReference = externalReference;
                    Address = address;
                }
                
                «generateAttribute(type, true)»
                
                public string? GlobalReference { get; }
                
                public string? ExternalReference { get; }
                
                public Reference? Address { get; }
            }

    '''

    private def generateFieldWithMeta(RType type) {
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
                    public MetaFields(«IF !typesDistinct.empty»«FOR t : typesDistinct SEPARATOR ', '»«t.typeCall.type.name.toCSharpBasicType»? «t.name.toFirstLower»«ENDFOR», «ENDIF»string? globalKey, string? externalKey, IEnumerable<Key> location)
                    {
                        «FOR t : typesDistinct»
                        	«t.name.toFirstUpper» = «t.name.toFirstLower»;
                        «ENDFOR»
                        GlobalKey = globalKey;
                        ExternalKey = externalKey;
                        Location = location;
                    }
                    
                    «FOR t : typesDistinct SEPARATOR '\n\n        '»public «t.typeCall.type.name.toCSharpBasicType»? «t.name.toFirstUpper» { get; }«ENDFOR»
                    
                    public string? GlobalKey { get; }
                    
                    public string? ExternalKey { get; }
                    
                    public IEnumerable<Key> Location { get; }
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
                    public MetaAndTemplateFields(«IF !typesDistinct.empty»«FOR t : typesDistinct SEPARATOR ', '»«t.typeCall.type.name.toCSharpBasicType»? «t.name.toFirstLower»«ENDFOR», «ENDIF»string? globalKey, string? externalKey, string? templateGlobalReference, IEnumerable<Key> location)
                    {
                        «FOR t : typesDistinct SEPARATOR ';'»«t.name.toFirstUpper» = «t.name.toFirstLower»;«ENDFOR»
                        GlobalKey = globalKey;
                        ExternalKey = externalKey;
                        TemplateGlobalReference = templateGlobalReference;
                        Location = location;
                    }
                    
                    «FOR t : typesDistinct SEPARATOR '\n\n        '»public «t.typeCall.type.name.toCSharpBasicType»? «t.name.toFirstUpper» { get; }«ENDFOR»
                    
                    public string? GlobalKey { get; }
                    
                    public string? ExternalKey { get; }
                    
                    public string? TemplateGlobalReference { get; }
                    
                    public IEnumerable<Key> Location { get; }
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

    private def generateReferenceWithMeta(RType rawType) {
        val type = rawType.stripFromTypeAliasesExceptInt
        '''
        «""»
            public class ReferenceWithMeta«rawType.toMetaTypeName»«IF type instanceof REnumType»Enum«ENDIF» : «generateReferenceInterface(rawType)»
            {
                [JsonConstructor]
                public ReferenceWithMeta«rawType.toMetaTypeName»(«rawType.toOptionalCSharpType» value, string? globalReference, string? externalReference, Reference? address)
                {
                    Value = value;
                    GlobalReference = globalReference;
                    ExternalReference = externalReference;
                    Address = address;
                }
                
                «generateAttribute(rawType, true)»
                
                public string? GlobalReference { get; }
                
                public string? ExternalReference { get; }
                
                public Reference? Address { get; }
            }

    '''
    }
}
