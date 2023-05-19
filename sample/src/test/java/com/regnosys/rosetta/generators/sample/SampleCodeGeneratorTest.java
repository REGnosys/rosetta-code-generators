package com.regnosys.rosetta.generators.sample;

import static com.regnosys.rosetta.generators.test.TestHelper.toStringContents;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.hasSize;
import static org.hamcrest.Matchers.is;
import static org.hamcrest.Matchers.equalToCompressingWhiteSpace;

import java.net.URL;
import java.util.Map;
import org.junit.jupiter.api.Test;

import com.google.common.io.Resources;
import com.regnosys.rosetta.generator.java.RosettaJavaPackages.RootPackage;
import com.regnosys.rosetta.generators.test.TestHelper;
import com.regnosys.rosetta.rosetta.RosettaModel;

class SampleCodeGeneratorTest {

	@Test
	void simpleClass() throws Exception {
		TestHelper<SampleCodeGenerator> helper = new TestHelper<>(new SampleCodeGenerator());
		URL textModel = Resources.getResource("rosetta/sample.rosetta");
		RosettaModel model = helper.parse(textModel);
		RootPackage packages = new RootPackage(model);
		SampleCodeGenerator generator = helper.getExternalGenerator();
		Map<String, ? extends CharSequence> files = generator.generate(packages, model.getElements(),
				model.getVersion());
		assertGenerated(Resources.getResource("sample/Foo.groovy.sample"), files);
	}

	private void assertGenerated(URL source, Map<String, ? extends CharSequence> map) {
		assertThat(map.entrySet(), hasSize(1));
		Map.Entry<String, ? extends CharSequence> entry = map.entrySet().iterator().next();
		assertThat(entry.getKey(), is("com/rosetta/model/Foo.sample"));
		assertThat(entry.getValue().toString(), equalToCompressingWhiteSpace(toStringContents(source)));
	}
}
