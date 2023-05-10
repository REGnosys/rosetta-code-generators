package com.regnosys.rosetta.generators.sample

import com.google.inject.Inject
import com.google.inject.Provider
import com.regnosys.rosetta.tests.RosettaInjectorProvider
import org.eclipse.xtext.resource.XtextResourceSet
import org.eclipse.xtext.testing.InjectWith
import org.eclipse.xtext.testing.extensions.InjectionExtension

import org.junit.jupiter.api.Test
import org.junit.jupiter.api.^extension.ExtendWith

import static org.junit.jupiter.api.Assertions.*
import java.io.File
import java.nio.file.Files
import org.eclipse.xtext.testing.util.ParseHelper
import com.regnosys.rosetta.rosetta.RosettaModel
import com.regnosys.rosetta.rosetta.simple.Data

@ExtendWith(InjectionExtension)
@InjectWith(RosettaInjectorProvider)
class LoadRosettaModelsTest {

	@Inject extension ParseHelper<RosettaModel>

	@Inject
	Provider<XtextResourceSet> resourceSetProvider;
	
	
	@Test
	def void loadRosettaModels() {
		val resourceSet = resourceSetProvider.get
		val cdmPath = new File("../../../finos/common-domain-model/rosetta-source/src/main/rosetta")
		
		val rosettaFileContents = newArrayList(cdmPath)
			.map[listFiles[name.endsWith(".rosetta")].toList]
			.flatten
			.map[toPath]
			.map[new String(Files.readAllBytes(it))]
		
		assertEquals(86, rosettaFileContents.size)
		
		// comment out this line
		rosettaFileContents
			.forEach[parse(it, resourceSet)]
		
		val rosettaModels = rosettaFileContents
			.map[parse(it, resourceSet)]
		
		
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
		assertEquals("PriceQuantity", pqAttr.type.name)
	}
	
}