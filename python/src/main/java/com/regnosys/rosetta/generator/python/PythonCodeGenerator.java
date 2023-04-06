package com.regnosys.rosetta.generator.python;

import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

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
		enumGenerator = new PythonEnumGenerator();
	}

	@Override
	public Map<String, ? extends CharSequence> generate(RosettaJavaPackages packages, List<RosettaRootElement> elements, String version) {
		return Collections.emptyMap();
	}
	
	public Map<String, ? extends CharSequence> afterGenerate(Collection<? extends RosettaModel> models, Object element, HashMap<String, List<String>> importsVariables) {
		String version = models.stream().map(m->m.getVersion()).findFirst().orElse("No version");
		
		Map<String, CharSequence> result = new HashMap<>();
		
		models.stream().flatMap(m->m.getElements().stream()).filter((e)-> e == element);
		
		List<Data> rosettaClasses = models.stream().flatMap(m->m.getElements().stream())
				.filter((e)-> e == element).filter((e)-> e instanceof Data)
				.map(Data.class::cast).collect(Collectors.toList());
		List<RosettaMetaType> metaTypes = models.stream().flatMap(m->m.getElements().stream()).filter((e)-> e == element).filter(RosettaMetaType.class::isInstance)
				.map(RosettaMetaType.class::cast).collect(Collectors.toList());

		List<RosettaEnumeration> rosettaEnums = models.stream().flatMap(m->m.getElements().stream()).filter((e)-> e == element).filter(RosettaEnumeration.class::isInstance)
				.map(RosettaEnumeration.class::cast).collect(Collectors.toList());
		
		List<Function> rosettaFunctions = models.stream().flatMap(m->m.getElements().stream()).filter((e)-> e == element).filter(t -> Function.class.isInstance(t))
				.map(Function.class::cast).collect(Collectors.toList());
		result.putAll(utils.createImports(rosettaClasses, rosettaEnums, rosettaFunctions, importsVariables));
		result.putAll(pojoGenerator.generate(rosettaClasses, metaTypes, version, importsVariables));
		result.putAll(enumGenerator.generate(rosettaEnums, version));
		result.putAll(funcGenerator.generate(rosettaFunctions, version));
		return result;
	}
	
	public Map<String, ? extends CharSequence> afterGenerateTest(Collection<? extends RosettaModel> models) {
		String version = models.stream().map(m->m.getVersion()).findFirst().orElse("No version");
		
		HashMap<String, List<String>> imports = new HashMap<String, List<String>>();
		
		Map<String, CharSequence> result = new HashMap<>();
		
		models.stream().flatMap(m->m.getElements().stream());
		
		List<Data> rosettaClasses = models.stream().flatMap(m->m.getElements().stream())
				.filter((e)-> e instanceof Data)
				.map(Data.class::cast).collect(Collectors.toList());
		List<RosettaMetaType> metaTypes = models.stream().flatMap(m->m.getElements().stream()).filter(RosettaMetaType.class::isInstance)
				.map(RosettaMetaType.class::cast).collect(Collectors.toList());

		List<RosettaEnumeration> rosettaEnums = models.stream().flatMap(m->m.getElements().stream()).filter(RosettaEnumeration.class::isInstance)
				.map(RosettaEnumeration.class::cast).collect(Collectors.toList());
		
		List<Function> rosettaFunctions = models.stream().flatMap(m->m.getElements().stream()).filter(t -> Function.class.isInstance(t))
				.map(Function.class::cast).collect(Collectors.toList());
		result.putAll(utils.createImports(rosettaClasses, rosettaEnums, rosettaFunctions, imports));
		result.putAll(pojoGenerator.generate(rosettaClasses, metaTypes, version, imports));
		result.putAll(enumGenerator.generate(rosettaEnums, version));
		result.putAll(funcGenerator.generate(rosettaFunctions, version));
		return result;
	}

}