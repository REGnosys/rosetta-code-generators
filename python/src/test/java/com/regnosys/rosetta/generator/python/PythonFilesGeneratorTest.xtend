package com.regnosys.rosetta.generator.python

import com.google.inject.Inject
import com.google.inject.Provider
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.rosetta.RosettaRootElement
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.simple.Function
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import java.io.File
import java.io.FileReader
import java.io.FileWriter
import java.io.IOException
import java.nio.charset.StandardCharsets
import java.nio.file.Files
import java.nio.file.Path
import java.nio.file.Paths
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import java.util.Map
import org.apache.commons.configuration2.INIConfiguration
import org.apache.commons.io.FileUtils
import org.eclipse.emf.common.util.URI
import org.eclipse.xtext.resource.XtextResourceSet
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.eclipse.xtext.testing.util.ParseHelper
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith
import org.slf4j.LoggerFactory

/*
 * Test Principal
 */
@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class PythonFilesGeneratorTest {

	static val LOGGER = LoggerFactory.getLogger(PythonFilesGeneratorTest);

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
		//	- delete any existing directory and create a new one
		//	- produce new python from the dsl definitions 
		// 3) produce toml and version files
		// 4) loop through the directory structure to add an empty __init__.py file
		
		try {
			val iniFileName	 = new File("build/pythonCDMGenerator.ini")
			if(!iniFileName.exists()){
				println ('PythonFilesGeneratorTest::generatePython ... start ... no ini file detected')
				return
			}
			LOGGER.info("generatePython ... reading ini file: {}", iniFileName)
			
			val iniConfig	 = new INIConfiguration()
			val fileReader	= new FileReader(iniFileName)
			iniConfig.read(fileReader)
			
			val dslPath			= iniConfig.getSection('paths').getProperty ('dslPath').toString ()
			// pythonTgtPath is the target directory for the generated python
			val pythonTgtPath	= iniConfig.getSection('paths').getProperty ('pythonTgtPath').toString ()
			val tomlTemplatePath = iniConfig.getSection('paths').getProperty ('tomlTemplatePath').toString ()
			val tomlTargetPath	 = iniConfig.getSection('paths').getProperty ('tomlTargetPath').toString ()
			// get the version of CDM that will be generated
			val cdmVersion		 = iniConfig.getSection('CDM').getProperty ('version').toString ()
	
			// Create a resource set and add the common Rosetta models to it
			LOGGER.info("generatePython ... get resource set")
			val resourceSet = resourceSetProvider.get	
			parse(ModelHelper.commonTestTypes, resourceSet)
			resourceSet.getResource(URI.createURI('classpath:/model/basictypes.rosetta'), true)
			resourceSet.getResource(URI.createURI('classpath:/model/annotations.rosetta'), true)
		
			// Get a list of all the DSL input files and filter out non-Rosetta files
			val dirs = new File(dslPath)
			val files = dirs.listFiles.filter[it.getName.endsWith(".rosetta")].sort()
			files.forEach [file |
				LOGGER.info("generatePython ... reading file: {}", file.name)
				val content = new String(Files.readAllBytes(file.toPath))
				parse(content, resourceSet)
			]
			files.forEach [file |
				LOGGER.info("generatePython ... reading file a 2nd time: {}", file.name)
					val content = new String(Files.readAllBytes(file.toPath))
					parse(content,URI.createURI("def_"+file.toPath), resourceSet)
			]
			
			val rosettaModels	= resourceSet.resources.filter[it.getURI().toString.contains("def_")].map[contents.filter(RosettaModel)].flatten.toList
			LOGGER.info ("generatePython ... found {} rosetta files in {}", rosettaModels.length.toString (), dslPath)					
			val generatedFiles = generator.afterGenerate(rosettaModels)
			
			deleteFolderContent(pythonTgtPath)
			
			writeFiles(pythonTgtPath, generatedFiles)
			createProjectToml(tomlTemplatePath, cdmVersion, tomlTargetPath)
			LOGGER.info ("generatePython ... done")
		} 
		catch (IOException ioE) {
			println ('PythonFilesGeneratorTest::generatePython ... processing failed with an IO Exception')
			ioE.printStackTrace ()
		}
		catch (ClassCastException ccE) {
			println ('PythonFilesGeneratorTest::generatePython ... processing failed with a ClassCastException')
			ccE.printStackTrace ()
		}
		catch(Exception e) {
			println ('PythonFilesGeneratorTest::generatePython ... processing failed with an Exception')
			e.printStackTrace ()
		}
	}
	
	@Test
	def void generatePythonOneParse() {
		// the process 
		// 1) get directory information from the ini file
		// 2) loop through each of the rosetta dsl definitions
		//	- delete any existing directory and create a new one
		//	- produce new python from the dsl definitions 
		// 3) produce toml and version files
		// 4) loop through the directory structure to add an empty __init__.py file
		
		try {
			val iniFileName	 = new File("build/pythonCDMGenerator.ini")
			if(!iniFileName.exists()){
				println ('PythonFilesGeneratorTest::generatePythonOneParse ... start ... no ini file detected')
				return
			}
			LOGGER.info("generatePython ... reading ini file: {}", iniFileName)
			
			val iniConfig	     = new INIConfiguration()
			val fileReader	     = new FileReader(iniFileName)
			iniConfig.read(fileReader)
			
			val dslPath			 = iniConfig.getSection('paths').getProperty ('dslPath').toString ()
			// pythonTgtPath is the target directory for the generated python
			val pythonTgtPath	 = iniConfig.getSection('paths').getProperty ('pythonTgtPathOneParse').toString ()
			val tomlTemplatePath = iniConfig.getSection('paths').getProperty ('tomlTemplatePath').toString ()
			val tomlTargetPath	 = iniConfig.getSection('paths').getProperty ('tomlTargetPath').toString ()
			// get the version of CDM that will be generated
			val cdmVersion		 = iniConfig.getSection('CDM').getProperty ('version').toString ()
	
			// Create a resource set and add the common Rosetta models to it
			LOGGER.info("generatePython ... get resource set")
			val resourceSet = resourceSetProvider.get	
			parse(ModelHelper.commonTestTypes, resourceSet)
			resourceSet.getResource(URI.createURI('classpath:/model/basictypes.rosetta'), true)
			resourceSet.getResource(URI.createURI('classpath:/model/annotations.rosetta'), true)
		
			// Get a list of all the DSL input files and filter out non-Rosetta files
			val dirs = new File(dslPath)
			val files = dirs.listFiles.filter[it.getName.endsWith(".rosetta")].sort()
			files.forEach [file |
				LOGGER.info ("generatePythonOneParse ... reading file: {}", file.name)
					val content = new String(Files.readAllBytes(file.toPath))
					parse(content, resourceSet)
			]
			
			val rosettaModels	= resourceSet.resources.map[contents.filter(RosettaModel)].flatten.toList
			LOGGER.info ("generatePython ... found {} rosetta files in {}", rosettaModels.length.toString (), dslPath)					
			val generatedFiles = generator.afterGenerate(rosettaModels)
			
			deleteFolderContent(pythonTgtPath)
			
			writeFiles(pythonTgtPath, generatedFiles)
			createProjectToml(tomlTemplatePath, cdmVersion, tomlTargetPath)
			LOGGER.info ("generatePython ... done")
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
	
	@Test
	def void generatePythonOneParseWithGetResource () {
		// the process 
		// 1) get directory information from the ini file
		// 2) loop through each of the rosetta dsl definitions
		//	- delete any existing directory and create a new one
		//	- produce new python from the dsl definitions 
		// 3) produce toml and version files
		// 4) loop through the directory structure to add an empty __init__.py file
		
		try {
			val iniFileName	 = new File("build/pythonCDMGenerator.ini")
			if(!iniFileName.exists()){
				println ('PythonFilesGeneratorTest::generatePythonOneParse ... start ... no ini file detected')
				return
			}
			LOGGER.info("generatePython ... reading ini file: {}", iniFileName)
			
			val iniConfig	     = new INIConfiguration()
			val fileReader	     = new FileReader(iniFileName)
			iniConfig.read(fileReader)
			
			val dslPath			 = iniConfig.getSection('paths').getProperty ('dslPath').toString ()
			val buildPath        = iniConfig.getSection('paths').getProperty ('buildPath').toString ()
			// get the version of CDM that will be generated
	
			// Create a resource set and add the common Rosetta models to it
			LOGGER.info("generatePython ... get resource set")
			val resourceSet = resourceSetProvider.get	
			parse(ModelHelper.commonTestTypes, resourceSet)
			resourceSet.getResource(URI.createURI('classpath:/model/basictypes.rosetta'), true)
			resourceSet.getResource(URI.createURI('classpath:/model/annotations.rosetta'), true)
		
			// Get a list of all the DSL input files and filter out non-Rosetta files
			val rosettaFilePaths = newArrayList (new File(dslPath))
				.map[listFiles[name.endsWith("rosetta")].toList]
				.flatten
				.map[toPath]
			val resources 		 = rosettaFilePaths
				.map[resourceSet.getResource(URI.createURI(it.toString()), true)]
				.toList
			val rosettaModels 	 = resources
				.flatMap[contents.filter(RosettaModel)]
				.toList
			LOGGER.info ("generatePython ... found {} rosetta files in {}", rosettaModels.length.toString (), dslPath)					
			val generatedFiles = generator.afterGenerate(rosettaModels)
			
			deleteFolderContent(buildPath)
			
			writeFiles(buildPath, generatedFiles)
//			createProjectToml(tomlTemplatePath, cdmVersion, tomlTargetPath)
			LOGGER.info ("generatePython ... done")
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
	
	def static deleteFolderContent(String folderPath) {
		val folder = new File(folderPath + File.separator + "src")
		if (folder.exists() && folder.isDirectory()) {
			try {
				FileUtils.cleanDirectory(folder)
			} catch (IOException e) {
				System.err.println("Failed to delete folder content: " + e.message)
			}
		} else {
			System.err.println("Folder does not exist or is not a directory")
		}
	}
	
	def writeFiles(String pythonTgtPath, Map<String, ? extends CharSequence> generatedFiles){
		// Assuming 'generatedFiles' is a HashMap<String, CharSequence>
		for (entry : generatedFiles.entrySet) {
			// Split the key into its components and replace '.' with the file separator
			val filePath	 = entry.key
			val fileContents = entry.value.toString
			val outputPath   = Path.of(pythonTgtPath + File.separator + filePath);
			LOGGER.info("Writing {}", outputPath);
			Files.createDirectories(outputPath.parent);
			Files.write(outputPath, fileContents.getBytes(StandardCharsets.UTF_8))		}
		
	}
	
	/*
	 * Initialize the top directory with a specific __init__.py, version.py and the project toml file
	 */
	def private void initializeTopDirectory(String dslPath, String cdmVersion, String pythonTgtPath) {
		print ('PythonFilesGeneratorTest::initializeTopDirectory ... start ... updating: ' + pythonTgtPath)
		// Determine where to put the generated code
		val pythonTgtFile		 = new File(pythonTgtPath)
		// create a top-level __init__.py file with the current version
		pythonTgtFile.mkdirs()
		val initFile			= new File(pythonTgtFile+File.separator+"__init__.py")
		val initFileWriter		= new FileWriter(initFile)
		initFileWriter.write("from .version import __version__")
		initFileWriter.close()		
		val cdmVersionComma	 = cdmVersion.replace ('.', ',')
		val versionFile		 = new File(pythonTgtFile+File.separator+"version.py")
		 	val versionFileWriter	 = new FileWriter(versionFile)
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

	
	/*
	 * Write the content inside python files, if the file contains "types" it also add an import referring the enums of the same folder
	 */
	def private void createProjectToml(String tomlTemplatePath, String cdmVersion, String pythonTgtPath) {
		// TOML files are used by python to manage packages.	This one needs to be updated with the version
		// read in the TOML template, update the version, write out the TOML file		
		
		val tomlTemplate = Files.readString (Paths.get (tomlTemplatePath))
		val toml		 = tomlTemplate.replace ('[CDMVERSION]', cdmVersion)
		Files.write (Paths.get (pythonTgtPath, "pyproject.toml"), toml.getBytes ()) 
	 	}
	
	 	/*
	 * Creates the DeserializationFile
	 */
}
