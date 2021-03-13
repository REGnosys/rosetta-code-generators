package com.regnosys.rosetta.generator.kotlin.util;

import com.google.common.base.Objects;
import com.regnosys.rosetta.generator.object.ExpandedType;
import com.regnosys.rosetta.types.RCalculationType;
import com.regnosys.rosetta.types.RQualifiedType;
import org.eclipse.xtend2.lib.StringConcatenation;
import org.eclipse.xtext.xbase.lib.StringExtensions;

@SuppressWarnings("all")
public class KotlinTranslator {
  public static String toKotlinBasicType(final String typename) {
    String _switchResult = null;
    boolean _matched = false;
    if (Objects.equal(typename, "string")) {
      _matched=true;
      _switchResult = "String";
    }
    if (!_matched) {
      if (Objects.equal(typename, "int")) {
        _matched=true;
        _switchResult = "Int";
      }
    }
    if (!_matched) {
      if (Objects.equal(typename, "time")) {
        _matched=true;
        _switchResult = "LocalDateTime";
      }
    }
    if (!_matched) {
      if (Objects.equal(typename, "date")) {
        _matched=true;
        _switchResult = "LocalDate";
      }
    }
    if (!_matched) {
      if (Objects.equal(typename, "dateTime")) {
        _matched=true;
        _switchResult = "LocalDateTime";
      }
    }
    if (!_matched) {
      if (Objects.equal(typename, "zonedDateTime")) {
        _matched=true;
        _switchResult = "LocalDateTime";
      }
    }
    if (!_matched) {
      if (Objects.equal(typename, "number")) {
        _matched=true;
        _switchResult = "Number";
      }
    }
    if (!_matched) {
      if (Objects.equal(typename, "boolean")) {
        _matched=true;
        _switchResult = "Boolean";
      }
    }
    if (!_matched) {
      String _qualifiedType = RQualifiedType.PRODUCT_TYPE.getQualifiedType();
      if (Objects.equal(typename, _qualifiedType)) {
        _matched=true;
        _switchResult = "String";
      }
    }
    if (!_matched) {
      String _qualifiedType_1 = RQualifiedType.EVENT_TYPE.getQualifiedType();
      if (Objects.equal(typename, _qualifiedType_1)) {
        _matched=true;
        _switchResult = "String";
      }
    }
    if (!_matched) {
      String _calculationType = RCalculationType.CALCULATION.getCalculationType();
      if (Objects.equal(typename, _calculationType)) {
        _matched=true;
        _switchResult = "String";
      }
    }
    return _switchResult;
  }
  
  public static String toKotlinType(final ExpandedType type) {
    final String basicType = KotlinTranslator.toKotlinBasicType(type.getName());
    if ((basicType != null)) {
      return basicType;
    } else {
      boolean _isEnumeration = type.isEnumeration();
      if (_isEnumeration) {
        StringConcatenation _builder = new StringConcatenation();
        String _firstUpper = StringExtensions.toFirstUpper(type.getName());
        _builder.append(_firstUpper);
        return _builder.toString();
      } else {
        return StringExtensions.toFirstUpper(type.getName());
      }
    }
  }
}
