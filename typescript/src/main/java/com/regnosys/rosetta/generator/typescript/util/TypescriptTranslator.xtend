package com.regnosys.rosetta.generator.typescript.util

class TypescriptTranslator {
				
	static def toTSBasicType(String typename) {
		switch typename {
			case 'String',
			case 'string',				
			case 'calculation',				
			case 'productType',				
			case 'eventType':
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
