package com.regnosys.rosetta.sample.setup;

import com.google.inject.Provider;
import com.google.inject.Singleton;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;

@Singleton
public class ExternalGeneratorProvider<T extends AbstractExternalGenerator> implements Provider<T> {

	private final T externalGenerator;

	public ExternalGeneratorProvider(T externalGenerator) {
		this.externalGenerator = externalGenerator;
	}

	@Override
	@Singleton
	public T get() {
		return externalGenerator;
	}
}