package com.regnosys.rosetta.generator.scala.util

import com.regnosys.rosetta.types.RCalculationType
import com.regnosys.rosetta.types.RQualifiedType
import com.regnosys.rosetta.generator.object.ExpandedType

class ScalaTranslator {
				
	static def toScalaBasicType(String typename) {
		switch typename {
			case 'string':
				'String'
			case 'int':
				'Int'
			case 'time':
				'java.time.LocalTime'
			case 'date':
				'java.time.LocalDate'
			case 'dateTime':
				'java.time.LocalDateTime'
			case 'zonedDateTime':
				'java.time.ZonedDateTime'
			case 'number':
				'scala.math.BigDecimal'
			case 'boolean':
				'Boolean'
			case RQualifiedType.PRODUCT_TYPE.qualifiedType:
				'String'
			case RQualifiedType.EVENT_TYPE.qualifiedType:
				'String'
			case RCalculationType.CALCULATION.calculationType:
				'String'
		}
	}

	static def toScalaType(ExpandedType type) {
		val basicType = ScalaTranslator.toScalaBasicType(type.name);
		if (basicType !== null)
			return basicType
		else if (type.enumeration)
			return '''«type.name.toFirstUpper».Value'''
		else
			return type.name.toFirstUpper
	}
}
