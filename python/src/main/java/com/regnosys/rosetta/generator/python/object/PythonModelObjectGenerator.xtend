package com.regnosys.rosetta.generator.python.object

import com.google.inject.Inject
import com.regnosys.rosetta.RosettaExtensions
import com.regnosys.rosetta.generator.object.ExpandedAttribute
import com.regnosys.rosetta.generator.python.expressions.PythonExpressionGenerator
import com.regnosys.rosetta.generator.python.util.PythonModelGeneratorUtil
import com.regnosys.rosetta.rosetta.RosettaMetaType
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.generator.python.util.PythonTranslator
import com.regnosys.rosetta.generator.python.util.Util
import java.util.HashMap
import java.util.List
import java.util.Map

import static extension com.regnosys.rosetta.generator.util.RosettaAttributeExtensions.*

class PythonModelObjectGenerator {

    @Inject extension RosettaExtensions
    @Inject extension PythonModelObjectBoilerPlate
    @Inject PythonExpressionGenerator expressionGenerator;

    var List<String> importsFound = newArrayList


    static def toPythonType(Data c, ExpandedAttribute attribute) throws Exception {
        var basicType = PythonTranslator::toPythonType(attribute);
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
                if (mname == "reference") { 
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
        String version) {
        val result = new HashMap

        for (Data type : rosettaClasses) {
            val model = type.eContainer as RosettaModel
            val namespace = Util::getNamespace (model)
            val classes = type.generateClasses(namespace, version).replaceTabsWithSpaces
            result.put(PythonModelGeneratorUtil::toPyFileName(model.name, type.name), PythonModelGeneratorUtil::createImports(type.name) + classes)
        }

        result;
    }

    def boolean checkBasicType(ExpandedAttribute rosettaAttribute) {
        val rosettaType = (rosettaAttribute !== null) ? rosettaAttribute.toRawType : null;
        return (rosettaType !== null && PythonTranslator::checkPythonType (rosettaType.toString()))
    }

    /**
     * Generate the classes
     */
    private def generateClasses(Data rosettaClass, String namespace, String version) {
        var List<String> enumImports = newArrayList
        var List<String> dataImports = newArrayList
        var List<String> classDefinitions = newArrayList
        var superType = rosettaClass.superType
        if (superType !== null && superType.name === null) {
            throw new Exception("SuperType is null for " + rosettaClass.name)
        }
        importsFound = getImportsFromAttributes(rosettaClass)
        expressionGenerator.importsFound = this.importsFound;
        val classDefinition = generateClassDefinition(rosettaClass)
        classDefinitions.add(classDefinition)

        enumImports = enumImports.toSet().toList()
        dataImports = dataImports.toSet().toList()

        return '''
            «IF superType!==null»from «(superType.eContainer as RosettaModel).name».«superType.name» import «superType.name»«ENDIF»
            
            «classDefinition»
            
            import «namespace» 
            «FOR dataImport : importsFound SEPARATOR "\n"»«dataImport»«ENDFOR»
        '''      
    }

    private def getImportsFromAttributes(Data rosettaClass) {
        val filteredAttributes = rosettaClass.allExpandedAttributes.filter[enclosingType == rosettaClass.name].filter [
            (it.name !== "reference") && (it.name !== "meta") && (it.name !== "scheme")
        ].filter[!checkBasicType(it)]

        val imports = newArrayList
        for (attribute : filteredAttributes) {
            val model = attribute.type.model
            if (model !== null) {
                val importStatement = '''import «model.name».«attribute.toRawType»'''
                imports.add(importStatement)
            }
        }

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

<<<<<<< HEAD
        var attrName        = (attribute.name == "global") ? "rosetta_attr_global" : attribute.name
=======
        var attrName        = (attribute.name == "global") ? "_global" : attribute.name
>>>>>>> master
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
