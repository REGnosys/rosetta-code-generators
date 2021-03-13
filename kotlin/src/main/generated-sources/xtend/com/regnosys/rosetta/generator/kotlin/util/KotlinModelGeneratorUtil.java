package com.regnosys.rosetta.generator.kotlin.util;

import com.regnosys.rosetta.generator.object.ExpandedAttribute;
import org.eclipse.xtend2.lib.StringConcatenation;

@SuppressWarnings("all")
public class KotlinModelGeneratorUtil {
  public static CharSequence fileComment(final String version) {
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("/**");
    _builder.newLine();
    _builder.append(" ");
    _builder.append("* This file is auto-generated from the ISDA Common Domain Model, do not edit.");
    _builder.newLine();
    _builder.append(" ");
    _builder.append("* Version: ");
    _builder.append(version, " ");
    _builder.newLineIfNotEmpty();
    _builder.append(" ");
    _builder.append("*/");
    _builder.newLine();
    return _builder;
  }
  
  public static CharSequence comment(final String definition) {
    StringConcatenation _builder = new StringConcatenation();
    {
      if (((definition != null) && (!definition.isEmpty()))) {
        _builder.append("// ");
        _builder.append(definition);
        _builder.newLineIfNotEmpty();
      }
    }
    return _builder;
  }
  
  public static CharSequence classComment(final String definition, final Iterable<ExpandedAttribute> attributes) {
    StringConcatenation _builder = new StringConcatenation();
    {
      if (((definition != null) && (!definition.isEmpty()))) {
        _builder.append("/**");
        _builder.newLine();
        _builder.append(" ");
        _builder.append("* ");
        _builder.append(definition, " ");
        _builder.newLineIfNotEmpty();
        _builder.append(" ");
        _builder.append("*");
        _builder.newLine();
        {
          for(final ExpandedAttribute attribute : attributes) {
            _builder.append(" ");
            _builder.append("* @param ");
            String _name = attribute.getName();
            _builder.append(_name, " ");
            _builder.append(" ");
            String _definition = attribute.getDefinition();
            _builder.append(_definition, " ");
            _builder.newLineIfNotEmpty();
          }
        }
        _builder.append(" ");
        _builder.append("*/");
        _builder.newLine();
      }
    }
    return _builder;
  }
}
