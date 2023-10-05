package com.regnosys.rosetta.generators.csv

import com.regnosys.rosetta.generator.external.AbstractExternalGenerator
import org.eclipse.emf.ecore.resource.Resource
import com.regnosys.rosetta.rosetta.RosettaModel
import org.eclipse.emf.ecore.resource.ResourceSet
import java.util.Collection
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.simple.Attribute
import org.eclipse.emf.ecore.EObject
import org.eclipse.xtext.nodemodel.util.NodeModelUtils
import org.eclipse.xtext.nodemodel.ILeafNode

class CsvGenerator extends AbstractExternalGenerator {

	new() {
		super("Csv")
	}

	override generate(Resource resource, RosettaModel model, String version) {
		newHashMap
	}

	override afterAllGenerate(ResourceSet set, Collection<? extends RosettaModel> models, String version) {
		val res = newHashMap

		val dataLines = newArrayList;
		dataLines.add(dataTypeHeader)
		models.flatMap[elements].filter(Data).flatMap[dataAndAttributes].forEach[dataLines.add(it)]
		res.put("types.csv", dataLines.join(System.lineSeparator()))

		val enumLines = newArrayList;
		enumLines.add(enumHeader)
		models.flatMap[elements].filter(RosettaEnumeration).flatMap[enumAndValues].forEach[enumLines.add(it)]
		res.put("enums.csv", enumLines.join(System.lineSeparator()))

		return res
	}

	def dataTypeHeader() '''"Category","Namespace","Type Name","Attribute Name","Type","Cardinality","Definition"'''

	def enumHeader() '''"Category","Namespace","Enum Name","Enum Value","Definition"'''

	def dataAndAttributes(Data it) {
		val dataLines = newArrayList;
		dataLines.add(dataType);
		attributes.map[dataAttribute].forEach[dataLines.add(it)]
		return dataLines
	}

	def enumAndValues(RosettaEnumeration _enum) {
		val enumLines = newArrayList;
		enumLines.add(enumType(_enum));
		_enum.enumValues.map[enumValue].forEach[enumLines.add(it)]
		return enumLines
	}

	def dataType(Data data) {
		val category = "data type"
		val namespace = (data.eContainer as RosettaModel).name
		val typeName = data.name
		val definition = data.definition

		'''"«category»","«namespace»","«typeName»","","","","«definition.escapeSpecialCharacters»"'''
	}

	def dataAttribute(Attribute attribute) {
		val category = "attribute";
		val namespace = (attribute.eContainer.eContainer as RosettaModel).name
		val typeName = (attribute.eContainer as Data).name;
		val attributeName = attribute.name
		val attributeType = attribute.typeCall.type.name;
		val cardinality = attribute.card.extractGrammarText
		val definition = attribute.getDefinition();

		'''"«category»","«namespace»","«typeName»","«attributeName»","«attributeType»","«cardinality»","«definition.escapeSpecialCharacters»"'''
	}

	def enumType(RosettaEnumeration _enum) {
		val category = "enum"
		val namespace = (_enum.eContainer as RosettaModel).name
		val enumName = _enum.name
		val definition = _enum.definition

		'''"«category»","«namespace»","«enumName»","","«definition.escapeSpecialCharacters»"'''
	}

	def enumValue(RosettaEnumValue enumValue) {
		val category = 'enum value';
		val namespace = (enumValue.eContainer.eContainer as RosettaModel).name
		val enumName = (enumValue.eContainer as RosettaEnumeration).name;
		val enumValueName = enumValue.name
		val definition = enumValue.getDefinition();

		'''"«category»","«namespace»","«enumName»","«enumValueName»","«definition.escapeSpecialCharacters»"'''
	}

	def extractGrammarText(EObject object) {
		val node = NodeModelUtils.getNode(object);
		if (node === null) {
			return null;
		}
		return if (node instanceof ILeafNode)
			node.text.trim
		else {
			val builder = new StringBuilder(Math.max(node.getTotalLength(), 1));
			for (ILeafNode leaf : node.leafNodes) {
				builder.append(leaf.text);
			}
			builder.toString.trim;
		}

	}

	def escapeSpecialCharacters(String data) {
		if(data === null) return ''
		var res = data

		if (res.contains('"'))
			res = res.replace('"','\'')

		res = res.replaceAll('\\R',' ')
	}
}
