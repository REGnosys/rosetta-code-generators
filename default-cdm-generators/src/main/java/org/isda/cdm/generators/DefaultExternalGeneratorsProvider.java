package org.isda.cdm.generators;

import java.util.Collections;
import java.util.Iterator;
import java.util.List;

import com.google.inject.Inject;
import com.google.inject.Provider;
import com.regnosys.rosetta.generator.daml.DamlCodeGenerator;
import com.regnosys.rosetta.generator.external.ExternalGenerator;
import com.regnosys.rosetta.generator.external.ExternalGenerators;

public class DefaultExternalGeneratorsProvider implements Provider<ExternalGenerators>{

	@Inject
	DamlCodeGenerator generator;
	
	@Override
	public ExternalGenerators get() {
		return new DefaultGenerators();
	}
	
	private final class DefaultGenerators implements ExternalGenerators {

		List<ExternalGenerator> gens = Collections.singletonList(generator);
		
		@Override
		public Iterator<ExternalGenerator> iterator() {
			return gens.iterator();
		}
		
	}

}
