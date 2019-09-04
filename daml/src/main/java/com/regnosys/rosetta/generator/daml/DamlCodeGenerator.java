package com.regnosys.rosetta.generator.daml;

import com.google.inject.Inject;
import com.regnosys.rosetta.generator.daml.enums.DamlEnumGenerator;
import com.regnosys.rosetta.generator.daml.object.DamlModelObjectGenerator;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;
import com.regnosys.rosetta.generator.java.RosettaJavaPackages;
import com.regnosys.rosetta.rosetta.RosettaClass;
import com.regnosys.rosetta.rosetta.RosettaEnumeration;
import com.regnosys.rosetta.rosetta.RosettaMetaType;
import com.regnosys.rosetta.rosetta.RosettaRootElement;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class DamlCodeGenerator extends AbstractExternalGenerator {

	@Inject
	DamlModelObjectGenerator pojoGenerator;
	@Inject
	private DamlEnumGenerator enumGenerator;

	public DamlCodeGenerator() {
		super("Daml");
		enumGenerator = new DamlEnumGenerator();
	}

	@Override
	public Map<String, ? extends CharSequence> generate(RosettaJavaPackages packages, List<RosettaRootElement> elements,
			String version) {
		Map<String, CharSequence> result = new HashMap<>();

		List<RosettaClass> rosettaClasses = elements.stream().filter(RosettaClass.class::isInstance)
				.map(RosettaClass.class::cast).collect(Collectors.toList());
		List<RosettaMetaType> metaTypes = elements.stream().filter(RosettaMetaType.class::isInstance)
				.map(RosettaMetaType.class::cast).collect(Collectors.toList());

		List<RosettaEnumeration> rosettaEnums = elements.stream().filter(RosettaEnumeration.class::isInstance)
				.map(RosettaEnumeration.class::cast).collect(Collectors.toList());

		result.putAll(pojoGenerator.generate(rosettaClasses, metaTypes, version));
		result.putAll(enumGenerator.generate(rosettaEnums, version));
		return result;
	}

}
