package com.regnosys.rosetta.generator.golang.util

class GolangTranslator {
				
	static def toGOBasicType(String typename) {
		switch typename {
			case 'String',				
			case 'string',				
			case 'calculation',				
			case 'productType',				
			case 'eventType':
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
