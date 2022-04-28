package com.regnosys.rosetta.generator.elm;

import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

import com.google.inject.Inject;
import com.regnosys.rosetta.generator.elm.enums.ElmEnumGenerator;
import com.regnosys.rosetta.generator.elm.functions.ElmFunctionGenerator;
import com.regnosys.rosetta.generator.elm.object.ElmModelObjectGenerator;
import com.regnosys.rosetta.generator.elm.rule.ReportRuleGenerator;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;
import com.regnosys.rosetta.generator.java.RosettaJavaPackages;
import com.regnosys.rosetta.rosetta.RosettaBlueprintReport;
import com.regnosys.rosetta.rosetta.RosettaEnumeration;
import com.regnosys.rosetta.rosetta.RosettaModel;
import com.regnosys.rosetta.rosetta.RosettaNamed;
import com.regnosys.rosetta.rosetta.RosettaRootElement;
import com.regnosys.rosetta.rosetta.simple.Data;
import com.regnosys.rosetta.rosetta.simple.Function;

public class ElmCodeGenerator extends AbstractExternalGenerator {

	@Inject	private ElmModelObjectGenerator pojoGenerator;
	@Inject private ElmEnumGenerator enumGenerator;
	@Inject	private ElmFunctionGenerator functionGenerator;
	@Inject private ReportRuleGenerator reportRuleGenerator;

	public ElmCodeGenerator() {
		super("Golang");
	}

	@Override
	public Map<String, ? extends CharSequence> generate(RosettaJavaPackages packages, List<RosettaRootElement> elements,
			String version) {
		return Collections.emptyMap();
	}
	
	@Override	
	public Map<String, ? extends CharSequence> afterGenerate(Collection<? extends RosettaModel> rosettaModels) {
		
		
		Map<String, CharSequence> result = new HashMap<>();

		
		
		Map<String, List<RosettaModel>> modelsGroupedByNamespace = rosettaModels.stream()
				.collect(Collectors.<RosettaModel, String>groupingBy(x -> x.getName()));
		
		
		for (Map.Entry<String, List<RosettaModel>> entry : modelsGroupedByNamespace.entrySet()) {
			String namespace = entry.getKey();
			List<RosettaModel> models = entry.getValue();
			String version = models.stream().map(m->m.getVersion()).findFirst().orElse("No version");

			List<Data> rosettaClasses = models.stream().flatMap(m->m.getElements().stream())
					.filter((e)-> e instanceof Data)
					.map(Data.class::cast).collect(Collectors.toList());
			

			List<RosettaEnumeration> rosettaEnums = models.stream().flatMap(m->m.getElements().stream())
					.filter(RosettaEnumeration.class::isInstance)
					.map(RosettaEnumeration.class::cast).collect(Collectors.toList());
			
			List<RosettaNamed> rosettaFunctions = models.stream().flatMap(m->m.getElements().stream())
					.filter(t -> Function.class.isInstance(t))
					.map(RosettaNamed.class::cast).collect(Collectors.toList());

			List<RosettaBlueprintReport> rosettaReports = models.stream().flatMap(m->m.getElements().stream())
					.filter(RosettaBlueprintReport.class::isInstance)
					.map(RosettaBlueprintReport.class::cast).collect(Collectors.toList());

			result.putAll(pojoGenerator.generate(namespace, rosettaClasses, version));
			
			// TODO - add these
			 result.putAll(enumGenerator.generate(namespace, rosettaEnums, version));
			 result.putAll(reportRuleGenerator.generate(namespace, rosettaReports, rosettaClasses, rosettaEnums, version));
			 
			 
			// result.putAll(functionGenerator.generate(namespace, rosettaFunctions, version));
		}
		
		result.put("Com/Rosetta/Model/Type.elm", 
				"module Com.Rosetta.Model.Type exposing (..)"
				+ "\n"
				+ "import Morphir.SDK.LocalTime exposing (LocalTime)\n"
				+ "\n"
				+ "type alias Date =\n"
				+ "    { day : Int\n"
				+ "    , month : Int\n"
				+ "    , year : Int\n"
				+ "    }\n"
				+ "\n"
				+ "type alias ZonedDateTime =\n"
				+ "    { date : Date\n"
				+ "    , time : LocalTime\n"
				+ "    , timezone : String\n"
				+ "    }");
		

		return result;
	}

}
