package com.regnosys.rosetta.generator.daml.object;

import com.google.common.base.Objects;
import com.regnosys.rosetta.generator.daml.util.DamlTranslator;
import com.regnosys.rosetta.generator.object.ExpandedAttribute;
import com.regnosys.rosetta.rosetta.RosettaClass;
import com.regnosys.rosetta.rosetta.RosettaType;
import org.eclipse.xtend2.lib.StringConcatenation;
import org.eclipse.xtext.xbase.lib.StringExtensions;

@SuppressWarnings("all")
public class DamlModelObjectBoilerPlate {
  public CharSequence toAttributeName(final ExpandedAttribute attribute) {
    CharSequence _xifexpression = null;
    String _name = attribute.getName();
    boolean _equals = Objects.equal(_name, "type");
    if (_equals) {
      StringConcatenation _builder = new StringConcatenation();
      _builder.append("_type");
      _xifexpression = _builder;
    } else {
      _xifexpression = StringExtensions.toFirstLower(attribute.getName());
    }
    return _xifexpression;
  }
  
  public String replaceTabsWithSpaces(final CharSequence code) {
    return code.toString().replace("\t", "  ");
  }
  
  public CharSequence toType(final ExpandedAttribute attribute) {
    CharSequence _xifexpression = null;
    boolean _isMultiple = attribute.isMultiple();
    if (_isMultiple) {
      StringConcatenation _builder = new StringConcatenation();
      _builder.append("[");
      CharSequence _rawType = this.toRawType(attribute);
      _builder.append(_rawType);
      _builder.append("]");
      _xifexpression = _builder;
    } else {
      _xifexpression = this.prefixSingleOptional(this.wrapSingleMetaInBrackets(this.toRawType(attribute), attribute), attribute);
    }
    return _xifexpression;
  }
  
  private CharSequence toRawType(final ExpandedAttribute attribute) {
    CharSequence _xifexpression = null;
    boolean _hasMetas = attribute.hasMetas();
    boolean _not = (!_hasMetas);
    if (_not) {
      _xifexpression = DamlTranslator.toDamlType(attribute.getTypeName());
    } else {
      CharSequence _xifexpression_1 = null;
      int _refIndex = attribute.refIndex();
      boolean _greaterEqualsThan = (_refIndex >= 0);
      if (_greaterEqualsThan) {
        CharSequence _xifexpression_2 = null;
        RosettaType _type = attribute.getType();
        if ((_type instanceof RosettaClass)) {
          _xifexpression_2 = this.toReferenceWithMetaTypeName(attribute.getTypeName());
        } else {
          _xifexpression_2 = this.toBasicReferenceWithMetaTypeName(attribute.getTypeName());
        }
        _xifexpression_1 = _xifexpression_2;
      } else {
        _xifexpression_1 = this.toFieldWithMetaTypeName(attribute.getTypeName());
      }
      _xifexpression = _xifexpression_1;
    }
    return _xifexpression;
  }
  
  private CharSequence toReferenceWithMetaTypeName(final String type) {
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("ReferenceWithMeta ");
    String _firstUpper = StringExtensions.toFirstUpper(DamlTranslator.toDamlType(type));
    _builder.append(_firstUpper);
    return _builder;
  }
  
  private CharSequence toBasicReferenceWithMetaTypeName(final String type) {
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("BasicReferenceWithMeta ");
    String _firstUpper = StringExtensions.toFirstUpper(DamlTranslator.toDamlType(type));
    _builder.append(_firstUpper);
    return _builder;
  }
  
  private CharSequence toFieldWithMetaTypeName(final String type) {
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("FieldWithMeta ");
    String _firstUpper = StringExtensions.toFirstUpper(DamlTranslator.toDamlType(type));
    _builder.append(_firstUpper);
    return _builder;
  }
  
  private CharSequence prefixSingleOptional(final CharSequence type, final ExpandedAttribute attribute) {
    CharSequence _xifexpression = null;
    boolean _isSingleOptional = attribute.isSingleOptional();
    if (_isSingleOptional) {
      StringConcatenation _builder = new StringConcatenation();
      _builder.append("Optional ");
      _builder.append(type);
      _xifexpression = _builder;
    } else {
      _xifexpression = type;
    }
    return _xifexpression;
  }
  
  private CharSequence wrapSingleMetaInBrackets(final CharSequence type, final ExpandedAttribute attribute) {
    CharSequence _xifexpression = null;
    boolean _hasMetas = attribute.hasMetas();
    if (_hasMetas) {
      StringConcatenation _builder = new StringConcatenation();
      _builder.append("(");
      _builder.append(type);
      _builder.append(")");
      _xifexpression = _builder;
    } else {
      _xifexpression = type;
    }
    return _xifexpression;
  }
}
