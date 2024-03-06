package com.regnosys.rosetta.generator.python.func

import com.google.inject.Inject
import com.regnosys.rosetta.generator.python.expressions.PythonExpressionGenerator
import com.regnosys.rosetta.generator.python.util.PythonModelGeneratorUtil
import com.regnosys.rosetta.generator.python.util.PythonTranslator
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.simple.Function
import com.regnosys.rosetta.rosetta.simple.Operation
import com.regnosys.rosetta.rosetta.simple.Segment
import com.regnosys.rosetta.rosetta.simple.ShortcutDeclaration
import java.util.HashMap
import java.util.List
import java.util.Map
import org.eclipse.emf.ecore.EObject
import org.slf4j.Logger
import org.slf4j.LoggerFactory
import java.util.Set
import com.regnosys.rosetta.rosetta.simple.AssignPathRoot
import java.util.Collections

class  PythonFunctionGenerator {
    
    static final Logger LOGGER = LoggerFactory.getLogger(PythonFunctionGenerator);
    var List<String> importsFound = newArrayList
    @Inject PythonModelGeneratorUtil utils;
    @Inject FunctionDependencyProvider functionDependencyProvider
    @Inject PythonExpressionGenerator expressionGenerator;
    
    def Map<String, ? extends CharSequence> generate(List<Function> rosettaFunctions, String version) {
        val result = new HashMap
        
        if(rosettaFunctions.size()>0){
            for(Function func: rosettaFunctions){
                val tr = func.eContainer as RosettaModel
                val namespace = tr.name
                try{
                    val funcs = func.generateFunctions(version)			
                    result.put(utils.toPyFunctionFileName(namespace, func.name), 
                        utils.createImportsFunc(func.name) + funcs)
                }
                catch(Exception ex){
                    LOGGER.error("Exception occurred generating func {}", func.name, ex)	
                }		
            } 
        }
        return result
    }

    private def generateFunctions(Function function,String version) {
        // importsFound = getImportsFromAttributes(function)
        // //var List<String> updateForwardRefs = newArrayList
        // //updateForwardRefs.add('''«function.name».update_forward_refs()''')
        
        // '''
        // «generatesBody(function)»
        
        // «FOR dataImport : importsFound SEPARATOR "\n"»«dataImport»«ENDFOR»
                    
        // '''	
        val dependencies = collectFunctionDependencies(function);

        '''
        «generateImports(dependencies, function)»
        
        
        @replaceable
        def «function.name»«generatesInputs(function)»:
            «generateDescription(function)»
            self = inspect.currentframe()
            
            «generateConditions(function)»
            
        «generateIfBlocks(function)»
            «generateAlias(function)»
            «generateOperations(function)»
            «generatesOutput(function)»
        '''
    }
    
    private def generateImports(Iterable<EObject> dependencies, Function function) {
        val imports = new StringBuilder();

        for (EObject dependency : dependencies) {
            // Assuming a simple mapping from class names to import paths
            // This mapping needs to be defined based on your project structure
            val tr = dependency.eContainer as RosettaModel
            val importPath = tr.name;
            if(dependency instanceof Function){
                imports.append("from ").append(importPath).append(".functions.").append(dependency.name).append(" import ").append(dependency.name).append("\n");
            }else if(dependency instanceof RosettaEnumeration){
                imports.append("from ").append(importPath).append(".").append(dependency.name).append(" import ").append(dependency.name).append("\n");      	
            }
            else if(dependency instanceof Data){
                imports.append("from ").append(importPath).append(".").append(dependency.name).append(" import ").append(dependency.name).append("\n");      	
            }
        }
        imports.append("\n")
        imports.append('''__all__ = [«"'"+function.name+"'"»]''')

        return imports.toString();
    }
    
    private def generatesOutput(Function function) {
        val output = function.output
        if(output!==null){
            '''
            «IF function.operations.size==0 && function.getShortcuts().size==0»
                «output.name» = _resolve_rosetta_attr(self, "«output.name»")
            «ENDIF»
            
            «generatePostConditions(function)»
            
            return «output.name»
            '''
        }	
    }
    
