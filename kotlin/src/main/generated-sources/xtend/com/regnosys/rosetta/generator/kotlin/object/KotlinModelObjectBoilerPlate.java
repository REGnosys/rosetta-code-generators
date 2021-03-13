package com.regnosys.rosetta.generator.kotlin.object;

import com.google.common.base.Objects;
import com.regnosys.rosetta.generator.kotlin.util.KotlinTranslator;
import com.regnosys.rosetta.generator.object.ExpandedAttribute;
import com.regnosys.rosetta.generator.object.ExpandedType;
import org.eclipse.xtend2.lib.StringConcatenation;
import org.eclipse.xtext.xbase.lib.StringExtensions;

@SuppressWarnings("all")
public class KotlinModelObjectBoilerPlate {
  public CharSequence toAttributeName(final ExpandedAttribute attribute) {
    CharSequence _xifexpression = null;
    String _name = attribute.getName();
    boolean _equals = Objects.equal(_name, "val");
    if (_equals) {
      StringConcatenation _builder = new StringConcatenation();
      _builder.append("val");
      _xifexpression = _builder;
    } else {
      _xifexpression = StringExtensions.toFirstLower(attribute.getName());
    }
    return _xifexpression;
  }
  
  public String replaceTabsWithSpaces(final CharSequence code) {
    return code.toString().replace("\t", "  ");
  }
  
  public CharSequence toEnumAnnotationType(final ExpandedType type) {
    StringConcatenation _builder = new StringConcatenation();
    String _name = type.getName();
    _builder.append(_name);
    return _builder;
  }
  
  public CharSequence toType(final ExpandedAttribute attribute) {
    CharSequence _xifexpression = null;
    boolean _isMultiple = attribute.isMultiple();
    if (_isMultiple) {
      StringConcatenation _builder = new StringConcatenation();
      _builder.append("MutableList<");
      CharSequence _rawType = this.toRawType(attribute);
      _builder.append(_rawType);
      _builder.append(">");
      _xifexpression = _builder;
    } else {
      CharSequence _xifexpression_1 = null;
      boolean _isSingleOptional = attribute.isSingleOptional();
      if (_isSingleOptional) {
        StringConcatenation _builder_1 = new StringConcatenation();
        CharSequence _rawType_1 = this.toRawType(attribute);
        _builder_1.append(_rawType_1);
        _builder_1.append("?");
        _xifexpression_1 = _builder_1;
      } else {
        StringConcatenation _builder_2 = new StringConcatenation();
        CharSequence _rawType_2 = this.toRawType(attribute);
        _builder_2.append(_rawType_2);
        _xifexpression_1 = _builder_2;
      }
      _xifexpression = _xifexpression_1;
    }
    return _xifexpression;
  }
  
  private CharSequence toRawType(final ExpandedAttribute attribute) {
    CharSequence _xifexpression = null;
    boolean _hasMetas = attribute.hasMetas();
    boolean _not = (!_hasMetas);
    if (_not) {
      _xifexpression = KotlinTranslator.toKotlinType(attribute.getType());
    } else {
      CharSequence _xifexpression_1 = null;
      int _refIndex = attribute.refIndex();
      boolean _greaterEqualsThan = (_refIndex >= 0);
      if (_greaterEqualsThan) {
        CharSequence _xifexpression_2 = null;
        boolean _isType = attribute.getType().isType();
        if (_isType) {
          _xifexpression_2 = this.toReferenceWithMetaTypeName(attribute.getType());
        } else {
          _xifexpression_2 = this.toBasicReferenceWithMetaTypeName(attribute.getType());
        }
        _xifexpression_1 = _xifexpression_2;
      } else {
        _xifexpression_1 = this.toFieldWithMetaTypeName(attribute.getType());
      }
      _xifexpression = _xifexpression_1;
    }
    return _xifexpression;
  }
  
  public CharSequence toReferenceWithMetaTypeName(final ExpandedType type) {
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("ReferenceWithMeta");
    String _metaTypeName = KotlinModelObjectBoilerPlate.toMetaTypeName(type);
    _builder.append(_metaTypeName);
    return _builder;
  }
  
  public CharSequence toBasicReferenceWithMetaTypeName(final ExpandedType type) {
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("BasicReferenceWithMeta");
    String _metaTypeName = KotlinModelObjectBoilerPlate.toMetaTypeName(type);
    _builder.append(_metaTypeName);
    return _builder;
  }
  
  public CharSequence toFieldWithMetaTypeName(final ExpandedType type) {
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("FieldWithMeta");
    String _metaTypeName = KotlinModelObjectBoilerPlate.toMetaTypeName(type);
    _builder.append(_metaTypeName);
    return _builder;
  }
  
  public static String toMetaTypeName(final ExpandedType type) {
    final String name = KotlinTranslator.toKotlinType(type);
    boolean _isEnumeration = type.isEnumeration();
    if (_isEnumeration) {
      return name;
    } else {
      boolean _contains = name.contains(".");
      if (_contains) {
        int _lastIndexOf = name.lastIndexOf(".");
        int _plus = (_lastIndexOf + 1);
        return StringExtensions.toFirstUpper(name.substring(_plus));
      }
    }
    return StringExtensions.toFirstUpper(name);
  }
}
