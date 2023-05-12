package com.regnosys.rosetta.generator.python;

import java.io.File;
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
import com.regnosys.rosetta.generator.java.RosettaJavaPackages;
import com.regnosys.rosetta.generator.python.enums.PythonEnumGenerator;
import com.regnosys.rosetta.generator.python.object.PythonModelObjectGenerator;
import com.regnosys.rosetta.generator.python.func.PythonFunctionGenerator;
import com.regnosys.rosetta.rosetta.RosettaEnumeration;
import com.regnosys.rosetta.rosetta.RosettaMetaType;
import com.regnosys.rosetta.rosetta.RosettaModel;
import com.regnosys.rosetta.rosetta.RosettaRootElement;
import com.regnosys.rosetta.rosetta.simple.Data;
import com.regnosys.rosetta.rosetta.simple.Function;
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
	public Map<String, ? extends CharSequence> generate(RosettaJavaPackages packages, List<RosettaRootElement> elements, String version) {
		return Collections.emptyMap();
	}
	
	@Override
	public Map<String, ? extends CharSequence> afterGenerate(Collection<? extends RosettaModel> models) {

//		String version = models.stream().map(m -> m.getVersion()).findFirst().orElse("No version");
		String version   = "3.3.2";

		LOGGER.info("Generating python for model {} from DSL version {}", "CDM", version);

		Map<String, CharSequence> result = new HashMap<>();
		AtomicReference<String> previousNamespace = new AtomicReference<>("");
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
				
				if(!m.getName().equals(previousNamespace.get())) {
					previousNamespace.set(m.getName());
					LOGGER.info("processing module: {}", m.getName());
				}

				try {
					result.putAll(pojoGenerator.generate(rosettaClasses, metaTypes, version, models));
					result.putAll(enumGenerator.generate(rosettaEnums, version));
					result.putAll(funcGenerator.generate(rosettaFunctions, version));
				} catch (Exception e) {
					System.out.println ("Exception while generating python");
					e.printStackTrace();
				}
			});
		String namespace = "cdm";
		result.put(utils.toPyFileName (namespace, "__init__"), utils.createTopLevelInitFile(version));
		result.put(utils.toPyFileName (namespace, "version"), utils.createVersionFile (version));
		result.put("pyproject.toml", utils.createPYProjectTomlFile(version));
		return result;
	}
}
