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

        val metas = rosettaClasses.flatMap[expandedAttributes].filter[hasMetas && !metas.exists[name == "reference"]].
            map[type].toSet

        for (meta : metas) {
            referenceWithMeta += generateFieldWithMeta(meta).toString
        }

        val metaFields = genMetaFields(metaTypes.filter[t|t.name != "id" && t.name != "reference"], version)

        return '''
        «fileComment(version)»
        
        #nullable enable // Allow nullable reference types
        
        «metaFieldsImports»
        «referenceWithMeta»
        «metaFields»
        }'''
    }

    private def generateAttribute(ExpandedType type) {
        /*if (type.enumeration) {
         *      // TODO: Work out indentation!!! affects shouldGenerateMetaTypes??
         * '''@JsonDeserialize(contentAs = classOf[«type.name».Value])
         *     @JsonCSharpEnumeration(classOf[«type.name».Class])
         *     «type.toCSharpType»? value'''
         } else */
        {
            '''public «type.toOptionalCSharpType» Value { get; }'''
        }
    }

    private def generateBasicReferenceWithMeta(ExpandedType type) '''
        «""»
            public class BasicReferenceWithMeta«type.toMetaTypeName»
            {
                [JsonConstructor]
                public BasicReferenceWithMeta«type.toMetaTypeName»(«type.toOptionalCSharpType» value, string? globalReference, string? externalReference)
                {
                    Value = value;
                    GlobalReference = globalReference;
                    ExternalReference = externalReference;
                }
                
                «generateAttribute(type)»
                
                public string? GlobalReference { get; }
                
                public string? ExternalReference { get; }
            }
            
    '''

    private def generateFieldWithMeta(ExpandedType type) '''
        «""»
            public class FieldWithMeta«type.toMetaTypeName»
            {
                [JsonConstructor]
                public FieldWithMeta«type.toMetaTypeName»(«type.toOptionalCSharpType» value, MetaFields? meta)
                {
                    Value = value;
                    Meta = meta;
                }
                
                «generateAttribute(type)»
                
                public MetaFields? Meta { get; }
            }
            
    '''

    private def genMetaFields(Iterable<RosettaMetaType> types, String version) {
        val typesDistinct = types.distinct()
        '''
            «""»
                public class MetaFields
                {
                    [JsonConstructor]
                    public MetaFields(«FOR t : typesDistinct SEPARATOR ', '»«t.type.name.toCSharpBasicType»? «t.name.toFirstLower»«ENDFOR», string? globalKey, string? externalKey)
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

    private def generateMetaFieldsImports() '''
        namespace Org.Isda.Cdm.MetaFields
        {
            using System.Collections.Generic;
            using System.Linq;
        
            using Newtonsoft.Json;
            using NodaTime;
        
    '''

    private def generateReferenceWithMeta(ExpandedType type) '''
        «""»
            public class ReferenceWithMeta«type.toMetaTypeName»
            {
                [JsonConstructor]
                public ReferenceWithMeta«type.toMetaTypeName»(«type.toOptionalCSharpType» value, string? globalReference, string? externalReference)
                {
                    Value = value;
                    GlobalReference = globalReference;
                    ExternalReference = externalReference;
                }
                
                «generateAttribute(type)»
                
                public string? GlobalReference { get; }
                
                public string? ExternalReference { get; }
            }
            
    '''
}
