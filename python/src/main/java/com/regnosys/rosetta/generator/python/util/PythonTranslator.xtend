package com.regnosys.rosetta.generator.python.util


import com.regnosys.rosetta.generator.object.ExpandedType
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import java.util.Arrays

class PythonTranslator {
    static private def String toPythonBasicTypeInnerFunction (String rosettaType) {
        // inner private function to convert from Rosetta type to Python type
        // returns null if no matching type
        switch (rosettaType) {
            case 'string', 
            case 'eventType',
            case 'calculation',
            case 'productType':             
                return 'str'
            case 'time':
                return 'datetime.time'
            case 'date': 
                return 'datetime.date'
            case 'dateTime',
            case 'zonedDateTime':
                return 'datetime.datetime'
            case 'number': 
                return 'Decimal'
            case 'boolean': 
                return 'bool'
            case 'int': 
                return 'int'
            default:
                return null
        }
    }
    static def String mangleName (String attrib) {
        // prepend "rosetta_attr_" if attrib is a Python keyword, soft keyword or begins with an "_"
        switch (attrib) {
            case 'False',
            case 'await',
            case 'else',
            case 'import',
            case 'pass',
            case 'None',
            case 'break',
            case 'except',
            case 'in',
            case 'raise',
            case 'True',
            case 'class',
            case 'finally',
            case 'is',
            case 'return',
            case 'and',
            case 'continue',
            case 'for',
            case 'lambda',
            case 'try',
            case 'as',
            case 'def',
            case 'from',
            case 'nonlocal',
            case 'while',
            case 'assert',
            case 'del',
            case 'global',
            case 'not',
            case 'with',
            case 'async',
            case 'elif',
            case 'if',
            case 'or',
            case 'yield',
            case 'match',
            case 'case',
            case 'type',
            case '_':
                return 'rosetta_attr_' + attrib
            default:
                return (attrib.charAt(0) == '_') ? 'rosetta_attr_' + attrib : attrib
        }
    }
    static def String toPythonBasicType(String rosettaType) {
        val pythonType = toPythonBasicTypeInnerFunction (rosettaType)
        return (pythonType === null) ? rosettaType : pythonType
    }
    static def String toPythonType(ExpandedType rosettaExpandedType) {
        if (rosettaExpandedType === null)
            return null
        var pythonType = toPythonBasicTypeInnerFunction (rosettaExpandedType.name)
        if (pythonType === null)
            pythonType = (rosettaExpandedType.enumeration) ? 
                         '''«rosettaExpandedType.name.toFirstUpper»''' :  
                         rosettaExpandedType.name.toFirstUpper
        return pythonType
    }
    static def String toPythonType (ExpandedAttribute rosettaAttribute) {
        if (rosettaAttribute === null || rosettaAttribute.type === null || rosettaAttribute.type.name === null)
            return null
        val rosettaType = rosettaAttribute.type.name;
        val pythonType  = toPythonBasicTypeInnerFunction (rosettaType);
        return (pythonType === null) ? rosettaAttribute.type.model.name + '.' + rosettaType + '.' + rosettaType : pythonType
    }
    static def String toPythonType(Attribute rosettaAttributeType) {
        if (rosettaAttributeType === null)
            return null;
        val rosettaType = rosettaAttributeType.getTypeCall.type.name
        val pythonType  = toPythonBasicTypeInnerFunction (rosettaType)
        return (pythonType === null) ? rosettaType.toFirstUpper : pythonType
    }
    static def boolean checkBasicType(Attribute rosettaAttributeType) {
        return (rosettaAttributeType !== null && toPythonBasicTypeInnerFunction (rosettaAttributeType.getTypeCall.type.name) !== null)
    }
    static def boolean checkBasicType(String rosettaType) {
        return (rosettaType !== null && toPythonBasicTypeInnerFunction (rosettaType) !== null)
    }
    static def boolean checkPythonType (String pythonType) {
        val types = Arrays.asList('int', 
                                  'str', 
                                  'Decimal', 
                                  'date', 
                                  'datetime', 
                                  'datetime.datetime', 
                                  'datetime.date', 
                                  'datetime.time', 
                                  'time',
                                  'bool')
        return types.contains (pythonType)
    }   
}