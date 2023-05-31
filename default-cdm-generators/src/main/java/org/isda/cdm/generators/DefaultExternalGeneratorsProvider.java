package org.isda.cdm.generators;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

import com.google.inject.Inject;
import com.google.inject.Provider;
import com.regnosys.rosetta.generator.c_sharp.CSharp8CodeGenerator;
import com.regnosys.rosetta.generator.c_sharp.CSharp9CodeGenerator;
import com.regnosys.rosetta.generator.daml.DamlCodeGenerator;
import com.regnosys.rosetta.generator.external.ExternalGenerator;
import com.regnosys.rosetta.generator.external.ExternalGenerators;
import com.regnosys.rosetta.generator.golang.GolangCodeGenerator;
import com.regnosys.rosetta.generator.kotlin.KotlinCodeGenerator;
import com.regnosys.rosetta.generator.python.PythonCodeGenerator;
import com.regnosys.rosetta.generator.scala.ScalaCodeGenerator;
import com.regnosys.rosetta.generator.typescript.TypescriptCodeGenerator;

public final class DefaultExternalGeneratorsProvider implements Provider<ExternalGenerators> {

	@Inject
	private CSharp8CodeGenerator csharp8Generator;

	@Inject
	private CSharp9CodeGenerator csharp9Generator;

	@Inject
	private DamlCodeGenerator damlGenerator;

	@Inject
	private ScalaCodeGenerator scalaGenerator;

	@Inject
	private TypescriptCodeGenerator typescriptGenerator;

	@Inject
	private GolangCodeGenerator golangGenerator;
	
	@Inject
	private KotlinCodeGenerator kotlinGenerator;
	
	@Inject
	private PythonCodeGenerator pythonGenerator;

	@Override
	public ExternalGenerators get() {
		return new DefaultGenerators();
	}

	private final class DefaultGenerators implements ExternalGenerators {

		private List<ExternalGenerator> gens = Arrays.asList(damlGenerator, scalaGenerator, typescriptGenerator,
				golangGenerator, csharp8Generator, csharp9Generator, kotlinGenerator, pythonGenerator);

		@Override
		public Iterator<ExternalGenerator> iterator() {
			return gens.iterator();
		}
	}
}
