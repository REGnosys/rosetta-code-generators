package com.regnosys.rosetta.generator.c_sharp

import com.google.inject.Inject
import com.regnosys.rosetta.generator.c_sharp.object.CSharpModelObjectGenerator
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import java.io.File
import java.nio.file.Files
import java.nio.file.Paths
import java.util.List
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Disabled
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*
import com.regnosys.rosetta.generators.test.TestUtil

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class CSharpModelObjectGeneratorTest {

    @Inject
    extension ModelHelper
    
    @Inject
    extension TestUtil

    @Inject
    CSharp8CodeGenerator generator8

    @Inject
    CSharp9CodeGenerator generator9

    protected def boolean containsCdmVersionAttribute(String c_sharp) {
        c_sharp.contains('[assembly: Rosetta.Lib.Attributes.CdmVersion("test")]')
    }

    protected def boolean containsCoreNamespace(String c_sharp) {
        containsNamespace(c_sharp, "Org.Isda.Cdm")
    }

    protected def boolean containsEnumNamespace(String c_sharp) {
        containsNamespace(c_sharp, "Org.Isda.Cdm.Enums")
    }

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
        containsUsings(c_sharp, true, true)
    }

    protected def boolean containsUsings(String c_sharp, boolean includeRosetta, boolean includeMetaFields) {
        c_sharp.contains('''
            «""»
                using System.Collections.Generic;
            
                using Newtonsoft.Json;
                using Newtonsoft.Json.Converters;
            
                using NodaTime;
            
                «IF includeRosetta»
                    using Rosetta.Lib;
                    using Rosetta.Lib.Attributes;
                    using Rosetta.Lib.Meta;
                    using Rosetta.Lib.Validation;

                «ENDIF»
                «IF includeMetaFields»
                    using Org.Isda.Cdm.Meta;
                    using Org.Isda.Cdm.MetaFields;
                    using _MetaFields = Org.Isda.Cdm.MetaFields.MetaFields;
                «ENDIF»
        ''')
    }

    protected def boolean containsUsingNamespace(String c_sharp, String namespace) {
        c_sharp.contains('''using «namespace»;''')
    }

    def void generateCdm(CSharpCodeGenerator generator, String subDirectory, List<RosettaModel> rosettaModels) {
        val generatedFiles = generator.afterGenerate(rosettaModels)

        val dir =  Paths.get("./target/classes/" + subDirectory + "/Cdm")

        generatedFiles.forEach [ fileName, contents | 
            { 
                val filePath = dir.resolve(fileName)
                val parent = filePath.getParent()
                if (!Files.exists(parent)) {
                    val parentDir = new File(parent.toUri)
                    parentDir.mkdirs()
                }
                Files.write(filePath, contents.toString.bytes) 
                
            }
        ]
    }

    @Test
    def void shouldGenerateAssemblyVersion() {
        assertEquals(CSharpModelObjectGenerator.getAssemblyVersion("2.71.7"), "2.71.7");
        assertEquals(CSharpModelObjectGenerator.getAssemblyVersion("0.0.0.master"), "0.0.0");
    }

    @Test
    @Disabled("Test to generate the C# for CDM")
    def void generateCdm() {
        val dirs = #[
            '../../../finos/common-domain-model/rosetta-source/src/main/rosetta',
            '../../rosetta-dsl/rosetta-lang/src/main/resources/model'            
        ]
		
        val rosettaModels = dirs.parseAllRosettaFiles
        
        generateCdm(generator8, "NetStandard.2.1", rosettaModels)
        generateCdm(generator9, "Net.5.0", rosettaModels)
    }
    
    def toFile(String s) {
    	new File(s)
    }

    @Test
    def void shouldGenerateEnums() {
        val c_sharp = '''
            enum TestEnum: <"Test enum description.">
                 TestEnumValue1 displayName "Enum Value 1" <"Test enum value 1">
                 TestEnumValue2 <"Test  enum value 2">
            
            enum Test2:
                Test2Value1
                Test2Value2
        '''.generateCSharp

        val enums = c_sharp.get('Enums.cs').toString
        //println("enums ==>\n" + enums)

        assertTrue(containsFileComment(enums))
        assertTrue(containsEnumNamespace(enums))

        assertTrue(enums.contains('''
            «""»
               /// <summary>
                /// Test enum description.
                /// </summary>
                [CdmName("TestEnum")]
                public enum Test
                {
                    /// <summary>
                    /// Test enum value 1
                    /// </summary>
                    [EnumMember(Value = "Enum Value 1")]
                    TestEnumValue1,
                    
                    /// <summary>
                    /// Test  enum value 2
                    /// </summary>
                    [EnumMember(Value = "TEST_ENUM_VALUE_2")]
                    TestEnumValue2
                }
                
                public static partial class Extension
                {
                    public static string GetDisplayName(this Test value)
                    {
                        return value switch
                        {
                            Test.TestEnumValue1 => "Enum Value 1",
                            _ => nameof(value)
                        };
                    }
                }
        '''))
        
        assertTrue(enums.contains('''
            «""»
                [CdmName("Test2")]
                public enum Test2
                {
                    [EnumMember(Value = "TEST_2_VALUE_1")]
                    Test2Value1,
                    
                    [EnumMember(Value = "TEST_2_VALUE_2")]
                    Test2Value2
                }
        '''))
    }
    
    @Test
    def void shouldGenerateQualifiedEnums() {
        val c_sharp = '''
            enum Test2:
                Test2Value1
                Test2Value2
                
            type TestType:
                test2 Test2 (0..1)
        '''.generateCSharp

        val enums = c_sharp.get('Enums.cs').toString
        val types = c_sharp.get('Types.cs').toString
        //println("enums ==>\n" + enums)
        //println("types ==>\n" + types )

        assertTrue(containsFileComment(enums))
        assertTrue(containsEnumNamespace(enums))

        assertTrue(enums.contains('''
            «""»
                [CdmName("Test2")]
                public enum Test2
                {
                    [EnumMember(Value = "TEST_2_VALUE_1")]
                    Test2Value1,
                    
                    [EnumMember(Value = "TEST_2_VALUE_2")]
                    Test2Value2
                }
        '''))
        
        assertTrue(types.contains('''
           «""»
               public class TestType : AbstractRosettaModelObject<TestType>
               {
                   private static readonly IRosettaMetaData<TestType> metaData = new TestTypeMeta();
                   
                   [JsonConstructor]
                   public TestType(Enums.Test2? test2)
                   {
                       Test2 = test2;
                   }
                   
                   /// <inheritdoc />
                   [JsonIgnore]
                   public override IRosettaMetaData<TestType> MetaData => metaData;
                   
                   [JsonConverter(typeof(StringEnumConverter))]
                   public Enums.Test2? Test2 { get; }
               }'''))
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
        //println(enums)

        assertTrue(containsFileComment(enums))
        assertTrue(enums.contains("using System.Runtime.Serialization"))
        assertTrue(enums.contains("using Rosetta.Lib.Attributes;"))
        assertTrue(containsEnumNamespace(enums))

        assertTrue(enums.contains('''
            «""»
«««                [RosettaSynonym(Value = "SynonymTestEnum", Source = "A")]
«««                [RosettaSynonym(Value = "SynonymTestEnum", Source = "B")]
«««                [RosettaSynonym(Value = "SynonymTestEnum", Source = "C")]
                [CdmName("SynonymEnum")]
                public enum Synonym
                {
                    [RosettaSynonym(Value = "Value1", Source = "A")]
                    [RosettaSynonym(Value = "Value1", Source = "B")]
                    [RosettaSynonym(Value = "Value1", Source = "C")]
                    [RosettaSynonym(Value = "Enum Value 1", Source = "D")]
                    [EnumMember(Value = "ENUM_VALUE_1")]
                    EnumValue1,
                    
                    [RosettaSynonym(Value = "Value2", Source = "A")]
                    [RosettaSynonym(Value = "Value2", Source = "B")]
                    [RosettaSynonym(Value = "Value2", Source = "C")]
                    [EnumMember(Value = "ENUM_VALUE_2")]
                    EnumValue2,
                    
                    [RosettaSynonym(Value = "Value3", Source = "A")]
                    [RosettaSynonym(Value = "Value3", Source = "B")]
                    [RosettaSynonym(Value = "Value3", Source = "C")]
                    [RosettaSynonym(Value = "Enum Value 3", Source = "D")]
                    [EnumMember(Value = "ENUM_VALUE_3")]
                    EnumValue3
                }
        '''))
    }

    @Test
    def void shouldGenerateEnumMemberDisplayName() {
        val c_sharp = '''
            enum TestEnum:
                 ISDA1993Commodity
                 ISDA1998FX
                 iTraxxEuropeDealer
                 StandardLCDS
                 _1_1 displayName "1/1"
                 _30E_360_ISDA displayName "30E/360.ISDA"
                 ACT_365L
                 AED_EBOR_Reuters displayName "AED-EBOR-Reuters"
                 DJ_iTraxx_Europe displayName "DJ.iTraxx.Europe"
                 novation
                 Currency1PerCurrency2
        '''.generateCSharp

        val enums = c_sharp.get('Enums.cs').toString
        //println("enums ===\n" + enums)
                
        assertTrue(containsEnumNamespace(enums))
        assertTrue(enums.contains("public enum Test"))
        assertTrue(enums.contains(" ISDA1993Commodity"))
        assertTrue(enums.contains(" ISDA1998FX"))
        assertTrue(enums.contains('''
        «""»
                [EnumMember(Value = "I_TRAXX_EUROPE_DEALER")]
                ITraxxEuropeDealer'''))
        assertTrue(enums.contains(" StandardLCDS"))
        assertTrue(enums.contains('''
        «""»
                [EnumMember(Value = "1/1")]
                _1_1'''));
        assertTrue(enums.contains('''
        «""»
                [EnumMember(Value = "30E/360.ISDA")]
                _30E_360_ISDA'''))
        assertTrue(enums.contains(' ACT_365L'))
        assertTrue(enums.contains('''
        «""»
                [EnumMember(Value = "AED-EBOR-Reuters")]
                AED_EBOR_Reuters'''));
        assertTrue(enums.contains('''
        «""»
                [EnumMember(Value = "DJ.iTraxx.Europe")]
                DJ_iTraxx_Europe'''));
        assertTrue(enums.contains(''' 
        «""»
                [EnumMember(Value = "NOVATION")]
                Novation'''))
        assertTrue(enums.contains(''' 
        «""»
                [EnumMember(Value = "CURRENCY_1_PER_CURRENCY_2")]
                Currency1PerCurrency2'''))
        
        assertTrue(enums.contains(" public static string GetDisplayName(this Test value)"))
        assertTrue(enums.contains(" Test.AED_EBOR_Reuters => \"AED-EBOR-Reuters\""))
        assertTrue(enums.contains(" Test.DJ_iTraxx_Europe => \"DJ.iTraxx.Europe\""))
    }

    @Test
    def void shouldRenameKeywords() {
        val c_sharp = '''
        type KeyWordType:
            string string(0..1)
            event string(1..1)
            int   int(0..*)
            decimal number(0..1)
        '''.generateCSharp

        val types = c_sharp.get('Types.cs').toString
        //println("keywords: " + types);

        assertTrue(containsFileComment(types))
        assertTrue(containsCdmVersionAttribute(types))
        assertTrue(containsCoreNamespace(types))
        assertTrue(containsNullable(types))
        assertTrue(containsUsings(types))

        assertTrue(types.contains('''
            «""»
                public class KeyWordType : AbstractRosettaModelObject<KeyWordType>
                {
                    private static readonly IRosettaMetaData<KeyWordType> metaData = new KeyWordTypeMeta();
                    
                    [JsonConstructor]
                    public KeyWordType(decimal? decimalValue, string eventValue, IEnumerable<int> intValue, string? stringValue)
                    {
                        Decimal = decimalValue;
                        Event = eventValue;
                        Int = intValue;
                        String = stringValue;
                    }
                    
                    /// <inheritdoc />
                    [JsonIgnore]
                    public override IRosettaMetaData<KeyWordType> MetaData => metaData;
                    
                    public decimal? Decimal { get; }
                    
                    public string Event { get; }
                    
                    public IEnumerable<int> Int { get; }
                    
                    public string? String { get; }
                }
        '''))
    }

    @Test
    def void shouldRenameEnclosedType() {
        val c_sharp = '''
        type EnclosingType:
            EnclosingType string(0..1)
        '''.generateCSharp

        val types = c_sharp.get('Types.cs').toString

        assertTrue(containsFileComment(types))
        assertTrue(containsCdmVersionAttribute(types))
        assertTrue(containsCoreNamespace(types))
        assertTrue(containsNullable(types))
        assertTrue(containsUsings(types))

        assertTrue(types.contains('''
            «""»
                public class EnclosingType : AbstractRosettaModelObject<EnclosingType>
                {
                    private static readonly IRosettaMetaData<EnclosingType> metaData = new EnclosingTypeMeta();
                    
                    [JsonConstructor]
                    public EnclosingType(string? enclosingType)
                    {
                        EnclosingTypeValue = enclosingType;
                    }
                    
                    /// <inheritdoc />
                    [JsonIgnore]
                    public override IRosettaMetaData<EnclosingType> MetaData => metaData;
                    
                    [JsonProperty(PropertyName = "enclosingType")]
                    public string? EnclosingTypeValue { get; }
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
        
        //println("types: " + types);
        
        assertTrue(containsFileComment(types))
        assertTrue(containsCdmVersionAttribute(types))
        assertTrue(containsCoreNamespace(types))
        assertTrue(containsNullable(types))
        assertTrue(containsUsings(types))

        assertEquals('''
	        // This file is auto-generated from the ISDA Common Domain Model, do not edit.
	        //
	        // Version: test
	        //
	        [assembly: Rosetta.Lib.Attributes.CdmVersion("test")]
	        
	        #nullable enable // Allow nullable reference types
	        
	        namespace Org.Isda.Cdm
	        {
	            using System.Collections.Generic;
	        
	            using Newtonsoft.Json;
	            using Newtonsoft.Json.Converters;
	        
	            using NodaTime;
	        
	            using Rosetta.Lib;
	            using Rosetta.Lib.Attributes;
	            using Rosetta.Lib.Meta;
	            using Rosetta.Lib.Validation;
	        
	            using Org.Isda.Cdm.Meta;
	            using Org.Isda.Cdm.MetaFields;
	            using _MetaFields = Org.Isda.Cdm.MetaFields.MetaFields;
	            
	            /// <summary>
	            /// Test type description.
	            /// </summary>
	            public class GtTestType : AbstractRosettaModelObject<GtTestType>
	            {
	                private static readonly IRosettaMetaData<GtTestType> metaData = new GtTestTypeMeta();
	                
	                [JsonConstructor]
	                public GtTestType(Enums.GtTest? gtTestEnum, string gtTestTypeValue1, string? gtTestTypeValue2, IEnumerable<string> gtTestTypeValue3, GtTestType2 gtTestTypeValue4)
	                {
	                    GtTestEnum = gtTestEnum;
	                    GtTestTypeValue1 = gtTestTypeValue1;
	                    GtTestTypeValue2 = gtTestTypeValue2;
	                    GtTestTypeValue3 = gtTestTypeValue3;
	                    GtTestTypeValue4 = gtTestTypeValue4;
	                }
	                
	                /// <inheritdoc />
	                [JsonIgnore]
	                public override IRosettaMetaData<GtTestType> MetaData => metaData;
	                
	                /// <summary>
	                /// Optional test enum
	                /// </summary>
	                [JsonConverter(typeof(StringEnumConverter))]
	                public Enums.GtTest? GtTestEnum { get; }
	                
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
	            
	            public class GtTestType2 : AbstractRosettaModelObject<GtTestType2>
	            {
	                private static readonly IRosettaMetaData<GtTestType2> metaData = new GtTestType2Meta();
	                
	                [JsonConstructor]
	                public GtTestType2(Enums.GtTest gtTestEnum, IEnumerable<decimal> gtTestType2Value1, LocalDate? gtTestType2Value2)
	                {
	                    GtTestEnum = gtTestEnum;
	                    GtTestType2Value1 = gtTestType2Value1;
	                    GtTestType2Value2 = gtTestType2Value2;
	                }
	                
	                /// <inheritdoc />
	                [JsonIgnore]
	                public override IRosettaMetaData<GtTestType2> MetaData => metaData;
	                
	                /// <summary>
	                /// Test enum
	                /// </summary>
	                [JsonConverter(typeof(StringEnumConverter))]
	                public Enums.GtTest GtTestEnum { get; }
	                
	                /// <summary>
	                /// Test number list
	                /// </summary>
	                public IEnumerable<decimal> GtTestType2Value1 { get; }
	                
	                /// <summary>
	                /// Test optional date
	                /// </summary>
	                [JsonConverter(typeof(Rosetta.Lib.LocalDateConverter))]
	                public LocalDate? GtTestType2Value2 { get; }
	            }
	        }
        '''.toString, types)
    }
    
    @Test
    def void shouldGenerateCalculationType() {
        val c_sharp = '''
			type Foo:
			     attr calculation (0..1)
        '''.generateCSharp

        val types = c_sharp.get('Types.cs')
        
        assertEquals('''
	        // This file is auto-generated from the ISDA Common Domain Model, do not edit.
	        //
	        // Version: test
	        //
	        [assembly: Rosetta.Lib.Attributes.CdmVersion("test")]
	        
	        #nullable enable // Allow nullable reference types
	        
	        namespace Org.Isda.Cdm
	        {
	            using System.Collections.Generic;
	        
	            using Newtonsoft.Json;
	            using Newtonsoft.Json.Converters;
	        
	            using NodaTime;
	        
	            using Rosetta.Lib;
	            using Rosetta.Lib.Attributes;
	            using Rosetta.Lib.Meta;
	            using Rosetta.Lib.Validation;
	        
	            using Org.Isda.Cdm.Meta;
	            using Org.Isda.Cdm.MetaFields;
	            using _MetaFields = Org.Isda.Cdm.MetaFields.MetaFields;
	            
	            public class Foo : AbstractRosettaModelObject<Foo>
	            {
	                private static readonly IRosettaMetaData<Foo> metaData = new FooMeta();
	                
	                [JsonConstructor]
	                public Foo(string? attr)
	                {
	                    Attr = attr;
	                }
	                
	                /// <inheritdoc />
	                [JsonIgnore]
	                public override IRosettaMetaData<Foo> MetaData => metaData;
	                
	                public string? Attr { get; }
	            }
	        }
        '''.toString, types.toString)
    }
    
    @Test
    def void shouldGenerateProductAndEventType() {
        val c_sharp = '''
			type Foo:
			     productAttr productType (0..1)
			     eventAttr eventType (0..1)
        '''.generateCSharp

        val types = c_sharp.get('Types.cs')
        
        assertEquals('''
	        // This file is auto-generated from the ISDA Common Domain Model, do not edit.
	        //
	        // Version: test
	        //
	        [assembly: Rosetta.Lib.Attributes.CdmVersion("test")]
	        
	        #nullable enable // Allow nullable reference types
	        
	        namespace Org.Isda.Cdm
	        {
	            using System.Collections.Generic;
	        
	            using Newtonsoft.Json;
	            using Newtonsoft.Json.Converters;
	        
	            using NodaTime;
	        
	            using Rosetta.Lib;
	            using Rosetta.Lib.Attributes;
	            using Rosetta.Lib.Meta;
	            using Rosetta.Lib.Validation;
	        
	            using Org.Isda.Cdm.Meta;
	            using Org.Isda.Cdm.MetaFields;
	            using _MetaFields = Org.Isda.Cdm.MetaFields.MetaFields;
	            
	            public class Foo : AbstractRosettaModelObject<Foo>
	            {
	                private static readonly IRosettaMetaData<Foo> metaData = new FooMeta();
	                
	                [JsonConstructor]
	                public Foo(string? eventAttr, string? productAttr)
	                {
	                    EventAttr = eventAttr;
	                    ProductAttr = productAttr;
	                }
	                
	                /// <inheritdoc />
	                [JsonIgnore]
	                public override IRosettaMetaData<Foo> MetaData => metaData;
	                
	                public string? EventAttr { get; }
	                
	                public string? ProductAttr { get; }
	            }
	        }
        '''.toString, types.toString)
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
        
        //println("interfaces =>" + interfaces)

        assertTrue(containsFileComment(interfaces))
        assertTrue(containsCoreNamespace(interfaces))
        assertTrue(containsNullable(interfaces))
        assertTrue(containsUsings(interfaces, false, true))

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
        //println("typeExtends =" + types)
        assertTrue(containsFileComment(types))
        assertTrue(containsCdmVersionAttribute(types))
        assertTrue(containsCoreNamespace(types))
        assertTrue(containsNullable(types))

        assertTrue(types.contains('''
            «""»
                public class GteTestType : AbstractRosettaModelObject<GteTestType>, IGteTestType2
                {
                    private static readonly IRosettaMetaData<GteTestType> metaData = new GteTestTypeMeta();
                    
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
                    
                    /// <inheritdoc />
                    [JsonIgnore]
                    public override IRosettaMetaData<GteTestType> MetaData => metaData;
                    
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
                    [JsonConverter(typeof(Rosetta.Lib.LocalDateConverter))]
                    public IEnumerable<LocalDate> GteTestType2Value2 { get; }
                    
                    /// <inheritdoc/>
                    public string? GteTestType3Value1 { get; }
                    
                    /// <inheritdoc/>
                    public IEnumerable<int> GteTestType3Value2 { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                public class GteTestType2 : AbstractRosettaModelObject<GteTestType2>, IGteTestType2, IGteTestType3
                {
                    private static readonly IRosettaMetaData<GteTestType2> metaData = new GteTestType2Meta();
                    
                    [JsonConstructor]
                    public GteTestType2(decimal? gteTestType2Value1, IEnumerable<LocalDate> gteTestType2Value2, string? gteTestType3Value1, IEnumerable<int> gteTestType3Value2)
                    {
                        GteTestType2Value1 = gteTestType2Value1;
                        GteTestType2Value2 = gteTestType2Value2;
                        GteTestType3Value1 = gteTestType3Value1;
                        GteTestType3Value2 = gteTestType3Value2;
                    }
                    
                    /// <inheritdoc />
                    [JsonIgnore]
                    public override IRosettaMetaData<GteTestType2> MetaData => metaData;
                    
                    /// <inheritdoc/>
                    public decimal? GteTestType2Value1 { get; }
                    
                    /// <inheritdoc/>
                    [JsonConverter(typeof(Rosetta.Lib.LocalDateConverter))]
                    public IEnumerable<LocalDate> GteTestType2Value2 { get; }
                    
                    /// <inheritdoc/>
                    public string? GteTestType3Value1 { get; }
                    
                    /// <inheritdoc/>
                    public IEnumerable<int> GteTestType3Value2 { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                public class GteTestType3 : AbstractRosettaModelObject<GteTestType3>, IGteTestType3
                {
                    private static readonly IRosettaMetaData<GteTestType3> metaData = new GteTestType3Meta();
                    
                    [JsonConstructor]
                    public GteTestType3(string? gteTestType3Value1, IEnumerable<int> gteTestType3Value2)
                    {
                        GteTestType3Value1 = gteTestType3Value1;
                        GteTestType3Value2 = gteTestType3Value2;
                    }
                    
                    /// <inheritdoc />
                    [JsonIgnore]
                    public override IRosettaMetaData<GteTestType3> MetaData => metaData;
                    
                    /// <inheritdoc/>
                    public string? GteTestType3Value1 { get; }
                    
                    /// <inheritdoc/>
                    public IEnumerable<int> GteTestType3Value2 { get; }
                }
        '''))
    }

    @Test
    @Disabled
    def void shouldGenerateTypesExtendsWithRenamedProperty() {

         val c_sharp = '''
            enum AEnum:
                X
                Y
            
            type A:
                a AEnum (1..1)
            
            type B extends A:
                b int (1..1)
                
                condition RenamedProperty:
                    a <> AEnum->X
            
        '''.generateCSharp

        val interfaces = c_sharp.get('Interfaces.cs').toString
        //println("interfaces =>" + interfaces)
        assertTrue(containsFileComment(interfaces))
        assertTrue(containsCoreNamespace(interfaces))
        assertTrue(containsNullable(interfaces))
        assertTrue(containsUsings(interfaces, false, true))

        assertTrue(interfaces.contains('''
            «""»
                interface IA
                {
                    Enums.A AValue { get; }
                }
        '''))

        val types = c_sharp.get('Types.cs').toString
        //println("typeExtends =" + types)
        assertTrue(containsFileComment(types))
        assertTrue(containsCdmVersionAttribute(types))
        assertTrue(containsCoreNamespace(types))
        assertTrue(containsNullable(types))

        assertTrue(types.contains('''
            «""»
                public class A : AbstractRosettaModelObject<A>, IA
                {
                    private static readonly IRosettaMetaData<A> metaData = new AMeta();
                    
                    [JsonConstructor]
                    public A(Enums.A a)
                    {
                        AValue = a;
                    }
                    
                    /// <inheritdoc />
                    [JsonIgnore]
                    public override IRosettaMetaData<A> MetaData => metaData;
                    
                    [JsonConverter(typeof(StringEnumConverter))]
                    [JsonProperty(PropertyName = "a")]
                    public Enums.A AValue { get; }
                }
        '''))

        assertTrue(types.contains('''
            «""»
                public class B : AbstractRosettaModelObject<B>, IA
                {
                    private static readonly IRosettaMetaData<B> metaData = new BMeta();
                    
                    [JsonConstructor]
                    public B(int b, Enums.A a)
                    {
                        BValue = b;
                        AValue = a;
                    }
                    
                    /// <inheritdoc />
                    [JsonIgnore]
                    public override IRosettaMetaData<B> MetaData => metaData;
                    
                    [JsonProperty(PropertyName = "b")]
                    public int BValue { get; }
                    
                    [JsonConverter(typeof(StringEnumConverter))]
                    [JsonProperty(PropertyName = "a")]
                    public Enums.A AValue { get; }
                }
        '''))
        
        val dataRules = c_sharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(dataRules.contains(''' 
            «""»
                [RosettaDataRule("BRenamedProperty")]
                public class BRenamedProperty : AbstractDataRule<B>
                {
                    protected override string Definition => "a <> AEnum->X";
                    
                    protected override IComparisonResult? RuleIsApplicable(B b)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(B b)
                    {
                        try
                        {
                            return ComparisonResult.FromBoolean(b.AValue != Enums.A.X);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }'''))
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
                 
                 gmtTestType2List3 GmtTestEnum (1..*)
                      [metadata scheme]
                 
                 gmtTestType2Value4 date (1..1)
                      [metadata reference]
                 
                 gmtTestType2List4 date (1..*)
                      [metadata reference]
        '''.generateCSharp

        val metaTypes = c_sharp.values.join('\n').toString

//        println("types => " + metaTypes);

        assertTrue(containsFileComment(metaTypes))
        assertTrue(containsNamespace(metaTypes, "Org.Isda.Cdm.MetaFields"))
       // assertTrue(containsNamespace(metaTypes, "Rosetta.Lib.Meta"))
        assertTrue(containsNullable(metaTypes))
        assertTrue(containsUsings(metaTypes, false, false))

        assertTrue(metaTypes.contains('''
            «""»
                public class MetaFields
                {
                    [JsonConstructor]
                    public MetaFields(string? scheme, string? globalKey, string? externalKey, IEnumerable<Key> location)
                    {
                        Scheme = scheme;
                        GlobalKey = globalKey;
                        ExternalKey = externalKey;
                        Location = location;
                    }
                    
                    public string? Scheme { get; }
                    
                    public string? GlobalKey { get; }
                    
                    public string? ExternalKey { get; }
                    
                    public IEnumerable<Key> Location { get; }
                }
        '''))

        assertTrue(metaTypes.contains('''
            «""»
                public class FieldWithMetaString : IFieldWithMeta<string>
                {
                    [JsonConstructor]
                    public FieldWithMetaString(string value, MetaFields? meta)
                    {
                        Value = value;
                        Meta = meta;
                    }
                    
                    public string Value { get; }
                    
                    public MetaFields? Meta { get; }
                }
        '''))

        assertTrue(metaTypes.contains('''
            «""»
                public class FieldWithMetaGmtTestEnum : IEnumFieldWithMeta<Enums.GmtTest>
                {
                    [JsonConstructor]
                    public FieldWithMetaGmtTestEnum(Enums.GmtTest value, MetaFields? meta)
                    {
                        Value = value;
                        Meta = meta;
                    }
                    
                    [JsonConverter(typeof(StringEnumConverter))]
                    public Enums.GmtTest Value { get; }
                    
                    public MetaFields? Meta { get; }
                }
        '''))

        assertTrue(metaTypes.contains('''
            «""»
                public class ReferenceWithMetaGmtTestType2 : IReferenceWithMeta<GmtTestType2>
                {
                    [JsonConstructor]
                    public ReferenceWithMetaGmtTestType2(GmtTestType2? value, string? globalReference, string? externalReference, Reference? address)
                    {
                        Value = value;
                        GlobalReference = globalReference;
                        ExternalReference = externalReference;
                        Address = address;
                    }
                    
                    public GmtTestType2? Value { get; }
                    
                    public string? GlobalReference { get; }
                    
                    public string? ExternalReference { get; }
                    
                    public Reference? Address { get; }
                }
        '''))

        assertTrue(metaTypes.contains('''
            «""»
                public class BasicReferenceWithMetaDecimal : IReferenceWithMeta<decimal>
                {
                    [JsonConstructor]
                    public BasicReferenceWithMetaDecimal(decimal? value, string? globalReference, string? externalReference, Reference? address)
                    {
                        Value = value;
                        GlobalReference = globalReference;
                        ExternalReference = externalReference;
                        Address = address;
                    }
                    
                    public decimal? Value { get; }
                    
                    public string? GlobalReference { get; }
                    
                    public string? ExternalReference { get; }
                    
                    public Reference? Address { get; }
                }
        '''))

        assertTrue(metaTypes.contains('''
            «""»
                public class BasicReferenceWithMetaLocalDate : IValueReferenceWithMeta<NodaTime.LocalDate>
                {
                    [JsonConstructor]
                    public BasicReferenceWithMetaLocalDate(NodaTime.LocalDate? value, string? globalReference, string? externalReference, Reference? address)
                    {
                        Value = value;
                        GlobalReference = globalReference;
                        ExternalReference = externalReference;
                        Address = address;
                    }
                    
                    [JsonConverter(typeof(Rosetta.Lib.LocalDateConverter))]
                    public NodaTime.LocalDate? Value { get; }
                    
                    public string? GlobalReference { get; }
                    
                    public string? ExternalReference { get; }
                    
                    public Reference? Address { get; }
                }
        '''))

        assertTrue(metaTypes.contains('''
            «""»
                public class GmtTestType : AbstractRosettaModelObject<GmtTestType>
                {
                    private static readonly IRosettaMetaData<GmtTestType> metaData = new GmtTestTypeMeta();
                    
                    [JsonConstructor]
                    public GmtTestType(ReferenceWithMetaGmtTestType2 gmtTestTypeValue1, _MetaFields? meta)
                    {
                        GmtTestTypeValue1 = gmtTestTypeValue1;
                        Meta = meta;
                    }
                    
                    /// <inheritdoc />
                    [JsonIgnore]
                    public override IRosettaMetaData<GmtTestType> MetaData => metaData;
                    
                    public ReferenceWithMetaGmtTestType2 GmtTestTypeValue1 { get; }
                    
                    public _MetaFields? Meta { get; }
                }
        '''))

        assertTrue(metaTypes.contains('''
            «""»
                public class GmtTestType2 : AbstractRosettaModelObject<GmtTestType2>
                {
                    private static readonly IRosettaMetaData<GmtTestType2> metaData = new GmtTestType2Meta();
                    
                    [JsonConstructor]
                    public GmtTestType2(IEnumerable<FieldWithMetaGmtTestEnum> gmtTestType2List3, IEnumerable<BasicReferenceWithMetaLocalDate> gmtTestType2List4, BasicReferenceWithMetaDecimal gmtTestType2Value1, FieldWithMetaString gmtTestType2Value2, FieldWithMetaGmtTestEnum gmtTestType2Value3, BasicReferenceWithMetaLocalDate gmtTestType2Value4)
                    {
                        GmtTestType2List3 = gmtTestType2List3;
                        GmtTestType2List4 = gmtTestType2List4;
                        GmtTestType2Value1 = gmtTestType2Value1;
                        GmtTestType2Value2 = gmtTestType2Value2;
                        GmtTestType2Value3 = gmtTestType2Value3;
                        GmtTestType2Value4 = gmtTestType2Value4;
                    }
                    
                    /// <inheritdoc />
                    [JsonIgnore]
                    public override IRosettaMetaData<GmtTestType2> MetaData => metaData;
                    
                    public IEnumerable<FieldWithMetaGmtTestEnum> GmtTestType2List3 { get; }
                    
                    public IEnumerable<BasicReferenceWithMetaLocalDate> GmtTestType2List4 { get; }
                    
                    public BasicReferenceWithMetaDecimal GmtTestType2Value1 { get; }
                    
                    public FieldWithMetaString GmtTestType2Value2 { get; }
                    
                    public FieldWithMetaGmtTestEnum GmtTestType2Value3 { get; }
                    
                    public BasicReferenceWithMetaLocalDate GmtTestType2Value4 { get; }
                }
        '''))
    }
    
    @Test
    @Disabled
    def void shouldGenerateMetaTypesCondition() {

        val c_sharp = '''
            metaType scheme string
            
            enum GmtTestEnum:
                 GmtTestEnumValue1
                 GmtTestEnumValue2
            
            type GmtTestType:
                 gmtTestType GmtTestEnum (1..*)
                      [metadata scheme]
                 
                 condition EnumMetaCollectionContains:
                 	gmtTestType contains GmtTestEnum -> GmtTestEnumValue1
        '''.generateCSharp

        val metaTypes = c_sharp.values.join('\n').toString

        //println("types => " + metaTypes);

        assertTrue(containsFileComment(metaTypes))
        assertTrue(containsNamespace(metaTypes, "Org.Isda.Cdm.MetaFields"))
       // assertTrue(containsNamespace(metaTypes, "Rosetta.Lib.Meta"))
        assertTrue(containsNullable(metaTypes))
        assertTrue(containsUsings(metaTypes, false, false))
        
        assertTrue(metaTypes.contains('''
            «""»
                public class GmtTestType : AbstractRosettaModelObject<GmtTestType>
                {
                    private static readonly IRosettaMetaData<GmtTestType> metaData = new GmtTestTypeMeta();
                    
                    [JsonConstructor]
                    public GmtTestType(IEnumerable<FieldWithMetaGmtTestEnum> gmtTestType)
                    {
                        GmtTestTypeValue = gmtTestType;
                    }
                    
                    /// <inheritdoc />
                    [JsonIgnore]
                    public override IRosettaMetaData<GmtTestType> MetaData => metaData;
                    
                    [JsonProperty(PropertyName = "gmtTestType")]
                    public IEnumerable<FieldWithMetaGmtTestEnum> GmtTestTypeValue { get; }
                }
        '''))
        
        // TODO: this is wrong, it should be:
        // return gmtTestType.GmtTestTypeValue.Select(x => x.Value).Includes(Enums.GmtTest.GmtTestEnumValue1);
        assertTrue(metaTypes.contains('''
			«""»
			    public class GmtTestTypeEnumMetaCollectionContains : AbstractDataRule<GmtTestType>
			    {
			        protected override string Definition => "gmtTestType contains GmtTestEnum -> GmtTestEnumValue1";
			        
			        protected override IComparisonResult? RuleIsApplicable(GmtTestType gmtTestType)
			        {
			            return ComparisonResult.Success();
			        }
			        
			        protected override IComparisonResult? EvaluateThenExpression(GmtTestType gmtTestType)
			        {
			            try
			            {
			                return gmtTestType.GmtTestTypeValue.Includes(Enums.GmtTest.GmtTestEnumValue1);
			            }
			            catch (Exception ex)
			            {
			                return ComparisonResult.Failure(ex.Message);
			            }
			        }
			    }'''))
    }
    
    private def void hasDataRuleUsings(String dataRules) {
        assertTrue(containsUsingNamespace(dataRules, "Org.Isda.Cdm"))
        assertTrue(containsUsingNamespace(dataRules, "System.Linq"))
        assertTrue(containsUsingNamespace(dataRules, "Rosetta.Lib.Attributes"))
        assertTrue(containsUsingNamespace(dataRules, "Rosetta.Lib.Validation"))
        
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleForOptionalExists() {
        val rosettaCode = '''
            type A:
            
            optionalInt int (0..1 )
            
            condition Rule: 
                if optionalInt exists
                then optionalInt > 10'''
        
        val dataRules = rosettaCode.generateCSharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        hasDataRuleUsings(dataRules)
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("ARule")]
                public class ARule : AbstractDataRule<A>
                {
                    protected override string Definition => "if optionalInt exists then optionalInt > 10";
                    
                    protected override IComparisonResult? RuleIsApplicable(A a)
                    {
                        try
                        {
                            return Exists(a.OptionalInt);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(A a)
                    {
                        try
                        {
                            return ComparisonResult.FromBoolean(a.OptionalInt > 10);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }''')
        )
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleForNonOptional() {
        val rosettaCode = '''
            type B:
            
            intValue int (1..1 )
            
            condition Rule: 
                intValue < 100'''
        
        val dataRules = rosettaCode.generateCSharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        hasDataRuleUsings(dataRules)
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("BRule")]
                public class BRule : AbstractDataRule<B>
                {
                    protected override string Definition => "intValue < 100";
                    
                    protected override IComparisonResult? RuleIsApplicable(B b)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(B b)
                    {
                        try
                        {
                            return ComparisonResult.FromBoolean(b.IntValue < 100);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }''')
        )    
    }
    
    @Test
    @Disabled
    def void shouldGenerateDataRuleForEquality() {
        val rosettaCode = '''
            type C:
            
            optionalBoolean boolean (0..1 )
            
            condition Rule: 
                if optionalBoolean exists
                then optionalBoolean = False'''
        
        val dataRules = rosettaCode.generateCSharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        hasDataRuleUsings(dataRules)
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("CRule")]
                public class CRule : AbstractDataRule<C>
                {
                    protected override string Definition => "if optionalBoolean exists then optionalBoolean = False";
                    
                    protected override IComparisonResult? RuleIsApplicable(C c)
                    {
                        try
                        {
                            return Exists(c.OptionalBoolean);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(C c)
                    {
                        try
                        {
                            return ComparisonResult.FromBoolean(c.OptionalBoolean == false);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }''')
        )
    }
    
    @Test
    @Disabled
    def void shouldGenerateDataRuleForCollection() {
        val rosettaCode = '''
            type D:
                isApplicable boolean (1..1)
            
            
            type F:
                booleanValue boolean (1..1)
                otherBooleanValue boolean (1..1)
                collection D (0..2)
            
                condition Rule1:
                    if booleanValue = True then
                    collection->isApplicable = False
                
                condition Rule2:
                    if booleanValue = False and collection->isApplicable = False
                    then otherBooleanValue = False
            '''
        
        val csharp = rosettaCode.generateCSharp
        //println("types: " + csharp.get("Types.cs").toString)
        val dataRules = csharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)

        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("FRule1")]
                public class FRule1 : AbstractDataRule<F>
                {
                    protected override string Definition => "if booleanValue = True then collection->isApplicable = False";
                    
                    protected override IComparisonResult? RuleIsApplicable(F f)
                    {
                        try
                        {
                            return ComparisonResult.FromBoolean(f.BooleanValue == true);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(F f)
                    {
                        try
                        {
                            return f.Collection.Select(d => d.IsApplicable).IsEqual(false);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))
        
        assertTrue(dataRules.contains('''
            «""»
               [RosettaDataRule("FRule2")]
                public class FRule2 : AbstractDataRule<F>
                {
                    protected override string Definition => "if booleanValue = False and collection->isApplicable = False then otherBooleanValue = False";
                    
                    protected override IComparisonResult? RuleIsApplicable(F f)
                    {
                        try
                        {
                            return And(ComparisonResult.FromBoolean(f.BooleanValue == false),
                                f.Collection.Select(d => d.IsApplicable).IsEqual(false));
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(F f)
                    {
                        try
                        {
                            return ComparisonResult.FromBoolean(f.OtherBooleanValue == false);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))        
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleForSubCollection() {
        val rosettaCode ='''
        
        type B:
            a int (0..1)
            
        type C:
            b B (1..*)

        type D:
            c C (1..1)
            
            condition SubCollection:
                c->b->a exists'''
    
        val csharp = rosettaCode.generateCSharp
        //println("types: " + csharp.get("Types.cs").toString)
        val dataRules = csharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("DSubCollection")]
                public class DSubCollection : AbstractDataRule<D>
                {
                    protected override string Definition => "c->b->a exists";
                    
                    protected override IComparisonResult? RuleIsApplicable(D d)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(D d)
                    {
                        try
                        {
                            return Exists(d.C.B
                                .Select(b => b.A));
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleForSubCollectionOfOptional() {
        val rosettaCode ='''
        
        type A:
            x int (1..1)

        type B:
            a A (0..1)
            
        type C:
            b B (1..*)

            
            condition OptionalSubCollection:
                b->a->x exists'''
    
        val csharp = rosettaCode.generateCSharp
        //println("types: " + csharp.get("Types.cs").toString)
        val dataRules = csharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("COptionalSubCollection")]
                public class COptionalSubCollection : AbstractDataRule<C>
                {
                    protected override string Definition => "b->a->x exists";
                    
                    protected override IComparisonResult? RuleIsApplicable(C c)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(C c)
                    {
                        try
                        {
                            return Exists(c.B.Select(b => b.A)
                                .Select(a => a?.X));
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleForMetaCollection() {
        val rosettaCode ='''
        
        type A:
            x int (1..1)

        type B:
            a A (0..*)
            [metadata reference]

        type C:
            b B (1..1)

            condition MetaCollection:
                b->a->x exists'''
    
        val csharp = rosettaCode.generateCSharp
        //println("types: " + csharp.get("Types.cs").toString)
        val dataRules = csharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("CMetaCollection")]
                public class CMetaCollection : AbstractDataRule<C>
                {
                    protected override string Definition => "b->a->x exists";
                    
                    protected override IComparisonResult? RuleIsApplicable(C c)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(C c)
                    {
                        try
                        {
                            return Exists(c.B.A
                                .Select(a => a.Value?.X));
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))
    }
    
    @Test
    @Disabled
    def void shouldGenerateDataRuleForMetaLeafCollection() {
        val rosettaCode ='''
        
        type A:
            x int (1..1)

        type B:
            a A (0..*)
            [metadata location]

        type C:
            b B (1..1)

            condition MetaLeafCollection:
                D(b->a) = True
        
        func D:
        	inputs:
        		aList A (0..*)
        	output:
        		result boolean (1..1)
        
        '''
    
        val csharp = rosettaCode.generateCSharp
        //println("types: " + csharp.get("Types.cs").toString)
        val dataRules = csharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("CMetaLeafCollection")]
                public class CMetaLeafCollection : AbstractDataRule<C>
                {
                    protected override string Definition => "D(b->a) = True";
                    
                    protected override IComparisonResult? RuleIsApplicable(C c)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(C c)
                    {
                        try
                        {
                            return ComparisonResult.FromBoolean(D.Evaluate(c.B.A.EmptyIfNull().Select(a => a.Value)) == true);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
    	'''))
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleForCollectionOfCollections() {
        val rosettaCode ='''
        
        type A:
            x int (0..1)

        type B:
            a A (1..*)
            [metadata reference]

        type C:
            b B (1..*)

            condition NestedCollections:
                b->a->x exists'''
    
        val cSharp = rosettaCode.generateCSharp
        //println("types: " + cSharp.get('Types.cs').toString)
        //println("meta: " + cSharp.get('MetaTypes.cs').toString)
        //println("metaFields: " + cSharp.get('MetaFieldTypes.cs').toString)

        val dataRules = cSharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("CNestedCollections")]
                public class CNestedCollections : AbstractDataRule<C>
                {
                    protected override string Definition => "b->a->x exists";
                    
                    protected override IComparisonResult? RuleIsApplicable(C c)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(C c)
                    {
                        try
                        {
                            return Exists(c.B.SelectMany(b => (b.A).EmptyIfNull())
                                .Select(a => a.Value?.X));
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleForMetaReferenceTypes() {
        val rosettaCode ='''
        metaType reference string

        type A:
        
            inner A (0..1)
                [metadata reference]

            condition MetaCollection:
                A->inner -> reference exists'''
    
        val cSharp = rosettaCode.generateCSharp
        //println("types: " + cSharp.get('Types.cs').toString)
        
        val dataRules = cSharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("AMetaCollection")]
                public class AMetaCollection : AbstractDataRule<A>
                {
                    protected override string Definition => "A->inner -> reference exists";
                    
                    protected override IComparisonResult? RuleIsApplicable(A a)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(A a)
                    {
                        try
                        {
                            return Exists(a.Inner?.GlobalReference);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleForMetaTypes() {
        val rosettaCode ='''
        metaType reference string

        type A:
            x int (0..1)
        
        type B:
        
            a A (1..1)
                [metadata id]

            condition MetaCollection:
                a-> x exists'''
    
        val cSharp = rosettaCode.generateCSharp
        //println("types: " + cSharp.get('Types.cs').toString)
        
        val dataRules = cSharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("BMetaCollection")]
                public class BMetaCollection : AbstractDataRule<B>
                {
                    protected override string Definition => "a-> x exists";
                    
                    protected override IComparisonResult? RuleIsApplicable(B b)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(B b)
                    {
                        try
                        {
                            return Exists(b.A.Value.X);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
        '''))
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleForResultCount() {
        val rosettaCode ='''
        
        type A:
            b int (1..*)

        type B:
            a A (1..1)
            
            condition ResultCount:
                a->b count >= 2'''
    
        val dataRules = rosettaCode.generateCSharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("BResultCount")]
                public class BResultCount : AbstractDataRule<B>
                {
                    protected override string Definition => "a->b count >= 2";
                    
                    protected override IComparisonResult? RuleIsApplicable(B b)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(B b)
                    {
                        try
                        {
                            return ComparisonResult.FromBoolean(b.A.B.Count() >= 2);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleForAndIf() {
        val rosettaCode ='''
        enum CounterpartyEnum:
            Party1
            Party2
        
        type BuyerSeller:
            buyer CounterpartyEnum (0..1) 
            seller CounterpartyEnum (0..1)
            
            condition BuyerAndSellerExists: <"Either both or neither">
                if buyer exists then seller exists and if seller exists then buyer exists

            condition CheckEnumValue:
                if buyer exists then buyer = CounterpartyEnum -> Party1'''

        val dataRules = rosettaCode.generateCSharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                /// <summary>
                /// Either both or neither
                /// </summary>
                [RosettaDataRule("BuyerSellerBuyerAndSellerExists")]
                public class BuyerSellerBuyerAndSellerExists : AbstractDataRule<BuyerSeller>
                {
                    protected override string Definition => "if buyer exists then seller exists and if seller exists then buyer exists";
                    
                    protected override IComparisonResult? RuleIsApplicable(BuyerSeller buyerSeller)
                    {
                        try
                        {
                            return Exists(buyerSeller.Buyer);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(BuyerSeller buyerSeller)
                    {
                        try
                        {
                            return And(Exists(buyerSeller.Seller),
                                IfThen(Exists(buyerSeller.Seller),
                                    Exists(buyerSeller.Buyer)));
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
            
        '''))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("BuyerSellerCheckEnumValue")]
                public class BuyerSellerCheckEnumValue : AbstractDataRule<BuyerSeller>
                {
                    protected override string Definition => "if buyer exists then buyer = CounterpartyEnum -> Party1";
                    
                    protected override IComparisonResult? RuleIsApplicable(BuyerSeller buyerSeller)
                    {
                        try
                        {
                            return Exists(buyerSeller.Buyer);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(BuyerSeller buyerSeller)
                    {
                        try
                        {
                            return ComparisonResult.FromBoolean(buyerSeller.Buyer == Enums.Counterparty.Party1);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleForSum() {
        val rosettaCode ='''
        func Sum:
            inputs: x number (0..*)
            output: sum number (1..1)

        type A:
            amount number (1..1)
            
        type B:
            a A (1..*)
            
        type C:
            b1 B (1..1)
            b2 B (1..1) 

            condition Sum:
                 Sum(b1->a->amount) = b2->a->amount'''

        val dataRules = rosettaCode.generateCSharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("CSum")]
                public class CSum : AbstractDataRule<C>
                {
                    protected override string Definition => "Sum(b1->a->amount) = b2->a->amount";
                    
                    protected override IComparisonResult? RuleIsApplicable(C c)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(C c)
                    {
                        try
                        {
                            return Sum.Evaluate(c.B1.A
                                .Select(a => a.Amount)).IsEqual(c.B2.A
                                .Select(a => a.Amount));
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleChainedCalls() {
        val rosettaCode ='''
        type A:
            idea int (1..1)
        
        type B:
            a A (1..1) 
            
            condition ChainRule:
                a->idea <> 9'''
        val dataRules = rosettaCode.generateCSharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("BChainRule")]
                public class BChainRule : AbstractDataRule<B>
                {
                    protected override string Definition => "a->idea <> 9";
                    
                    protected override IComparisonResult? RuleIsApplicable(B b)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(B b)
                    {
                        try
                        {
                            return ComparisonResult.FromBoolean(b.A.Idea != 9);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleBooleanExists() {
        val rosettaCode ='''
        type A:
            b int (0..1)
            c int (1..1)
            d string (0..1)
            f string (1..1)
        
            condition OrExists:
                (b exists or c exists) or (d is absent and f is absent)'''
        val dataRules = rosettaCode.generateCSharp.get('DataRules.cs').toString
//        println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("AOrExists")]
                public class AOrExists : AbstractDataRule<A>
                {
                    protected override string Definition => "(b exists or c exists) or (d is absent and f is absent)";
                    
                    protected override IComparisonResult? RuleIsApplicable(A a)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(A a)
                    {
                        try
                        {
                            return Or(Or(Exists(a.B),
                                ComparisonResult.Success()),
                                And(NotExists(a.D),
                                    ComparisonResult.Failure("Field is not optional and must exist")));
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleWithEnumRenaming() {
        val rosettaCode ='''
        enum AEnum:
            X
            Y
        
        type A:
            a AEnum (0..1)

            condition NotNull:
                a exists'''
        val dataRules = rosettaCode.generateCSharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("ANotNull")]
                public class ANotNull : AbstractDataRule<A>
                {
                    protected override string Definition => "a exists";
                    
                    protected override IComparisonResult? RuleIsApplicable(A a)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(A a)
                    {
                        try
                        {
                            return Exists(a.AValue);
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))
    }

    @Test
    @Disabled
    def void shouldGenerateDataRuleForOnlyExists() {
        val rosettaCode ='''
	        type A:
	            a int (0..1)
	            [metadata scheme]
	            b string (0..1)

	        type B:
	            a A (0..1)
	            
	            condition OnlyExists:
	                a->a only exists'''
        val dataRules = rosettaCode.generateCSharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("BOnlyExists")]
                public class BOnlyExists : AbstractDataRule<B>
                {
                    protected override string Definition => "a->a only exists";
                    
                    protected override IComparisonResult? RuleIsApplicable(B b)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(B b)
                    {
                        try
                        {
                            return OnlyExists(b.A, new HashSet<string> {"AValue"});
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))
    }
    
    @Test
    @Disabled
    def void shouldGenerateDataRuleForOnlyExistsMultiplePaths() {
        val rosettaCode ='''
	        type A:
	            a int (0..1)
	            [metadata scheme]
	            b string (0..1)

	        type B:
	            a A (0..1)
	            
	            condition OnlyExists:
	                (a->a, a->b) only exists'''
        val dataRules = rosettaCode.generateCSharp.get('DataRules.cs').toString
        //println("dataRules: " + dataRules)
        assertTrue(containsFileComment(dataRules))
        assertTrue(containsNamespace(dataRules, "Org.Isda.Cdm.Validation.DataRule"))
        assertTrue(dataRules.contains('''
            «""»
                [RosettaDataRule("BOnlyExists")]
                public class BOnlyExists : AbstractDataRule<B>
                {
                    protected override string Definition => "(a->a, a->b) only exists";
                    
                    protected override IComparisonResult? RuleIsApplicable(B b)
                    {
                        return ComparisonResult.Success();
                    }
                    
                    protected override IComparisonResult? EvaluateThenExpression(B b)
                    {
                        try
                        {
                            return OnlyExists(b.A, new HashSet<string> {"AValue", "B"});
                        }
                        catch (Exception ex)
                        {
                            return ComparisonResult.Failure(ex.Message);
                        }
                    }
                }
        '''))
    }
    
    def generateCSharp(CharSequence model) {
        val eResource = model.parseRosettaWithNoErrors.eResource

        generator8.afterGenerate(eResource.contents.filter(RosettaModel).toList)
    }
}
