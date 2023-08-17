package com.regnosys.rosetta.generators.excel

import com.regnosys.rosetta.generator.external.AbstractExternalGenerator
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Data
import java.io.ByteArrayOutputStream
import java.util.Collection
import java.util.List
import org.apache.poi.ss.usermodel.Row
import org.apache.poi.xssf.usermodel.XSSFWorkbook
import org.eclipse.emf.ecore.EObject
import org.eclipse.emf.ecore.resource.Resource
import org.eclipse.emf.ecore.resource.ResourceSet
import org.eclipse.xtext.nodemodel.ILeafNode
import org.eclipse.xtext.nodemodel.util.NodeModelUtils
import java.nio.file.Files
import java.nio.file.Paths
import org.apache.poi.openxml4j.opc.ZipPackage
import java.util.Base64

class ExcelGenerator extends AbstractExternalGenerator {

	new() {
		super("Csv")
	}

	override generate(Resource resource, RosettaModel model, String version) {
		newHashMap
	}

	override afterAllGenerate(ResourceSet set, Collection<? extends RosettaModel> models, String version) {

		val workbook = new XSSFWorkbook();

		val typesSheet = workbook.createSheet("types");
		val typesHeader = typesSheet.createRow(0);
		populateRow(typesHeader, dataTypeHeader())
		models.flatMap[elements].filter(Data).flatMap[dataAndAttributes].forEach [ row, index |
			val typesRow = typesSheet.createRow(index + 1);
			populateRow(typesRow, row)
		]

		val enumsSheet = workbook.createSheet("enums");
		val enumsHeader = enumsSheet.createRow(0);
		populateRow(enumsHeader, enumHeader())
		models.flatMap[elements].filter(RosettaEnumeration).flatMap[enumAndValues].forEach [ row, index |
			val enumsRow = enumsSheet.createRow(index + 1);
			populateRow(enumsRow, row)
		]

		val baos = new ByteArrayOutputStream

		workbook.write(baos);
		workbook.close();


		val res = newHashMap
		res.put("model.xlsx", Base64.getEncoder().encodeToString(baos.toByteArray))
		return res
	}

	def populateRow(Row row, List<String> cells) {
		cells.forEach [ element, index |
			val headerCell = row.createCell(index);
			headerCell.setCellValue(element);
		]
	}

	def dataTypeHeader() {
		#["Category", "Namespace", "Type Name", "Attribute Name", "Type", "Cardinality", "Definition"]
	}

	def enumHeader() {
		#["Category", "Namespace", "Enum Name", "Enum Value", "Definition"]

	}

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

		#[category, namespace, typeName, "", "", "", definition]
	}

	def dataAttribute(Attribute attribute) {
		val category = "attribute";
		val namespace = (attribute.eContainer.eContainer as RosettaModel).name
		val typeName = (attribute.eContainer as Data).name;
		val attributeName = attribute.name
		val attributeType = attribute.typeCall.type.name;
		val cardinality = attribute.card.extractGrammarText
		val definition = attribute.getDefinition();

		#[category, namespace, typeName, attributeName, attributeType, cardinality, definition]
	}

	def enumType(RosettaEnumeration _enum) {
		val category = "enum"
		val namespace = (_enum.eContainer as RosettaModel).name
		val enumName = _enum.name
		val definition = _enum.definition

		#[category, namespace, enumName, "", definition]
	}

	def enumValue(RosettaEnumValue enumValue) {
		val category = 'enum value';
		val namespace = (enumValue.eContainer.eContainer as RosettaModel).name
		val enumName = (enumValue.eContainer as RosettaEnumeration).name;
		val enumValueName = enumValue.name
		val definition = enumValue.getDefinition();

		#[category, namespace, enumName, enumValueName, definition]
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

}
