package com.regnosys.rosetta.sample;

import static com.regnosys.rosetta.sample.framework.TestHelper.toStringContents;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.hasSize;
import static org.hamcrest.Matchers.is;

import java.net.URL;
import java.util.Map;

import org.junit.jupiter.api.Test;

import com.regnosys.rosetta.generator.external.AbstractExternalGenerator;
import com.regnosys.rosetta.generator.java.RosettaJavaPackages;
import com.regnosys.rosetta.rosetta.RosettaHeader;
import com.regnosys.rosetta.rosetta.RosettaModel;
import com.regnosys.rosetta.sample.framework.TestHelper;

class GroovyCodeGeneratorTest {

	@Test
	void simpleClass() throws Exception {
		TestHelper helper = new TestHelper();
		RosettaModel model = helper.parse( this.getClass().getResource("/rosetta/sample.rosetta"));
		RosettaHeader header = model.getHeader();
		RosettaJavaPackages packages = new RosettaJavaPackages(header.getNamespace());
		GroovyCodeGenerator gen = helper.getExternalGenerator();
		Map<String, ? extends CharSequence> files = gen.generate(packages, model.getElements(), header.getVersion());
		assertGenerated(this.getClass().getResource("/groovy/Foo.groovy"), files);
	}

	private void assertGenerated(URL source, Map<String, ? extends CharSequence> map) {
		assertThat(map.entrySet(), hasSize(1));
		Map.Entry<String, ? extends CharSequence> entry = map.entrySet().iterator().next();
		System.out.println(entry.getKey());
		assertThat(entry.getKey(), is("com/rosetta/sample/model/Foo.groovy"));
		System.out.println(entry.getValue());
		assertThat(entry.getValue(), is(toStringContents(source)));
	}
}

