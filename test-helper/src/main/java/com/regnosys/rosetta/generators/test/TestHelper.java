package com.regnosys.rosetta.generators.test;

import java.io.IOException;
import java.net.URL;

import org.apache.commons.io.IOUtils;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.xtext.testing.util.ParseHelper;

import com.google.common.base.Charsets;
import com.google.common.io.Resources;
import com.google.inject.Injector;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;
import com.regnosys.rosetta.rosetta.RosettaModel;

/**
 * Helper class to parse a rosetta text file into the corresponding root Ecore Rosetta object
 * 
 *
 * @param <T> the type of ExternalGenerator that will be used to configured the setup
 */
public class TestHelper<T extends AbstractExternalGenerator> {

	private final Injector injector;

	public TestHelper(T codeGenerator) {
		ExternalGeneratorProvider<T> provider = new ExternalGeneratorProvider<>(codeGenerator);
		this.injector = new RosettaServerSetup(provider).createInjectorDoSetup();
	}

	public RosettaModel parse(URL rosetta) throws Exception {
		@SuppressWarnings("unchecked")
		ParseHelper<RosettaModel> parseHelper = injector.getInstance(ParseHelper.class);
		RosettaModel basicModel = parseHelper.parse(basicTypes());
		ResourceSet resourceSet = basicModel.eResource().getResourceSet();
		return parseHelper.parse(toStringContents(rosetta), resourceSet);
	}

	@SuppressWarnings("unchecked")
	public T getExternalGenerator() {
		return (T) injector.getInstance(AbstractExternalGenerator.class);
	}

	private String basicTypes() {
		URL resource = Resources.getResource("rosetta/types.rosetta");
		return toStringContents(resource);
	}

	public static String toStringContents(URL url) {
		try {
			return IOUtils.toString(url, Charsets.UTF_8);
		} catch (IOException e) {
			throw new RuntimeException("Error reading from url " + url, e);
		}
	}
}
