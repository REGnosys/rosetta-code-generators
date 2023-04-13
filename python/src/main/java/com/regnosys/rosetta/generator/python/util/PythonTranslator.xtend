package com.regnosys.rosetta.generator.python.util

import com.regnosys.rosetta.types.RCalculationType
import com.regnosys.rosetta.types.RQualifiedType
import com.regnosys.rosetta.generator.object.ExpandedType

class PythonTranslator {

    static def toPythonBasicType(String typename) {
        switch typename {
            case 'string': 'str'
            case 'time': 'time'
            case 'date': 'date'
            case 'dateTime': 'datetime'
            case 'zonedDateTime': 'datetime'
            case 'number': 'Decimal'
            case 'boolean': 'bool'
            case 'int': 'int'
            case RQualifiedType.PRODUCT_TYPE.qualifiedType: 'str'
            case RQualifiedType.EVENT_TYPE.qualifiedType: 'str'
            case RCalculationType.CALCULATION.calculationType: 'str'
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

}