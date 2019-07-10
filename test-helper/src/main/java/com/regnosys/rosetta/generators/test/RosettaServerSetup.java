package com.regnosys.rosetta.generators.test;

import org.eclipse.xtext.util.Modules2;

import com.google.inject.Guice;
import com.google.inject.Injector;
import com.regnosys.rosetta.RosettaRuntimeModule;
import com.regnosys.rosetta.RosettaStandaloneSetup;

/**
 * Initialization support for the rosetta module.
 * Adds a module for external generator supplied code
 * 
 */
public class RosettaServerSetup extends RosettaStandaloneSetup {

	private final ExternalGeneratorProvider<?> externalGeneratorsProvider;

	public RosettaServerSetup(ExternalGeneratorProvider<?> externalGeneratorsProvider) {
		this.externalGeneratorsProvider = externalGeneratorsProvider;
	}

	public Injector createInjectorDoSetup() {
		return createInjectorAndDoEMFRegistration();
	}

	@Override
	public Injector createInjector() {
		return Guice.createInjector(
				Modules2.mixin(new RosettaRuntimeModule(), new RosettaExternalGeneratorsModule(externalGeneratorsProvider)));
	}

}