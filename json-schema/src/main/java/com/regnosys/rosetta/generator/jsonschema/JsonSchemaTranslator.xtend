package com.regnosys.rosetta.generator.jsonschema

import com.regnosys.rosetta.generator.object.ExpandedType

class JsonSchemaTranslator {
				
	static def toJsonSchemaBasicType(String typename) {
		switch typename {
			case 'string':
				'string'
			case 'int':
				'integer'
//			case 'time':
//				'java.time.LocalTime'
//			case 'date':
//				'java.time.LocalDate'
//			case 'dateTime':
//				'java.time.LocalDateTime'
//			case 'zonedDateTime':
//				'java.time.ZonedDateTime'
			case 'number':
				'number'
			case 'boolean':
				'boolean'
		}
	}

	static def toJsonSchemaType(ExpandedType type) {
		val basicType = JsonSchemaTranslator.toJsonSchemaBasicType(type.name);
		if (basicType !== null)
			return basicType
		else if (type.enumeration)
			return '''«type.name.toFirstUpper».Value'''
		else
			return type.name.toFirstUpper
	}
}
