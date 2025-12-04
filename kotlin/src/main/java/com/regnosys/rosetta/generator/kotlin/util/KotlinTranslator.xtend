package com.regnosys.rosetta.generator.kotlin.util

import com.regnosys.rosetta.types.RType
import com.regnosys.rosetta.types.RDataType
import com.regnosys.rosetta.types.RAliasType
import com.regnosys.rosetta.types.REnumType

class KotlinTranslator {

    def String toKotlinBasicType(String typename) {
        switch typename {
            case 'string',				
			case 'calculation',				
			case 'productType',				
			case 'eventType':
            	'String'
            case 'int': 'Int'
            case 'time': 'String'
            case 'date': 'Date'
            case 'dateTime': 'Date'
            case 'zonedDateTime': 'Date'
            case 'number': 'Float'
            case 'boolean': 'Boolean'
        }

    }

    def String toKotlinType(RType rawType) {
    	val type = rawType.stripFromTypeAliasesExceptInt
        val basicType = toKotlinBasicType(type.name);
        if (basicType !== null)
            return basicType
        else if (type instanceof REnumType)
            return '''«type.name.toFirstUpper»'''
		else
        return type.name.toFirstUpper
    }

	def RType stripFromTypeAliasesExceptInt(RType type) {
		var curr = type
		while (curr instanceof RAliasType && curr.name != "int") {
			curr = (curr as RAliasType).refersTo
		}
		return curr
	}
	
	def boolean requiresMetaFields(RDataType type) {
		return type.hasMetaAttribute("key")
	}
}