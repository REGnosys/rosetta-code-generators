package com.regnosys.rosetta.generator.daml.object;

import com.google.inject.Inject;
import com.regnosys.rosetta.RosettaExtensions;
import com.regnosys.rosetta.generator.daml.object.DamlMetaFieldGenerator;
import com.regnosys.rosetta.generator.daml.object.DamlModelObjectBoilerPlate;
import com.regnosys.rosetta.generator.daml.util.DamlModelGeneratorUtil;
import com.regnosys.rosetta.generator.object.ExpandedAttribute;
import com.regnosys.rosetta.generator.util.RosettaAttributeExtensions;
import com.regnosys.rosetta.rosetta.RosettaClass;
import com.regnosys.rosetta.rosetta.RosettaMetaType;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.eclipse.xtend2.lib.StringConcatenation;
import org.eclipse.xtext.xbase.lib.Extension;
import org.eclipse.xtext.xbase.lib.Functions.Function1;
import org.eclipse.xtext.xbase.lib.InputOutput;
import org.eclipse.xtext.xbase.lib.IterableExtensions;

@SuppressWarnings("all")
public class DamlModelObjectGenerator {
  @Inject
  @Extension
  private RosettaExtensions _rosettaExtensions;
  
  @Inject
  @Extension
  private DamlModelObjectBoilerPlate _damlModelObjectBoilerPlate;
  
  @Inject
  @Extension
  private DamlMetaFieldGenerator _damlMetaFieldGenerator;
  
  private static final String CLASSES_FILENAME = "Org/Isda/Cdm/Classes.daml";
  
  private static final String META_FIELDS_FILENAME = "Org/Isda/Cdm/MetaFields.daml";
  
  public Map<String, ? extends CharSequence> generate(final Iterable<RosettaClass> rosettaClasses, final Iterable<RosettaMetaType> metaTypes, final String version) {
    HashMap<String, String> _xblockexpression = null;
    {
      final HashMap<String, String> result = new HashMap<String, String>();
      final Function1<RosettaClass, String> _function = (RosettaClass it) -> {
        return it.getName();
      };
      final String classes = this._damlModelObjectBoilerPlate.replaceTabsWithSpaces(this.generateClasses(IterableExtensions.<RosettaClass, String>sortBy(rosettaClasses, _function), version));
      result.put(DamlModelObjectGenerator.CLASSES_FILENAME, classes);
      final String metaFields = this._damlModelObjectBoilerPlate.replaceTabsWithSpaces(this._damlMetaFieldGenerator.generateMetaFields(metaTypes, version));
      result.put(DamlModelObjectGenerator.META_FIELDS_FILENAME, metaFields);
      _xblockexpression = result;
    }
    return _xblockexpression;
  }
  
  /**
   * DAML requires:
   * - tabs not spaces
   * - keyword "deriving" should in indented as additional 2 spaces
   * - class name and folders in title case
   * - must contain "import Prelude hiding (...)" line to avoid name clashes with DAML keywords
   * - nullable fields must be declared with the keyword "Optional"
   */
  private CharSequence generateClasses(final List<RosettaClass> rosettaClasses, final String version) {
    CharSequence _xblockexpression = null;
    {
      final RosettaClass classz = rosettaClasses.get(0);
      final Set<RosettaClass> p = this._rosettaExtensions.getAllSuperTypes(classz);
      InputOutput.<Set<RosettaClass>>println(p);
      StringConcatenation _builder = new StringConcatenation();
      _builder.append("daml 1.2");
      _builder.newLine();
      _builder.newLine();
      String _fileComment = DamlModelGeneratorUtil.fileComment(version);
      _builder.append(_fileComment);
      _builder.newLineIfNotEmpty();
      _builder.append("module Org.Isda.Cdm.Classes");
      _builder.newLine();
      _builder.append("  ");
      _builder.append("( module Org.Isda.Cdm.Classes ) where");
      _builder.newLine();
      _builder.newLine();
      _builder.append("import Org.Isda.Cdm.Enums");
      _builder.newLine();
      _builder.append("import Org.Isda.Cdm.ZonedDateTime");
      _builder.newLine();
      _builder.append("import Org.Isda.Cdm.MetaClasses");
      _builder.newLine();
      _builder.append("import Org.Isda.Cdm.MetaFields");
      _builder.newLine();
      _builder.append("import Prelude hiding (Party, exercise, id, product, agreement)");
      _builder.newLine();
      _builder.newLine();
      {
        for(final RosettaClass c : rosettaClasses) {
          CharSequence _classComment = DamlModelGeneratorUtil.classComment(c.getDefinition());
          _builder.append(_classComment);
          _builder.newLineIfNotEmpty();
          _builder.append("data ");
          String _name = c.getName();
          _builder.append(_name);
          _builder.append(" = ");
          String _name_1 = c.getName();
          _builder.append(_name_1);
          _builder.append(" with ");
          _builder.newLineIfNotEmpty();
          {
            List<ExpandedAttribute> _expandedAttributes = RosettaAttributeExtensions.getExpandedAttributes(this._rosettaExtensions.getAllSuperTypes(c));
            for(final ExpandedAttribute attribute : _expandedAttributes) {
              _builder.append("  ");
              CharSequence _attributeName = this._damlModelObjectBoilerPlate.toAttributeName(attribute);
              _builder.append(_attributeName, "  ");
              _builder.append(" : ");
              CharSequence _type = this._damlModelObjectBoilerPlate.toType(attribute);
              _builder.append(_type, "  ");
              _builder.newLineIfNotEmpty();
              _builder.append("  ");
              _builder.append("  ");
              CharSequence _methodComment = DamlModelGeneratorUtil.methodComment(attribute.getDefinition());
              _builder.append(_methodComment, "    ");
              _builder.newLineIfNotEmpty();
            }
          }
          _builder.append("    ");
          _builder.append("deriving (Eq, Ord, Show)");
          _builder.newLine();
          _builder.newLine();
        }
      }
      _xblockexpression = _builder;
    }
    return _xblockexpression;
  }
}
