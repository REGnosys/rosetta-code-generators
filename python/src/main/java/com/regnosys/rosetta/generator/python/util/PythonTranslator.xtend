package com.regnosys.rosetta.generator.python.util


import com.regnosys.rosetta.generator.object.ExpandedType

import com.regnosys.rosetta.rosetta.simple.Attribute

class PythonTranslator {

    static def toPythonBasicType(String typename) {
        switch typename {
           case 'string': 'str'
            case 'time': 'datetime.time'
            case 'date': 'datetime.date'
            case 'dateTime': 'datetime.datetime'
            case 'zonedDateTime': 'datetime.datetime'
            case 'number': 'Decimal'
            case 'boolean': 'bool'
            case 'int': 'int'
            case 'calculation',				
            case 'productType',				
            case 'eventType':
                'str'

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
    

}