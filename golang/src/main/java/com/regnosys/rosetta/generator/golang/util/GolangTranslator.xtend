package com.regnosys.rosetta.generator.golang.util

import com.regnosys.rosetta.types.RCalculationType
import com.regnosys.rosetta.types.RQualifiedType

class GolangTranslator {
				
	static def toGOBasicType(String typename) {
		switch typename {
			case 'String',				
			case 'string':
				'string'								 			
			case 'int':
				'int'
			case 'time':
				'time.Time'
			case 'date':
				'time.Time'
			case 'Date':
				'time.Time'
			case 'zonedDateTime':
				'time.Time'
			case 'number':
				'float64'
			case 'boolean':
				'bool'
			case RQualifiedType.PRODUCT_TYPE.qualifiedType:
				'string'
			case RQualifiedType.EVENT_TYPE.qualifiedType:
				'string'
			case RCalculationType.CALCULATION.calculationType:
				'string'
		}
	}

	static def toGOType(String typename) {
		val basicType = com.regnosys.rosetta.generator.golang.util.GolangTranslator.toGOBasicType(typename);
		if (basicType !== null)
			return basicType
		else
			return typename
	}
}
