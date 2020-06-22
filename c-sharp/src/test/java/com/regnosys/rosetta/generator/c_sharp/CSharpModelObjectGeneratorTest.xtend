package com.regnosys.rosetta.generator.c_sharp

import com.google.inject.Inject
import com.google.inject.Provider
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import java.io.File
import java.nio.file.Files
import java.nio.file.Paths
import org.eclipse.xtext.resource.XtextResourceSet
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.eclipse.xtext.testing.util.ParseHelper
import org.junit.jupiter.api.Disabled
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class CSharpModelObjectGeneratorTest {

    @Inject
    extension ModelHelper

    @Inject
    CSharpCodeGenerator generator;

    protected def boolean containsFileComment(String c_sharp) {
        c_sharp.startsWith('''
            // This file is auto-generated from the ISDA Common Domain Model, do not edit.
            //
            // Version: test
            //
        ''')
    }

    protected def boolean containsNamespace(String c_sharp, String namespace) {
        c_sharp.contains('''
            namespace «namespace»
            {
        ''')
    }

    protected def boolean containsNullable(String c_sharp) {
        c_sharp.contains('''#nullable enable''')
    }

    protected def boolean containsUsings(String c_sharp) {
        containsUsings(c_sharp, true)
    }

    protected def boolean containsUsings(String c_sharp, boolean includeMetaFields) {
        c_sharp.contains('''
            «""»
                using System.Collections.Generic;
                using System.Linq;
            
                using Newtonsoft.Json;
                using Newtonsoft.Json.Converters;
                using NodaTime;
                «IF includeMetaFields»using Org.Isda.Cdm.MetaFields;«ENDIF»
        ''')
    }

    @Test
    def void shouldGenerateEnums() {
        val c_sharp = '''
            enum TestEnum: <"Test enum description.">
                 TestEnumValue1 displayName "Enum Value 1" <"Test enum value 1">
                 TestEnumValue2 <"Test enum value 2">
        '''.generateCSharp

        val enums = c_sharp.get('Enums.cs').toString
        println("enums ===\n" + enums)

        assertTrue(containsFileComment(enums))
        assertTrue(containsNamespace(enums, "Org.Isda.Cdm"))

        assertTrue(enums.contains('''
            «""»
                /// <summary>
                /// Test enum description.
                /// </summary>
                public enum TestEnum
                {
                    /// <summary>
                    /// Test enum value 1
                    /// </summary>
                    TestEnumValue1,
                    
                    /// <summary>
                    /// Test enum value 2
                    /// </summary>
                    TestEnumValue2
                }
                
                public static partial class Extension
                {
                    public static string GetDisplayName(this TestEnum value)
                    {
                        return value switch
                        {
                            TestEnum.TestEnumValue1 => "Enum Value 1",
                            _ => nameof(value)
                        };
                    }
                }
        '''))
    }

    @Test
    def void shouldGenerateEnumWithSynonyms() {
        val c_sharp = '''
        synonym source A
        synonym source B
        synonym source C
        synonym source D
        
        enum SynonymEnum:
            [synonym A, B, C value "SynonymTestEnum"]
            EnumValue1
                [synonym A, B, C value "Value1"]
                [synonym D value "Enum Value 1"]
            EnumValue2
                [synonym A, B, C value "Value2"]
            EnumValue3
                [synonym A, B, C value "Value3"]
                [synonym D value "Enum Value 3"]
        '''.generateCSharp

        val enums = c_sharp.get('Enums.cs').toString
        println("enums ===\n" + enums)

        assertTrue(containsFileComment(enums))
        assertTrue(enums.contains("using Rosetta.Lib.Attributes;"))
        assertTrue(containsNamespace(enums, "Org.Isda.Cdm"))

        assertTrue(enums.contains('''
            «""»
«««                [RosettaSynonym(Value = "SynonymTestEnum", Source = "A")]
«««                [RosettaSynonym(Value = "SynonymTestEnum", Source = "B")]
«««                [RosettaSynonym(Value = "SynonymTestEnum", Source = "C")]
                public enum SynonymEnum
                {
                    [RosettaSynonym(Value = "Value1", Source = "A")]
                    [RosettaSynonym(Value = "Value1", Source = "B")]
                    [RosettaSynonym(Value = "Value1", Source = "C")]
                    [RosettaSynonym(Value = "Enum Value 1", Source = "D")]
                    EnumValue1,
                    
                    [RosettaSynonym(Value = "Value2", Source = "A")]
                    [RosettaSynonym(Value = "Value2", Source = "B")]
                    [RosettaSynonym(Value = "Value2", Source = "C")]
                    EnumValue2,
                    
                    [RosettaSynonym(Value = "Value3", Source = "A")]
                    [RosettaSynonym(Value = "Value3", Source = "B")]
                    [RosettaSynonym(Value = "Value3", Source = "C")]
                    [RosettaSynonym(Value = "Enum Value 3", Source = "D")]
                    EnumValue3
                }
        '''))
    }

    @Test
    @Disabled
    def void shouldGenerateUppercaseUnderscoreFormattedEnumNames() {
        val c_sharp = '''
            enum TestEnum:
                 ISDA1993Commodity
                 ISDA1998FX
«««                 iTraxxEuropeDealer
«««                 StandardLCDS
«««                 _1_1
«««                 _30E_360_ISDA
«««                 AED-EBOR-Reuters
«««                 DJ.iTraxx.Europe
«««                 novation
«««                 Currency1PerCurrency2
        '''.generateCSharp

        val enums = c_sharp.get('Enums.cs').toString
        println("enums ===\n" + enums)
                
        assertTrue(enums.contains("Isda1993Commodity"))
        /*assertTrue(enums.contains("ITraxxEuropeDealer"))
        assertTrue(enums.contains("StandardLCDS"))
        assertTrue(enums.contains("_1_1"))
        assertTrue(enums.contains("_30E_360_ISDA"))
        assertTrue(enums.contains('ACT_365L'))
        assertTrue(enums.contains("AedEborReuters"))
        assertTrue(enums.contains("DJ.CDX.NA"))
        assertTrue(enums.contains("Novation"))
        assertTrue(enums.contains("Currency1PerCurrency2")) */
    }


    @Test
    def void shouldGenerateTypes() {
        val c_sharp = '''
            type GtTestType: <"Test type description.">
                gtTestTypeValue1 string (1..1) <"Test string">
                gtTestTypeValue2 string (0..1) <"Test optional string">
                gtTestTypeValue3 string (0..*) <"Test string list">
                gtTestTypeValue4 GtTestType2 (1..1) <"Test TestType2">
                gtTestEnum GtTestEnum (0..1) <"Optional test enum">
            
            type GtTestType2:
                 gtTestType2Value1 number(1..*) <"Test number list">
                 gtTestType2Value2 date(0..1) <"Test optional date">
                 gtTestEnum GtTestEnum (1..1) <"Test enum">
            
            enum GtTestEnum: <"Test enum description.">
                GtTestEnumValue1 <"Test enum value 1">
                GtTestEnumValue2 <"Test enum value 2">
            
        '''.generateCSharp

        val types = c_sharp.get('Types.cs').toString
        
        assertTrue(containsFileComment(types))
        assertTrue(containsNamespace(types, "Org.Isda.Cdm"))
        assertTrue(containsNullable(types))
        assertTrue(containsUsings(types))

        assertTrue(types.contains('''
            «""»
                /// <summary>
                /// Test type description.
                /// </summary>
                public class GtTestType
                {
                    [JsonConstructor]
                    public GtTestType(GtTestEnum? gtTestEnum, string gtTestTypeValue1, string? gtTestTypeValue2, IEnumerable<string> gtTestTypeValue3, GtTestType2 gtTestTypeValue4)
                    {
                        GtTestEnum = gtTestEnum;
                        GtTestTypeValue1 = gtTestTypeValue1;
                        GtTestTypeValue2 = gtTestTypeValue2;
                        GtTestTypeValue3 = gtTestTypeValue3;
                        GtTestTypeValue4 = gtTestTypeValue4;
                    }
                    
                    /// <summary>
                    /// Optional test enum
                    /// </summary>
                    [JsonConverter(typeof(StringEnumConverter))]
                    public GtTestEnum? GtTestEnum { get; }
                    
                    /// <summary>
                    /// Test string
                    /// </summary>
                    public string GtTestTypeValue1 { get; }
                    
                    /// <summary>
                    /// Test optional string
                    /// </summary>
                    public string? GtTestTypeValue2 { get; }
                    
                    /// <summary>
                    /// Test string list
                    /// </summary>
                    public IEnumerable<string> GtTestTypeValue3 { get; }
                    
                    /// <summary>
                    /// Test TestType2
                    /// </summary>
                    public GtTestType2 GtTestTypeValue4 { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                public class GtTestType2
                {
                    [JsonConstructor]
                    public GtTestType2(GtTestEnum gtTestEnum, IEnumerable<decimal> gtTestType2Value1, LocalDate? gtTestType2Value2)
                    {
                        GtTestEnum = gtTestEnum;
                        GtTestType2Value1 = gtTestType2Value1;
                        GtTestType2Value2 = gtTestType2Value2;
                    }
                    
                    /// <summary>
                    /// Test enum
                    /// </summary>
                    [JsonConverter(typeof(StringEnumConverter))]
                    public GtTestEnum GtTestEnum { get; }
                    
                    /// <summary>
                    /// Test number list
                    /// </summary>
                    public IEnumerable<decimal> GtTestType2Value1 { get; }
                    
                    /// <summary>
                    /// Test optional date
                    /// </summary>
                    public LocalDate? GtTestType2Value2 { get; }
                }
        '''))
    }

    @Test
    def void shouldGenerateTypesExtends() {

         val c_sharp = '''
            type GteTestType extends GteTestType2:
                 GteTestTypeValue1 string (1..1) <"Test string">
                 GteTestTypeValue2 int (0..1) <"Test int">
            
            type GteTestType2 extends GteTestType3:
                 GteTestType2Value1 number (0..1) <"Test number">
                 GteTestType2Value2 date (0..*) <"Test date">
            
            type GteTestType3:
                 GteTestType3Value1 string (0..1) <"Test string">
                 GteTestType3Value2 int (1..*) <"Test int">
        '''.generateCSharp

        val interfaces = c_sharp.get('Interfaces.cs').toString

        assertTrue(containsFileComment(interfaces))
        assertTrue(containsNamespace(interfaces, "Org.Isda.Cdm"))
        assertTrue(containsNullable(interfaces))
        assertTrue(containsUsings(interfaces))

        /*assertTrue(interfaces.contains('''
         *        interface ITestType : ITestType2
         *        {
         *          /// <summary>
         *          /// Test number
         *          /// </summary>
         *          string testTypeValue1 { get; }
         *        
         *          /// <summary>
         *          /// Test date
         *          /// </summary>
         *          int? testTypeValue2 { get; }
         }'''))*/
        assertTrue(interfaces.contains('''
            «""»
                interface IGteTestType2 : IGteTestType3
                {
                    /// <summary>
                    /// Test number
                    /// </summary>
                    decimal? GteTestType2Value1 { get; }
                    
                    /// <summary>
                    /// Test date
                    /// </summary>
                    IEnumerable<LocalDate> GteTestType2Value2 { get; }
                }
        '''))

        assertTrue(interfaces.contains('''
            «""»
                interface IGteTestType3
                {
                    /// <summary>
                    /// Test string
                    /// </summary>
                    string? GteTestType3Value1 { get; }
                    
                    /// <summary>
                    /// Test int
                    /// </summary>
                    IEnumerable<int> GteTestType3Value2 { get; }
                }
        '''))

        val types = c_sharp.get('Types.cs').toString
        assertTrue(containsFileComment(types))
        assertTrue(containsNamespace(types, "Org.Isda.Cdm"))
        assertTrue(containsNullable(types))

        assertTrue(types.contains('''
            «""»
                public class GteTestType : IGteTestType2
                {
                    [JsonConstructor]
                    public GteTestType(string gteTestTypeValue1, int? gteTestTypeValue2, decimal? gteTestType2Value1, IEnumerable<LocalDate> gteTestType2Value2, string? gteTestType3Value1, IEnumerable<int> gteTestType3Value2)
                    {
                        GteTestTypeValue1 = gteTestTypeValue1;
                        GteTestTypeValue2 = gteTestTypeValue2;
                        GteTestType2Value1 = gteTestType2Value1;
                        GteTestType2Value2 = gteTestType2Value2;
                        GteTestType3Value1 = gteTestType3Value1;
                        GteTestType3Value2 = gteTestType3Value2;
                    }
                    
                    /// <summary>
                    /// Test string
                    /// </summary>
                    public string GteTestTypeValue1 { get; }
                    
                    /// <summary>
                    /// Test int
                    /// </summary>
                    public int? GteTestTypeValue2 { get; }
                    
                    /// <inheritdoc/>
                    public decimal? GteTestType2Value1 { get; }
                    
                    /// <inheritdoc/>
                    public IEnumerable<LocalDate> GteTestType2Value2 { get; }
                    
                    /// <inheritdoc/>
                    public string? GteTestType3Value1 { get; }
                    
                    /// <inheritdoc/>
                    public IEnumerable<int> GteTestType3Value2 { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                public class GteTestType2 : IGteTestType2, IGteTestType3
                {
                    [JsonConstructor]
                    public GteTestType2(decimal? gteTestType2Value1, IEnumerable<LocalDate> gteTestType2Value2, string? gteTestType3Value1, IEnumerable<int> gteTestType3Value2)
                    {
                        GteTestType2Value1 = gteTestType2Value1;
                        GteTestType2Value2 = gteTestType2Value2;
                        GteTestType3Value1 = gteTestType3Value1;
                        GteTestType3Value2 = gteTestType3Value2;
                    }
                    
                    /// <inheritdoc/>
                    public decimal? GteTestType2Value1 { get; }
                    
                    /// <inheritdoc/>
                    public IEnumerable<LocalDate> GteTestType2Value2 { get; }
                    
                    /// <inheritdoc/>
                    public string? GteTestType3Value1 { get; }
                    
                    /// <inheritdoc/>
                    public IEnumerable<int> GteTestType3Value2 { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                public class GteTestType3 : IGteTestType3
                {
                    [JsonConstructor]
                    public GteTestType3(string? gteTestType3Value1, IEnumerable<int> gteTestType3Value2)
                    {
                        GteTestType3Value1 = gteTestType3Value1;
                        GteTestType3Value2 = gteTestType3Value2;
                    }
                    
                    /// <inheritdoc/>
                    public string? GteTestType3Value1 { get; }
                    
                    /// <inheritdoc/>
                    public IEnumerable<int> GteTestType3Value2 { get; }
                }
        '''))
    }

    @Test
    def void shouldGenerateMetaTypes() {

        val c_sharp = '''
            metaType reference string
            metaType scheme string
            metaType id string
            
            type GmtTestType:
                 [metadata key]
                 gmtTestTypeValue1 GmtTestType2(1..1)
                      [metadata reference]
                      
            enum GmtTestEnum: <"Test enum description.">
                 GmtTestEnumValue1 <"Test enum value 1">
                 GmtTestEnumValue2 <"Test enum value 2">
            
            type GmtTestType2:
                 gmtTestType2Value1 number (1..1)
                      [metadata reference]
                      
                 gmtTestType2Value2 string (1..1)
                      [metadata id]
                      [metadata scheme]
                 
                 gmtTestType2Value3 GmtTestEnum (1..1)
                      [metadata scheme]
        '''.generateCSharp

        val types = c_sharp.values.join('\n').toString

        assertTrue(containsFileComment(types))
        assertTrue(containsNamespace(types, "Org.Isda.Cdm.MetaFields"))
        assertTrue(containsNullable(types))
        assertTrue(containsUsings(types, false))

        assertTrue(types.contains('''
            «""»
                public class MetaFields
                {
                    [JsonConstructor]
                    public MetaFields(string? scheme, string? globalKey, string? externalKey)
                    {
                        Scheme = scheme;
                        GlobalKey = globalKey;
                        ExternalKey = externalKey;
                    }
                    
                    public string? Scheme { get; }
                    
                    public string? GlobalKey { get; }
                    
                    public string? ExternalKey { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                public class FieldWithMetaString
                {
                    [JsonConstructor]
                    public FieldWithMetaString(string? value, MetaFields? meta)
                    {
                        Value = value;
                        Meta = meta;
                    }
                    
                    public string? Value { get; }
                    
                    public MetaFields? Meta { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                public class FieldWithMetaGmtTestEnum
                {
                    [JsonConstructor]
                    public FieldWithMetaGmtTestEnum(GmtTestEnum? value, MetaFields? meta)
                    {
                        Value = value;
                        Meta = meta;
                    }
                    
                    [JsonConverter(typeof(StringEnumConverter))]
                    public GmtTestEnum? Value { get; }
                    
                    public MetaFields? Meta { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                public class ReferenceWithMetaGmtTestType2
                {
                    [JsonConstructor]
                    public ReferenceWithMetaGmtTestType2(GmtTestType2? value, string? globalReference, string? externalReference)
                    {
                        Value = value;
                        GlobalReference = globalReference;
                        ExternalReference = externalReference;
                    }
                    
                    public GmtTestType2? Value { get; }
                    
                    public string? GlobalReference { get; }
                    
                    public string? ExternalReference { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                public class BasicReferenceWithMetaDecimal
                {
                    [JsonConstructor]
                    public BasicReferenceWithMetaDecimal(decimal? value, string? globalReference, string? externalReference)
                    {
                        Value = value;
                        GlobalReference = globalReference;
                        ExternalReference = externalReference;
                    }
                    
                    public decimal? Value { get; }
                    
                    public string? GlobalReference { get; }
                    
                    public string? ExternalReference { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                public class GmtTestType
                {
                    [JsonConstructor]
                    public GmtTestType(ReferenceWithMetaGmtTestType2 gmtTestTypeValue1, MetaFields? meta)
                    {
                        GmtTestTypeValue1 = gmtTestTypeValue1;
                        Meta = meta;
                    }
                    
                    public ReferenceWithMetaGmtTestType2 GmtTestTypeValue1 { get; }
                    
                    public MetaFields? Meta { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                public class GmtTestType2
                {
                    [JsonConstructor]
                    public GmtTestType2(BasicReferenceWithMetaDecimal gmtTestType2Value1, FieldWithMetaString gmtTestType2Value2, FieldWithMetaGmtTestEnum gmtTestType2Value3)
                    {
                        GmtTestType2Value1 = gmtTestType2Value1;
                        GmtTestType2Value2 = gmtTestType2Value2;
                        GmtTestType2Value3 = gmtTestType2Value3;
                    }
                    
                    public BasicReferenceWithMetaDecimal GmtTestType2Value1 { get; }
                    
                    public FieldWithMetaString GmtTestType2Value2 { get; }
                    
                    public FieldWithMetaGmtTestEnum GmtTestType2Value3 { get; }
                }
        '''))
    }

    @Test
    @Disabled("TODO fix oneOf code generation for attributes that are Lists")
    def void shouldGenerateOneOfCondition() {

        val c_sharp = '''
            type TestType: <"Test type with one-of condition.">
                field1 string (0..1) <"Test string field 1">
                field2 string (0..1) <"Test string field 2">
                field3 number (0..1) <"Test number field 3">
                field4 number (0..*) <"Test number field 4">
                condition: one-of
        '''.generateCSharp

        val types = c_sharp.get('Types.cs').toString

        assertTrue(containsFileComment(types))
        assertTrue(containsNamespace(types, "Org.Isda.Cdm"))
        assertTrue(containsNullable(types))
        assertTrue(containsUsings(types))

        assertTrue(types.contains('''
            «""»
                /// <summary>
                /// Test type with one-of condition.
                /// </summary>
                [OneOf]
                public sealed class TestType
                {
                /// <summary>
                /// Test string field 1
                /// </summary>
                public string? Field1 { get; }
                
                /// <summary>
                /// Test string field 2
                /// </summary>
                public string? Field2 { get; }
                
                /// <summary>
                /// Test number field 3
                /// </summary>
                public decimal? Field3 { get; }
                
                /// <summary>
                /// Test number field 4
                /// </summary>
                public IEnumerable<decimal> Field4 { get; }
                //val numberOfPopulatedFields = List(field1, field2, field3, field4).flatten.length
                //require(numberOfPopulatedFields == 1)
                }
        '''))
    }

    def generateCSharp(CharSequence model) {
        val eResource = model.parseRosettaWithNoErrors.eResource

        generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
    }
}
