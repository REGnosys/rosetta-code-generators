package com.regnosys.rosetta.sample;

import static com.regnosys.rosetta.sample.GeneratorUtils.*;
import static com.regnosys.rosetta.sample.GeneratorUtils.toGroovyType;

import java.util.List;
import java.util.Map;
import java.util.function.Consumer;
import java.util.stream.Collectors;

import org.eclipse.emf.ecore.resource.Resource;

import com.regnosys.rosetta.generator.external.ExternalGenerator;
import com.regnosys.rosetta.generator.external.ExternalOutputConfiguration;
import com.regnosys.rosetta.generator.java.RosettaJavaPackages;
import com.regnosys.rosetta.rosetta.RosettaClass;
import com.regnosys.rosetta.rosetta.RosettaRegularAttribute;
import com.regnosys.rosetta.rosetta.RosettaRootElement;

public class GroovyCodeGenerator implements ExternalGenerator {

	private static final String NAME = "groovy_sample";

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

	private static String attributes(RosettaClass clazz) {
		StringBuilder sb = new StringBuilder();
		for (RosettaRegularAttribute attr : clazz.getRegularAttributes()) {
			if (attr.getCard().getSup() == 1) {
				sb.append("\t").append(toGroovyType(attr.getType().getName()) + " ").append(attr.getName()).append(LINE_SEPARATOR);
			} else if (attr.getCard().isIsMany()) {
				sb.append("\t").append("List<").append(toGroovyType(attr.getType().getName()) + "> ").append(attr.getName()).append(LINE_SEPARATOR);
			}
		}
		return sb.toString();
	}

}
