package com.regnosys.rosetta.generator.daml.object;

import com.regnosys.rosetta.generator.daml.util.DamlModelGeneratorUtil;
import com.regnosys.rosetta.generator.daml.util.DamlTranslator;
import com.regnosys.rosetta.generator.util.Util;
import com.regnosys.rosetta.rosetta.RosettaMetaType;
import java.util.function.Function;
import org.eclipse.xtend2.lib.StringConcatenation;
import org.eclipse.xtext.xbase.lib.Functions.Function1;
import org.eclipse.xtext.xbase.lib.IterableExtensions;
import org.eclipse.xtext.xbase.lib.StringExtensions;

@SuppressWarnings("all")
public class DamlMetaFieldGenerator {
  public CharSequence generateMetaFields(final Iterable<RosettaMetaType> metaTypes, final String version) {
    final Function1<RosettaMetaType, Boolean> _function = (RosettaMetaType it) -> {
      String _name = it.getName();
      return Boolean.valueOf((_name != "reference"));
    };
    return this.metaFields(IterableExtensions.<RosettaMetaType>filter(metaTypes, _function), version);
  }
  
  public CharSequence metaFields(final Iterable<RosettaMetaType> types, final String version) {
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("daml 1.2");
    _builder.newLine();
    _builder.newLine();
    String _fileComment = DamlModelGeneratorUtil.fileComment(version);
    _builder.append(_fileComment);
    _builder.newLineIfNotEmpty();
    _builder.append("module Org.Isda.Cdm.MetaFields");
    _builder.newLine();
    _builder.append("  ");
    _builder.append("( module Org.Isda.Cdm.MetaFields ) where");
    _builder.newLine();
    _builder.newLine();
    _builder.append("data MetaFields = MetaFields with");
    _builder.newLine();
    {
      final Function<RosettaMetaType, String> _function = (RosettaMetaType t) -> {
        return StringExtensions.toFirstLower(t.getName());
      };
      Iterable<RosettaMetaType> _distinctBy = Util.<RosettaMetaType, String>distinctBy(types, _function);
      for(final RosettaMetaType type : _distinctBy) {
        _builder.append("  ");
        String _firstLower = StringExtensions.toFirstLower(type.getName());
        _builder.append(_firstLower, "  ");
        _builder.append(" : Optional ");
        String _damlType = DamlTranslator.toDamlType(type.getType().getName());
        _builder.append(_damlType, "  ");
        _builder.newLineIfNotEmpty();
      }
    }
    _builder.append("    ");
    _builder.append("deriving (Eq, Ord, Show)");
    _builder.newLine();
    _builder.newLine();
    return _builder;
  }
}
