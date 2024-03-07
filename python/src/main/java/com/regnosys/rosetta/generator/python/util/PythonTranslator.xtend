package com.regnosys.rosetta.generator.python.util


import com.regnosys.rosetta.generator.object.ExpandedType

import com.regnosys.rosetta.rosetta.simple.Attribute

class PythonTranslator {
    static def toPythonBasicType(String typename) {
        switch (typename) {
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
                return typename
        }
    }
    static def toPythonType(ExpandedType type) {
        val basicType = PythonTranslator.toPythonBasicType(type.name);
        if (basicType !== null)
            return basicType
        else if (type.enumeration)
            return '''«type.name.toFirstUpper»'''
        else
        return type.name.toFirstUpper
    }
    
    def toPythonType(Attribute attr) {
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