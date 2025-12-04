package com.regnosys.rosetta.generator.c_sharp.util

import com.google.common.base.Splitter
import com.regnosys.rosetta.generator.c_sharp.enums.CSharpEnumGenerator
import com.regnosys.rosetta.types.RType
import com.regnosys.rosetta.types.REnumType
import jakarta.inject.Inject
import com.regnosys.rosetta.types.TypeSystem
import com.regnosys.rosetta.types.RAliasType
import com.regnosys.rosetta.types.RDataType

class CSharpTranslator {
	@Inject
	TypeSystem typeSystem
				
	def toCSharpBasicType(String typename) {
		switch typename {
			case 'string',				
			case 'calculation',				
			case 'productType',				
			case 'eventType':
				'string'
			case 'int':
				'int'
			case 'time':
				'NodaTime.LocalTime'
			case 'date':
				'NodaTime.LocalDate'
			case 'dateTime':
				'NodaTime.LocalDateTime'
			case 'zonedDateTime':
				'NodaTime.ZonedDateTime'
			case 'number':
				'decimal'
			case 'boolean':
				'bool'
//			Ensure we rename MetaFields data members to avoid name clashes with the enclosing namespace.
			case 'MetaFields':
			    '_MetaFields'
		}
	}
	
	private def toCSharpType(String typename) {
        val basicType = toCSharpBasicType(typename);
        if (basicType === null) {
            return typename
        } else {
            return Splitter.on('.').splitToList(basicType).last
        }
    }
	
	def isStruct(RType type) {
	   switch type.name {
            case 'time': true
            case 'date': true
            case 'dateTime': true
            case 'zonedDateTime': true
            default: false
        }
	}

	def isDate(RType type) {
	    // TODO: local date time??
	    return type.name == 'date'
	}

	def String toCSharpType(RType type) {
		val rawType = type.stripFromTypeAliasesExceptInt
		val basicType = toCSharpBasicType(rawType.name);
		if (basicType !== null)
			return basicType
		else
			return rawType.name.toFirstUpper
	}

    def toQualifiedCSharpType(RType type) {
        if (type instanceof REnumType) {
            return CSharpEnumGenerator.toCSharpName(type.name, true)
        }
        else {
            return toCSharpType(type)
        }
    }

    def toOptionalCSharpType(RType type) {
        return toQualifiedCSharpType(type) + '?';
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
