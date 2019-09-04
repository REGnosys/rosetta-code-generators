package org.isda.cdm.generators;

import org.isda.cdm.generators.CDMRosettaSetup.CDMRuntimeModule;

import com.google.inject.Binder;
import com.google.inject.Guice;
import com.google.inject.Injector;
import com.google.inject.Module;
import com.google.inject.Provider;
import com.regnosys.rosetta.RosettaRuntimeModule;
import com.regnosys.rosetta.RosettaStandaloneSetup;
import com.regnosys.rosetta.generator.external.ExternalGenerators;

public class CDMRosettaSetup extends RosettaStandaloneSetup{

	public class CDMRuntimeModule extends RosettaRuntimeModule {

		@Override
		public Class<? extends Provider<ExternalGenerators>> provideExternalGenerators() {
			return DefaultExternalGeneratorsProvider.class;
		}
		

	}

	@Override
	public Injector createInjector() {
		return Guice.createInjector(new CDMRuntimeModule());
	}
	
	

}
