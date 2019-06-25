package com.regnosys.rosetta.sample;

import static com.regnosys.rosetta.sample.framework.TestHelper.toStringContents;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.hasSize;
import static org.hamcrest.Matchers.is;

import java.net.URL;
import java.util.Map;
import java.util.function.Consumer;

import org.junit.jupiter.api.Test;

import com.regnosys.rosetta.generator.external.ExternalGenerator;
import com.regnosys.rosetta.generator.java.RosettaJavaPackages;
import com.regnosys.rosetta.rosetta.RosettaHeader;
import com.regnosys.rosetta.rosetta.RosettaModel;
import com.regnosys.rosetta.sample.framework.TestHelper;

class GroovyCodeGeneratorTest {

	@Test
	void singleAttributeClass() throws Exception {
		URL pathToRosetta = this.getClass().getResource("/rosetta/sample.rosetta");
		TestHelper helper = new TestHelper();
		RosettaModel model = helper.parse(pathToRosetta);
		RosettaHeader header = model.getHeader();
		RosettaJavaPackages packages = new RosettaJavaPackages(header.getNamespace());
		ExternalGenerator gen = new GroovyCodeGenerator();
		// TODO improve this
		URL generatedSource = this.getClass().getResource("/rosetta/Foo.groovy");
		Consumer<Map<String, ? extends CharSequence>> consumer = map -> validate(generatedSource, map);
		gen.generate(packages, model.getElements(), header.getVersion(), consumer, model.eResource());
	}

	private void validate(URL generated, Map<String, ? extends CharSequence> map) {
		assertThat(map.entrySet(), hasSize(1));
		Map.Entry<String, ? extends CharSequence> entry = map.entrySet().iterator().next();
		System.out.println(entry.getKey());
		assertThat(entry.getKey(), is("com/rosetta/sample/model/Foo.groovy"));
		System.out.println(entry.getValue());
		assertThat(entry.getValue(), is(toStringContents(generated)));
	}
}

