package com.regnosys.rosetta.generator.scala.util

import com.regnosys.rosetta.generator.object.ExpandedType

class ScalaTranslator {
				
	static def toScalaBasicType(String typename) {
		switch typename {
			case 'string',				
			case 'calculation',				
			case 'productType',				
			case 'eventType':
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
