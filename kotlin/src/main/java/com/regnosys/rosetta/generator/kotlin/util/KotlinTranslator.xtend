package com.regnosys.rosetta.generator.kotlin.util

import com.regnosys.rosetta.types.RCalculationType
import com.regnosys.rosetta.types.RQualifiedType
import com.regnosys.rosetta.generator.object.ExpandedType

class KotlinTranslator {

    static def toKotlinBasicType(String typename) {
        switch typename {
            case 'string': 'String'
            case 'int': 'Int'
            case 'time': 'String'
            case 'date': 'Date'
            case 'dateTime': 'Date'
            case 'zonedDateTime': 'Date'
            case 'number': 'Float'
            case 'boolean': 'Boolean'
            case RQualifiedType.PRODUCT_TYPE.qualifiedType: 'String'
            case RQualifiedType.EVENT_TYPE.qualifiedType: 'String'
            case RCalculationType.CALCULATION.calculationType: 'String'
        }

    }

    static def toKotlinType(ExpandedType type) {
        val basicType = KotlinTranslator.toKotlinBasicType(type.name);
        if (basicType !== null)
            return basicType
        else if (type.enumeration)
            return '''«type.name.toFirstUpper»'''
		else
        return type.name.toFirstUpper
    }

}