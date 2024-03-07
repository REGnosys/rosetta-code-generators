package com.regnosys.rosetta.generator.python.object

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import com.regnosys.rosetta.generator.python.util.PythonModelGeneratorUtil
import com.regnosys.rosetta.rosetta.RosettaCallableWithArgs
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumValueReference
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaFeature
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.rosetta.expression.ChoiceOperation
import com.regnosys.rosetta.rosetta.expression.ListLiteral
import com.regnosys.rosetta.rosetta.expression.ModifiableBinaryOperation
import com.regnosys.rosetta.rosetta.expression.Necessity
import com.regnosys.rosetta.rosetta.expression.OneOfOperation
import com.regnosys.rosetta.rosetta.expression.RosettaAbsentExpression
import com.regnosys.rosetta.rosetta.expression.RosettaBinaryOperation
import com.regnosys.rosetta.rosetta.expression.RosettaBooleanLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaConditionalExpression
import com.regnosys.rosetta.rosetta.expression.RosettaCountOperation
import com.regnosys.rosetta.rosetta.expression.RosettaExistsExpression
import com.regnosys.rosetta.rosetta.expression.RosettaExpression
import com.regnosys.rosetta.rosetta.expression.RosettaFeatureCall
import com.regnosys.rosetta.rosetta.expression.RosettaImplicitVariable
import com.regnosys.rosetta.rosetta.expression.RosettaIntLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaNumberLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaOnlyElement
import com.regnosys.rosetta.rosetta.expression.RosettaOnlyExistsExpression
import com.regnosys.rosetta.rosetta.expression.RosettaReference
import com.regnosys.rosetta.rosetta.expression.RosettaStringLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaSymbolReference
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Condition
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.simple.impl.FunctionImpl
import java.util.ArrayList
import java.util.Arrays
import java.util.HashMap
import java.util.List
import java.util.Map

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*
import com.regnosys.rosetta.generator.python.expressions.PythonExpressionGenerator

class PythonModelObjectGenerator {

    @Inject extension RosettaExtensions
    @Inject extension PythonModelObjectBoilerPlate

    @Inject
    PythonModelGeneratorUtil utils;
    
    @Inject
    PythonExpressionGenerator expressionGenerator;

    var List<String> importsFound = newArrayList
    var if_cond_blocks = new ArrayList<String>()

    static def toPythonBasicType(ExpandedAttribute attribute) {
        val typename = attribute.type.name;
        switch typename {
            case 'string':
                'str'
            case 'time':
                'datetime.time'
            case 'date':
                'datetime.date'
            case 'dateTime':
                'datetime.datetime'
            case 'zonedDateTime':
                'datetime.datetime'
            case 'number':
                'Decimal'
            case 'boolean':
                'bool'
            case 'int':
                'int'
            case 'calculation',
            case 'productType',
            case 'eventType':
                'str'
            default:
                if (typename === null) {
                    return null;
                }
                else {
                    return attribute.type.model.name + '.' + typename + '.' + typename;
                }
        }
    }

    static def toPythonType(Data c, ExpandedAttribute attribute) throws Exception {
        // var basicType = toPythonBasicType(attribute.type.name);
        var basicType = toPythonBasicType(attribute);
        if (basicType === null) {
            throw new Exception("Attribute type is null for " + attribute.name + " for class " + c.name)
        }
        if (attribute.hasMetas) {
            var helper_class = "Attribute";
            var is_ref = false;
            var is_address = false;
            var is_meta = false;
            for (ExpandedAttribute meta : attribute.getMetas()) {
                val mname = meta.getName();
                if (mname == "reference") { // what about location?!?
                    is_ref = true;
                } else if (mname == "address") {
                    is_address = true;
                } else if (mname == "key" || mname == "id" || mname == "scheme" || mname == "location") {
                    is_meta = true;
                } else {
                    helper_class += "---" + mname + "---";
                }
            }
            if (is_meta) {
                helper_class += "WithMeta";
            }
            if (is_address) {
                helper_class += "WithAddress";
            }
            if (is_ref) {
                helper_class += "WithReference";
            }
            if (is_meta || is_address) {
                helper_class += "[" + basicType + "]";
            }

            basicType = helper_class + " | " + basicType;
        }
        return basicType
    }

    def Map<String, ? extends CharSequence> generate(
        Iterable<Data> rosettaClasses,
        Iterable<RosettaMetaType> metaTypes,
        String version
    ) {
        val result = new HashMap

        for (Data type : rosettaClasses) {
            val model = type.eContainer as RosettaModel
            val classes = type.generateClasses(version).replaceTabsWithSpaces
            result.put(utils.toPyFileName(model.name, type.name), utils.createImports(type.name) + classes)
        }

        result;
    }

    def boolean checkBasicType(ExpandedAttribute attr) {
        val types = Arrays.asList('int', 'str', 'Decimal', 'date', 'datetime', 'datetime.datetime', 'datetime.date', 'datetime.time', 'time',
            'bool', 'number')
        return (attr !== null && attr.toRawType !== null) ? types.contains(attr.toRawType.toString()) : false
    }

    def boolean checkBasicType(String attr) {
        val types = Arrays.asList('int', 'str', 'Decimal', 'date', 'datetime', 'datetime.datetime', 'datetime.date', 'datetime.time', 'time',
            'bool', 'number')
        return types.contains(attr)
    }

