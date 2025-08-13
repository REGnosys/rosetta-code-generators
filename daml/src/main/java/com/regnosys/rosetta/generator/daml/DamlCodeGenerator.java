package com.regnosys.rosetta.generator.daml;

import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import org.apache.commons.text.WordUtils;
import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;

import com.google.common.collect.HashMultimap;
import com.google.common.collect.Multimap;
import com.google.common.collect.SetMultimap;
import com.google.inject.Inject;
import com.regnosys.rosetta.generator.daml.enums.DamlEnumGenerator;
import com.regnosys.rosetta.generator.daml.functions.DamlFunctionGenerator;
import com.regnosys.rosetta.generator.daml.object.DamlModelObjectGenerator;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;
import com.regnosys.rosetta.rosetta.RosettaEnumeration;
import com.regnosys.rosetta.rosetta.RosettaMetaType;
import com.regnosys.rosetta.rosetta.RosettaModel;
import com.regnosys.rosetta.rosetta.simple.Data;
import com.regnosys.rosetta.rosetta.simple.Function;

public class DamlCodeGenerator extends AbstractExternalGenerator {

	@Inject
	DamlModelObjectGenerator pojoGenerator;
	@Inject
	private DamlEnumGenerator enumGenerator;
	@Inject
	private DamlFunctionGenerator functionGenerator;
	
	private static String CLASSES_DAML="Classes";
	private static String META_FIELDS_DAML="MetaFields";
	private static String META_CLASSES_DAML="MetaClasses";
	private static String ZONED_DATE_TIME_DAML="ZonedDateTime";
	private static String FUNCTION_DAML="Functions";
	private static String ENUM_DAML="Enums";
	

	public DamlCodeGenerator() {
		super("Daml");
		enumGenerator = new DamlEnumGenerator();
	}

	@Override
	public Map<String, ? extends CharSequence> generate(Resource resource, RosettaModel model, String version) {
		return Collections.emptyMap();
	}
	
	
	@Override	
	public Map<String, ? extends CharSequence> afterAllGenerate(ResourceSet set, Collection<? extends RosettaModel> models, String version) {		
		Map<String, CharSequence> result = new HashMap<>();

		List<Data> rosettaClasses = models.stream().flatMap(m->m.getElements().stream()).filter((e)-> e instanceof Data).map(Data.class::cast).collect(Collectors.toList());
		List<RosettaMetaType> metaTypes = models.stream().flatMap(m->m.getElements().stream()).filter(RosettaMetaType.class::isInstance)
				.map(RosettaMetaType.class::cast).collect(Collectors.toList());

		List<RosettaEnumeration> rosettaEnums = models.stream().flatMap(m->m.getElements().stream()).filter(RosettaEnumeration.class::isInstance)
				.map(RosettaEnumeration.class::cast).collect(Collectors.toList());
		
		List<Function> rosettaFunctions = models.stream().flatMap(m->m.getElements().stream()).filter(t -> Function.class.isInstance(t))
				.map(Function.class::cast).collect(Collectors.toList());
		
		
		SetMultimap<String, String> imports = getExistingImports(rosettaClasses, metaTypes, rosettaEnums, rosettaFunctions);
		
		result.putAll(pojoGenerator.generate(rosettaClasses, metaTypes, imports, version));
		result.putAll(enumGenerator.generate(rosettaEnums, version));
		result.putAll(functionGenerator.generate(rosettaFunctions, imports, version));
		return result;
	}
	
	private SetMultimap<String, String> getExistingImports(List<Data> rosettaClasses,List<RosettaMetaType> metaTypes, List<RosettaEnumeration> rosettaEnums, List<Function> rosettaFunctions) {		
		SetMultimap<String, String> results = HashMultimap.create();
		
		rosettaClasses.forEach(rosettaClass -> {
			addToMap(results, rosettaClass.getModel(), CLASSES_DAML);
			addToMap(results, rosettaClass.getModel(), META_CLASSES_DAML);
			addToMap(results, rosettaClass.getModel(), ZONED_DATE_TIME_DAML);
		});
		
		metaTypes.forEach(metaType -> {
			addToMap(results, metaType.getModel(), META_FIELDS_DAML);
		});
		
		rosettaEnums.forEach(rosettaEnum -> {
			addToMap(results, rosettaEnum.getModel(), ENUM_DAML);
		});
		
		rosettaFunctions.forEach(rosettaFunction -> {
			addToMap(results, rosettaFunction.getModel(), FUNCTION_DAML);
		});
		
		return results;
	}
	
	private void addToMap(SetMultimap<String, String> map, RosettaModel rosettaModel, String damlType) {
		map.put(WordUtils.capitalize(rosettaModel.getName(), '.'), generateImport(rosettaModel, damlType));
	}
	
	private String generateImport(RosettaModel rosettaModel, String damlType) {
		String namespace =  Arrays.stream(rosettaModel.getName().split("\\."))
				.map(modelPart -> modelPart.substring(0, 1).toUpperCase() + modelPart.substring(1))
				.collect(Collectors.joining("."));
		
		return "Org.Isda." + namespace + "." + damlType;
	}

}
