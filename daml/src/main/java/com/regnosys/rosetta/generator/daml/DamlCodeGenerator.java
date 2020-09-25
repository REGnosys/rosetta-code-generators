package com.regnosys.rosetta.generator.daml;

import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import com.google.inject.Inject;
import com.regnosys.rosetta.generator.daml.enums.DamlEnumGenerator;
import com.regnosys.rosetta.generator.daml.functions.DamlFunctionGenerator;
import com.regnosys.rosetta.generator.daml.object.DamlModelObjectGenerator;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;
import com.regnosys.rosetta.generator.java.RosettaJavaPackages;
import com.regnosys.rosetta.rosetta.RosettaEnumeration;
import com.regnosys.rosetta.rosetta.RosettaMetaType;
import com.regnosys.rosetta.rosetta.RosettaModel;
import com.regnosys.rosetta.rosetta.RosettaNamed;
import com.regnosys.rosetta.rosetta.RosettaRootElement;
import com.regnosys.rosetta.rosetta.simple.Data;
import com.regnosys.rosetta.rosetta.simple.Function;

public class DamlCodeGenerator extends AbstractExternalGenerator {

	@Inject
	DamlModelObjectGenerator pojoGenerator;
	@Inject
	private DamlEnumGenerator enumGenerator;
	@Inject
	private DamlFunctionGenerator functionGenerator;

	public DamlCodeGenerator() {
		super("Daml");
		enumGenerator = new DamlEnumGenerator();
	}

	@Override
	public Map<String, ? extends CharSequence> generate(RosettaJavaPackages packages, List<RosettaRootElement> elements,
			String version) {
		return Collections.emptyMap();
	}
	
	
	@Override	
	public Map<String, ? extends CharSequence> afterGenerate(Collection<? extends RosettaModel> models) {
		String version = models.stream().map(m->m.getVersion()).findFirst().orElse("No version");
		
		Map<String, CharSequence> result = new HashMap<>();

		List<Data> rosettaClasses = models.stream().flatMap(m->m.getElements().stream()).filter((e)-> e instanceof Data).map(Data.class::cast).collect(Collectors.toList());
		List<RosettaMetaType> metaTypes = models.stream().flatMap(m->m.getElements().stream()).filter(RosettaMetaType.class::isInstance)
				.map(RosettaMetaType.class::cast).collect(Collectors.toList());

		List<RosettaEnumeration> rosettaEnums = models.stream().flatMap(m->m.getElements().stream()).filter(RosettaEnumeration.class::isInstance)
				.map(RosettaEnumeration.class::cast).collect(Collectors.toList());
		
		List<RosettaNamed> rosettaFunctions = models.stream().flatMap(m->m.getElements().stream()).filter(t -> Function.class.isInstance(t))
				.map(RosettaNamed.class::cast).collect(Collectors.toList());

		result.putAll(pojoGenerator.generate(rosettaClasses, metaTypes, version));
		result.putAll(enumGenerator.generate(rosettaEnums, version));
		result.putAll(functionGenerator.generate(rosettaFunctions, version));
		return result;
	}

}
