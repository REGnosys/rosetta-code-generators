package com.regnosys.rosetta.generator.daml;

import static com.regnosys.rosetta.generators.test.TestHelper.toStringContents;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.equalToCompressingWhiteSpace;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.net.URL;
import java.util.Collections;
import java.util.Map;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.google.common.io.Resources;
import com.google.inject.AbstractModule;
import com.google.inject.Injector;
import com.regnosys.rosetta.generators.test.TestHelper;
import com.regnosys.rosetta.rosetta.RosettaModel;
import com.regnosys.rosetta.tests.RosettaInjectorProvider;

public class DamlCodeGeneratorTest {

	private DamlCodeGenerator codeGenerator;

	@BeforeEach
	public void setup() {
		Injector injector = new RosettaInjectorProvider().getInjector();
		codeGenerator = injector.getInstance(DamlCodeGenerator.class);
	}

	@Test
	void simpleClass() throws Exception {
		TestHelper<DamlCodeGenerator> helper = new TestHelper<>(codeGenerator);
		URL textModel = Resources.getResource("rosetta/sample.rosetta");
		RosettaModel model = helper.parse(textModel);
		DamlCodeGenerator generator = helper.getExternalGenerator();
		Map<String, ? extends CharSequence> files = generator.afterAllGenerate(model.eResource().getResourceSet(), Collections.singletonList(model), "test");
		assertGenerated(Resources.getResource("sample/Classes.daml"), files);
	}

	private void assertGenerated(URL source, Map<String, ? extends CharSequence> map) {
		assertEquals(6, map.entrySet().size());
		assertTrue(map.containsKey("Org/Isda/Cdm/Classes.daml"));
		assertThat(map.get("Org/Isda/Cdm/Classes.daml").toString(), equalToCompressingWhiteSpace(toStringContents(source)));
	}

	class CodeGenModule extends AbstractModule {

		@Override
		protected void configure() {
		}

	}
}
