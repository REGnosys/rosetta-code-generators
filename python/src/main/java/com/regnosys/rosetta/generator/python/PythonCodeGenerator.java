package com.regnosys.rosetta.generator.python;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.inject.Inject;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;
import com.regnosys.rosetta.generator.java.RosettaJavaPackages;
import com.regnosys.rosetta.generator.python.enums.PythonEnumGenerator;
import com.regnosys.rosetta.generator.python.func.PythonFunctionGenerator;
import com.regnosys.rosetta.generator.python.object.PythonModelObjectGenerator;
import com.regnosys.rosetta.generator.python.util.PythonModelGeneratorUtil;
import com.regnosys.rosetta.rosetta.RosettaEnumeration;
import com.regnosys.rosetta.rosetta.RosettaRootElement;
import com.regnosys.rosetta.rosetta.simple.Data;
import com.regnosys.rosetta.rosetta.simple.Function;


public class PythonCodeGenerator extends AbstractExternalGenerator {
	
	private static final String EMPTY_FILE_CONTENTS = "";

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
		LOGGER.info("generate [packages={}, elements={}, version={}]", packages.model().withForwardSlashes(), elements.size(), version);
		
		Map<String, CharSequence> result = new HashMap<>();
		
		result.put(toPyFileName(packages, "__init__"), EMPTY_FILE_CONTENTS);
		
		elements.stream()
				.filter(Data.class::isInstance)
				.map(Data.class::cast)
				.forEach(data -> {
					// TODO pojoGenerator.generate to generate single pojo file contents
					String dataFileContents = EMPTY_FILE_CONTENTS;
					result.put(toPyFileName(packages, data.getName()), dataFileContents);
				});

		elements.stream()
				.filter(RosettaEnumeration.class::isInstance)
				.map(RosettaEnumeration.class::cast)
				.forEach(e -> {
					// TODO enumGenerator.generate to generate single enum file contents
					String enumFileContents = EMPTY_FILE_CONTENTS;
					result.put(toPyFileName(packages, e.getName()), enumFileContents);
				});
		
		elements.stream()
				.filter(Function.class::isInstance)
				.map(Function.class::cast)
				.forEach(func -> {
					// TODO funcGenerator.generate to generate single func file contents
					String funcFileContents = EMPTY_FILE_CONTENTS;
					result.put(toPyFileName(packages, func.getName()), funcFileContents);
				});
		
		// Generate at top level.  TODO Move to different method where only generated once
		result.put("version.py", getVersionFile(version));
		result.put("pyproject.toml", getPyProjectTomlFile(version));
		
		return result;
	}

	private String getVersionFile(String version) {
		return String.format("__version__ = \"%s\"", version);
	}
	
	private String getPyProjectTomlFile(String version) {
		return "";
	}
	
	private String toPyFileName(RosettaJavaPackages packages, String fileName) {
		return packages.model().withForwardSlashes() + "/" + fileName + ".py";
	}
}