package com.regnosys.rosetta.generator.c_sharp.object

import com.regnosys.rosetta.generator.object.ExpandedAttribute
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.List
import org.eclipse.xtend2.lib.StringConcatenationClient

import static com.regnosys.rosetta.generator.c_sharp.util.CSharpModelGeneratorUtil.*

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*

class CSharpValidatorsGenerator {
    
    def generateValidators(List<Data> rosettaClasses, String version) {
        '''
        «fileComment(version)»
        
        #nullable enable // Allow nullable reference types
        
        namespace Org.Isda.Cdm.Validation.DataRule
        {
            using System.Collections.Generic;
            using System.Linq;
            
            using Org.Isda.Cdm;
            
            using Rosetta.Lib.Functions;
            using Rosetta.Lib.Validation;
            
            «FOR rosettaClass : rosettaClasses»
                «rosettaClass.validatorClassBody»
                «rosettaClass.onlyExistsValidatorClassBody»
            «ENDFOR»
        }'''
    }

    private def StringConcatenationClient validatorClassBody(Data data) {
        val attributes = data.getExpandedAttributes(false)
        '''
        public class «data.name»Validator : AbstractValidator<«data.name»>
        {
        
            public «data.name»Validator() {}
        
            protected override IEnumerable<IComparisonResult> GetResults(«data.name» obj)
            {
                «FOR attr : attributes»
                    «checkCardinality(data.name, attr)»
                «ENDFOR»
                yield break;
            }
        }
        
    '''
    }

/*
    static def onlyExistsValidatorName(RosettaType c) {
        return c.name + 'OnlyExistsValidator'
    }
*/
    private def StringConcatenationClient onlyExistsValidatorClassBody(Data data) '''
        «val name = data.name»
        public class «data.name»OnlyExistsValidator : AbstractOnlyExistsValidator<«name»> {
        
            protected override IDictionary<string, bool> GetFields(«name» obj)
            {
                return new Dictionary<string, bool>()
                {
                    «FOR attr : data.attributes SEPARATOR ","»
                        «val property = attr.getPropertyName(name)»
                        { "«property»", IsSet(obj.«property»!) }
                    «ENDFOR»
                };
            }
        }
        
    '''

    def StringConcatenationClient getPropertyName(Attribute attr, String className) { 
        return getPropertyName(attr.name, className)
    }

    def StringConcatenationClient getPropertyName(ExpandedAttribute attr, String className) {
        return getPropertyName(attr.name, className)
    }
    
    private def boolean hasReferenceMetas(ExpandedAttribute attr) {
        return attr.hasMetas && attr.refIndex >= 0
    }

    private def StringConcatenationClient getPropertyName(String attrName, String className) 
        '''«val property = attrName?.toFirstUpper»«property»«IF property == className»Value«ENDIF»'''

    private def StringConcatenationClient checkCardinality(String className, ExpandedAttribute attr) '''
        «val property = attr.getPropertyName(className)»
        «IF attr.isMultiple»
            yield return CheckCardinality(Name, obj.«property».EmptyIfNull().Count(), «attr.inf», «attr.sup»);
        «ELSEIF attr.isSingleOptional»
            yield return CheckCardinality(Name, obj.«property»«IF attr.hasMetas»?.Value«ENDIF» != null ? 1 : 0, «attr.inf», «attr.sup»);
        «ELSEIF attr.hasReferenceMetas»
            yield return CheckCardinality(Name, obj.«property».Value != null ? 1 : 0, «attr.inf», «attr.sup»);
        «ENDIF»
    '''
}
    