package com.regnosys.rosetta.generator.daml.util

import com.regnosys.rosetta.rosetta.RosettaBasicType
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaRecordType
import com.regnosys.rosetta.rosetta.RosettaType
import com.regnosys.rosetta.rosetta.RosettaTypeAlias
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.types.RAliasType
import com.regnosys.rosetta.types.RDataType
import com.regnosys.rosetta.types.REnumType
import com.regnosys.rosetta.types.RType
import com.regnosys.rosetta.types.builtin.RBasicType
import com.regnosys.rosetta.types.builtin.RRecordType

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
				'Datetime'
			case 'zonedDateTime':
				'ZonedDateTime'
			case 'number':
				'Decimal'
			case 'boolean':
				'Bool'
		}
	}

	static def String toDamlType(RosettaType type) {
		switch (type) {
			RosettaBasicType:
				toDamlBasicType(type.name)
			RosettaTypeAlias: {
				// first check it there is a basic type that matches the typeAlias, e.g. int
				val aliasType = toDamlBasicType(type.name)
				if (aliasType !== null) {
					return aliasType
				}
				// if not, get the typeAlias's referred type
				toDamlType(type.typeCall.type)
			}
			Data,
			RosettaEnumeration,
			RosettaRecordType:
				type.name.toFirstUpper
			default: {
				type.name.toFirstUpper
			}
		}
	}

	static def String toDamlType(RType rType) {
		switch (rType) {
			RBasicType:
				toDamlBasicType(rType.name)
			RAliasType: {
				// first check it there is a basic type that matches the typeAlias, e.g. int
				val aliasType = toDamlBasicType(rType.name)
				if (aliasType !== null) {
					return aliasType
				}
				// if not, get the typeAlias's referred type
				toDamlType(rType.refersTo)
			}
			RDataType,
			REnumType,
			RRecordType:
				rType.name.toFirstUpper
			default: {
				rType.name.toFirstUpper
			}
		}
	}
}
