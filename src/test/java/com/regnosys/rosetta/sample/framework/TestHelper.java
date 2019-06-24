package com.regnosys.rosetta.sample.framework;

import java.io.IOException;
import java.net.URL;
import java.util.List;

import org.apache.commons.io.IOUtils;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.eclipse.xtext.testing.util.ParseHelper;

import com.google.common.base.Charsets;
import com.google.inject.Injector;
import com.regnosys.rosetta.rosetta.RosettaModel;
import com.regnosys.rosetta.sample.GroovyCodeGenerator;
import com.regnosys.rosetta.sample.setup.ExternalGeneratorsProvider;

public class TestHelper {

	private final Injector injector;

	public TestHelper() {
		ExternalGeneratorsProvider provider = new ExternalGeneratorsProvider(List.of(new GroovyCodeGenerator()));
		this.injector = new RosettaServerSetup(provider).createInjectorDoSetup();
	}

	public RosettaModel parse(URL model) throws Exception {
		ParseHelper<RosettaModel> parseHelper = injector.getInstance(ParseHelper.class);
		RosettaModel basicModel = parseHelper.parse(basicTypes());
		ResourceSet resourceSet = basicModel.eResource().getResourceSet();
		RosettaModel parsedModel = parseHelper.parse(toStringContents(model), resourceSet);
		return parsedModel;
	}

	private String basicTypes() {
		URL resource = this.getClass().getResource("/rosetta/types.rosetta");
		return toStringContents(resource);
	}

	public static String toStringContents(URL url) {
		try {
			return IOUtils.toString(url, Charsets.UTF_8);
		} catch (IOException e) {
			throw new RuntimeException("Error reading url", e);
		}
	}
}
