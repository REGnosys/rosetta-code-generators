package com.regnosys.rosetta.generator.util;

import com.regnosys.rosetta.RosettaEcoreUtil;
import com.regnosys.rosetta.generator.object.ExpandedAttribute;
import com.regnosys.rosetta.generator.object.ExpandedType;
import com.regnosys.rosetta.rosetta.*;
import com.regnosys.rosetta.rosetta.simple.Attribute;
import com.regnosys.rosetta.rosetta.simple.Data;
import com.regnosys.rosetta.scoping.RosettaScopeProvider;

import java.util.*;

/**
 * Note that these methods will add a "meta" attribute if the data type has annotations.
 * Where noted, an instance of RosettaEcoreUtil is created ad-hoc instead of DI.
 *
 * @deprecated since 10.0.0. Use RosettaExtensions instead.
 */
@Deprecated
public class RosettaAttributeExtensions {
    public static boolean cardinalityIsSingleValue(ExpandedAttribute attribute) {
        return attribute.getSup() == 1;
    }

    public static boolean cardinalityIsListValue(ExpandedAttribute attribute) {
        return !cardinalityIsSingleValue(attribute);
    }

    /**
     * Note that these methods will add a "meta" attribute if the data type has annotations
     */
    public static List<ExpandedAttribute> getExpandedAttributes(Data data) {
        List<ExpandedAttribute> result = new ArrayList<>();
        for (Attribute a : data.getAttributes()) {
            result.add(toExpandedAttribute(a));
        }
        result.addAll(additionalAttributes(data));
        return result;
    }

    public static List<ExpandedAttribute> expandedAttributesPlus(Data data) {
        List<ExpandedAttribute> atts = getExpandedAttributes(data);
        if (hasSuperType(data)) {
            List<ExpandedAttribute> attsWithSuper = expandedAttributesPlus(data.getSuperType());
            List<ExpandedAttribute> merged = new ArrayList<>();
            // Override by name if present on this type
            for (ExpandedAttribute s : attsWithSuper) {
                ExpandedAttribute overridden = atts.stream().filter(att -> Objects.equals(att.getName(), s.getName())).findFirst().orElse(null);
                merged.add(overridden != null ? overridden : s);
            }
            for (ExpandedAttribute a : atts) {
                if (!containsByIdentityOrName(merged, a)) merged.add(a);
            }
            return merged;
        }
        return atts;
    }

    private static boolean hasSuperType(Data d) {
        // In Xtend code this was a property "hasSuperType"; emulate it
        return d.getSuperType() != null;
    }

    private static boolean containsByIdentityOrName(List<ExpandedAttribute> list, ExpandedAttribute candidate) {
        for (ExpandedAttribute e : list) {
            if (e == candidate) return true;
            if (Objects.equals(e.getName(), candidate.getName())) return true;
        }
        return false;
    }

    private static List<ExpandedAttribute> additionalAttributes(Data data) {
        List<ExpandedAttribute> res = new ArrayList<>();
        // Can't inject as used in rosetta-translate and daml directly
        RosettaEcoreUtil rosExt = new RosettaEcoreUtil();
        if (rosExt.hasKeyedAnnotation(data)) {
            res.add(new ExpandedAttribute(
                    "meta",
                    data.getName(),
                    provideMetaFieldsType(data),
                    null,
                    false,
                    0,
                    1,
                    false,
                    "",
                    Collections.emptyList(),
                    false,
                    Collections.emptyList()
            ));
        }
        return res;
    }

    public static String METAFIELDS_CLASS_NAME = "MetaFields";

    /**
     * @deprecated since 10.0.0. Template metadata fields are deprecated. Kept for rosetta-translate compatibility.
     */
    @Deprecated
    public static String META_AND_TEMPLATE_FIELDS_CLASS_NAME = "MetaAndTemplateFields";

    // A simple cache keyed by Data identity (these EObjects are identity-stable within a resource)
    private static Map<Data, ExpandedType> META_FIELDS_CACHE = Collections.synchronizedMap(new IdentityHashMap<>());

    private static ExpandedType provideMetaFieldsType(Data data) {
        ExpandedType cached = META_FIELDS_CACHE.get(data);
        if (cached != null) return cached;

        // Build a synthetic type in the lib namespace
        RosettaModel rosModel = RosettaFactory.eINSTANCE.createRosettaModel();
        rosModel.setName(RosettaScopeProvider.LIB_NAMESPACE);

        ExpandedType computed = new ExpandedType(rosModel, METAFIELDS_CLASS_NAME, true, false, false);
        META_FIELDS_CACHE.put(data, computed);
        return computed;
    }

    public static List<ExpandedAttribute> getExpandedAttributes(RosettaEnumeration rosettaEnum) {
        List<ExpandedAttribute> result = new ArrayList<>();
        for (RosettaEnumValue v : rosettaEnum.getEnumValues()) {
            result.add(expandedEnumAttribute(v));
        }
        return result;
    }

    public static ExpandedAttribute expandedEnumAttribute(RosettaEnumValue value) {
        return new ExpandedAttribute(
                value.getName(),
                value.getEnumeration().getName(),
                null,
                null,
                false,
                0,
                0,
                false,
                value.getDefinition(),
                value.getReferences(),
                true,
                Collections.emptyList()
        );
    }

    public static boolean isList(ExpandedAttribute a) {
        return cardinalityIsListValue(a);
    }

    public static ExpandedAttribute toExpandedAttribute(Attribute attr) {
        // Build meta attributes for annotation refs on this attribute
        List<ExpandedAttribute> metas = new ArrayList<>();
        List<com.regnosys.rosetta.rosetta.simple.AnnotationRef> annotations = attr.getAnnotations();
        for (int i = 0; i < annotations.size(); i++) {
            com.regnosys.rosetta.rosetta.simple.AnnotationRef annoRef = annotations.get(i);
            Attribute annoAttr = annoRef.getAttribute();
            if (annoAttr != null && annoAttr.getTypeCall() != null && annoAttr.getTypeCall().getType() != null) {
                metas.add(new ExpandedAttribute(
                        annoAttr.getName(),
                        annoRef.getAnnotation().getName(),
                        toExpandedType(annoAttr.getTypeCall().getType()),
                        annoAttr.getTypeCall(),
                        false,
                        0,
                        1,
                        false,
                        attr.getDefinition(),
                        attr.getReferences(),
                        false,
                        Collections.emptyList()
                ));
            }
        }

        return new ExpandedAttribute(
                attr.getName(),
                ((RosettaType) attr.eContainer()).getName(),
                attr.getTypeCall() != null && attr.getTypeCall().getType() != null ? toExpandedType(attr.getTypeCall().getType()) : null,
                attr.getTypeCall(),
                false,
                attr.getCard().getInf(),
                attr.getCard().getSup(),
                attr.getCard().isUnbounded(),
                attr.getDefinition(),
                attr.getReferences(),
                isEnumeration(attr),
                metas
        );
    }

    public static ExpandedType toExpandedType(RosettaType type) {
        return new ExpandedType(
                type.getModel(),
                type.getName(),
                type instanceof Data,
                type instanceof RosettaEnumeration,
                type instanceof RosettaMetaType
        );
    }

    private static boolean isEnumeration(RosettaTypedFeature a) {
        return a.getTypeCall() != null && a.getTypeCall().getType() instanceof RosettaEnumeration;
    }
}
