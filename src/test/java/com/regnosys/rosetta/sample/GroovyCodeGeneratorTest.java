package com.regnosys.rosetta.sample;

import static com.regnosys.rosetta.sample.framework.TestHelper.toStringContents;
import static org.hamcrest.MatcherAssert.assertThat;
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
		// TODO use a different technique, ie. a Captor
		URL pathToClass = this.getClass().getResource("/rosetta/Foo.groovy");
		Consumer<Map<String, ? extends CharSequence>> consumer = map -> {
			map.entrySet().forEach(e -> {
				System.out.println(e.getKey());
				assertThat(e.getKey(), is("com/rosetta/sample/model/Foo.groovy"));
				System.out.println(e.getValue());
				assertThat(e.getValue(), is(toStringContents(pathToClass)));
			});
		};
		gen.generate(packages, model.getElements(), header.getVersion(), consumer, model.eResource());
	}
}
