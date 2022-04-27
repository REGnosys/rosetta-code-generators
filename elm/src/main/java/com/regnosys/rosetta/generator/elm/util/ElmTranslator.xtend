package com.regnosys.rosetta.generator.elm.util

import com.regnosys.rosetta.types.RCalculationType
import com.regnosys.rosetta.types.RQualifiedType

class ElmTranslator {
				
	static def toBasicType(String typename) {
		switch typename {
			case 'String',				
			case 'string':
				'String'								 			
			case 'int':
				'Int'
			case 'time':
				'LocalTime'
			case 'date':
				'LocalDate'
			case 'Date':
				'LocalDate'
			case 'zonedDateTime':
				'ZonedDateTime'
			case 'number':
				'Float'
			case 'boolean':
				'Bool'
			case RQualifiedType.PRODUCT_TYPE.qualifiedType:
				'String'
			case RQualifiedType.EVENT_TYPE.qualifiedType:
				'String'
			case RCalculationType.CALCULATION.calculationType:
				'String'
		}
	}

	static def toElmType(String typename) {
		val basicType = com.regnosys.rosetta.generator.elm.util.ElmTranslator.toBasicType(typename);
		if (basicType !== null)
			return basicType
		else
			return typename
	}
}
