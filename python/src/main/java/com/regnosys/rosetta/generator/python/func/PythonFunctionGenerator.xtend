package com.regnosys.rosetta.generator.python.func

import com.google.inject.Inject
import com.regnosys.rosetta.generator.python.expressions.PythonExpressionGenerator
import com.regnosys.rosetta.generator.python.util.PythonModelGeneratorUtil
import com.regnosys.rosetta.generator.python.util.PythonTranslator
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.rosetta.simple.AssignPathRoot
import com.regnosys.rosetta.rosetta.simple.Attribute
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.simple.Function
import com.regnosys.rosetta.rosetta.simple.Operation
import com.regnosys.rosetta.rosetta.simple.Segment
import java.util.ArrayList
import java.util.Collections
import java.util.HashMap
import java.util.List
import java.util.Map
import java.util.Set
import org.eclipse.emf.ecore.EObject
import org.slf4j.Logger
import org.slf4j.LoggerFactory

class  PythonFunctionGenerator {
    
    static final Logger LOGGER = LoggerFactory.getLogger(PythonFunctionGenerator);
    
    var List<String> importsFound = newArrayList
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
                    result.put(PythonModelGeneratorUtil::toPyFunctionFileName(namespace, func.name), 
           				PythonModelGeneratorUtil::createImportsFunc(func.name) + funcs);
                }
                catch(Exception ex){
                    LOGGER.error("Exception occurred generating func {}", func.name, ex)	
                }		
            } 
        }
        return result
    }

    private def generateFunctions(Function function,String version) {
        val dependencies = collectFunctionDependencies(function);
        '''
        «generateImports(dependencies, function)»
        
        
        @replaceable
        def «function.name»«generatesInputs(function)»:
            «generateDescription(function)»
            «IF function.conditions.size()>0»    
            _pre_registry = {}
            «ENDIF»
            «IF function.postConditions.size()>0»    
            _post_registry = {}
            «ENDIF»
            self = inspect.currentframe()
            
            «generateConditions(function)»
            
        «generateIfBlocks(function)»
            «generateAlias(function)»
            «generateOperations(function)»
            «generatesOutput(function)»

        sys.modules[__name__].__class__ = create_module_attr_guardian(sys.modules[__name__].__class__)
        '''
    }
    
    private def generateImports(Iterable<EObject> dependencies, Function function) {
        val imports = new StringBuilder();

        for (EObject dependency : dependencies) {
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
<<<<<<< HEAD
                «output.name» = rosetta_resolve_attr(self, "«output.name»")
=======
                «output.name» = _resolve_rosetta_attr(self, "«output.name»")
>>>>>>> master
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
                            PythonTranslator.toPythonBasicType(typeName)  
            result += input.getName() + ": " + type
            if (input.getCard().inf == 0)  
                result += " | None"
            if (inputs.indexOf(input) < inputs.size() - 1)
                result += ", "
        }
        result += ") -> "
        if (output !== null)
            result += PythonTranslator.toPythonBasicType(output.getTypeCall().getType().getName())  
        else
            result += "None"  
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
<<<<<<< HEAD

=======
    
>>>>>>> master
        func.shortcuts.forEach[shortcut |
            dependencies.addAll(functionDependencyProvider.findDependencies(shortcut.expression))
        ]
        func.operations.forEach[operation |
            dependencies.addAll(functionDependencyProvider.findDependencies(operation.expression))
        ]
<<<<<<< HEAD

        (func.conditions + func.postConditions).forEach[condition |
            dependencies.addAll(functionDependencyProvider.findDependencies(condition.expression))
        ]

=======
    
        (func.conditions + func.postConditions).forEach[condition |
            dependencies.addAll(functionDependencyProvider.findDependencies(condition.expression))
        ]
    
>>>>>>> master
        func.inputs.forEach[input |
            if (input.getTypeCall()?.getType() !== null) {
                dependencies.add(input.getTypeCall().getType())
            }
        ]
<<<<<<< HEAD

        if (func.output?.getTypeCall()?.getType() !== null) {
            dependencies.add(func.output.getTypeCall().getType())
        }
        
        dependencies.removeIf[
		    it instanceof Function && (it as Function).name == func.name
		]

        return dependencies
    }


=======
    
        if (func.output?.getTypeCall()?.getType() !== null) {
            dependencies.add(func.output.getTypeCall().getType())
        }
    
        return dependencies
    }

>>>>>>> master
    private def generateIfBlocks(Function function) {
        val levelList = newArrayList(0) 
    
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
        «expressionGenerator.generateFunctionConditions(function.conditions, "_pre_registry")»
        # Execute all registered conditions
        execute_local_conditions(_pre_registry, 'Pre-condition')
        «ENDIF»
        '''
    }
    
    private def generatePostConditions(Function function) {	
        '''     
        «IF function.postConditions.size>0»
        # post-conditions
        «expressionGenerator.generateFunctionConditions(function.postConditions, "_post_registry")»
        # Execute all registered post-conditions
        execute_local_conditions(_post_registry, 'Post-condition')
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
<<<<<<< HEAD
                result = '''«attributeRoot.name» = set_rosetta_attr(rosetta_resolve_attr(self, '«attributeRoot.name»'), «generateAttributesPath(operation.path)», «expression»)'''
=======
                result = '''«attributeRoot.name» = set_rosetta_attr(_resolve_rosetta_attr(self, '«attributeRoot.name»'), «generateAttributesPath(operation.path)», «expression»)'''
>>>>>>> master
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
        return null 
    }
    
    private def String buildObject(String expression, Segment path) {
        if (path === null || path.next === null) {
            return expression;
        }

        val attribute = path.getAttribute();
        return '''_get_rosetta_object('«attribute.typeCall.type.name»', «getNextPathElementName(path.next)», «buildObject(expression, path.next)»)'''
    }
    
    private def String generateFullPath(Iterable<Attribute> attrs, String root) {
        if (attrs.isEmpty) {
            return "self" 
        }
    
        val attr = attrs.head
        val remainingAttrs = attrs.tail.toList 
    
<<<<<<< HEAD
        val nextPath = if (remainingAttrs.isEmpty) '''rosetta_resolve_attr(self, «root»)''' else generateFullPath(remainingAttrs, root)
    
        return '''rosetta_resolve_attr(«nextPath», '«attr.name»')'''
=======
        val nextPath = if (remainingAttrs.isEmpty) '''_resolve_rosetta_attr(self, «root»)''' else generateFullPath(remainingAttrs, root)
    
        return '''_resolve_rosetta_attr(«nextPath», '«attr.name»')'''
>>>>>>> master
    }

    private def getReversedAttributes(Segment segment) {
        val attributes = new ArrayList<Attribute>();
        var current = segment;
    
        while (current !== null) {
            attributes.add(current.getAttribute());
            current = current.getNext();
        }
    
        Collections.reverse(attributes);
    
        return attributes;
    }


    def addImportsFromConditions(String variable, String namespace) {
        val import = '''from «namespace».«variable» import «variable»'''
        if (!importsFound.contains(import)) {
            importsFound.add(import)
        }
    }
}