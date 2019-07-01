package com.regnosys.rosetta.generators.framework;

import com.google.inject.AbstractModule;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;

public class RosettaExternalGeneratorsModule extends AbstractModule {

	private final ExternalGeneratorProvider externalGeneratorProvider;

	public RosettaExternalGeneratorsModule(ExternalGeneratorProvider externalGeneratorProvider) {
		this.externalGeneratorProvider = externalGeneratorProvider;
	}

	@Override
	protected void configure() {
		bind(AbstractExternalGenerator.class).toProvider(externalGeneratorProvider);
	}
}