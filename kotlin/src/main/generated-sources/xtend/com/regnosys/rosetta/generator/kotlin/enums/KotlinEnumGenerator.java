package com.regnosys.rosetta.generator.kotlin.enums;

import com.google.common.collect.Iterables;
import com.google.inject.Inject;
import com.regnosys.rosetta.generator.java.enums.EnumHelper;
import com.regnosys.rosetta.generator.kotlin.object.KotlinModelObjectBoilerPlate;
import com.regnosys.rosetta.generator.kotlin.util.KotlinModelGeneratorUtil;
import com.regnosys.rosetta.rosetta.RosettaEnumSynonym;
import com.regnosys.rosetta.rosetta.RosettaEnumValue;
import com.regnosys.rosetta.rosetta.RosettaEnumeration;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Consumer;
import org.eclipse.emf.common.util.EList;
import org.eclipse.xtend2.lib.StringConcatenation;
import org.eclipse.xtext.xbase.lib.Extension;
import org.eclipse.xtext.xbase.lib.Functions.Function1;
import org.eclipse.xtext.xbase.lib.IterableExtensions;
import org.eclipse.xtext.xbase.lib.ListExtensions;

@SuppressWarnings("all")
public class KotlinEnumGenerator {
  @Inject
  @Extension
  private KotlinModelObjectBoilerPlate _kotlinModelObjectBoilerPlate;
  
  private final static String FILENAME = "Enums.kt";
  
  public Map<String, ? extends CharSequence> generate(final Iterable<RosettaEnumeration> rosettaEnums, final String version) {
    final HashMap<String, String> result = new HashMap<String, String>();
    final Function1<RosettaEnumeration, String> _function = (RosettaEnumeration it) -> {
      return it.getName();
    };
    final String enums = this._kotlinModelObjectBoilerPlate.replaceTabsWithSpaces(this.generateEnums(IterableExtensions.<RosettaEnumeration, String>sortBy(rosettaEnums, _function), version));
    result.put(KotlinEnumGenerator.FILENAME, enums);
    return result;
  }
  
  public static String toJavaEnumName(final RosettaEnumeration enumeration, final RosettaEnumValue rosettaEnumValue) {
    String _name = enumeration.getName();
    String _plus = (_name + ".");
    String _convertValues = EnumHelper.convertValues(rosettaEnumValue);
    return (_plus + _convertValues);
  }
  
  private List<RosettaEnumValue> allEnumsValues(final RosettaEnumeration enumeration) {
    final ArrayList<RosettaEnumValue> enumValues = new ArrayList<RosettaEnumValue>();
    RosettaEnumeration e = enumeration;
    while ((e != null)) {
      {
        final Consumer<RosettaEnumValue> _function = (RosettaEnumValue it) -> {
          enumValues.add(it);
        };
        e.getEnumValues().forEach(_function);
        e = e.getSuperType();
      }
    }
    final Function1<RosettaEnumValue, String> _function = (RosettaEnumValue it) -> {
      return it.getName();
    };
    return IterableExtensions.<RosettaEnumValue, String>sortBy(enumValues, _function);
  }
  
  private CharSequence generateEnums(final List<RosettaEnumeration> enums, final String version) {
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("                ");
    CharSequence _fileComment = KotlinModelGeneratorUtil.fileComment(version);
    _builder.append(_fileComment, "                ");
    _builder.newLineIfNotEmpty();
    _builder.append("            ");
    _builder.append("package org.isda.cdm");
    _builder.newLine();
    _builder.append("import kotlinx.serialization.*");
    _builder.newLine();
    _builder.append("            ");
    _builder.append("import kotlinx.serialization.json.*");
    _builder.newLine();
    _builder.newLine();
    {
      for(final RosettaEnumeration e : enums) {
        _builder.append("        ");
        final List<RosettaEnumValue> allEnumValues = this.allEnumsValues(e);
        _builder.newLineIfNotEmpty();
        _builder.append("        ");
        CharSequence _comment = KotlinModelGeneratorUtil.comment(e.getDefinition());
        _builder.append(_comment, "        ");
        _builder.newLineIfNotEmpty();
        _builder.append("@Serializable");
        _builder.newLine();
        _builder.append("enum class ");
        String _name = e.getName();
        _builder.append(_name);
        _builder.append(" {");
        _builder.newLineIfNotEmpty();
        {
          boolean _hasElements = false;
          for(final RosettaEnumValue value : allEnumValues) {
            if (!_hasElements) {
              _hasElements = true;
            } else {
              _builder.appendImmediate(",", "\t\t\t\t");
            }
            _builder.append("\t\t\t\t");
            CharSequence _comment_1 = KotlinModelGeneratorUtil.comment(value.getDefinition());
            _builder.append(_comment_1, "\t\t\t\t");
            _builder.newLineIfNotEmpty();
            _builder.append("\t\t\t\t");
            String _convertValues = EnumHelper.convertValues(value);
            _builder.append(_convertValues, "\t\t\t\t");
            _builder.newLineIfNotEmpty();
          }
        }
        _builder.append("}");
        _builder.newLine();
        _builder.newLine();
      }
    }
    return _builder;
  }
  
  public boolean anyValueHasSynonym(final RosettaEnumeration enumeration) {
    final Function1<RosettaEnumValue, EList<RosettaEnumSynonym>> _function = (RosettaEnumValue it) -> {
      return it.getEnumSynonyms();
    };
    int _size = IterableExtensions.size(Iterables.<RosettaEnumSynonym>concat(ListExtensions.<RosettaEnumValue, EList<RosettaEnumSynonym>>map(this.allEnumsValues(enumeration), _function)));
    return (_size > 0);
  }
}
