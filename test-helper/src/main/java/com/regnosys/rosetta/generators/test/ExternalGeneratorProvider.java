package com.regnosys.rosetta.generators.test;

import com.google.inject.Provider;
import com.google.inject.Singleton;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;

/**
 * The {@link Provider} implementation class that provides an external generator
 * 
 * @param <T>
 */
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