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

    @Inject
    extension ParseHelper<RosettaModel>
    @Inject
    Provider<XtextResourceSet> resourceSetProvider;

    @Test
    @Disabled("Test to generate the c_sharp for CDM")
    def void generateCdm() {
        val dirs = newArrayList(
            // ('/Users/hugohills/code/src/github.com/REGnosys/rosetta-cdm/src/main/rosetta'),
            // ('/Users/hugohills/code/src/github.com/REGnosys/rosetta-dsl/com.regnosys.rosetta.lib/src/main/java/model')
            ('rosetta-cdm/src/main/rosetta'),
            ('rosetta-dsl/com.regnosys.rosetta.lib/src/main/java/model')
        );

        val resourceSet = resourceSetProvider.get

        dirs.map[new File(it)].map[listFiles[it.name.endsWith('.rosetta')]].flatMap [
            map[Files.readAllBytes(toPath)].map[new String(it)]
        ].forEach[parse(resourceSet)]

        val rosettaModels = resourceSet.resources.map[contents.filter(RosettaModel)].flatten.toList

        val generatedFiles = generator.afterGenerate(rosettaModels)

        val cdmDir = Files.createDirectories(Paths.get("cdm"))
        generatedFiles.forEach [ fileName, contents |
            Files.write(cdmDir.resolve(fileName), contents.toString.bytes)
        ]
    }

    @Test
    def void shouldGenerateEnums() {
        val c_sharp = '''
            enum TestEnum: <"Test enum description.">
                 TestEnumValue1 <"Test enum value 1">
                 TestEnumValue2 <"Test enum value 2">
        '''.generateCSharp

        val enums = c_sharp.get('Enums.cs').toString
        assertTrue(enums.contains('''
            // This file is auto-generated from the ISDA Common Domain Model, do not edit.
            //
            // Version: test
            //
            namespace Org.Isda.Cdm
            {
                /// <summary>
                /// Test enum description.
                /// </summary>
                public enum TestEnum
                {
                    /// <summary>
                    /// Test enum value 1
                    /// </summary>
                    TEST_ENUM_VALUE_1,
                    
                    /// <summary>
                    /// Test enum value 2
                    /// </summary>
                    TEST_ENUM_VALUE_2
                }
            }
        '''))
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

        assertTrue(types.contains('''
        // This file is auto-generated from the ISDA Common Domain Model, do not edit.
        //
        // Version: test
        //'''))

        assertTrue(types.contains('''
            namespace Org.Isda.Cdm
            {
        '''));

        assertTrue(types.contains('''
            «""»
                /// <summary>
                /// Test type description.
                /// </summary>
                class GtTestType
                {
                    /// <summary>
                    /// Optional test enum
                    /// </summary>
                    GtTestEnum? GtTestEnum { get; }
                    
                    /// <summary>
                    /// Test string
                    /// </summary>
                    string GtTestTypeValue1 { get; }
                    
                    /// <summary>
                    /// Test optional string
                    /// </summary>
                    string? GtTestTypeValue2 { get; }
                    
                    /// <summary>
                    /// Test string list
                    /// </summary>
                    IEnumerable<string> GtTestTypeValue3 { get; }
                    
                    /// <summary>
                    /// Test TestType2
                    /// </summary>
                    GtTestType2 GtTestTypeValue4 { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                class GtTestType2
                {
                    /// <summary>
                    /// Test enum
                    /// </summary>
                    GtTestEnum GtTestEnum { get; }
                    
                    /// <summary>
                    /// Test number list
                    /// </summary>
                    IEnumerable<decimal> GtTestType2Value1 { get; }
                    
                    /// <summary>
                    /// Test optional date
                    /// </summary>
                    NodaTime.LocalDate? GtTestType2Value2 { get; }
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

        val traits = c_sharp.get('Traits.cs').toString

        /*assertTrue(traits.contains('''
         *        interface ITestTypeTrait : ITestType2Trait
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

        assertTrue(traits.contains('''
            «""»
                interface IGteTestType2Trait : IGteTestType3Trait
                {
                    /// <summary>
                    /// Test number
                    /// </summary>
                    decimal? GteTestType2Value1 { get; }
                    
                    /// <summary>
                    /// Test date
                    /// </summary>
                    IEnumerable<NodaTime.LocalDate> GteTestType2Value2 { get; }
                }
        '''))

        assertTrue(traits.contains('''
            «""»
                interface IGteTestType3Trait
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

        assertTrue(types.contains('''
            «""»
                class GteTestType : IGteTestType2Trait
                {
                    /// <summary>
                    /// Test string
                    /// </summary>
                    string GteTestTypeValue1 { get; }
                    
                    /// <summary>
                    /// Test int
                    /// </summary>
                    int? GteTestTypeValue2 { get; }
                    
                    /// <inheritdoc/>
                    decimal? GteTestType2Value1 { get; }
                    
                    /// <inheritdoc/>
                    IEnumerable<NodaTime.LocalDate> GteTestType2Value2 { get; }
                    
                    /// <inheritdoc/>
                    string? GteTestType3Value1 { get; }
                    
                    /// <inheritdoc/>
                    IEnumerable<int> GteTestType3Value2 { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                class GteTestType2 : IGteTestType2Trait, IGteTestType3Trait
                {
                    /// <inheritdoc/>
                    decimal? GteTestType2Value1 { get; }
                    
                    /// <inheritdoc/>
                    IEnumerable<NodaTime.LocalDate> GteTestType2Value2 { get; }
                    
                    /// <inheritdoc/>
                    string? GteTestType3Value1 { get; }
                    
                    /// <inheritdoc/>
                    IEnumerable<int> GteTestType3Value2 { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                class GteTestType3 : IGteTestType3Trait
                {
                    /// <inheritdoc/>
                    string? GteTestType3Value1 { get; }
                    
                    /// <inheritdoc/>
                    IEnumerable<int> GteTestType3Value2 { get; }
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

        assertTrue(types.contains('''
            «""»
                class MetaFields
                {
                    string? Scheme { get; }
                    
                    string? GlobalKey { get; }
                    
                    string? ExternalKey { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                class FieldWithMetaString
                {
                    string? Value { get; }
                    
                    MetaFields? Meta { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                class FieldWithMetaGmtTestEnum
                {
                    GmtTestEnum? Value { get; }
                    
                    MetaFields? Meta { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                class FieldWithMetaString
                {
                    string? Value { get; }
                    
                    MetaFields? Meta { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                class ReferenceWithMetaGmtTestType2
                {
                    GmtTestType2? Value { get; }
                    
                    string? GlobalReference { get; }
                    
                    string? ExternalReference { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                class BasicReferenceWithMetaDecimal
                {
                    decimal? Value { get; }
                    
                    string? GlobalReference { get; }
                    
                    string? ExternalReference { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                class GmtTestType
                {
                    ReferenceWithMetaGmtTestType2 GmtTestTypeValue1 { get; }
                    
                    MetaFields? Meta { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                class GmtTestType2
                {
                    BasicReferenceWithMetaDecimal GmtTestType2Value1 { get; }
                    
                    FieldWithMetaString GmtTestType2Value2 { get; }
                    
                    FieldWithMetaGmtTestEnum GmtTestType2Value3 { get; }
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

        assertTrue(types.contains('''
            // This file is auto-generated from the ISDA Common Domain Model, do not edit.
            //
            // Version: test
            //
            namespace Org.Isda.Cdm
            {
                Using Org.Isda.Cdm.Metafields;
                
                /// <summary>
                /// Test type with one-of condition.
                /// </summary>
                class TestType
                {
                    /// <summary>
                    /// Test string field 1
                    /// </summary>
                    string? Field1 { get; }
                    
                    /// <summary>
                    /// Test string field 2
                    /// </summary>
                    string? Field2 { get; }
                    
                    /// <summary>
                    /// Test number field 3
                    /// </summary>
                    decimal? Field3 { get; }
                    
                    /// <summary>
                    /// Test number field 4
                    /// </summary>
                    IEnumerable<decimal> Field4 { get; }
                    //val numberOfPopulatedFields = List(field1, field2, field3, field4).flatten.length
                    //require(numberOfPopulatedFields == 1)
                }
            }
        '''))
    }

    def generateCSharp(CharSequence model) {
        val eResource = model.parseRosettaWithNoErrors.eResource

        generator.afterGenerate(eResource.contents.filter(RosettaModel).toList)
    }
}
