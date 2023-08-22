package com.regnosys.rosetta.generators.sample;

import java.util.Map;
import java.util.stream.Collectors;

import org.eclipse.emf.ecore.resource.Resource;

import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;
import com.regnosys.rosetta.rosetta.RosettaModel;
import com.regnosys.rosetta.rosetta.simple.Attribute;
import com.regnosys.rosetta.rosetta.simple.Data;
import com.rosetta.util.DottedPath;

/**
 * Implementation of a code generator for the Groovy language
 */
public class SampleCodeGenerator extends AbstractExternalGenerator {

	/**
	 * Constructs a generator with a name
	 */
	public SampleCodeGenerator() {
		super("Sample");
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	public Map<String, ? extends CharSequence> generate(Resource resource, RosettaModel model, String version) {
		DottedPath namespace = DottedPath.splitOnDots(model.getName());
		Map<String, ? extends CharSequence> generatedFiles = model.getElements().stream().filter(Data.class::isInstance)
				.map(Data.class::cast).collect(
						Collectors.toMap(e -> generateFilename(namespace, e), e -> generateClass(namespace, e, version)));

		return generatedFiles;
	}

	private String generateFilename(DottedPath root, Data clazz) {
		return root.withForwardSlashes() + "/" + clazz.getName() + ".sample";
	}

	private String generateClass(DottedPath root, Data clazz, String version) {
		StringBuilder sb = new StringBuilder();
		sb.append("package ").append(root);
		sb.append(GeneratorUtils.LINE_SEPARATOR).append(GeneratorUtils.LINE_SEPARATOR);
		sb.append(GeneratorUtils.groovyDocWithVersion(clazz.getDefinition(), version));
		sb.append("class ").append(clazz.getName()).append(" {");
		sb.append(GeneratorUtils.LINE_SEPARATOR);
		sb.append(attributes(clazz));
		sb.append("}");
		sb.append(GeneratorUtils.LINE_SEPARATOR);
		return sb.toString();
	}

	private static String attributes(Data clazz) {
		StringBuilder sb = new StringBuilder();
		for (Attribute attr : clazz.getAttributes()) {
			if (attr.getCard().getSup() == 1) {
				sb.append("\t").append(GeneratorUtils.toGroovyType(attr.getTypeCall().getType().getName()) + " ")
						.append(attr.getName()).append(GeneratorUtils.LINE_SEPARATOR);
			} else if (attr.getCard().isIsMany()) {
				sb.append("\t").append("List<").append(GeneratorUtils.toGroovyType(attr.getTypeCall().getType().getName()) + "> ")
						.append(attr.getName()).append(GeneratorUtils.LINE_SEPARATOR);
			}
		}
		return sb.toString();
	}

}
