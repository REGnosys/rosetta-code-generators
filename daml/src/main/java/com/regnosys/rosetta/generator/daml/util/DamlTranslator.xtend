package com.regnosys.rosetta.generator.daml.util

class DamlTranslator {
				
	static def toDamlBasicType(String typename) {
		switch typename {
			case 'String',
			case 'string',				
			case 'calculation',				
			case 'productType',				
			case 'eventType':
				'Text'
			case 'int':
				'Int'
			case 'time':
				'Text'
			case 'date':
				'Date'
			case 'dateTime':
				'Time'
			case 'zonedDateTime':
				'ZonedDateTime'
			case 'number':
				'Decimal'
			case 'boolean':
				'Bool'
		}
	}

	static def toDamlType(String typename) {
		val basicType = toDamlBasicType(typename);
		if (basicType !== null)
			return basicType
		else
			return typename
	}
}
