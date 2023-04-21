package com.regnosys.rosetta.generator.python

import com.google.inject.Inject
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import java.io.File
import java.io.FileReader
import java.io.FileWriter
import java.nio.file.Files
import java.nio.file.Paths
import java.util.Collections
import java.util.Arrays
import java.util.Map
import java.util.Scanner
import org.eclipse.emf.common.util.URI
import org.eclipse.emf.ecore.resource.ResourceSet
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.eclipse.xtext.testing.util.ParseHelper
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith
import com.regnosys.rosetta.rosetta.RosettaRootElement
import java.util.HashMap
import com.regnosys.rosetta.rosetta.simple.Data;
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import java.util.ArrayList
import java.util.List
import com.regnosys.rosetta.rosetta.simple.Function
import org.apache.commons.io.FileUtils
import java.io.IOException
import org.apache.commons.configuration2.INIConfiguration
import static java.nio.file.StandardCopyOption.*
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import java.lang.reflect.Array
import org.junit.jupiter.api.Disabled
import com.google.inject.Provider
import org.eclipse.xtext.resource.XtextResourceSet

/*
 * Test Principal
 */
@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class PythonFilesGeneratorTest {

    @Inject PythonCodeGenerator generator

    @Inject extension ParseHelper<RosettaModel>
	
	@Inject
    Provider<XtextResourceSet> resourceSetProvider;
	/*
	 * Test which is used as main to create all the Python Generation
	 */
	 
	@Test
    def void generatePython() {
		// the process 
		// 1) get directory information from the ini file
		// 2) loop through each of the rosetta dsl definitions
		//    - delete any existing directory and create a new one
		//    - produce new python from the dsl definitions 
		// 3) produce toml and version files
		// 4) loop through the directory structure to add an empty __init__.py file
		
		try {
			val iniFileName   = new File("build/pythonCDMGenerator.ini")
			println ('PythonFilesGeneratorTest::generatePython ... start ... reading ini file:' + iniFileName)
			val iniConfig     = new INIConfiguration()
			val fileReader    = new FileReader(iniFileName)
			iniConfig.read(fileReader)
	
		    val resourcesPath    = iniConfig.getSection('paths').getProperty ('resources').toString () 
			val dslPath          = iniConfig.getSection('paths').getProperty ('dslPath').toString ()
			// pythonTgtPath is the target directory for the generated python
		    val pythonTgtPath    = iniConfig.getSection('paths').getProperty ('pythonTgtPath').toString ()
		    val tomlTemplatePath = iniConfig.getSection('paths').getProperty ('tomlTemplatePath').toString ()
		    val tomlTargetPath   = iniConfig.getSection('paths').getProperty ('tomlTargetPath').toString ()
			// get the version of CDM that will be generated
			val cdmVersion       = iniConfig.getSection('CDM').getProperty ('version').toString ()
	
		    // Create a resource set and add the common Rosetta models to it
		    val resourceSet = resourceSetProvider.get  
            parse(ModelHelper.commonTestTypes, resourceSet)
		    resourceSet.getResource(URI.createURI('classpath:/model/basictypes.rosetta'), true)
		    resourceSet.getResource(URI.createURI('classpath:/model/annotations.rosetta'), true)
		
		    // Get a list of all the DSL input files and filter out non-Rosetta files
		    var dslFile   = new File(dslPath)
		    var listFiles = dslFile.listFiles[it.name.endsWith('.rosetta')] as File[]
		    Arrays.sort(listFiles)
		    println ('PythonFilesGeneratorTest::generatePython ... found ' + listFiles.length.toString () + ' rosetta files in: ' + dslPath)
		
		    // Get a list of all the Rosetta models in the resource set
			println ('PythonFilesGeneratorTest::generatePython ... get resource set')
	
		    val rosettaModels = resourceSet.resources.map[contents.filter(RosettaModel)].flatten.toList
		
		    // Create a map to store the import statements and variables for each file

		    var importsVariables = new HashMap<String, List<String>>()
		
		    // Load the Rosetta models in the input files and add their import statements and variables to the map
		    importsVariables = loadResourceSet(listFiles, resourceSet, importsVariables)
		
		    // Generate the Python files and structure
		    createStrucurePython(resourcesPath, dslPath, cdmVersion, pythonTgtPath, listFiles, resourceSet, importsVariables) 
	
	        // create the Toml file    
	
	        createProjectToml(tomlTemplatePath, cdmVersion, tomlTargetPath)
			println ('PythonFilesGeneratorTest::generatePython ... done')
		} 
	    catch (IOException ioE) {
	    	println ('PythonFilesGeneratorTest::generatePython ... processing failed with an IO Exception')
	    	println (ioE.toString ())
	    	ioE.printStackTrace ()
	    }
	    catch (ClassCastException ccE) {
	    	println ('PythonFilesGeneratorTest::generatePython ... processing failed with a ClassCastException')
	    	println (ccE.toString ())
	    	ccE.printStackTrace ()
	    }
	    catch(Exception e) {
	    	println ('PythonFilesGeneratorTest::generatePython ... processing failed with an Exception')
	    	println (e.toString ())
	    	e.printStackTrace ()
		}
	}
    
    /*
     * Initialize the top directory with a specific __init__.py, version.py and the project toml file
     */
    def private void initializeTopDirectory(String dslPath, String cdmVersion, String pythonTgtPath) {
		print ('PythonFilesGeneratorTest::initializeTopDirectory ... start ... updating: ' + pythonTgtPath)
    	// Determine where to put the generated code
    	val pythonTgtFile       = new File(pythonTgtPath)
		// create a top-level __init__.py file with the current version
		pythonTgtFile.mkdirs()
		val initFile            = new File(pythonTgtFile+File.separator+"__init__.py")
        val initFileWriter      = new FileWriter(initFile)
        initFileWriter.write("from .version import __version__")
        initFileWriter.close()        
        val cdmVersionComma     = cdmVersion.replace ('.', ',')
        val versionFile         = new File(pythonTgtFile+File.separator+"version.py")
       	val versionFileWriter   = new FileWriter(versionFile)
       	versionFileWriter.write("version = ("+cdmVersionComma+",0)\n"+
       										"version_str = '"+cdmVersion+"-0'\n"+
       										"__version__ = '"+cdmVersion+"'\n"+
       										"__build_time__ = '"+LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_DATE_TIME)+"'")       	
        versionFileWriter.close()
    	// create project.toml (uses the model version) and copy static files
		println (' ... done')
	}
    
    def String getNameRootElement(RosettaRootElement element) {
	    if (element instanceof Data) {
	        return (element as Data).name
	    } else if (element instanceof RosettaEnumeration) {
	        return (element as RosettaEnumeration).name
	    } else if (element instanceof Function) {
	        return (element as Function).name
	    }
	    return null
	}

    
    /*
     * Method that generates python by iterating through each Rosetta definition
     */

	def private void createStrucurePython(String resourcesPath, String dslPath, String cdmVersion,  
    									  String pythonTgtPath, File[] listFiles, ResourceSet resourceSet, 
    									  HashMap<String, List<String>> importsVariables) {
		// remember which directories we've passed through and how many files have been updated
	    var dirFileCount  = new HashMap () 
        var seenRoot      = false;
	    
	    // Iterate through each Rosetta file in the input list
		val rosettaModels = resourceSet.resources.map[contents.filter(RosettaModel)].flatten.toList
	    for (RosettaModel model: rosettaModels){
	        var className = ""        // Initialize the class name to an empty string
            // Get a list of existing functions that have already been generated
            val existingCreatedFunctions = new File(resourcesPath + File.separator + "functions").list().map[it.split("\\.").get(0)]
            
            // Iterate through each element in the model
            for(RosettaRootElement element: model.elements){
                // Get the name of the current root element
                className = getNameRootElement(element)
                // If the current element is a RosettaEnumeration, Data, or Function object
                if(element instanceof RosettaEnumeration || element instanceof Data || element instanceof Function){
                    // Generate Python code from the current model element
                    val python         = generator.afterGenerate(Collections.singletonList(model), element, importsVariables)
                    
                    // Remove any leading or trailing whitespace from the generated code
                    val generatedFiles = checkNoWhiteSpaces(getContent(python))
                    
                    // Set the directory for the generated file
                    var directory      = pythonTgtPath
                    // Split the model name into its constituent parts
                    var parseModelName = model.name.split("\\.")
					var topLevelKey    = Array.get(parseModelName, 0) as String 
					var secondLevelKey = Array.get(parseModelName, 1) as String
					var lastLevelKey   = Array.get (parseModelName, parseModelName.length - 1)
                    // Iterate through each part of the name
                    for ( String key : parseModelName ) {
                        // Update the directory with the current part of the name
                        directory = directory + File.separator + key
						if (key == topLevelKey && !seenRoot) {
                        	// initialize the top most directory if this is the first time through
			    	    	println ('PythonFilesGeneratorTest::createStrucurePython ... writing Python files')
							initializeTopDirectory (dslPath,  cdmVersion, directory)
							seenRoot = true;
							dirFileCount.put (key, 0)
						} else {
							val newDir = new File(directory)
							if (key == secondLevelKey && !dirFileCount.containsKey (key)) {
	                        	// delete the second level subdirectory to ensure that we have cleaned up
	                        	if(newDir.exists()){
	                        		FileUtils.forceDelete (new File (directory))
	                        	}
			    	    		println ('PythonFilesGeneratorTest::createStrucurePython ... removed and created directory: ' + directory + ' key: ' + key)
								dirFileCount.put (key, 0)
							}
	                        // Create a new directory if it does not already exist and add __init__.py
							// ensure that the current directory has been created
							FileUtils.forceMkdir (new File (directory))
						    // initialize any subdirectories other than the top leve
							FileUtils.touch (new File (directory + File.separator + '__init__.py'))
						}
                        // Add the file if this is the last part of the name
                        if(key == lastLevelKey){
                            // Check if the generated file contains a function that has already been created
                            val containsKey = importsVariables.containsKey(className)
                            val isFunc      = importsVariables.get(className).get(1)=="FUNC"
                            val funcExists  = existingCreatedFunctions.contains(className)
                            
                            // If the file contains a function that has already been created, do not create the function file again
                            if(containsKey){
                                if(isFunc && funcExists){
									Files.copy (Paths.get (resourcesPath + File.separator + "functions" + File.separator +className+".py"),
												Paths.get (directory + File.separator + className +".py"), 
												REPLACE_EXISTING
									) 
								}
                            }  
                            
                            // write the file if it is not a function keeping track of how many files have been written
                            if(!isFunc) {
								val countKey = (key == topLevelKey) ? topLevelKey : secondLevelKey
                            	writePythonFiles(generatedFiles, directory, className)
                            	dirFileCount.put (countKey, dirFileCount.get (countKey) + 1)
                            }
                        }
                    }
                }
            }
        }
        for (String key : dirFileCount.keySet ()) {
   	    	println ('PythonFilesGeneratorTest::createStrucurePython ... created dir: ' + key + ' with # files: ' + dirFileCount.get(key))
        }
    }
    
    /*
     * Write the content inside python files, if the file contains "types" it also add an import referring the enums of the same folder
     */
    def private writePythonFiles(String generatedFiles, String directory, String fileName){
    	// Set the file name with a .py extension
		val filename = fileName +".py"
		// Create a scanner to read the contents of the generated files
		val scanner = new Scanner(generatedFiles);
		// Set variables to keep track of whether or not imports have been set and inserted
		var setImports = false
		var insertedImports = false
		// Create a file object with the specified directory and file name
		val pythonFile = new File(directory+File.separator+filename)
		// Create a writer object to write to the Python file
		val myWriter = new FileWriter(pythonFile)
		
		// Loop through each line in the generated files
		while (scanner.hasNextLine()) {
			// Get the next line
			val line = scanner.nextLine();
			
			// Check if the file name contains "type"
			if(fileName.contains("type")){
				// If not already done, add any import statements to the new Python file
				if(!insertedImports){
					// If the line contains an import statement, set the setImports flag and write the line to the new Python file
					if(line.contains("import")){
						setImports = true
						myWriter.write(line + "\n")	
					}
					// If the line does not contain an import statement and the setImports flag is true,
					// add any required import statements for imported files to the new Python file
					if(!line.contains("import") && setImports == true){
						
						myWriter.write("\n")
						// Set the insertedImports flag to true
						insertedImports=true	
					}
				}						
				// If the line is not an import statement, write it to the new Python file
				else{
					myWriter.write(line+ "\n")		
				}
			}
			// If the file name does not contain "type", write the generated files to the new Python file
			else{
				Files.write(Paths.get(directory).resolve(filename), generatedFiles.toString.bytes)
			}
		}
		
		// Close the writer and scanner objects
		myWriter.close()
		scanner.close()
    }
    
    /*
     * Loads all the resources and they are stored in the variable resourceSet
     */
    def private HashMap<String,List<String>> loadResourceSet(File[] listFiles, ResourceSet resourceSet, HashMap<String, List<String>> importsVariables){
    	for (File file: listFiles){
         	val filePath = file.path
     		val content  = new String(Files.readAllBytes(Paths.get(filePath)))
			parse(content,resourceSet)
		}
    	
    	for (File file: listFiles){
			println ('PythonFilesGeneratorTest::loadResourceSet ... parsing file: ' + file.name)
         	val filePath = file.path
     		val content  = new String(Files.readAllBytes(Paths.get(filePath)))   		
			parse(content,URI.createURI(filePath),resourceSet)
			
			val model = resourceSet.getResource(URI.createURI(filePath), false).contents.filter(RosettaModel).get(0)
			val List<Data> types = new ArrayList<Data>()
			val List<RosettaEnumeration> enums = new ArrayList<RosettaEnumeration>()
			val List<Function> funcs = new ArrayList<Function>()
			for(RosettaRootElement element: model.elements){
				if(element instanceof Data){
					types.add(element)
				}
				if(element instanceof RosettaEnumeration){
					enums.add(element)
				}
				if(element instanceof Function){
					funcs.add(element)
				}
			}
			for(Data type: types){
				val data = new ArrayList<String>()
				data.add(model.name)
				data.add("DATA")
				importsVariables.put(type.name, data)
			}
			for(RosettaEnumeration enum: enums){
				val data = new ArrayList<String>()
				data.add(model.name)
				data.add("ENUM")
				importsVariables.put(enum.name, data)
			}
			for(Function func: funcs){
				val data = new ArrayList<String>()
				data.add(model.name)
				data.add("FUNC")
				importsVariables.put(func.name, data)
			}
		}
		return importsVariables
    }
    def private void createProjectToml(String tomlTemplatePath, String cdmVersion, String pythonTgtPath) {
		// TOML files are used by python to manage packages.  This one needs to be updated with the version
		// read in the TOML template, update the version, write out the TOML file    	
    	
        val tomlTemplate = Files.readString (Paths.get (tomlTemplatePath))
        val toml         = tomlTemplate.replace ('[CDMVERSION]', cdmVersion)
		Files.write (Paths.get (pythonTgtPath, "pyproject.toml"), toml.getBytes ()) 
   	}
    
   	/*
	 * Creates the DeserializationFile
	 */
	def private String checkNoWhiteSpaces(String content) {
    	var lsep = System.lineSeparator()
    	var contentSplitted = content.split(lsep)
    	var result = ""
    	for(String con: contentSplitted) {
    		if (con.trim().length() > 0) {
    			result += con + lsep
    		}
    		else{
    			result += lsep
    		}
    	}
    	return result
    }

    /*
     * Get all the content of a generated Python
     */
    def private getContent(Map<String, ? extends CharSequence> python){
    	
    	val List<String> keys = Arrays.asList("Imports.py", "Enums.py", "Types.py", "Funcs.py");
	    val content = new StringBuilder();
	    for (String key : keys) {
	        if (python.containsKey(key)) {
	            content.append(python.get(key).toString());
	        }
	    }
	    return content.toString();
    }
}
