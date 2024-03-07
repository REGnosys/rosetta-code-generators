package com.regnosys.rosetta.generator.python.util


import com.regnosys.rosetta.generator.object.ExpandedType

import com.regnosys.rosetta.rosetta.simple.Attribute

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
            case 'time',
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
    static def String toPythonBasicType(String rosettaType) {
        // basic conversion from Rosetta type as a string to Python type
        // returns rosettaType if unable to convert
        val pythonType = toPythonBasicTypeInnerFunction (rosettaType)
        return (pythonType === null) ? rosettaType : pythonType
    }
    static def String toPythonType(ExpandedType rosettaExpandedType) {
        // conversion from Rosetta type as an ExpandedType to Python type
        // if unable to convert returns
        //      '''«rosettaExpandedType.name.toFirstUpper»''' for an enumeration or 
        //      returns rosettaExpandedType.name.toFirstUpper  otherwise
        if (rosettaExpandedType === null)
            return null
        var pythonType = toPythonBasicTypeInnerFunction (rosettaExpandedType.name)
        if (pythonType === null)
            pythonType = (rosettaExpandedType.enumeration) ? 
                         '''«rosettaExpandedType.name.toFirstUpper»''' :  
                         rosettaExpandedType.name.toFirstUpper
        return pythonType
    }
    
    static def String toPythonType(Attribute rosettaAttributeType) {
        // conversion from Rosetta type as an Attribute to Python type
        // returns rosettaAttributeType.getTypeCall.type.name if unable to convert
        if (rosettaAttributeType === null)
            return null;
        val rosettaType = rosettaAttributeType.getTypeCall.type.name
        val pythonType = toPythonBasicTypeInnerFunction (rosettaType)
        return (pythonType === null) ? rosettaType.toFirstUpper : pythonType
    }
    static def boolean checkBasicType(Attribute rosettaAttributeType) {
        // check if rosettaAttributeType is valid
        return (rosettaAttributeType !== null && toPythonBasicTypeInnerFunction (rosettaAttributeType.getTypeCall.type.name) !== null)
    }	    

}