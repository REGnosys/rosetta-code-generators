package com.regnosys.rosetta.generator.c_sharp;

import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import com.google.inject.Inject;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;
import com.regnosys.rosetta.generator.java.RosettaJavaPackages.RootPackage;
import com.regnosys.rosetta.generator.c_sharp.enums.CSharpEnumGenerator;
import com.regnosys.rosetta.generator.c_sharp.object.CSharpCodeInfo;
import com.regnosys.rosetta.generator.c_sharp.object.CSharpModelObjectGenerator;
import com.regnosys.rosetta.rosetta.RosettaEnumeration;
import com.regnosys.rosetta.rosetta.RosettaMetaType;
import com.regnosys.rosetta.rosetta.RosettaModel;
import com.regnosys.rosetta.rosetta.RosettaRootElement;
import com.regnosys.rosetta.rosetta.simple.Data;

public abstract class CSharpCodeGenerator extends AbstractExternalGenerator implements CSharpCodeInfo {
	
	@Inject
	private CSharpModelObjectGenerator pocoGenerator;

	@Inject
	private CSharpEnumGenerator enumGenerator;

	protected CSharpCodeGenerator(int version) {
		super("CSharp" + version);
		enumGenerator = new CSharpEnumGenerator();
	}

	@Override
	public Map<String, ? extends CharSequence> afterGenerate(Collection<? extends RosettaModel> models) {
		String version = models.stream().map(m -> m.getVersion()).findFirst().orElse("No version");

		Map<String, CharSequence> result = new HashMap<>();

		List<Data> rosettaClasses = models.stream().flatMap(m -> m.getElements().stream())
				.filter((e) -> e instanceof Data).map(Data.class::cast).collect(Collectors.toList());
		List<RosettaMetaType> metaTypes = models.stream().flatMap(m -> m.getElements().stream())
				.filter(RosettaMetaType.class::isInstance).map(RosettaMetaType.class::cast)
				.collect(Collectors.toList());

		List<RosettaEnumeration> rosettaEnums = models.stream().flatMap(m -> m.getElements().stream())
				.filter(RosettaEnumeration.class::isInstance).map(RosettaEnumeration.class::cast)
				.collect(Collectors.toList());

		result.putAll(enumGenerator.generate(rosettaEnums, version));
		result.putAll(pocoGenerator.generate(rosettaClasses, metaTypes, version, this));
		return result;
	}

	@Override
	public Map<String, ? extends CharSequence> generate(RootPackage root, List<RosettaRootElement> elements,
			String version) {
		return Collections.emptyMap();
	}
}
