package com.regnosys.rosetta.generator.python;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicReference;
import java.util.stream.Collectors;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import com.google.inject.Inject;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;
import com.regnosys.rosetta.generator.java.RosettaJavaPackages.RootPackage;
import com.regnosys.rosetta.rosetta.RosettaEnumeration;
import com.regnosys.rosetta.rosetta.RosettaMetaType;
import com.regnosys.rosetta.rosetta.RosettaModel;
import com.regnosys.rosetta.rosetta.RosettaRootElement;
import com.regnosys.rosetta.rosetta.simple.Data;
import com.regnosys.rosetta.rosetta.simple.Function;
import com.regnosys.rosetta.generator.python.enums.PythonEnumGenerator;
import com.regnosys.rosetta.generator.python.object.PythonModelObjectGenerator;
import com.regnosys.rosetta.generator.python.func.PythonFunctionGenerator;
import com.regnosys.rosetta.generator.python.util.PythonModelGeneratorUtil;

public class PythonCodeGenerator extends AbstractExternalGenerator {
	private static final Logger LOGGER = LoggerFactory.getLogger(PythonCodeGenerator.class);
	
	@Inject
	PythonModelObjectGenerator pojoGenerator;
	@Inject
	PythonFunctionGenerator funcGenerator;
	@Inject
	private PythonEnumGenerator enumGenerator;
	
	@Inject
	PythonModelGeneratorUtil utils;

	public PythonCodeGenerator() {
		super("Python");
	}

	@Override
	public Map<String, ? extends CharSequence> generate(RootPackage arg0, List<RosettaRootElement> arg1, String arg2) {
		return Collections.emptyMap();
	}
	private String getVersion (String version) {
		if (version == null || version.equals ("${project.version}")) {
			version = "0.0.0";
		} else {
			String[] versionParts = version.split ("\\.");
			if (versionParts.length > 2) {
				version = versionParts[0] + "." + versionParts[1] + "." + versionParts[2];
			}
		}
		return version;
	}
	@Override
	public Map<String, ? extends CharSequence> afterGenerate(Collection<? extends RosettaModel> models) {
		// get version in format "#.#.#" defaulting to "0.0.0" if none provided
		final String version = getVersion(models.stream().map(m -> m.getVersion()).findFirst().orElse(null));
		LOGGER.info("Generating python for model {} from DSL version {}", "CDM", version);

		Map<String, CharSequence> result = new HashMap<>();
		AtomicReference<String> previousNamespace = new AtomicReference<>("");
		
		List<String> subfolders = new ArrayList<String>();

		models.stream()
			  .sorted(Comparator.comparing(RosettaModel::getName, String.CASE_INSENSITIVE_ORDER)) // Sort models by name, case-insensitive
			  .forEach(m -> {
				  
				  List<Data> rosettaClasses = m.getElements().stream()
						  .filter(e -> e instanceof Data)
						  .map(Data.class::cast).collect(Collectors.toList());

				  List<RosettaMetaType> metaTypes = m.getElements().stream()
						  .filter(RosettaMetaType.class::isInstance)
						  .map(RosettaMetaType.class::cast).collect(Collectors.toList());

				  List<RosettaEnumeration> rosettaEnums = m.getElements().stream()
						  .filter(RosettaEnumeration.class::isInstance)
						  .map(RosettaEnumeration.class::cast).collect(Collectors.toList());

				  List<Function> rosettaFunctions = m.getElements().stream()
						  .filter(t -> Function.class.isInstance(t))
						  .map(Function.class::cast).collect(Collectors.toList());
				  
				  if(rosettaFunctions.size()>0) {
					  if(!subfolders.contains(m.getName())) {
							  subfolders.add(m.getName());
					  }
					  if(!subfolders.contains(m.getName()+".functions")) {
							  subfolders.add(m.getName()+".functions");
					  }
				  }
				
				if(!m.getName().equals(previousNamespace.get())) {
					previousNamespace.set(m.getName());
					LOGGER.info("processing module: {}", m.getName());
				}
				result.putAll(pojoGenerator.generate(rosettaClasses, metaTypes, version, models));
				result.putAll(enumGenerator.generate(rosettaEnums, version));
				result.putAll(funcGenerator.generate(rosettaFunctions, version));
			});
		List<String> workspaces = getWorkspaces(subfolders);
		result.putAll(generateWorkspaces(workspaces, version));
		result.putAll(generateInits(subfolders));
		result.put("pyproject.toml", utils.createPYProjectTomlFile(version));
		return result;
	}
	
	public static ArrayList<String> getWorkspaces(List<String> subfolders) {
		ArrayList<String> firstElements = new ArrayList<>();

		for (String subfolder : subfolders) {
			String[] parts = subfolder.split("\\.");
			if (parts.length > 0) {
				if(!firstElements.contains(parts[0]))
					firstElements.add(parts[0]);
			}
		}

		return firstElements;
	}
	
	public HashMap<String, String> generateWorkspaces(List<String> workspaces, String version) {
		HashMap<String, String> result = new HashMap<>();

		for (String workspace : workspaces) {
			result.put(utils.toPyFileName(workspace, "__init__"), utils.createTopLevelInitFile(version));
			result.put(utils.toPyFileName(workspace, "version"), utils.createVersionFile(version));

		}	

		return result;
	}
	
	public HashMap<String, String> generateInits(List<String> subfolders) {
		HashMap<String, String> result = new HashMap<>();

		for (String subfolder : subfolders) {
			String[] parts = subfolder.split("\\.");
			for (int i = 1; i < parts.length; i++) {
				StringBuilder keyBuilder = new StringBuilder(parts[0]);
				for (int j = 1; j <= i; j++) {
					keyBuilder.append(".").append(parts[j]);
				}
				String key = utils.toPyFileName(keyBuilder.toString(), "__init__");
				result.putIfAbsent(key, " ");
			}
		}

		return result;
	}
}
