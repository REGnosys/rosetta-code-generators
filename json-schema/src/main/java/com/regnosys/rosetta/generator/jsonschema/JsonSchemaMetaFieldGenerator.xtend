package com.regnosys.rosetta.generator.jsonschema

import com.google.inject.Inject
import com.regnosys.rosetta.generator.object.ExpandedType
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.simple.Data
import java.util.List
import java.util.Map

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*
import static extension com.regnosys.rosetta.generator.jsonschema.JsonSchemaGeneratorHelper.*

class JsonSchemaMetaFieldGenerator {

	@Inject extension JsonSchemaGeneratorHelper


    def Map<String, ? extends CharSequence> generateMetaFields(List<Data> data, Iterable<RosettaMetaType> metaTypes) {
        
        val result = newHashMap
        
        val refs = data
                .flatMap[expandedAttributes]
 				.filter[hasMetas && metas.exists[name=="reference" || name=="address"]]
                .map[type]
                .toSet

        for (ref:refs) {
            result.put(getFilename(ref.metaNamespace, ref.toReferenceWithMetaTypeName), generateReferenceWithMeta(ref))
        }

        val metas =  data
                .flatMap[expandedAttributes]
                .filter[hasMetas && !metas.exists[name=="reference" || name=="address"]]
                .map[type]
                .toSet

        for (meta:metas) {
            result.put(getFilename(meta.metaNamespace, meta.toFieldWithMetaTypeName), generateFieldWithMeta(meta))
        }

		result.put(getFilename("com.rosetta.model.metafields", "MetaFields"), genMetaFields())
        result.put(getFilename("com.rosetta.model.lib.meta", "Key"), genKey())
        result.put(getFilename("com.rosetta.model.lib.meta", "Reference"), genReference())

        return result
    }

    private def String generateFieldWithMeta(ExpandedType type) '''
		{
		  "$schema": "http://json-schema.org/draft-04/schema#",
		  "$anchor": "«type.model.name»",
		  "type": "object",
		  "title": "«type.toFieldWithMetaTypeName»",
		  "properties": {
		    "value": {
		      «type.attributeType»
		    },
		    "meta": {
		      "$ref": "com-rosetta-model-metafields-MetaFields.schema.json"
		    }
		  }
		}
	'''

	def String getAttributeType(ExpandedType type) {
		if (type.isBuiltInType) {
			return '''"type": "«JsonSchemaTranslator.toJsonSchemaType(type)»"'''
		} else {
			return '''"$ref": "«getFilename(type.model.name, JsonSchemaTranslator.toJsonSchemaType(type))»"'''
		}
	}

    private def String generateReferenceWithMeta(ExpandedType type) '''
		{
		  "$schema": "http://json-schema.org/draft-04/schema#",
		  "$anchor": "«type.model.name».metafields",
		  "type": "object",
		  "title": "ReferenceWithMeta«type.toMetaTypeName»",
		  "properties": {
		    "globalReference": {
		      "type": "string"
		    },
		    "externalReference": {
		      "type": "string"
		    },
		    "address": {
		      "$ref": "com-rosetta-model-lib-meta-Reference.schema.json"
		    }
		  }
		}
	'''

    private def String genMetaFields() '''
		{
		  "$schema": "http://json-schema.org/draft-04/schema#",
		  "$anchor": "com.rosetta.model.metafields",
		  "type": "object",
		  "title": "MetaFields",
		  "properties": {
		    "scheme": {
		      "type": "string"
		    },
		    "globalKey": {
		      "type": "string"
		    },
		    "externalKey": {
		      "type": "string"
		    },
		    "key": {
		      "type": "array",
		      "items": {
		        "$ref": "com-rosetta-model-lib-meta-Key.schema.json"
		      },
		      "minItems": 0
		    }
		  }
		}
	'''

    private def String genKey() '''
		{
		  "$schema": "http://json-schema.org/draft-04/schema#",
		  "$anchor": "com.rosetta.model.lib.meta",
		  "type": "object",
		  "title": "Key",
		  "properties": {
		    "scope": {
		      "type": "string"
		    },
		    "value": {
		      "type": "string"
		    }
		  }
		}
    '''
    
    private def String genReference() '''
		{
		  "$schema": "http://json-schema.org/draft-04/schema#",
		  "$anchor": "com.rosetta.model.lib.meta",
		  "type": "object",
		  "title": "Reference",
		  "properties": {
		    "scope": {
		      "type": "string"
		    },
		    "value": {
		      "type": "string"
		    }
		  }
		}
    '''
}