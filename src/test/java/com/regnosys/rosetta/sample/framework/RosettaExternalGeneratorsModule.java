package com.regnosys.rosetta.sample.framework;

import com.google.inject.AbstractModule;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;
import com.regnosys.rosetta.sample.setup.ExternalGeneratorProvider;

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