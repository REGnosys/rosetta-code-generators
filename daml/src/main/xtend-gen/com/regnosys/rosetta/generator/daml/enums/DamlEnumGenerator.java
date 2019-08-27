package com.regnosys.rosetta.generator.daml.enums;

import com.google.common.collect.Iterables;
import com.google.inject.Inject;
import com.regnosys.rosetta.generator.daml.object.DamlModelObjectBoilerPlate;
import com.regnosys.rosetta.generator.daml.util.DamlModelGeneratorUtil;
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
public class DamlEnumGenerator {
  @Inject
  @Extension
  private DamlModelObjectBoilerPlate _damlModelObjectBoilerPlate;
  
  private static final String FILENAME = "Org/Isda/Cdm/Enums.daml";
  
  public Map<String, ? extends CharSequence> generate(final Iterable<RosettaEnumeration> rosettaEnums, final String version) {
    final HashMap<String, String> result = new HashMap<String, String>();
    final Function1<RosettaEnumeration, String> _function = (RosettaEnumeration it) -> {
      return it.getName();
    };
    final String enums = this._damlModelObjectBoilerPlate.replaceTabsWithSpaces(this.generateEnums(IterableExtensions.<RosettaEnumeration, String>sortBy(rosettaEnums, _function), version));
    result.put(DamlEnumGenerator.FILENAME, enums);
    return result;
  }
  
  public static String toJavaEnumName(final RosettaEnumeration enumeration, final RosettaEnumValue rosettaEnumValue) {
    String _name = enumeration.getName();
    String _plus = (_name + ".");
    String _convertValues = DamlEnumGenerator.convertValues(rosettaEnumValue);
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
    _builder.append("daml 1.2");
    _builder.newLine();
    _builder.newLine();
    String _fileComment = DamlModelGeneratorUtil.fileComment(version);
    _builder.append(_fileComment);
    _builder.newLineIfNotEmpty();
    _builder.append("module Org.Isda.Cdm.Enums");
    _builder.newLine();
    _builder.append("  ");
    _builder.append("( module Org.Isda.Cdm.Enums ) where");
    _builder.newLine();
    _builder.newLine();
    {
      for(final RosettaEnumeration e : enums) {
        final List<RosettaEnumValue> allEnumValues = this.allEnumsValues(e);
        _builder.newLineIfNotEmpty();
        int i = 0;
        _builder.newLineIfNotEmpty();
        CharSequence _classComment = DamlModelGeneratorUtil.classComment(e.getDefinition());
        _builder.append(_classComment);
        _builder.newLineIfNotEmpty();
        _builder.append("data ");
        String _name = e.getName();
        _builder.append(_name);
        _builder.append(" ");
        _builder.newLineIfNotEmpty();
        {
          for(final RosettaEnumValue value : allEnumValues) {
            _builder.append("  ");
            {
              int _plusPlus = i++;
              boolean _lessThan = (_plusPlus < 1);
              if (_lessThan) {
                _builder.append("=");
              } else {
                _builder.append("|");
              }
            }
            _builder.append(" ");
            String _name_1 = e.getName();
            _builder.append(_name_1, "  ");
            _builder.append("_");
            String _convertValues = DamlEnumGenerator.convertValues(value);
            _builder.append(_convertValues, "  ");
            {
              int _size = allEnumValues.size();
              boolean _equals = (_size == 1);
              if (_equals) {
                _builder.append("()");
              }
            }
            _builder.newLineIfNotEmpty();
            _builder.append("  ");
            CharSequence _methodComment = DamlModelGeneratorUtil.methodComment(value.getDefinition());
            _builder.append(_methodComment, "  ");
            _builder.newLineIfNotEmpty();
          }
        }
        _builder.append("    ");
        _builder.append("deriving (Eq, Ord, Show)");
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
  
  public static String convertValues(final RosettaEnumValue enumValue) {
    return DamlEnumGenerator.formatEnumName(enumValue.getName());
  }
  
  public static String formatEnumName(final String name) {
    return name;
  }
}
