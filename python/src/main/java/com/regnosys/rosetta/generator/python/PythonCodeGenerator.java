package com.regnosys.rosetta.generator.python;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.concurrent.atomic.AtomicReference;
import java.util.stream.Collectors;

import org.eclipse.emf.ecore.resource.Resource;
import org.eclipse.emf.ecore.resource.ResourceSet;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import com.google.inject.Inject;
import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;
import com.regnosys.rosetta.rosetta.RosettaEnumeration;
import com.regnosys.rosetta.rosetta.RosettaMetaType;
import com.regnosys.rosetta.rosetta.RosettaModel;
import com.regnosys.rosetta.rosetta.simple.Data;
import com.regnosys.rosetta.rosetta.simple.Function;
import com.regnosys.rosetta.generator.python.enums.PythonEnumGenerator;
import com.regnosys.rosetta.generator.python.object.PythonModelObjectGenerator;
import com.regnosys.rosetta.generator.python.func.PythonFunctionGenerator;
import com.regnosys.rosetta.generator.python.util.PythonModelGeneratorUtil;
import com.regnosys.rosetta.generator.python.util.Util;

public class PythonCodeGenerator extends AbstractExternalGenerator {
    private static final Logger LOGGER = LoggerFactory.getLogger(PythonCodeGenerator.class);

    @Inject PythonModelObjectGenerator pojoGenerator;
    @Inject PythonFunctionGenerator funcGenerator;
    @Inject PythonEnumGenerator enumGenerator;

    private List<String> subfolders;
    private AtomicReference<String> previousNamespace;
    private static String namespace;
    public PythonCodeGenerator() {
        super("Python");
    }

    @Override
    public Map<String, ? extends CharSequence> beforeAllGenerate(ResourceSet set,
            Collection<? extends RosettaModel> models, String version) {
        subfolders        = new ArrayList<String>();
        previousNamespace = new AtomicReference<>("");
        namespace         = null;
        return Collections.emptyMap();
    }

    @Override
    public Map<String, ? extends CharSequence> generate(Resource resource, 
                                                        RosettaModel model,
                                                        String version) {
        String cleanVersion = cleanVersion(version);

        Map<String, CharSequence> result = new HashMap<>();

        List<Data> rosettaClasses = model.getElements().stream().filter(e -> e instanceof Data)
                .map(Data.class::cast).collect(Collectors.toList());

        List<RosettaMetaType> metaTypes =
                model.getElements().stream().filter(RosettaMetaType.class::isInstance)
                        .map(RosettaMetaType.class::cast).collect(Collectors.toList());

        List<RosettaEnumeration> rosettaEnums =
                model.getElements().stream().filter(RosettaEnumeration.class::isInstance)
                        .map(RosettaEnumeration.class::cast).collect(Collectors.toList());

        List<Function> rosettaFunctions =
                model.getElements().stream().filter(t -> Function.class.isInstance(t))
                        .map(Function.class::cast).collect(Collectors.toList());

        if (rosettaClasses.size() > 0 ||
            metaTypes.size () > 0 ||
            rosettaEnums.size() > 0 ||
            rosettaFunctions.size() > 0) {
            if (!subfolders.contains(model.getName())) {
                subfolders.add(model.getName());
            }
            if (rosettaFunctions.size()> 0 && !subfolders.contains(model.getName() + ".functions")) {
                subfolders.add(model.getName() + ".functions");
            }
        }

        if (!model.getName().equals(previousNamespace.get())) {
            previousNamespace.set(model.getName());
            LOGGER.debug("processing module: {}", model.getName());
        }
        result.putAll(pojoGenerator.generate(rosettaClasses, metaTypes, cleanVersion));
        result.putAll(enumGenerator.generate(rosettaEnums, cleanVersion));
        result.putAll(funcGenerator.generate(rosettaFunctions, cleanVersion));

        return result;
    }

    private String cleanVersion(String version) {
        String cleanVersion = "0.0.0";
        if (version != null && !version.equals("${project.version}")) {
            String[] versionParts = version.split("\\.");
            if (versionParts.length > 2) {
                String thirdPart = versionParts[2].replaceAll("[^\\d]", "");
                cleanVersion = versionParts[0] + "." + versionParts[1] + "." + thirdPart;
            }
        }
        return cleanVersion;
    }

    @Override
    public Map<String, ? extends CharSequence> afterAllGenerate(ResourceSet set,
                                                                Collection<? extends RosettaModel> models, 
                                                                String version) {
        String cleanVersion = cleanVersion(version);
        Map<String, CharSequence> result = new HashMap<>();

        List<String> workspaces = getWorkspaces(subfolders);
        result.putAll(generateWorkspaces(workspaces, cleanVersion));
        result.putAll(generateInits(subfolders));
        if (namespace == null) {
            Iterator<? extends RosettaModel> iterator = models.iterator();
            if (iterator.hasNext()) {
                namespace = Util.getNamespace(iterator.next());
            }
        }
        if (namespace != null) {
            result.put("pyproject.toml", PythonModelGeneratorUtil.createPYProjectTomlFile(namespace, cleanVersion));
        }
        return result;
    }

    private ArrayList<String> getWorkspaces(List<String> subfolders) {
        ArrayList<String> firstElements = new ArrayList<>();

        for (String subfolder : subfolders) {
            String[] parts = subfolder.split("\\.");
            if (parts.length > 0) {
                if (!firstElements.contains(parts[0]))
                    firstElements.add(parts[0]);
            }
        }

        return firstElements;
    }

    private Map<String, String> generateWorkspaces(List<String> workspaces, String version) {
        Map<String, String> result = new HashMap<>();

        for (String workspace : workspaces) {
            result.put(PythonModelGeneratorUtil.toPyFileName(workspace, "__init__"), PythonModelGeneratorUtil.createTopLevelInitFile(version));
            result.put(PythonModelGeneratorUtil.toPyFileName(workspace, "version"), PythonModelGeneratorUtil.createVersionFile(version));
            result.put(PythonModelGeneratorUtil.toFileName(workspace, "py.typed"), "");
        }

        return result;
    }

    public Map<String, String> generateInits(List<String> subfolders) {
        Map<String, String> result = new HashMap<>();

        for (String subfolder : subfolders) {
            String[] parts = subfolder.split("\\.");
            for (int i = 1; i < parts.length; i++) {
                StringBuilder keyBuilder = new StringBuilder(parts[0]);
                for (int j = 1; j <= i; j++) {
                    keyBuilder.append(".").append(parts[j]);
                }
                String key = PythonModelGeneratorUtil.toPyFileName(keyBuilder.toString(), "__init__");
                result.putIfAbsent(key, " ");
            }
        }

        return result;
    }
}
