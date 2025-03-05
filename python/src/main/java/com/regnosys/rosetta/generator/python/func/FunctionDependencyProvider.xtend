package com.regnosys.rosetta.generator.python.func;

import com.regnosys.rosetta.rosetta.RosettaEnumValueReference
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import com.regnosys.rosetta.rosetta.RosettaExternalFunction
import com.regnosys.rosetta.rosetta.RosettaRule
import com.regnosys.rosetta.rosetta.RosettaSymbol
import com.regnosys.rosetta.rosetta.expression.InlineFunction
import com.regnosys.rosetta.rosetta.expression.ListLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaBinaryOperation
import com.regnosys.rosetta.rosetta.expression.RosettaConditionalExpression
import com.regnosys.rosetta.rosetta.expression.RosettaConstructorExpression
import com.regnosys.rosetta.rosetta.expression.RosettaExpression
import com.regnosys.rosetta.rosetta.expression.RosettaFeatureCall
import com.regnosys.rosetta.rosetta.expression.RosettaFunctionalOperation
import com.regnosys.rosetta.rosetta.expression.RosettaLiteral
import com.regnosys.rosetta.rosetta.expression.RosettaOnlyExistsExpression
import com.regnosys.rosetta.rosetta.expression.RosettaReference
import com.regnosys.rosetta.rosetta.expression.RosettaSymbolReference
import com.regnosys.rosetta.rosetta.expression.RosettaUnaryOperation
import com.regnosys.rosetta.rosetta.expression.RosettaDeepFeatureCall
import com.regnosys.rosetta.rosetta.simple.Data
import com.regnosys.rosetta.rosetta.simple.Function
import com.regnosys.rosetta.types.RFunction
import com.regnosys.rosetta.types.RObjectFactory
import java.util.HashSet
import java.util.Set
import javax.inject.Inject
import org.eclipse.emf.ecore.EObject
import org.eclipse.xtext.EcoreUtil2

/**
 * Determine the Rosetta dependencies for a Rosetta object
 */
class FunctionDependencyProvider {
    @Inject RObjectFactory rTypeBuilderFactory;

    Set<EObject> visited = new HashSet<EObject>();

    var dependencies = null as Set<EObject>;

    def Set<EObject> findDependencies(EObject object) {
        if (visited.contains(object)) {
            return newHashSet();
        }
        return generateDependencies(object);
    }

    def Set<EObject> generateDependencies(EObject object) {
        switch object {
            RosettaBinaryOperation: {
                dependencies = newHashSet(
                    generateDependencies(object.left) + generateDependencies(object.right)
                )
            }
            RosettaConditionalExpression: {
                dependencies = newHashSet(
                    generateDependencies(object.^if) + generateDependencies(object.ifthen) +
                        generateDependencies(object.elsethen))
            }
            RosettaOnlyExistsExpression: {
                dependencies = findDependenciesFromIterable(object.args)
            }
            RosettaFunctionalOperation: {
                dependencies = newHashSet(generateDependencies(object.argument) + generateDependencies(object.function))
            }
            RosettaUnaryOperation: {
                dependencies = generateDependencies(object.argument)
            }
            RosettaFeatureCall:
                dependencies = generateDependencies(object.receiver)
            RosettaSymbolReference: {
                dependencies = newHashSet(generateDependencies(object.symbol) +
                    findDependenciesFromIterable(object.args))
            }
            Function,
            Data,
            RosettaEnumeration: {
                dependencies = newHashSet(object)
            }
            InlineFunction: {
                dependencies = generateDependencies(object.body)
            }
            ListLiteral: {
                dependencies = newHashSet(object.elements.flatMap[generateDependencies])
            }
            RosettaConstructorExpression: {
                val typeDependencies = (object.typeCall?.type !== null) ? newHashSet(
                        object.typeCall.type) : newHashSet()
                val keyValuePairsDependencies = object.values.map[valuePair|generateDependencies(valuePair.value)].
                    flatten
                dependencies = newHashSet(typeDependencies + keyValuePairsDependencies)
            }
            RosettaExternalFunction,
            RosettaEnumValueReference,
            RosettaLiteral,
            RosettaReference,
            RosettaSymbol,
            RosettaDeepFeatureCall:
                dependencies = newHashSet()
            default:
                if (object !== null)
                    throw new IllegalArgumentException('''«object?.eClass?.name»: generating dependency in a function for this type is not yet implemented.''')
                else
                    dependencies = newHashSet()
        }
        if (dependencies !== null) {
            visited.add(object)
        }
        return dependencies
    }

    def Set<EObject> findDependenciesFromIterable(Iterable<? extends EObject> objects) {
        val allDependencies = objects.map[object|generateDependencies(object)].flatten.toSet
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

    def void reset() {
        visited.clear();
    }
}
