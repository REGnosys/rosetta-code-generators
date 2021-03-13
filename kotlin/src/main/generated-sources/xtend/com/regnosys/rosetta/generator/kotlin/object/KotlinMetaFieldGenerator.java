package com.regnosys.rosetta.generator.kotlin.object;

import com.google.common.base.Objects;
import com.regnosys.rosetta.generator.kotlin.object.KotlinModelObjectBoilerPlate;
import com.regnosys.rosetta.generator.kotlin.util.KotlinModelGeneratorUtil;
import com.regnosys.rosetta.generator.kotlin.util.KotlinTranslator;
import com.regnosys.rosetta.generator.object.ExpandedAttribute;
import com.regnosys.rosetta.generator.object.ExpandedType;
import com.regnosys.rosetta.generator.util.RosettaAttributeExtensions;
import com.regnosys.rosetta.generator.util.Util;
import com.regnosys.rosetta.rosetta.RosettaMetaType;
import com.regnosys.rosetta.rosetta.simple.Data;
import java.util.List;
import java.util.Set;
import java.util.function.Function;
import org.eclipse.xtend2.lib.StringConcatenation;
import org.eclipse.xtext.xbase.lib.Functions.Function1;
import org.eclipse.xtext.xbase.lib.IterableExtensions;
import org.eclipse.xtext.xbase.lib.StringExtensions;

@SuppressWarnings("all")
public class KotlinMetaFieldGenerator {
  public String generateMetaFields(final List<Data> rosettaClasses, final Iterable<RosettaMetaType> metaTypes, final String version) {
    final String metaFieldsImports = this.generateMetaFieldsImports().toString();
    final Function1<Data, List<ExpandedAttribute>> _function = (Data it) -> {
      return RosettaAttributeExtensions.getExpandedAttributes(it);
    };
    final Function1<ExpandedAttribute, Boolean> _function_1 = (ExpandedAttribute it) -> {
      return Boolean.valueOf((it.hasMetas() && IterableExtensions.<ExpandedAttribute>exists(it.getMetas(), ((Function1<ExpandedAttribute, Boolean>) (ExpandedAttribute it_1) -> {
        String _name = it_1.getName();
        return Boolean.valueOf(Objects.equal(_name, "reference"));
      }))));
    };
    final Function1<ExpandedAttribute, ExpandedType> _function_2 = (ExpandedAttribute it) -> {
      return it.getType();
    };
    final Set<ExpandedType> refs = IterableExtensions.<ExpandedType>toSet(IterableExtensions.<ExpandedAttribute, ExpandedType>map(IterableExtensions.<ExpandedAttribute>filter(IterableExtensions.<Data, ExpandedAttribute>flatMap(rosettaClasses, _function), _function_1), _function_2));
    String referenceWithMeta = "";
    for (final ExpandedType ref : refs) {
      boolean _isType = ref.isType();
      if (_isType) {
        String _referenceWithMeta = referenceWithMeta;
        String _string = this.generateReferenceWithMeta(ref).toString();
        referenceWithMeta = (_referenceWithMeta + _string);
      } else {
        String _referenceWithMeta_1 = referenceWithMeta;
        String _string_1 = this.generateBasicReferenceWithMeta(ref).toString();
        referenceWithMeta = (_referenceWithMeta_1 + _string_1);
      }
    }
    final Function1<Data, List<ExpandedAttribute>> _function_3 = (Data it) -> {
      return RosettaAttributeExtensions.getExpandedAttributes(it);
    };
    final Function1<ExpandedAttribute, Boolean> _function_4 = (ExpandedAttribute it) -> {
      return Boolean.valueOf((it.hasMetas() && (!IterableExtensions.<ExpandedAttribute>exists(it.getMetas(), ((Function1<ExpandedAttribute, Boolean>) (ExpandedAttribute it_1) -> {
        String _name = it_1.getName();
        return Boolean.valueOf(Objects.equal(_name, "reference"));
      })))));
    };
    final Function1<ExpandedAttribute, ExpandedType> _function_5 = (ExpandedAttribute it) -> {
      return it.getType();
    };
    final Set<ExpandedType> metas = IterableExtensions.<ExpandedType>toSet(IterableExtensions.<ExpandedAttribute, ExpandedType>map(IterableExtensions.<ExpandedAttribute>filter(IterableExtensions.<Data, ExpandedAttribute>flatMap(rosettaClasses, _function_3), _function_4), _function_5));
    for (final ExpandedType meta : metas) {
      String _referenceWithMeta_2 = referenceWithMeta;
      String _string_2 = this.generateFieldWithMeta(meta).toString();
      referenceWithMeta = (_referenceWithMeta_2 + _string_2);
    }
    final Function1<RosettaMetaType, Boolean> _function_6 = (RosettaMetaType t) -> {
      return Boolean.valueOf(((!Objects.equal(t.getName(), "id")) && (!Objects.equal(t.getName(), "reference"))));
    };
    final CharSequence metaFields = this.genMetaFields(IterableExtensions.<RosettaMetaType>filter(metaTypes, _function_6), version);
    CharSequence _fileComment = KotlinModelGeneratorUtil.fileComment(version);
    String _plus = (_fileComment + metaFieldsImports);
    String _plus_1 = (_plus + referenceWithMeta);
    return (_plus_1 + metaFields);
  }
  
