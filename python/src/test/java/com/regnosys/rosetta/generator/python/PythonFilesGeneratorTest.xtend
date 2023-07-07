package com.regnosys.rosetta.generator.python

import com.google.inject.Inject
import com.google.inject.Provider
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import com.regnosys.rosetta.tests.util.ModelHelper
import java.io.File
import java.io.FileReader
import java.io.IOException
import java.nio.charset.StandardCharsets
import java.nio.file.Files
import java.nio.file.Path
import java.util.Map
import java.util.Properties
import java.lang.CharSequence
import org.apache.commons.io.FileUtils
import org.apache.maven.model.io.xpp3.MavenXpp3Reader
import org.eclipse.emf.common.util.URI
import org.eclipse.xtext.resource.XtextResourceSet
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.eclipse.xtext.testing.util.ParseHelper
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith
import org.junit.jupiter.api.Disabled
import java.util.Collection
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

	def private Properties getProperties () throws Exception {
		var reader     = new MavenXpp3Reader();
		var model      = reader.read(new FileReader("pom.xml"))
		val properties = model.getProperties();
		if (properties.getProperty ('codebase.outputpath') === null) {
			throw new Exception ('Initialization failure: code base output path specified')
		}
		if (properties.getProperty ('rosetta.source.path') === null) {
			throw new Exception('Initialization failure: Rosetta path not specified')
		}
		return properties
	}
	def private void deleteFolderContent(String folderPath) {
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
	
	def private writeFiles(String pythonTgtPath, Map<String, ? extends CharSequence> generatedFiles){
		// Assuming 'generatedFiles' is a HashMap<String, CharSequence>
		for (entry : generatedFiles.entrySet) {
			// Split the key into its components and replace '.' with the file separator
			val filePath	 = entry.key
			val fileContents = entry.value.toString
			val outputPath   = Path.of(pythonTgtPath + File.separator + filePath)
			Files.createDirectories(outputPath.parent);
			Files.write(outputPath, fileContents.getBytes(StandardCharsets.UTF_8))		
		}
		LOGGER.info("Write Files ... wrote: {}", generatedFiles.size ())
		
	}
	@Test
	def void generatePython () {
		// the process 
		// 1) get directory information from the ini file
		// 2) loop through each of the rosetta dsl definitions
		//	- delete any existing directory and create a new one
		//	- produce new python from the dsl definitions 
		// 3) produce toml and version files
		// 4) loop through the directory structure to add an empty __init__.py file
		
		try {
			val properties    = getProperties ()
			val rosettaSource = properties.get ('rosetta.source.path') as String
			// Create a resource set and add the common Rosetta models to it
			LOGGER.info("generatePython ... get resource set")
			val resourceSet   = resourceSetProvider.get	
			parse(ModelHelper.commonTestTypes, resourceSet)
			resourceSet.getResource(URI.createURI('classpath:/model/basictypes.rosetta'), true)
			resourceSet.getResource(URI.createURI('classpath:/model/annotations.rosetta'), true)
		
			// Get a list of all the DSL input files and filter out non-Rosetta files
			val rosettaFilePaths = newArrayList (new File(rosettaSource))
				.map[listFiles[name.endsWith("rosetta")].toList]
				.flatten
				.map[toPath]
			val resources 	   = rosettaFilePaths
				.map[resourceSet.getResource(URI.createURI(it.toString()), true)]
				.toList
			val rosettaModels  = resources
				.flatMap[contents.filter(RosettaModel)]
				.toList as Collection<RosettaModel>
			LOGGER.info ("generatePython ... found {} rosetta files in {}", rosettaModels.length.toString (), rosettaSource)					
			val generatedFiles = newHashMap
			for (model : rosettaModels) {
				val version = model.version
				LOGGER.info ("generatePython ... processing model: {}", model.name)					
				generatedFiles.putAll(generator.beforeAllGenerate(resourceSet, #{model}, version))
				generatedFiles.putAll(generator.beforeGenerate(model.eResource, model, version))
				generatedFiles.putAll(generator.generate(model.eResource, model, version))
				generatedFiles.putAll(generator.afterGenerate(model.eResource, model, version))
				generatedFiles.putAll(generator.afterAllGenerate(resourceSet, #{model}, version))
			}
			val outputPath     = properties.getProperty ('codebase.outputpath')
			deleteFolderContent(outputPath)
			writeFiles(outputPath, generatedFiles)
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
}