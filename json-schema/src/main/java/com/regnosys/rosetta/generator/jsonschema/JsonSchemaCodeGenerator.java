package com.regnosys.rosetta.generator.jsonschema;

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
import com.regnosys.rosetta.rosetta.RosettaEnumeration;
import com.regnosys.rosetta.rosetta.RosettaMetaType;
import com.regnosys.rosetta.rosetta.RosettaModel;
import com.regnosys.rosetta.rosetta.simple.Data;

public class JsonSchemaCodeGenerator extends AbstractExternalGenerator {

	@Inject
	private JsonSchemaTypeGenerator typeSchemaGenerator;

	@Inject 
	private JsonSchemaMetaFieldGenerator metaFieldGenerator;

	@Inject
	private JsonSchemaEnumGenerator enumGenerator;
	
	public JsonSchemaCodeGenerator() {
		super("JsonSchema");
	}

	@Override
	public Map<String, ? extends CharSequence> generate(Resource resource, RosettaModel model, String version) {
		return Collections.emptyMap();
	}

	@Override
	public Map<String, ? extends CharSequence> afterAllGenerate(ResourceSet set,
			Collection<? extends RosettaModel> models, String version) {

		List<Data> rosettaData = models.stream().flatMap(m -> m.getElements().stream()).filter((e) -> e instanceof Data)
				.map(Data.class::cast).collect(Collectors.toList());

		List<RosettaMetaType> metaTypes = models.stream().flatMap(m -> m.getElements().stream())
				.filter(RosettaMetaType.class::isInstance).map(RosettaMetaType.class::cast)
				.collect(Collectors.toList());

		List<RosettaEnumeration> rosettaEnums = models.stream().flatMap(m -> m.getElements().stream())
				.filter(RosettaEnumeration.class::isInstance).map(RosettaEnumeration.class::cast)
				.collect(Collectors.toList());

		Map<String, CharSequence> result = new HashMap<>();

		result.putAll(typeSchemaGenerator.generateTypeDefinitions(rosettaData));
		result.putAll(metaFieldGenerator.generateMetaFields(rosettaData, metaTypes));
		result.putAll(enumGenerator.generateEnumDefinitions(rosettaEnums));

		return result;
	}

}
