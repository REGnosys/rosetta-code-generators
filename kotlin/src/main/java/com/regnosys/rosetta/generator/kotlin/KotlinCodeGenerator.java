package com.regnosys.rosetta.generator.kotlin;

import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;

import com.google.inject.Inject;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;
import com.regnosys.rosetta.generator.kotlin.enums.KotlinEnumGenerator;
import com.regnosys.rosetta.generator.kotlin.object.KotlinModelObjectGenerator;
import com.regnosys.rosetta.rosetta.RosettaEnumeration;
import com.regnosys.rosetta.rosetta.RosettaMetaType;
import com.regnosys.rosetta.rosetta.RosettaModel;
import com.regnosys.rosetta.rosetta.simple.Data;
import com.rosetta.util.DottedPath;

public class KotlinCodeGenerator extends AbstractExternalGenerator {
	
	@Inject
	KotlinModelObjectGenerator pojoGenerator;
	@Inject
	private KotlinEnumGenerator enumGenerator;

	public KotlinCodeGenerator() {
		super("Kotlin");
		enumGenerator = new KotlinEnumGenerator();
	}

	@Override
	public Map<String, ? extends CharSequence> generate(Resource resource, RosettaModel model, String version) {
		return Collections.emptyMap();
	}
	
	@Override	
	public Map<String, ? extends CharSequence> afterAllGenerate(ResourceSet set, Collection<? extends RosettaModel> models, String version) {		
		Map<String, CharSequence> result = new HashMap<>();

		Collection<? extends RosettaModel> supportedModels = models.stream()
				.filter(this::isSupportedModel)
				.toList();
		
		List<Data> rosettaClasses = supportedModels.stream().flatMap(m->m.getElements().stream())
				.filter((e)-> e instanceof Data)
				.map(Data.class::cast).collect(Collectors.toList());
		List<RosettaMetaType> metaTypes = supportedModels.stream().flatMap(m->m.getElements().stream()).filter(RosettaMetaType.class::isInstance)
				.map(RosettaMetaType.class::cast).collect(Collectors.toList());

		List<RosettaEnumeration> rosettaEnums = supportedModels.stream().flatMap(m->m.getElements().stream()).filter(RosettaEnumeration.class::isInstance)
				.map(RosettaEnumeration.class::cast).collect(Collectors.toList());

		result.putAll(pojoGenerator.generate(rosettaClasses, metaTypes, version));
		result.putAll(enumGenerator.generate(rosettaEnums, version));
		return result;
	}
	
	private boolean isSupportedModel(RosettaModel model) {
		DottedPath namespace = DottedPath.splitOnDots(model.getName());
		boolean isFpmlModel = "fpml".equals(namespace.first());
		boolean isIngestOrMappingModel = namespace.stream().anyMatch(element -> element.equals("ingest") || element.equals("mapping"));
		return !isFpmlModel && !isIngestOrMappingModel;
	}
}