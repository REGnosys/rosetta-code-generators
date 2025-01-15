package com.regnosys.rosetta.generator.python

import com.google.inject.Inject
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.junit.jupiter.api.Disabled
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class PythonMetaDataGenerationTest {
    
    @Inject extension ModelHelper
    @Inject PythonCodeGenerator generator;

    
    
    @Test
    @Disabled("Test Meta Types")
        def void shouldGenerateMetaTypes() {
                val python = '''
                    metaType reference string
                    metaType address string
                    metaType scheme string
                    metaType id string

                    type TestType:
                        [metadata key]
                        testTypeValue1 TestType2 (1..1)
                            [metadata reference]
                        testTypeValue2 TestType3 (1..1)

                    enum TestEnum:
                        TestEnumValue1
                        TestEnumValue2

                    type TestType2:
                    	[metadata key]
                        testType2Value1 number (1..1)
                            [metadata reference]
                        testType2Value2 string (1..1)
                            [metadata id]
                            [metadata scheme]
                        testType2Value3 TestEnum (1..1)
                            [metadata scheme]
                        testTypeValue4 TestType4 (1..1)
                            [metadata address]

                    type TestType3:
                        testType3Value1 TestType4 (1..1)
                            [metadata location]

                    type TestType4:
                        testType4Value1 number (1..1)

                    '''.generatePython

                val types = python.values.join('\n').toString
                val expected1 =
                '''
                class ReferenceWithMetaTestType2:
                    value = TestType2()
                    globalReference = None
                    externalReference = None
                    address = Reference()
                '''

                assertTrue(types.contains(expected1))

                val expected2 =
                '''
                class ReferenceWithMetaTestType4:
                    value = TestType4()
                    globalReference = None
                    externalReference = None
                    address = Reference()
                '''
                assertTrue(types.contains(expected2))


                val expected3 =
                '''
                class BasicReferenceWithMetaDecimal:
                    value = None
                    globalReference = None
                    externalReference = None
                    address = Reference()
                '''
                assertTrue(types.contains(expected3))



                val expected4 =
                '''
                class FieldWithMetaStr:
                    value = None
                    meta = MetaFields()
                '''
                assertTrue(types.contains(expected4))

                val expected5 =
                '''
                class FieldWithMetaTestEnum:
                    value = TestEnum
                    meta = MetaFields()
                '''
                assertTrue(types.contains(expected5))


                val expected6 =
                '''
                class MetaFields:
                    scheme = None
                    globalKey = None
                    externalKey = None
                    location = []
                '''
                assertTrue(types.contains(expected6))


                val expected7 =
                '''
                class MetaAndTemplateFields:
                    scheme = None
                    globalKey = None
                    externalKey = None
                    templateGlobalReference = None
                    location = []
                '''
                assertTrue(types.contains(expected7))

                val expected8 =
                '''
                class Key:
                    scope = None
                    value = None
                '''
                assertTrue(types.contains(expected8))

                val expected9 =
                '''
                class Reference:
                    scope = None
                    value = None
                '''
                assertTrue(types.contains(expected9))

                val expected10 =
                '''
                class TestType:
                    meta = MetaFields()
                    testTypeValue1 = ReferenceWithMetaTestType2()
                    testTypeValue2 = TestType3()
                '''
                assertTrue(types.contains(expected10))

                /*val expected11=
                '''
                class TestType2:
                    testType2Value1 = BasicReferenceWithMetaDecimal()
                    testType2Value2 = FieldWithMetaStr()
                    testType2Value3 = FieldWithMetaTestEnum
                    testTypeValue4 = ReferenceWithMetaTestType4()
                '''
                assertTrue(types.contains(expected11))

                val expected12 =
                '''
                class TestType3:
                    testType3Value1 = FieldWithMetaTestType4()
                '''

                assertTrue(types.contains(expected12))*/
            }
            
    @Disabled   
    @Test
    def void func() {
        val python = 
        '''
        func Create_RejectedWorkflowStep: 
            [creation WorkflowStep]
            inputs:
                messageInformation MessageInformation (0..1) <"Contains all information pertaining the messaging header">
                timestamp EventTimestamp (1..*) <"The dateTime and qualifier associated with this event.">
                eventIdentifier Identifier (1..*) <"The identifiers that uniquely identify this lifecycle event.">
                proposedWorkflowStep WorkflowStep (1..1) <"Required previous WorkflowStep that provides lineage to WorkflowStep that precedes it.">
        
            output:
                rejectedWorkflowStep WorkflowStep (1..1) <"Rejected WorkflowStep with lineage to the proposed step that preceded it.">
        
            condition ProposedEventExists: <"The previous proposed step being rejected must exist">
                proposedWorkflowStep -> proposedEvent exists
            
            set rejectedWorkflowStep -> messageInformation: <"Assign the workflowStep action.">
                messageInformation
        
            add rejectedWorkflowStep -> timestamp: <"Assign the dateTime and qualifier associated with this event.">
                timestamp
        
            add rejectedWorkflowStep -> eventIdentifier: <"Assign the identifiers that uniquely identify this lifecycle event.">
                eventIdentifier
        
            set rejectedWorkflowStep -> previousWorkflowStep: <"Set the reference to the previous WorkflowStep to provide lineage">
                proposedWorkflowStep as-key
        
            set rejectedWorkflowStep -> rejected: <"Set the rejected flag to True">
                True
        '''.generatePython
    }  
            
    def generatePython(CharSequence model) {
        val m = model.parseRosettaWithNoErrors
        val resourceSet = m.eResource.resourceSet
        val version = m.version
        
        val result = newHashMap
        result.putAll(generator.beforeAllGenerate(resourceSet, #{m}, version))
        result.putAll(generator.beforeGenerate(m.eResource, m, version))
        result.putAll(generator.generate(m.eResource, m, version))
        result.putAll(generator.afterGenerate(m.eResource, m, version))
        result.putAll(generator.afterAllGenerate(resourceSet, #{m}, version))
        
        result
    }
    
}