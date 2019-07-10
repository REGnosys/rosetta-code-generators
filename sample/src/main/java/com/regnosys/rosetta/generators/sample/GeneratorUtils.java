package com.regnosys.rosetta.generators.sample;

import com.google.common.html.HtmlEscapers;

class GeneratorUtils {

	static final String LINE_SEPARATOR = System.getProperty("line.separator");

	static String toGroovyType(String typeName) {
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
		case "date":
			return "LocalDate";
		case "dateTime":
			return "LocalDateTime";
		case "zonedDateTime":
			return "ZonedDateTime";
		default:
			throw new RuntimeException("could not find the basic type for " + typeName);
		}
	}

	static String emptyGroovyDocWithVersion(String version) {
		StringBuilder sb = new StringBuilder();
		sb.append("/**").append(LINE_SEPARATOR);
		sb.append(" * @version ").append(version).append(LINE_SEPARATOR);
		sb.append("*/").append(LINE_SEPARATOR);
		return sb.toString();
	}

	static String groovyDocWithVersion(String definition, String version) {
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
}
