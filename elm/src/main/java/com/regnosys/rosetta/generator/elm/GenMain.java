package com.regnosys.rosetta.generator.elm;

import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import org.eclipse.xtext.util.Arrays;

import com.google.inject.Guice;
import com.google.inject.Injector;
import com.regnosys.rosetta.RosettaRuntimeModule;
import com.regnosys.rosetta.RosettaStandaloneSetup;
import com.regnosys.rosetta.common.util.ClassPathUtils;
import com.regnosys.rosetta.transgest.ModelLoader;
import com.regnosys.rosetta.transgest.ModelLoaderImpl;

public class GenMain {

	public static void main(String[] args) throws IOException {
		if (args.length != 2) {
			System.out.println("Must pass in 2 arguments. <rosetta-dir> <output-dir>");
			System.exit(1);
		}

		String rosettaFolder = args[0];
		String outFolder = args[1];
		Path outPath = Path.of(outFolder);

		if (!Files.exists(outPath)) {
			outPath = Files.createDirectories(outPath);
		}

		List<URL> rosettaFiles = Files.list(Path.of(rosettaFolder)).filter(c -> c.toString().endsWith(".rosetta"))
				.map(x -> extracted(x)).collect(Collectors.toList());

		List<URL> staticRosetta = ClassPathUtils.findStaticRosettaFilePaths().stream()
			.map(x -> extracted(x)).collect(Collectors.toList());
		
		URL[] array = Stream.concat(Files.list(Path.of(rosettaFolder)).filter(c -> c.toString().endsWith(".rosetta")),
				 ClassPathUtils.findStaticRosettaFilePaths().stream())
				.map(x -> extracted(x))
				.toArray(URL[]::new);
			
		ModelLoader loader = new ModelLoaderImpl(array);

		Injector injector = createInjector();

		ElmCodeGenerator codeGenerator = injector.getInstance(ElmCodeGenerator.class);

		Map<String, ? extends CharSequence> afterGenerate = codeGenerator.afterGenerate(loader.models());

		for (Map.Entry<String, ? extends CharSequence> e : afterGenerate.entrySet()) {
			String fileName = e.getKey();
			String contents = e.getValue().toString();
				
			Path file = outPath.resolve(fileName);
			Files.createDirectories(file.getParent());
		
			Files.write(file, contents.getBytes());
		}
	}

	private static URL extracted(Path x) {
		try {
			return x.toUri().toURL();
		} catch (MalformedURLException e) {
			throw new RuntimeException(e);
		}
	}

	protected static Injector createInjector() {
		return new RosettaStandaloneSetup() {
			@Override
			public Injector createInjector() {
				return Guice.createInjector(new RosettaRuntimeModule());
			}
		}.createInjectorAndDoEMFRegistration();
	}

}
