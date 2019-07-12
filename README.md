# Rosetta Code Generators



**Continuous Integration:**[![Codefresh build status]( https://g.codefresh.io/api/badges/pipeline/regnosysops/REGnosys%2Frosetta-code-generators%2Frosetta-code-generators?branch=master&key=eyJhbGciOiJIUzI1NiJ9.NWE1N2EyYTlmM2JiOTMwMDAxNDRiODMz.ZDeqVUhB-oMlbZGj4tfEiOg0cy6azXaBvoxoeidyL0g&type=cf-1)]( https://g.codefresh.io/pipelines/rosetta-code-generators/builds?repoOwner=REGnosys&repoName=rosetta-code-generators&serviceName=REGnosys%2Frosetta-code-generators&filter=trigger:build~Build;branch:master;pipeline:5d0a15a6a52a3deca9db7236~rosetta-code-generators) <br/>
**License:** [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)

**JavaDoc:** _Coming soon_

Did you want to leverage the power of the *Rosetta* DSL for your project but in a language other than the (Java) default implementation?

You can use this guide and write your own code generator in the language of your choosing.

### What is it

*Rosetta* is an open source DSL comprising a grammar and a set of code generators. To learn more, visit the [*Rosetta DSL* repository](https://github.com/REGnosys/rosetta-dsl), which is also public.

The DSL repository has 2 built-in code generators:
 - [Java](https://www.oracle.com/java/).  See code generator [here](https://github.com/REGnosys/rosetta-dsl/blob/master/com.regnosys.rosetta/src/com/regnosys/rosetta/generator/java/object/ModelObjectGenerator.xtend)
 - [DAML](https://daml.com/). See code generator [here](https://github.com/REGnosys/rosetta-dsl/blob/master/com.regnosys.rosetta/src/com/regnosys/rosetta/generator/daml/object/DamlModelObjectGenerator.xtend)

The DAML code generator will be moved to this repository in good time. 

This repository allows the *Rosetta* community to contribute code generators e.g. Go, Python etc. It works by allowing API hooks to get access to the [Ecore](https://wiki.eclipse.org/Ecore) model which represents the data elements in the *Rosetta* DSL, and allows you to perform a model transformation.

The API expects an input of a set *Rosetta* files (with extension .rosetta). We are putting together a comprehensive guide on how to write *Rosetta* files and will be available soon.

The *Rosetta* files are parsed and an Ecore model instance is produced. This Ecore Model is then accessible via an API hook in this repo.

![Here is an illustration of how code generation works](/images/rosetta-language-code-generation.png?raw=true)


### Quick start guide
You will need [Maven] and [Git] installed and configured in your envirornment.

[Fork and clone] the project in your own workspace.
Then run the first build;

```
  /path/to/workspace/rosetta-code-generators > mvn clean install
```
This project follows the Maven [multi-module](https://maven.apache.org/guides/mini/guide-multiple-modules.html) format, to make it easier to provide your own generator in its own separate module.

Simply come up with a sensible name for your module (that is, one relating to the progamming language that you want to generate code in!) and run the following command:

```
  > mvn archetype:generate -DgroupId=com.regnosys.rosetta.code-generators  -DartifactId=my-language
```

This will create a module named after your artifactId with the appropriate maven structure and also update the parent ```pom.xml```.

#### Writing a generator

There is already an example module named *sample* to help you get going:  we have written a rudimentary code generator (that generates some valid [Groovy](https://groovy-lang.org/) code): 

```
sample/src/main/java/com/regnosys/rosetta/generators/sample/SampleCodeGenerator.java
```

Within your just created module, create your own package under ```com/regnosys/rosetta/generators``` and add your source file(s).
Your generator must subclass the ``` AbstractExternalGenerator```  class and provide a concrete implementation of its generate method.

```
public abstract Map<String, ? extends CharSequence> generate(RosettaJavaPackages packages, List<RosettaRootElement> elements, String version);
```

#### Testing your generator

You can then test your code with a JUnit test, like in

```
sample/src/test/java/com/regnosys/rosetta/generators/sample/SampleCodeGeneratorTest.java
```

In folder ```sample/src/test/resources/rosetta``` you can see the file

```sample.rosetta```: it contains a simple rosetta text file with a few attributes of type ```string``` & ```int```

Finally, file ```sample/src/test/resources/sample/Foo.groovy.sample```contains the correct source code, against which we will compare our results.

Module ```test-helper``` contains some infrastructure code that is used to drive the tests in the other modules.

It weaves together, using the [Google Guice](https://github.com/google/guice/) dependency injection mechanism, all the necessary elements to run a rosetta enabled app and parses a rosetta file to the corresponding root Ecore object.

In folder ```test-helper/src/main/resources/rosetta``` you can see the file

```types.rosetta```: it contains the basic types that a rosetta DSL can contain, like  ```string```, ```int```, ```time``` etc.

These types are used to bootstrap the rosetta enabled app.



### How to contribute
[Please read the detailed guide](/CONTRIBUTING.md)

[Maven]: http://maven.apache.org/
[Git]: https://git-scm.com/
[Fork and clone]: https://help.github.com/articles/fork-a-repo
