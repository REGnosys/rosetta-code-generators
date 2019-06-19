package com.regnosys.rosetta.sample.framework;

import org.eclipse.xtext.util.Modules2;

import com.google.inject.Guice;
import com.google.inject.Injector;
import com.regnosys.rosetta.RosettaRuntimeModule;
import com.regnosys.rosetta.ide.RosettaIdeModule;
import com.regnosys.rosetta.ide.RosettaIdeSetup;
import com.regnosys.rosetta.sample.setup.ExternalGeneratorsProvider;

public class RosettaServerSetup extends RosettaIdeSetup {

	private final ExternalGeneratorsProvider externalGeneratorsProvider;

	public RosettaServerSetup(ExternalGeneratorsProvider externalGeneratorsProvider) {
		this.externalGeneratorsProvider = externalGeneratorsProvider;
	}

	public Injector createInjectorDoSetup() {
		return createInjectorAndDoEMFRegistration();
	}

	@Override
	public Injector createInjector() {
		return Guice.createInjector(
				Modules2.mixin(new RosettaRuntimeModule(), new RosettaIdeModule(), new RosettaExternalGeneratorsModule(externalGeneratorsProvider)));
	}

}