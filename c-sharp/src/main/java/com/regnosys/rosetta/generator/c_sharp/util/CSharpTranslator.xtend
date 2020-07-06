package com.regnosys.rosetta.generator.c_sharp.util

import com.regnosys.rosetta.types.RCalculationType
import com.regnosys.rosetta.types.RQualifiedType
import com.regnosys.rosetta.generator.object.ExpandedType
import com.regnosys.rosetta.generator.c_sharp.enums.CSharpEnumGenerator

class CSharpTranslator {
				
	static def toCSharpBasicType(String typename) {
		switch typename {
			case 'string':
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
			case RQualifiedType.PRODUCT_TYPE.qualifiedType:
				'string'
			case RQualifiedType.EVENT_TYPE.qualifiedType:
				'string'
			case RCalculationType.CALCULATION.calculationType:
				'string'

//			Ensure we rename MetaFields data members to avoid name clashes with the enclosing namespace.
			case 'MetaFields':
			    'Meta'
		}
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
