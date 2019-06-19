package com.regnosys.rosetta.sample.framework;

import com.google.inject.AbstractModule;
import com.regnosys.rosetta.generator.external.ExternalGenerators;
import com.regnosys.rosetta.sample.setup.ExternalGeneratorsProvider;

public class RosettaExternalGeneratorsModule extends AbstractModule {
	private final ExternalGeneratorsProvider externalGeneratorsProvider;

	public RosettaExternalGeneratorsModule(ExternalGeneratorsProvider externalGeneratorsProvider) {
		this.externalGeneratorsProvider = externalGeneratorsProvider;
	}

	@Override
	protected void configure() {
		bind(ExternalGenerators.class).toProvider(externalGeneratorsProvider);
	}
}