    private def generatesInputs(Function function) {
        val inputs = function.inputs
        val output = function.output
    
        var result = "("
        for (input : inputs) {
            val typeName = input.getTypeCall().getType().getName()
            val type = input.getCard().sup == 0 ? 
                            "list[" + PythonTranslator.toPythonBasicType(typeName) + "]" : 
                            PythonTranslator.toPythonBasicType(typeName)  // Adding List[type] if card.sup > 1
            result += input.getName() + ": " + type
            if (input.getCard().inf == 0)  // Check for optional parameter
                result += " | None"
            if (inputs.indexOf(input) < inputs.size() - 1)
                result += ", "
        }
        result += ") -> "
        if (output !== null)
            result += PythonTranslator.toPythonBasicType(output.getTypeCall().getType().getName())  // Append the return type of the function
        else
            result += "None"  // Default to 'None' if output is null
        '''«result»'''
    }
    
    private def generateDescription(Function function) {
        val inputs = function.inputs
        val output = function.output
        val description = function.getDefinition()
        
        return
        '''
        """
        «description»
        
        Parameters 
        ----------
        «FOR input : inputs SEPARATOR '\n'»
            «input.getName» : «input.getTypeCall().getType().getName()»
            «input.getDefinition()»
        «ENDFOR»
        
        Returns
        -------
        «IF output !== null»
            «output.getName()» : «output.getTypeCall().getType().getName()»
        «ELSE»
        No Return
        «ENDIF»
        
        """
        '''
    }
    
    private def collectFunctionDependencies(Function func) {
        val Set<EObject> dependencies = newHashSet()
    
        // Add dependencies from shortcuts and operations
        func.shortcuts.forEach[shortcut |
            dependencies.addAll(functionDependencyProvider.findDependencies(shortcut.expression))
        ]
        func.operations.forEach[operation |
            dependencies.addAll(functionDependencyProvider.findDependencies(operation.expression))
        ]
    
        // Add dependencies from conditions and post conditions
        (func.conditions + func.postConditions).forEach[condition |
            dependencies.addAll(functionDependencyProvider.findDependencies(condition.expression))
        ]
    
        // Add dependencies from input types
        func.inputs.forEach[input |
            if (input.getTypeCall()?.getType() !== null) {
                dependencies.add(input.getTypeCall().getType())
            }
        ]
    
        // Add dependency from output type if it exists
        if (func.output?.getTypeCall()?.getType() !== null) {
            dependencies.add(func.output.getTypeCall().getType())
        }
    
        return dependencies
    }

    private def generateIfBlocks(Function function) {
        val levelList = newArrayList(0) // List with a single element initialized to 0
    
        ''' 
        «FOR shortcut : function.shortcuts »
            «expressionGenerator.generateExpressionThenElse(shortcut.expression, levelList)»
        «ENDFOR»
        «FOR opeartion : function.operations »
            «expressionGenerator.generateExpressionThenElse(opeartion.expression, levelList)»
        «ENDFOR»
        '''
    }
    
    private def generateConditions(Function function) {
        '''     
        «IF function.conditions.size>0»
        # conditions
        «expressionGenerator.generateConditions(function.conditions)»
        # Execute all registered conditions
        execute_conditions(self)
        «ENDIF»
        '''
    }
    
    private def generatePostConditions(Function function) {	
        '''     
        «IF function.postConditions.size>0»
        # post-conditions
            «expressionGenerator.generatePostConditions(function.postConditions)»
        # Execute all registered post-conditions
        execute_post_conditions(self)
        «ENDIF»
        '''
    }
    
    private def generateAlias(Function function) {
        val lineSeparator = System.getProperty("line.separator")
        var result = new StringBuilder()
        var level = 0
    
        for (shortcut : function.shortcuts) {
            expressionGenerator.if_cond_blocks = new ArrayList<String>();	    	
            val expression = expressionGenerator.generateExpression(shortcut.expression, level);
            val if_cond_blocks = expressionGenerator.if_cond_blocks;
            val isEmpty = if_cond_blocks.isEmpty();
            if (!isEmpty) {
                level += 1
            }
            result.append('''«shortcut.name» = «expression»''' + lineSeparator)
        }
    
        return result.toString()
    }

    private def generateOperations(Function function) {  
        val lineSeparator = System.getProperty("line.separator")
        var result = new StringBuilder()
        var level = 0
        if (function.output !== null) {
            val setNames = new ArrayList<String>();
            for (operation: function.getOperations()) {
                val root = operation.getAssignRoot()
                val expression = expressionGenerator.generateExpression(operation.getExpression(), level)
                // Generate the full path using _resolve_rosetta_attr recursively
                val if_cond_blocks = expressionGenerator.if_cond_blocks;
                val isEmpty = if_cond_blocks.isEmpty();
                if (!isEmpty) {
                    level += 1
                }
                if (operation.isAdd()) {
                    result.append(generateAddOperation(root, operation, function, expression) + lineSeparator)
                 }else {
                     result.append(generateSetOperation(root, operation, function, expression, setNames) + lineSeparator)
                }
            }               
        }
        return result
    }
    
