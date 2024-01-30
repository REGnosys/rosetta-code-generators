package com.regnosys.rosetta.generator.python.func;

import com.regnosys.rosetta.rosetta.RosettaEnumValueReference;
import com.regnosys.rosetta.rosetta.RosettaExternalFunction;
import com.regnosys.rosetta.rosetta.RosettaSymbol;
import com.regnosys.rosetta.rosetta.expression.InlineFunction;
import com.regnosys.rosetta.rosetta.expression.ListLiteral;
import com.regnosys.rosetta.rosetta.expression.RosettaBinaryOperation;
import com.regnosys.rosetta.rosetta.expression.RosettaConditionalExpression;
import com.regnosys.rosetta.rosetta.expression.RosettaFeatureCall;
import com.regnosys.rosetta.rosetta.expression.RosettaFunctionalOperation;
import com.regnosys.rosetta.rosetta.expression.RosettaLiteral;
import com.regnosys.rosetta.rosetta.expression.RosettaOnlyExistsExpression;
import com.regnosys.rosetta.rosetta.expression.RosettaReference;
import com.regnosys.rosetta.rosetta.expression.RosettaSymbolReference;
import com.regnosys.rosetta.rosetta.expression.RosettaUnaryOperation;
import com.regnosys.rosetta.rosetta.simple.Data;
import com.regnosys.rosetta.rosetta.simple.Function;
import com.regnosys.rosetta.rosetta.RosettaEnumeration;
import com.regnosys.rosetta.types.RFunction;
import com.regnosys.rosetta.rosetta.expression.RosettaExpression;
import com.regnosys.rosetta.rosetta.RosettaRule;
import org.eclipse.emf.ecore.EObject;
import org.eclipse.xtext.EcoreUtil2;
import javax.inject.Inject;
import com.regnosys.rosetta.types.RObjectFactory;
import java.util.Set;
import com.google.common.collect.Sets;
import java.util.HashSet
import com.regnosys.rosetta.rosetta.expression.RosettaConstructorExpression

/**
 * A class that helps determine which Rosetta dependencies a Rosetta object refers to
 */
class FunctionDependencyProvider {
    @Inject 
    RObjectFactory rTypeBuilderFactory;

    private Set<EObject> visited = new HashSet<EObject>();

    def Set<EObject> dependencies(EObject object) {
        if (visited.contains(object)) {
            return newHashSet();
        }
        visited.add(object);

        try {
            switch object {
                RosettaBinaryOperation: {
                    newHashSet(dependencies(object.left) + dependencies(object.right))
                }
                RosettaConditionalExpression: {
                    newHashSet(
                        dependencies(object.^if) + dependencies(object.ifthen) +
                            dependencies(object.elsethen))
                }
                RosettaOnlyExistsExpression: {
                    dependencies(object.args)
                }
                RosettaFunctionalOperation: {
                    newHashSet(dependencies(object.argument) + dependencies(object.function))
                }
                RosettaUnaryOperation: {
                    dependencies(object.argument)
                }
                RosettaFeatureCall:
                    dependencies(object.receiver)
                RosettaSymbolReference: {
                    newHashSet(dependencies(object.symbol) + dependencies(object.args))
                }
                Function, Data, RosettaEnumeration: {
                    newHashSet(object)
                }
                InlineFunction: {
                    dependencies(object.body)
                }
                ListLiteral: {
                    newHashSet(object.elements.flatMap[dependencies])
                }
                RosettaConstructorExpression: {
                    val typeDependencies = if (object.typeCall?.type !== null) newHashSet(object.typeCall.type) else newHashSet()
                    val keyValuePairsDependencies = object.values.map[valuePair | dependencies(valuePair.value)].flatten
                    newHashSet(typeDependencies + keyValuePairsDependencies)
                }
                RosettaExternalFunction,
                RosettaEnumValueReference,
                RosettaLiteral,
                RosettaReference,
                RosettaSymbol:
                    newHashSet()
                default:
                    if (object !== null)
                        throw new IllegalArgumentException('''«object?.eClass?.name» is not covered yet.''')
                    else
                        newHashSet()
            }
        } finally {
            visited.remove(object);
        }
    }

    def Set<EObject> dependencies(Iterable<? extends EObject> objects) {
        val allDependencies = objects.map[object | dependencies(object)].flatten.toSet
        newHashSet(allDependencies)
    }

    def Set<RFunction> rFunctionDependencies(RosettaExpression expression) {
        val rosettaSymbols = EcoreUtil2.eAllOfType(expression, RosettaSymbolReference).map[it.symbol]
        (rosettaSymbols.filter(Function).map[rTypeBuilderFactory.buildRFunction(it)] +
            rosettaSymbols.filter(RosettaRule).map[rTypeBuilderFactory.buildRFunction(it)]).toSet
    }

    def Set<RFunction> rFunctionDependencies(Iterable<? extends RosettaExpression> expressions) {
        val allFunctionDependencies = expressions.flatMap [
            rFunctionDependencies
        ].toSet
        newHashSet(allFunctionDependencies)
    }

    // Reset the visited set if you want to reuse this provider
    def void reset() {
        visited.clear();
    }
}
