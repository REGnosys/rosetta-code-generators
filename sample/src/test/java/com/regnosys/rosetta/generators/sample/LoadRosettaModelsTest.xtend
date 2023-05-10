package com.regnosys.rosetta.generators.sample

import com.google.inject.Inject
import com.google.inject.Provider
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import java.io.File
import java.nio.file.Files
import org.eclipse.emf.common.util.URI
import org.eclipse.xtext.resource.XtextResourceSet
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension
import org.eclipse.xtext.testing.util.ParseHelper
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*
import java.util.List

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class LoadRosettaModelsTest {

	@Inject extension ParseHelper<RosettaModel>

	@Inject
	Provider<XtextResourceSet> resourceSetProvider;
	
	@Test
	def void shouldLoadRosettaModelsWithParseHelper_SingleParse() {
		val rosettaFilePaths = getRosettaFilePaths()
		
		val resourceSet = resourceSetProvider.get
		
		// read file contents, so they can be parsed
		val rosettaFileContents = rosettaFilePaths
			.map[new String(Files.readAllBytes(it))]
			.toList
		
		assertEquals(86, rosettaFileContents.size)
		
		// parse once
		val rosettaModels = rosettaFileContents
			.map[parse(it, resourceSet)]
		
		// assert TradeLot / PriceQuantity
		assertTradeLotAttributes(rosettaModels, null)
	}
	
	@Test
	def void shouldLoadRosettaModelsWithParseHelper_DoubleParse() {
		val rosettaFilePaths = getRosettaFilePaths()
		
		val resourceSet = resourceSetProvider.get
		
		// read file contents, so they can be parsed
		val rosettaFileContents = rosettaFilePaths
			.map[new String(Files.readAllBytes(it))]
			.toList
		
		assertEquals(86, rosettaFileContents.size)
		
		// parse once....
		rosettaFileContents
			.forEach[parse(it, resourceSet)]
		
		// then re-parse, and it all works
		val rosettaModels = rosettaFileContents
			.map[parse(it, resourceSet)]
		
		// assert TradeLot / PriceQuantity
		assertTradeLotAttributes(rosettaModels, "PriceQuantity")
	}
	
	@Test
	def void shouldLoadRosettaModelsWithGetResource() {
		val rosettaFilePaths = getRosettaFilePaths()
		
		val resourceSet = resourceSetProvider.get
		
		// Load resources using getResource (TODO check Path.toString() works on Windows)
		val resources = rosettaFilePaths
			.map[resourceSet.getResource(URI.createURI(it.toString()), true)]
			.toList
					
		assertEquals(86, resources.size)
		
		val rosettaModels = resources
			.flatMap[contents.filter(RosettaModel)]
			.toList
		
		// assert TradeLot / PriceQuantity
		assertTradeLotAttributes(rosettaModels, "PriceQuantity")
	}
	
	private def getRosettaFilePaths() {
		// TODO write test with local rosetta
		val cdmPath = new File("../../../finos/common-domain-model/rosetta-source/src/main/rosetta")
		
		return newArrayList(cdmPath)
			.map[listFiles[name.endsWith(".rosetta")].toList]
			.flatten
			.map[toPath]
	}
	
	private def void assertTradeLotAttributes(List<RosettaModel> rosettaModels, String expectedType) {
		val tradeLot = rosettaModels
			.map[elements]
			.flatten
			.filter(Data)
			.filter[it.name == "TradeLot"]
			.toList.get(0)
		
		println(tradeLot)
		
		assertEquals(2, tradeLot.attributes.size)
		
		val pqAttr = tradeLot.attributes.get(1)
		
		println(pqAttr)
		
		println(pqAttr.type.name)
		assertEquals(expectedType, pqAttr.type.name)
	}
}