    private def generateAddOperation(AssignPathRoot root, Operation operation, Function function, String expression){
        val lineSeparator = System.getProperty("line.separator")
        val attribute = root as Attribute
         val fullPath = generateFullPath(operation.getPath().getReversedAttributes, root.name)
        
        var result=""
        if(attribute.typeCall.type instanceof RosettaEnumeration){
            if(operation == function.getOperations().head){
                result = '''«root.name» = []'''  + lineSeparator	
            }
            result += '''«root.name».extend(«expression»)''' 		
        }else{
            if(operation == function.getOperations().head){
                result = '''«root.name» = «expression»''' 		
            }
            else{
                result = '''«root.name».add_rosetta_attr(«fullPath», «expression»)''' 		
            }
        }
        return result
    }
    /*
    private def List<Operation> getNonAddOperations(Function function) {
        return function.getOperations().filter[!isAdd()].toList()
    }	
     */
    private def generateSetOperation(AssignPathRoot root, Operation operation, Function function, String expression, List<String> setNames){
        var result=""
        
        // Use _get_rosetta_object for setting the attribute
        val attributeRoot = root as Attribute
        if(attributeRoot.typeCall.type instanceof RosettaEnumeration || operation.path===null){
            result = '''«attributeRoot.name» =  «expression»'''
        }
        else{
            if(!setNames.contains(attributeRoot.name)){
                result = '''«attributeRoot.name» = _get_rosetta_object('«attributeRoot.typeCall.type.name»', «getNextPathElementName(operation.path)», «buildObject(expression, operation.path)»)'''
                setNames.add(attributeRoot.name)
            }  	
            else{
                result = '''«attributeRoot.name» = set_rosetta_attr(_resolve_rosetta_attr(self, '«attributeRoot.name»'), «generateAttributesPath(operation.path)», «expression»)'''
            }
        }
        return result
    }
    
    private def generateAttributesPath(Segment path) {
        var currentPath = path
        var result = new StringBuilder()
        result.append("'")
        while(currentPath!==null){
            result.append(currentPath.getAttribute().name)
            if(currentPath.next!==null){
                result.append("->")
            }
            currentPath = currentPath.next
        }
        result.append("'")  
        return result   
    }
    
    private def getNextPathElementName(Segment path) {  
        if (path !== null) {
            val attribute = path.getAttribute()
            return "'" + attribute.name + "'"
        }
        return null // or an appropriate default value
    }
    
    private def String buildObject(String expression, Segment path) {
        if (path === null || path.next === null) {
            return expression;
        }
/*    
        if (path.next === null) {
            return expression;
        }
 */    
        val attribute = path.getAttribute();
        return '''_get_rosetta_object('«attribute.typeCall.type.name»', «getNextPathElementName(path.next)», «buildObject(expression, path.next)»)'''
    }
    
    private def String generateFullPath(Iterable<Attribute> attrs, String root) {
        // Base case: if there are no attributes, return "self" or appropriate root object
        if (attrs.isEmpty) {
            return "self" // or appropriate root object
        }
    
        val attr = attrs.head
        val remainingAttrs = attrs.tail.toList // Convert Iterable to List
    
        val nextPath = if (remainingAttrs.isEmpty) '''_resolve_rosetta_attr(self, «root»)''' else generateFullPath(remainingAttrs, root)
    
        return '''_resolve_rosetta_attr(«nextPath», '«attr.name»')'''
    }

    private def getReversedAttributes(Segment segment) {
        val attributes = new ArrayList<Attribute>();
        var current = segment;
    
        // Traverse the linked list and collect attributes
        while (current !== null) {
            attributes.add(current.getAttribute());
            current = current.getNext();
        }
    
        // Reverse the collected list of attributes
        Collections.reverse(attributes);
    
        return attributes;
    }
    
