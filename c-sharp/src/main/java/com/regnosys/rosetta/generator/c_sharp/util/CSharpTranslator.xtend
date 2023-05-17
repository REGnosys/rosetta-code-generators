package com.regnosys.rosetta.generator.c_sharp.util

import com.google.common.base.Splitter
import com.regnosys.rosetta.generator.object.ExpandedType
import com.regnosys.rosetta.generator.c_sharp.enums.CSharpEnumGenerator

class CSharpTranslator {
				
	static def toCSharpBasicType(String typename) {
		switch typename {
			case 'string',				
			case 'calculation',				
			case 'productType',				
			case 'eventType':
				'string'
			case 'int':
				'int'
			case 'time':
				'NodaTime.LocalTime'
			case 'date':
				'NodaTime.LocalDate'
			case 'dateTime':
				'NodaTime.LocalDateTime'
			case 'zonedDateTime':
				'NodaTime.ZonedDateTime'
			case 'number':
				'decimal'
			case 'boolean':
				'bool'
//			Ensure we rename MetaFields data members to avoid name clashes with the enclosing namespace.
			case 'MetaFields':
			    '_MetaFields'
		}
	}
	
	static def toCSharpType(String typename) {
        val basicType = toCSharpBasicType(typename);
        if (basicType === null) {
            return typename
        } else {
            return Splitter.on('.').splitToList(basicType).last
        }
    }
	
	static def isStruct(ExpandedType type) {
	   switch type.name {
            case 'time': true
            case 'date': true
            case 'dateTime': true
            case 'zonedDateTime': true
            default: false
        }
	} 
	
	static def isDate(ExpandedType type) {
	    // TODO: local date time??
	    return type.name == 'date'
	}

	static def toCSharpType(ExpandedType type) {
		val basicType = CSharpTranslator.toCSharpBasicType(type.name);
		if (basicType !== null)
			return basicType
		else
			return type.name.toFirstUpper
	}

    static def toQualifiedCSharpType(ExpandedType type) {
        if (type.enumeration) {
            return CSharpEnumGenerator.toCSharpName(type.name, true)
        }
        else {
            return toCSharpType(type)
        }
    }

    static def toOptionalCSharpType(ExpandedType type) {
        return toQualifiedCSharpType(type) + '?';
    }
}
