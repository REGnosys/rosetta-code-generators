package com.regnosys.rosetta.sample;

import java.util.List;
import java.util.Map;
import java.util.function.Consumer;
import java.util.stream.Collectors;

import org.eclipse.emf.ecore.resource.Resource;

import com.google.common.html.HtmlEscapers;
import com.regnosys.rosetta.generator.external.ExternalGenerator;
import com.regnosys.rosetta.generator.external.ExternalOutputConfiguration;
import com.regnosys.rosetta.generator.java.RosettaJavaPackages;
import com.regnosys.rosetta.rosetta.RosettaClass;
import com.regnosys.rosetta.rosetta.RosettaRegularAttribute;
import com.regnosys.rosetta.rosetta.RosettaRootElement;

public class GroovyCodeGenerator implements ExternalGenerator {

	private static final String LINE_SEPARATOR = System.getProperty("line.separator");

	private static final String NAME = "sample";

	@Override
	public ExternalOutputConfiguration getOutputConfiguration() {
		return new ExternalOutputConfiguration(NAME, "Code generation configuration");
	}

	@Override
	public void generate(RosettaJavaPackages packages, List<RosettaRootElement> elements, String version,
			Consumer<Map<String, ? extends CharSequence>> processResults, Resource resource) {
		// where might we need this??
		String resourceAsString = resource.getURI().toString();
		//
		Map<String, ? extends CharSequence> classFiles = elements.stream()
																 .filter(RosettaClass.class::isInstance)
																 .map(RosettaClass.class::cast)
																 .collect(Collectors.toMap(e -> generateFilename(packages, e),
																		 e -> generateClass(packages, e, version)));
		processResults.accept(classFiles);
	}

	private String generateFilename(RosettaJavaPackages packages, RosettaClass clazz) {
		return packages.model().directoryName() + "/" + clazz.getName() + ".groovy";
	}

	private String generateClass(RosettaJavaPackages packages, RosettaClass clazz, String version) {
		StringBuilder sb = new StringBuilder();
		sb.append("package ").append(packages.model().packageName());
		sb.append(LINE_SEPARATOR).append(LINE_SEPARATOR);
		sb.append(groovyDocWithVersion(clazz.getDefinition(), version));
		sb.append("class ").append(clazz.getName()).append(" {");
		sb.append(LINE_SEPARATOR);
		sb.append(attributes(clazz));
		sb.append("}");
		sb.append(LINE_SEPARATOR);
		return sb.toString();
	}

	private String attributes(RosettaClass clazz) {
		StringBuilder sb = new StringBuilder();
		for (RosettaRegularAttribute attr : clazz.getRegularAttributes()) {
			if (attr.getCard().getSup() == 1) {
				sb.append("\t").append(toGroovyType(attr.getType().getName()) + " ").append(attr.getName()).append(LINE_SEPARATOR);
			} else if (attr.getCard().getSup() > 1) {
				sb.append("\t").append("List<").append(attr.getType().getName() + ">").append(attr.getName()).append(LINE_SEPARATOR);
			}
		}
		return sb.toString();
	}

	private String groovyDocWithVersion(String definition, String version) {
		if (definition != null && !definition.isEmpty()) {
			StringBuilder sb = new StringBuilder();
			sb.append("/**").append(LINE_SEPARATOR);
			sb.append(" * ").append(HtmlEscapers.htmlEscaper().escape(definition)).append(LINE_SEPARATOR);
			sb.append(" *").append(LINE_SEPARATOR);
			sb.append(" * @version ").append(version).append(LINE_SEPARATOR);
			sb.append("*/").append(LINE_SEPARATOR);
			return sb.toString();
		} else {
			return emptyGroovyDocWithVersion(version);
		}

	}

	private String emptyGroovyDocWithVersion(String version) {
		StringBuilder sb = new StringBuilder();
		sb.append("/**").append(LINE_SEPARATOR);
		sb.append(" * @version ").append(version).append(LINE_SEPARATOR);
		sb.append("*/").append(LINE_SEPARATOR);
		return sb.toString();
	}

	private String toGroovyType(String typeName) {
		switch (typeName) {
		case "string":
			return "String";
		case "int":
			return "Integer";
		case "number":
			return "java.math.BigDecimal";
		case "boolean":
			return "Boolean";
		case "time":
			return "LocalTime";
		//				case 'date':
		//					'java.time.LocalDate'
		//				case 'dateTime':
		//					'java.time.LocalDateTime'
		//				case 'zonedDateTime':
		//					'java.time.ZonedDateTime'
		//				case 'number':
		//					'java.math.BigDecimal'
		}
		throw new RuntimeException("could not find the basic type for " + typeName);
	}
}