    /*private def generatesBody(Function function) {
 
        val output = function.output
        val defaultClassName = function.name+"Default"
        '''
        class «function.name»(ABC):
            def __init__(self,«generatesInputs(function)»):
                «FOR inp : function.inputs SEPARATOR "\n"»self.«inp.name»=«inp.name»«ENDFOR»
                
            def evaluate(self):
                «IF function.conditions !== null»
                    «generateFuncConditions(function,function.conditions)»
                «ENDIF»
                «output.name» = self.doEvaluate()
                «IF function.postConditions !== null»	
                    «generateFuncConditions(function,function.postConditions)»	
                «ENDIF»
                return «output.name»
            
            @abstractmethod
            def doEvaluate(self):
                pass
            
            «getAliases(function)»	
            

        class «defaultClassName»(«function.name»):
            def doEvaluate(self):
                «generateOutput(output)»
                return self.assignOutput(«output.name»)
                            
            def assignOutput(self,«output.name»):
                «generateConditions(function)»  
                «IF !checkBasicType(function.output) && !isList(function.output)»
                «output.name» = «output.typeCall.type.name»(«createObject(function)»)
                «ENDIF»
                return «output.name»
                
            «IF function.shortcuts !== null»
            «FOR shortcut : function.shortcuts»
            def «shortcut.name»(self):
            «generateAliasCondition(shortcut,function, 0)»
            «ENDFOR»
            «ENDIF»	
        '''
    }
    * 
    */
    
    /* ********************************************************************** */
    /* ***	   OUTPUT GENERATION	  										*** */
    /* ********************************************************************** */
    
    private def createObject(Function f) {
        var obj = ""
        for (var i = 0;i < f.operations.size;i++) {
            var attr = f.operations.get(i).path.attribute
            var typeName = attr.name
            var param = attr.typeCall.type instanceof RosettaEnumeration ?
            attr.typeCall.type.name+".returnResult_"+Integer.toString(i)+"()":getObjects(f.operations.get(i).path,i,"",0)
            obj+=typeName+" = "+param
            if (i!=f.operations.size-1) obj+=", "
        }
        '''«obj»'''
    }
    
    //Iterative versionn
    /*/private def getObjects(Operation op,int i) {
        var s = op.path
        var obj = ""
        if (s.next !== null) {
            var parenthesis = 0
            obj+="_get_rosetta_object("+'"'+s.attribute.typeCall.type.name+'"'+","+'"'+
                                         s.next.attribute.name+'"'
            while (s.next !== null) {
                if (s.next.next===null) obj+=", returnResult_"+Integer.toString(i)+")"
                else {
                    obj+= ", _get_rosetta_object("+'"'+s.attribute.typeCall.type.name+'"'+","+
                                             '"'+s.next.attribute.name+'"'
                    parenthesis++
                }
                s = s.next
            }
            for (var j = 0;j < parenthesis;j++) obj+=")"
            
        }
        else obj+="returnResult_"+Integer.toString(i)
        '''«obj»'''
    } */
    
    //Recursive version
    private def String getObjects(Segment s,int i,String object,int parenthesis) {
        var obj = object
        if (s.next !== null) {
            obj+="_get_rosetta_object("+'"'+s.attribute.typeCall.type.name+'"'+","+'"'+
                                         s.next.attribute.name+'"'
            if (s.next.next===null) {
                obj+=", returnResult_"+Integer.toString(i)+"())"
                for (var j = 0;j < parenthesis;j++) obj+=")"
            }
            else {
                obj+= ", "+getObjects(s.next,i,obj,parenthesis+1)
            }
    
        }
            
        else obj+="returnResult_"+Integer.toString(i)+"()"
        '''«obj»'''		
    }
    
    /* ********************************************************************** */
    /* ***	              END  OUTPUT GENERATION	  					   *** */
    /* ********************************************************************** */
    
    /* ********************************************************************** */
    /* ***	    Generation of function conditions and postcondition		  *** */
    /* ********************************************************************** */
    
    
    /*private def generateFuncConditions(Function function,EList<Condition> cond) {
        var n_condition = 0;
        var res = "";
        for (Condition c : cond) {
            res += generateFuncConditionBoilerplate(c,n_condition)+
            generateFuncExpressionCondition(function,c.expression,n_condition).toString
        }
        for (Condition c: cond) {
            var msg = c.definition !== null?c.definition:"Error"
            res+="validateCondition("+c.name+"()"+","+'"'+msg+'"'+")\n"
        }
        return res
    }
    
    private def generateFuncConditionBoilerplate(Condition c,int n_condition) {
        '''
        def «c.name»():
        '''
    }
    * 
    */
    
