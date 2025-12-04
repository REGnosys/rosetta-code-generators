package com.regnosys.rosetta.generator.scala.util

import com.regnosys.rosetta.types.RType
import jakarta.inject.Inject
import com.regnosys.rosetta.types.TypeSystem
import com.regnosys.rosetta.types.REnumType
import com.regnosys.rosetta.types.RAliasType
import com.regnosys.rosetta.types.RDataType

class ScalaTranslator {
	
	@Inject
	extension TypeSystem
				
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

	def String toScalaType(RType type) {
		val basicType = ScalaTranslator.toScalaBasicType(type.name);
		val rawType = type.stripFromTypeAliases
		val rawBasicType = ScalaTranslator.toScalaBasicType(rawType.name);
		if (basicType !== null)
			return basicType
		else if (rawBasicType !== null) {
			return rawBasicType
		}
		else if (rawType instanceof REnumType)
			return '''«type.name.toFirstUpper».Value'''
		else
			return type.name.toFirstUpper
	}
	
	def RType stripFromTypeAliasesExceptInt(RType type) {
		var curr = type
		while (curr instanceof RAliasType && curr.name != "int") {
			curr = (curr as RAliasType).refersTo
		}
		return curr
	}
	
	def boolean requiresMetaFields(RDataType type) {
		var curr = type
		while (curr !== null) {
			if (curr.hasMetaAttribute("key")) {
				return true
			}
			curr = curr.superType
		}
		return false;
	}
}