  private CharSequence generateMetaFieldsImports() {
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("            ");
    _builder.append("package org.isda.cdm.metafields");
    _builder.newLine();
    _builder.newLine();
    _builder.append("import kotlinx.serialization.*");
    _builder.newLine();
    _builder.append("            ");
    _builder.append("import kotlinx.serialization.json.*");
    _builder.newLine();
    _builder.newLine();
    _builder.append("            ");
    _builder.append("import org.isda.cdm.*");
    _builder.newLine();
    _builder.newLine();
    return _builder;
  }
  
  private CharSequence generateFieldWithMeta(final ExpandedType type) {
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("@Serializable");
    _builder.newLine();
    _builder.append("open class FieldWithMeta");
    String _metaTypeName = KotlinModelObjectBoilerPlate.toMetaTypeName(type);
    _builder.append(_metaTypeName);
    _builder.append("(");
    CharSequence _generateAttribute = this.generateAttribute(type);
    _builder.append(_generateAttribute);
    _builder.append(",");
    _builder.newLineIfNotEmpty();
    _builder.append("meta: MetaFields?) {}");
    _builder.newLine();
    _builder.newLine();
    return _builder;
  }
  
  private CharSequence generateAttribute(final ExpandedType type) {
    CharSequence _xifexpression = null;
    boolean _isEnumeration = type.isEnumeration();
    if (_isEnumeration) {
      StringConcatenation _builder = new StringConcatenation();
      _builder.append("value: ");
      String _kotlinType = KotlinTranslator.toKotlinType(type);
      _builder.append(_kotlinType);
      _builder.append("?");
      _xifexpression = _builder;
    } else {
      StringConcatenation _builder_1 = new StringConcatenation();
      _builder_1.append("value: ");
      String _kotlinType_1 = KotlinTranslator.toKotlinType(type);
      _builder_1.append(_kotlinType_1);
      _builder_1.append("?");
      _xifexpression = _builder_1;
    }
    return _xifexpression;
  }
  
  private CharSequence generateReferenceWithMeta(final ExpandedType type) {
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("@Serializable");
    _builder.newLine();
    _builder.append("open class ReferenceWithMeta");
    String _metaTypeName = KotlinModelObjectBoilerPlate.toMetaTypeName(type);
    _builder.append(_metaTypeName);
    _builder.append("(value: ");
    String _kotlinType = KotlinTranslator.toKotlinType(type);
    _builder.append(_kotlinType);
    _builder.append("?,");
    _builder.newLineIfNotEmpty();
    _builder.append("globalReference: String?,");
    _builder.newLine();
    _builder.append("externalReference: String?) {}");
    _builder.newLine();
    _builder.newLine();
    return _builder;
  }
  
  private CharSequence generateBasicReferenceWithMeta(final ExpandedType type) {
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("@Serializable");
    _builder.newLine();
    _builder.append("open class BasicReferenceWithMeta");
    String _metaTypeName = KotlinModelObjectBoilerPlate.toMetaTypeName(type);
    _builder.append(_metaTypeName);
    _builder.append("(value: ");
    String _kotlinType = KotlinTranslator.toKotlinType(type);
    _builder.append(_kotlinType);
    _builder.append("?,");
    _builder.newLineIfNotEmpty();
    _builder.append("globalReference: String?,");
    _builder.newLine();
    _builder.append("externalReference: String?) {}");
    _builder.newLine();
    _builder.newLine();
    return _builder;
  }
  
  private CharSequence genMetaFields(final Iterable<RosettaMetaType> types, final String version) {
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("@Serializable");
    _builder.newLine();
    _builder.append("open class MetaFields(");
    {
      final Function<RosettaMetaType, String> _function = (RosettaMetaType t) -> {
        return StringExtensions.toFirstLower(t.getName());
      };
      Iterable<RosettaMetaType> _distinctBy = Util.<RosettaMetaType, String>distinctBy(types, _function);
      boolean _hasElements = false;
      for(final RosettaMetaType type : _distinctBy) {
        if (!_hasElements) {
          _hasElements = true;
        } else {
          _builder.appendImmediate("\n\t\t", "");
        }
        String _firstLower = StringExtensions.toFirstLower(type.getName());
        _builder.append(_firstLower);
        _builder.append(": ");
        String _kotlinBasicType = KotlinTranslator.toKotlinBasicType(type.getType().getName());
        _builder.append(_kotlinBasicType);
        _builder.append("?,");
      }
    }
    _builder.newLineIfNotEmpty();
    _builder.append("globalKey: String?,");
    _builder.newLine();
    _builder.append("externalKey: String?) {}");
    _builder.newLine();
    _builder.newLine();
    return _builder;
  }
}
