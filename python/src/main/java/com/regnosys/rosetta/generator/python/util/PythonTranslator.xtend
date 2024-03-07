package com.regnosys.rosetta.generator.python.util


import com.regnosys.rosetta.generator.object.ExpandedType
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.generator.object.ExpandedAttribute

class PythonTranslator {

    static private def String toPythonBasicTypeInnerFunction (String rosettaType){
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
    static def String toPythonBasicType(ExpandedAttribute attribute) {
        if (attribute === null || attribute.type === null || attribute.type.name === null) 
            return null;
        val rosettaType = attribute.type.name;
        val pythonType  = PythonTranslator::toPythonBasicTypeInnerFunction (rosettaType);
        return (pythonType !== null) ? pythonType : attribute.type.model.name + '.' + rosettaType + '.' + rosettaType;
    }
    static def String toPythonBasicType(String rosettaType) {
        val pythonType = PythonTranslator::toPythonBasicTypeInnerFunction (rosettaType)
        return (pythonType !== null) ? pythonType : rosettaType
    }
    static def String toPythonType(ExpandedType type) {
        if (type === null) 
            return null;
        val basicType = PythonTranslator::toPythonBasicType(type.name);
        if (basicType !== null)
            return basicType
        else if (type.enumeration)
            return '''«type.name.toFirstUpper»'''
        else
            return type.name.toFirstUpper
    }
    
    static def String toPythonType(Attribute attr) {
        var type = attr.getTypeCall.type.name
        val basicType = PythonTranslator.toPythonBasicType(type);
        if (basicType !== null)
            return basicType
        return type.toFirstUpper
    }
    static def boolean checkBasicType(ExpandedAttribute attr) {
        return (attr !== null && attr.type !== null && checkBasicType (attr.type.toString))
    }
    static def boolean checkBasicType(Attribute attr) {
        return (attr !== null && checkBasicType(attr.toString))
    }   
    static def boolean checkBasicType(String attr) {
        return (toPythonBasicTypeInnerFunction (attr) !== null)
    }
}