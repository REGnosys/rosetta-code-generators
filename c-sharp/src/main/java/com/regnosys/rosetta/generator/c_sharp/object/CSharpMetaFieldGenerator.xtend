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
          
          val refs = rosettaClasses
               .flatMap[expandedAttributes]
               .filter[hasMetas && metas.exists[name=="reference"]]
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
               .filter[hasMetas && !metas.exists[name=="reference"]]
               .map[type]
               .toSet

          for (meta:metas) {
               referenceWithMeta += generateFieldWithMeta(meta).toString
          }
          
          val metaFields = genMetaFields(metaTypes.filter[t|t.name!="id" && t.name!="reference"], version)
          
          return fileComment(version) + metaFieldsImports + referenceWithMeta + metaFields + "\n}"
     }
     
     private def generateAttribute(ExpandedType type) {
          /*if (type.enumeration) {
               // TODO: Work out indentation!!! affects shouldGenerateMetaTypes??
'''@JsonDeserialize(contentAs = classOf[«type.name».Value])
    @JsonCSharpEnumeration(classOf[«type.name».Class])
    «type.toCSharpType»? value'''
          } else */{
               '''«type.toCSharpType»? Value { get; }'''
          }
     }
     
     private def generateBasicReferenceWithMeta(ExpandedType type) '''
        «""»
            class BasicReferenceWithMeta«type.toMetaTypeName»
            {
                «type.toCSharpType»? Value { get; }
                
                string? GlobalReference { get; }
                
                string? ExternalReference { get; }
            }
            
        '''
     
    private def generateFieldWithMeta(ExpandedType type) '''
        «""»
            class FieldWithMeta«type.toMetaTypeName»
            {
                «generateAttribute(type)»
                
                MetaFields? Meta { get; }
            }
            
        '''

     private def genMetaFields(Iterable<RosettaMetaType> types, String version) '''                    
        «""»
            class MetaFields
            {
                «FOR type : types.distinct() SEPARATOR '\n\n        '»«type.type.name.toCSharpBasicType»? «type.name.toFirstUpper» { get; }«ENDFOR»
                
                string? GlobalKey { get; }
                
                string? ExternalKey { get; }
            }
            
        '''

    private def generateMetaFieldsImports() '''
        namespace Org.Isda.Cdm.Metafields
        {
            using Org.Isda.Cdm;
        
        '''

    private def generateReferenceWithMeta(ExpandedType type) '''
        «""»
            class ReferenceWithMeta«type.toMetaTypeName»
            {
                «type.toCSharpType»? Value { get; }
                
                string? GlobalReference { get; }
                
                string? ExternalReference { get; }
            }
            
        '''
}
