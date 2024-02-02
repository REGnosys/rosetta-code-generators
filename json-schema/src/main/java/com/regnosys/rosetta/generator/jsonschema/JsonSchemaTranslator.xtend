package com.regnosys.rosetta.generator.jsonschema

import com.regnosys.rosetta.generator.object.ExpandedType

class JsonSchemaTranslator {
				
	static def toJsonSchemaBasicType(String typename) {
		switch typename {
			case 'string',
			case 'time',
			case 'date',
			case 'dateTime',
			case 'zonedDateTime',
			case 'calculation':
				'string'
			case 'int':
				'integer'
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
		else
			return type.name.toFirstUpper
	}
}