    /**
     * Generate the classes
     */
    // TODO remove Date implementation in beginning
    // TODO removed one-of condition due to limitations after instantiation of objects
    private def generateClasses(Data rosettaClass, String version) {
        var List<String> enumImports = newArrayList
        var List<String> dataImports = newArrayList
        var List<String> classDefinitions = newArrayList
        // var List<String> updateForwardRefs = newArrayList
        var superType = rosettaClass.superType
        if (superType !== null && superType.name === null) {
            throw new Exception("SuperType is null for " + rosettaClass.name)
        }
        importsFound = getImportsFromAttributes(rosettaClass)
        expressionGenerator.importsFound = this.importsFound;
        val classDefinition = generateClassDefinition(rosettaClass)
        classDefinitions.add(classDefinition)
        // updateForwardRefs.add('''«rosettaClass.name».update_forward_refs()''')

        // Remove duplicates
        enumImports = enumImports.toSet().toList()
        dataImports = dataImports.toSet().toList()

        // Return generated classes
        return '''
            «IF superType!==null»from «(superType.eContainer as RosettaModel).name».«superType.name» import «superType.name»«ENDIF»
            
            «classDefinition»
            
            import cdm
            «FOR dataImport : importsFound SEPARATOR "\n"»«dataImport»«ENDFOR»
        '''
        //	
        // 	«FOR updateForwardRef : updateForwardRefs SEPARATOR "\n"»«updateForwardRef»«ENDFOR»
        // '''
    }

    private def getImportsFromAttributes(Data rosettaClass) {
        val filteredAttributes = rosettaClass.allExpandedAttributes.filter[enclosingType == rosettaClass.name].filter [
            (it.name !== "reference") && (it.name !== "meta") && (it.name !== "scheme")
        ].filter[!checkBasicType(it)]

        val imports = newArrayList
        for (attribute : filteredAttributes) {
            // val originalIt = attribute
            val model = attribute.type.model
            if (model !== null) {
                // val importStatement = '''from «model.name».«originalIt.toRawType» import «originalIt.toRawType»'''
                val importStatement = '''import «model.name».«attribute.toRawType»'''
                imports.add(importStatement)
            }
        }

        // Remove duplicates by converting the list to a set and back to a list
        return imports.toSet.toList
    }

    private def generateClassDefinition(Data rosettaClass) {
        return '''
            class «rosettaClass.name»«IF rosettaClass.superType === null»«ENDIF»«IF rosettaClass.superType !== null»(«rosettaClass.superType.name»):«ELSE»(BaseDataClass):«ENDIF»
                «IF rosettaClass.definition !== null»
                    """
                    «rosettaClass.definition»
                    """
                «ENDIF»
                «generateAttributes(rosettaClass)»
                «expressionGenerator.generateConditions(rosettaClass)»
        '''
    }
    
    private def generateAttributes(Data c) {
        val attr = c.allExpandedAttributes.filter[enclosingType == c.name].filter [
            (it.name !== "reference") && (it.name !== "meta") && (it.name !== "scheme")
        ]
        val attrSize = attr.size()
        val conditionsSize = c.conditions.size()
        '''«IF attrSize === 0 && conditionsSize===0»pass«ELSE»«FOR attribute : attr SEPARATOR ""»«generateExpandedAttribute(c, attribute)»«ENDFOR»«ENDIF»'''
    }

    private def generateExpandedAttribute(Data c, ExpandedAttribute attribute) {
        var att = ""
        if (attribute.sup > 1 || attribute.unbound) {
            att += "List[" + toPythonType(c, attribute) + "]"
        } else {
            if (attribute.inf == 0) { // edge case (0..0) will come here
                att += "Optional[" + toPythonType(c, attribute) + "]"
            } else {
                att += toPythonType(c, attribute) // cardinality (1..1)
            }
        }

        var field_default = 'None'
        if (attribute.inf == 1 && attribute.sup == 1)
            field_default = '...' // mandatory field -> cardinality (1..1)
        else if (attribute.sup > 1 || attribute.unbound) { // List filed of cardinality (m..n)
            field_default = '[]'
        }

        var attrName        = (attribute.name == "global") ? "_global" : attribute.name
        var need_card_check = !((attribute.inf == 0 && attribute.sup == 1) || 
                                (attribute.inf == 1 && attribute.sup == 1) ||
                                (attribute.inf == 0 && attribute.unbound))


        var sup_str         = (attribute.unbound) ? 'None' : attribute.sup.toString()
         val attrDesc        = (attribute.definition === null) ? '' : attribute.definition.replaceAll('\\s+', ' ')
        '''
            «attrName»: «att» = Field(«field_default», description="«attrDesc»")
            «IF attribute.definition !== null»
                """
                «attribute.definition»
                """
            «ENDIF»
            «IF need_card_check»
                @rosetta_condition
                def cardinality_«attrName»(self):
                    return check_cardinality(self.«attrName», «attribute.inf», «sup_str»)
                
            «ENDIF»
        '''
    }

    def Iterable<ExpandedAttribute> allExpandedAttributes(Data type) {
        type.allSuperTypes.map[it.expandedAttributes].flatten
    }

    def String definition(Data element) {
        element.definition
    }
}