    /*private def generateFuncExpressionCondition(Function function,RosettaExpression exp,int n_condition) {
        if_cond_blocks = new ArrayList<String>()
        var expr = generateExpression(exp,function, 0)
        var blocks = ""
        if (!if_cond_blocks.isEmpty()) {
            blocks = '''	«FOR arg : if_cond_blocks»«arg»«ENDFOR»'''
        }
        '''
        «blocks»	return «expr»
        '''	
        
    }
    * 
    */
    
    /* ********************************************************************** */
    /* ***	   END of function conditions and postcondition		  *** */
    /* ********************************************************************** */
    
    
    /*private def generateConditions(Function function) {
        var n_condition = 0;
        var res = '';
        for (Operation op : function.operations) {
            res += generateConditionBoilerPlate(op, n_condition)+generateExpressionCondition(function,op,n_condition)
            n_condition += 1;
        }
        return res
    }
    * 
    */

    private def generateConditionBoilerPlate(Operation op, int n_condition) {
        '''
        def returnResult_«n_condition»():
        «IF op.definition!==null»
            """
            «op.definition»
            """
        «ENDIF»
        '''
    }

    /* ********************************************************************** */
    /* ***	   ALIAS GENERATION	  										  *** */
    /* ********************************************************************** */
    
    /*private def generateAliasCondition(ShortcutDeclaration s,Function function,int n_condition) {
        if_cond_blocks = new ArrayList<String>()
        var expr = generateExpression(s.expression,function, 0)
        var blocks = ""
        if (!if_cond_blocks.isEmpty()) {
            blocks = '''	«FOR arg : if_cond_blocks»«arg»«ENDFOR»'''
        }
        return 
        '''
        «blocks»	return «expr»
        
        '''
    }
    
    private def getAliases(Function function) {
        var out = ""
        for (shortcuts: function.shortcuts) {
            out+=getAlias(function,shortcuts)
        }
        '''
        «out»
        '''
    }
    * 
    */
    
    private def getAlias(Function function,ShortcutDeclaration s) {
        '''
        @abstractmethod
        def «s.name»(self):
            pass
        '''
    }
    
    /* ********************************************************************** */
    /* ***	  END ALIAS GENERATION	  										*** */
    /* ********************************************************************** */
    
    /*private def generateExpressionCondition(Function function, Operation op,int n_condition) {
        if_cond_blocks = new ArrayList<String>()
        var expr = generateExpression(op.expression,function, 0)
        var blocks = ""
        if (!if_cond_blocks.isEmpty()) {
            blocks = '''	«FOR arg : if_cond_blocks»«arg»«ENDFOR»'''
        }
        return 
        '''
        «blocks»	return «expr»
        
        «IF isList(function.output)» 
        «function.output.name».extend(returnResult_«n_condition»)
        «ELSEIF checkBasicType(function.output)»
        «function.output.name» = returnResult_«n_condition»()
        «ENDIF»
        '''
    }
    */

    def addImportsFromConditions(String variable, String namespace) {
        val import = '''from «namespace».«variable» import «variable»'''
        if (!importsFound.contains(import)) {
            importsFound.add(import)
        }
    }
<<<<<<< Updated upstream

    private def generateOutput(Attribute output) {
        var out = ""
        val outputName = output.name
        if (output.getCard.unbounded) out = outputName+"=[]"
        else out = outputName+"=None"
        '''
        «out»
        '''
    }

    private def boolean isList(Attribute output) {
        return output.getCard.unbounded
    }

    private def getImportsFromAttributes(Function function) {
        var filteredAttributes = new ArrayList
        for (f : function.inputs) if (!checkBasicType(f)) filteredAttributes.add(f)
        if (!checkBasicType(function.output)) filteredAttributes.add(function.output)
        
        val imports = newArrayList
        for (attribute : filteredAttributes) {
            val originalIt = attribute
            val model = function.model
            if (model !== null) {
                val importStatement = '''from «model.name».«translator.toPythonType(originalIt)» import «translator.toPythonType(originalIt)»'''
                imports.add(importStatement)
            }

        }

        // Remove duplicates by converting the list to a set and back to a list
        return imports.toSet.toList
        
    }

    def checkBasicType(Attribute attr) {
        val types = Arrays.asList('int', 'str', 'Decimal', 'date', 'datetime', 'datetime.date', 'datetime.time', 'time',
            'bool', 'number')
        return (attr !== null && translator.toPythonType(attr) !== null) ? types.contains(translator.toPythonType(attr).toString()) : false
    }	
=======
>>>>>>> Stashed changes
}