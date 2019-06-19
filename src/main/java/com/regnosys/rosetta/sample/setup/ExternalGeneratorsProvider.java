package com.regnosys.rosetta.sample.setup;

import java.util.List;

import com.google.inject.Provider;
import com.google.inject.Singleton;
import com.regnosys.rosetta.generator.external.ExternalGenerator;
import com.regnosys.rosetta.generator.external.ExternalGenerators;

@Singleton
public class ExternalGeneratorsProvider implements Provider<ExternalGenerators> {

	private final List<ExternalGenerator> externalGenerators;

	public ExternalGeneratorsProvider(List<ExternalGenerator> externalGenerators) {
		this.externalGenerators = externalGenerators;
	}

	@Override
	@Singleton
	public ExternalGenerators get() {
		return externalGenerators::iterator;
	}
}