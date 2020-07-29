package org.isda.cdm.generators;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

import com.google.inject.Inject;
import com.google.inject.Provider;
import com.regnosys.rosetta.generator.c_sharp.CSharpCodeGenerator;
import com.regnosys.rosetta.generator.daml.DamlCodeGenerator;
import com.regnosys.rosetta.generator.external.ExternalGenerator;
import com.regnosys.rosetta.generator.external.ExternalGenerators;
import com.regnosys.rosetta.generator.golang.GolangCodeGenerator;
import com.regnosys.rosetta.generator.scala.ScalaCodeGenerator;
import com.regnosys.rosetta.generator.typescript.TypescriptCodeGenerator;

public final class DefaultExternalGeneratorsProvider implements Provider<ExternalGenerators> {

	@Inject
	private DamlCodeGenerator damlGenerator;

	@Inject
	private ScalaCodeGenerator scalaGenerator;

	@Inject
	private TypescriptCodeGenerator typescriptGenerator;

	@Inject
	private GolangCodeGenerator golangGenerator;

	@Inject
	private CSharpCodeGenerator csharpGenerator;

	@Override
	public ExternalGenerators get() {
		return new DefaultGenerators();
	}

	private final class DefaultGenerators implements ExternalGenerators {

		private List<ExternalGenerator> gens = Arrays.asList(damlGenerator, scalaGenerator, typescriptGenerator,
				golangGenerator, csharpGenerator);

		@Override
		public Iterator<ExternalGenerator> iterator() {
			return gens.iterator();
		}

	}

}
