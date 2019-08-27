package com.regnosys.rosetta.generator.daml.util;

import com.google.common.html.HtmlEscapers;
import org.apache.commons.lang3.text.WordUtils;
import org.eclipse.xtend2.lib.StringConcatenation;

@SuppressWarnings("all")
public class DamlModelGeneratorUtil {
  public static String fileComment(final String version) {
    CharSequence _comment = DamlModelGeneratorUtil.comment("This file is auto-generated from the ISDA Common Domain Model, do not edit.", "-- |");
    StringConcatenation _builder = new StringConcatenation();
    _builder.append("--   @version ");
    _builder.append(version);
    return (_comment + _builder.toString());
  }
  
  public static CharSequence classComment(final String definition) {
    return DamlModelGeneratorUtil.comment(definition, "-- |");
  }
  
  public static CharSequence methodComment(final String definition) {
    return DamlModelGeneratorUtil.comment(definition, "-- ^");
  }
  
  private static CharSequence comment(final String definition, final String prefix) {
    StringConcatenation _builder = new StringConcatenation();
    {
      if (((definition != null) && (!definition.isEmpty()))) {
        _builder.append(prefix);
        _builder.append(" ");
        String _wrap = DamlModelGeneratorUtil.wrap(DamlModelGeneratorUtil.escape(DamlModelGeneratorUtil.removeNewLinesAndTabs(definition)));
        _builder.append(_wrap);
        _builder.newLineIfNotEmpty();
      }
    }
    return _builder;
  }
  
  private static String removeNewLinesAndTabs(final String definition) {
    return definition.replace("\n", "").replace("\t", "");
  }
  
  private static String escape(final String definition) {
    return HtmlEscapers.htmlEscaper().escape(definition);
  }
  
  private static String wrap(final String definition) {
    return WordUtils.wrap(definition, 53, "\n--   ", false);
  }
  
  public static String replaceTabsWithSpaces(final CharSequence code) {
    return code.toString().replace("\t", "    ");
  }
}
