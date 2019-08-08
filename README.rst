Overview of the Rosetta Code Generators
=======================================


.. role:: raw-html(raw)
    :format: html

**Continuous Integration:** |Codefresh build status| :raw-html:`<br />`
**License:** `Apache 2.0 <http://www.apache.org/licenses/LICENSE-2.0>`_

**JavaDoc:** *Coming soon*

Did you want to leverage the power of the *Rosetta DSL* for your project but in a language other than the default (Java) implementation?

You can use this guide and write your own code generator in the language of your choosing.

What are the Rosetta Code Generators
------------------------------------

Rosetta is an open source DSL comprising a grammar and a set of default code generators (see `documentation <https://docs.rosetta-technology.io/dsl/readme.html>`_). The open source `Rosetta DSL repository <https://github.com/REGnosys/rosetta-dsl>`_ has 2 built-in code generators:

- `Java <https://www.oracle.com/java/>`_. See `code generator <https://github.com/REGnosys/rosetta-dsl/blob/master/com.regnosys.rosetta/src/com/regnosys/rosetta/generator/java/object/ModelObjectGenerator.xtend>`_
- `DAML <https://daml.com/>`_. See `code generator <https://github.com/REGnosys/rosetta-dsl/blob/master/com.regnosys.rosetta/src/com/regnosys/rosetta/generator/daml/object/DamlModelObjectGenerator.xtend>`_

The Rosetta Code Generators repository allows the community to contribute code generators in other languages: e.g. Go, Python etc.

**Note**: The DAML code generator will be moved to this repository in good time. 

It works by allowing API hooks to get access to the `Ecore <https://wiki.eclipse.org/Ecore>`_ model, which represents the model elements in the Rosetta DSL and allows to perform a model transformation. The API expects a set *Rosetta* files (with extension *.rosetta*) as input. The files are parsed and an *Ecore* model instance is produced. This Ecore model is then accessible via an API hook in this repo.

A comprehensive guide on how to write Rosetta files will be available soon.

Here is an illustration of how code generation works:

.. figure:: /images/rosetta-language-code-generation.png?raw=true


Quick start guide
-----------------

You will need `Maven <http://maven.apache.org/>`_ and `Git <https://git-scm.com/>`_ installed and configured in your envirornment.

`Fork and clone <https://help.github.com/articles/fork-a-repo>`_ the project in your own workspace. Then run the first build:

.. code-block:: Java

 /path/to/workspace/rosetta-code-generators > mvn clean install

This project follows the Maven `multi-module <https://maven.apache.org/guides/mini/guide-multiple-modules.html>`_ format, to make it easier to provide your own generator in its own separate module.

Simply come up with a sensible name for your module (it should relate to the progamming language that you want to generate code in) and run the following command:

.. code-block:: Java

 > mvn archetype:generate -DgroupId=com.regnosys.rosetta.code-generators  -DartifactId=my-language

This will create a module named after your artifactId with the appropriate maven structure and also update the parent ``pom.xml``.

Writing a generator
^^^^^^^^^^^^^^^^^^^

There is already an example module named *sample* to help you get going:  we have written a rudimentary code generator (that generates some valid `Groovy <https://groovy-lang.org/>`_ code): 

.. code-block:: Java

 sample/src/main/java/com/regnosys/rosetta/generators/sample/SampleCodeGenerator.java

Within your just created module, create your own package under ``com/regnosys/rosetta/generators`` and add your source file(s). Your generator must subclass the ``AbstractExternalGenerator`` class and provide a concrete implementation of its ``generate`` method.

.. code-block:: Java

 public abstract Map<String, ? extends CharSequence> generate(RosettaJavaPackages packages, List<RosettaRootElement> elements, String version);

Testing your generator
^^^^^^^^^^^^^^^^^^^^^^

You can then test your code with a JUnit test, like in

.. code-block:: Java

 sample/src/test/java/com/regnosys/rosetta/generators/sample/SampleCodeGeneratorTest.java

In folder ``sample/src/test/resources/rosetta`` you can see the file: ``sample.rosetta``. It contains a simple Rosetta text file with a few attributes of type ``string`` & ``int``.

Finally, the file ``sample/src/test/resources/sample/Foo.groovy.sample`` contains the correct source code, against which we will compare our results.

The ``test-helper`` module contains some infrastructure code that is used to drive the tests in the other modules. It weaves together, using the `Google Guice <https://github.com/google/guice/>`_ dependency injection mechanism, all the necessary elements to run a Rosetta-enabled application and parses a .rosetta file into the corresponding root Ecore object.

In folder ``test-helper/src/main/resources/rosetta`` you can see the file: ``types.rosetta``. It contains the basic types contained in the Rosetta DSL, like ``string``, ``int``, ``time`` etc.

These types are used to bootstrap the Rosetta-enabled application.


How to contribute
-----------------

Please read the `detailed guide </CONTRIBUTING.md>`_.

.. |Codefresh build status| image:: https://g.codefresh.io/api/badges/pipeline/regnosysops/REGnosys%2Frosetta-code-generators%2Frosetta-code-generators?branch=master&key=eyJhbGciOiJIUzI1NiJ9.NWE1N2EyYTlmM2JiOTMwMDAxNDRiODMz.ZDeqVUhB-oMlbZGj4tfEiOg0cy6azXaBvoxoeidyL0g&type=cf-1
   :target: https://g.codefresh.io/pipelines/rosetta-code-generators/builds?repoOwner=REGnosys&repoName=rosetta-code-generators&serviceName=REGnosys%2Frosetta-code-generators&filter=trigger:build~Build;branch:master;pipeline:5d0a15a6a52a3deca9db7236~rosetta-code-generators
