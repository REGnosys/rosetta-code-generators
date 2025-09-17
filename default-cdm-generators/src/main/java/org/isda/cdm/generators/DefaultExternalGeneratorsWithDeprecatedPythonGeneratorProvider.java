package org.isda.cdm.generators;

import java.util.Collections;
import java.util.Iterator;

import com.google.common.collect.Iterables;
import com.google.inject.Inject;
import com.google.inject.Provider;
import com.regnosys.rosetta.generator.external.ExternalGenerator;
import com.regnosys.rosetta.generator.external.ExternalGenerators;
import com.regnosys.rosetta.generator.python.PythonCodeGenerator;

/**
 * @deprecated Use {@link DefaultExternalGeneratorsProvider} instead
 */
@Deprecated
public final class DefaultExternalGeneratorsWithDeprecatedPythonGeneratorProvider implements Provider<ExternalGenerators> {

    @Inject
    private DefaultExternalGeneratorsProvider defaultExternalGeneratorsProvider;

    @Inject
    private PythonCodeGenerator pythonGenerator;

    @Override
    public ExternalGenerators get() {
        return new DefaultGenerators();
    }

    private final class DefaultGenerators implements ExternalGenerators {
        @Override
        public Iterator<ExternalGenerator> iterator() {
            return Iterables.concat(defaultExternalGeneratorsProvider.get(), Collections.singletonList(pythonGenerator)).iterator();
        }
    }
}
