package com.regnosys.rosetta.generator.typescript.util

import com.regnosys.rosetta.types.RCalculationType
import com.regnosys.rosetta.types.RQualifiedType

class TypescriptTranslator {
				
	static def toTSBasicType(String typename) {
		switch typename {
			case 'String':
				'string'
			case 'string':
				'string'
			case 'int':
				'number'
			case 'time':
				'string'
			case 'date':
				'Date'
			case 'Date':
				'Date'
			case 'zonedDateTime':
				'Date'
			case 'number':
				'number'
			case 'boolean':
				'boolean'
			case RQualifiedType.PRODUCT_TYPE.qualifiedType:
				'string'
			case RQualifiedType.EVENT_TYPE.qualifiedType:
				'string'
			case RCalculationType.CALCULATION.calculationType:
				'string'
		}
	}

	static def toTSType(String typename) {
		val basicType = com.regnosys.rosetta.generator.typescript.util.TypescriptTranslator.toTSBasicType(typename);
		if (basicType !== null)
			return basicType
		else
			return typename
	}
}
