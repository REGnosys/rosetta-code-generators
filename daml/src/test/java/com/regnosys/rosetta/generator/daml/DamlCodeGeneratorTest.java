package com.regnosys.rosetta.generator.daml;

import static com.regnosys.rosetta.generators.test.TestHelper.toStringContents;
//import static org.hamcrest.MatcherAssert.assertThat;
//import static org.hamcrest.Matchers.*;
import static org.junit.jupiter.api.Assertions.*;

import java.net.URL;
import java.util.Collections;
import java.util.Map;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import com.google.common.io.Resources;
import com.google.inject.AbstractModule;
import com.google.inject.Guice;
import com.google.inject.Injector;
import com.regnosys.rosetta.generators.test.TestHelper;
import com.regnosys.rosetta.rosetta.RosettaModel;

public class DamlCodeGeneratorTest {

	private DamlCodeGenerator codeGenerator;

	@BeforeEach
	public void setup() {
		Injector injector = Guice.createInjector(new CodeGenModule());
		codeGenerator = injector.getInstance(DamlCodeGenerator.class);
	}

	@Test
	void simpleClass() throws Exception {
		TestHelper<DamlCodeGenerator> helper = new TestHelper<>(codeGenerator);
		URL textModel = Resources.getResource("rosetta/sample.rosetta");
		RosettaModel model = helper.parse(textModel);
		DamlCodeGenerator generator = helper.getExternalGenerator();
		Map<String, ? extends CharSequence> files = generator.afterGenerate(Collections.singletonList(model));
		assertGenerated(Resources.getResource("sample/Classes.daml"), files);
	}

	private void assertGenerated(URL source, Map<String, ? extends CharSequence> map) {
		assertEquals(4, map.entrySet().size());
		assertTrue(map.containsKey("Org/Isda/Cdm/Classes.daml"));
		assertEquals(toStringContents(source), map.get("Org/Isda/Cdm/Classes.daml"));
	}

	class CodeGenModule extends AbstractModule {

		@Override
		protected void configure() {
		}

	}
}
