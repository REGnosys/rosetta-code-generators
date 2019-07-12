package com.regnosys.rosetta.generators.test;

import com.google.inject.AbstractModule;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;

/**
 * A concrete implementation of Guice's {@link AbstractModule} that is then used
 * to register external generators See {@link RosettaServerSetup}
 *
 */
final class RosettaExternalGeneratorsModule extends AbstractModule {

	private final ExternalGeneratorProvider<? extends AbstractExternalGenerator> externalGeneratorProvider;

	RosettaExternalGeneratorsModule(
			ExternalGeneratorProvider<? extends AbstractExternalGenerator> externalGeneratorProvider) {
		this.externalGeneratorProvider = externalGeneratorProvider;
	}

	/**
	 * {@inheritDoc}
	 */
	@Override
	protected void configure() {
		bind(AbstractExternalGenerator.class).toProvider(externalGeneratorProvider);
	}
}
