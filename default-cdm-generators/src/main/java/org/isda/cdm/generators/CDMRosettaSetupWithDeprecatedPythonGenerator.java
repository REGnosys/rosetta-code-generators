package org.isda.cdm.generators;

import com.google.inject.Guice;
import com.google.inject.Injector;
import com.google.inject.Provider;
import com.regnosys.rosetta.RosettaRuntimeModule;
import com.regnosys.rosetta.RosettaStandaloneSetup;
import com.regnosys.rosetta.generator.external.ExternalGenerators;

/**
 * @deprecated Use {@link CDMRosettaSetup} instead
 */
@Deprecated
public final class CDMRosettaSetupWithDeprecatedPythonGenerator extends RosettaStandaloneSetup {

	public final class CDMRuntimeModule extends RosettaRuntimeModule {

		@Override
		public Class<? extends Provider<ExternalGenerators>> provideExternalGenerators() {
			return DefaultExternalGeneratorsWithDeprecatedPythonGeneratorProvider.class;
		}
	}

	@Override
	public Injector createInjector() {
		return Guice.createInjector(new CDMRuntimeModule());
	}

}
