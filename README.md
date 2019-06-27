# Rosetta Code Generators



**Continuous Integration:** [[![Codefresh build status]( https://g.codefresh.io/api/badges/pipeline/regnosysops/REGnosys%2Frosetta-code-generators%2Frosetta-code-generators?branch=master&key=eyJhbGciOiJIUzI1NiJ9.NWE1N2EyYTlmM2JiOTMwMDAxNDRiODMz.ZDeqVUhB-oMlbZGj4tfEiOg0cy6azXaBvoxoeidyL0g&type=cf-1)]( https://g.codefresh.io/pipelines/rosetta-code-generators/builds?repoOwner=REGnosys&repoName=rosetta-code-generators&serviceName=REGnosys%2Frosetta-code-generators&filter=trigger:build~Build;branch:master;pipeline:5d0a15a6a52a3deca9db7236~rosetta-code-generators)] <br/>
**License:** [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)

Did you want to leverage the power of the Rosetta DSL for your project but in a language other than the (Java) default implementation?

You can use this guide and write your own code generator in the language of your choosing.

### What is it

 It is a tool to translate Ecore model instances, created by parsing rosetta files, to classes in any programming language
 
 [Here is an illustration of how code generation works](/images/rosetta-language-code-generation.png)

### Writing a generator

To provide your own, you simply need to subclass the ``` AbstractExternalGenerator```  class and provide a concrete implementation of its generate method.

```
public abstract Map<String, ? extends CharSequence> generate(RosettaJavaPackages packages, List<RosettaRootElement> elements, String version);
```
 
There is already an example that generates some sample source code (it is valid Groovy code):

```
src/main/java/com/regnosys/rosetta/sample/SampleCodeGenerator.java
```

You can then test your code with a JUnit test, like 

```
src/test/java/com/regnosys/rosetta/sample/SampleCodeGeneratorTest.java
```

In package ```src/test/java/com/regnosys/rosetta/sample/framework``` there is some infrastructure code 

that weaves together, using the Google Guice dependency injection mechanism, all the necessary elements to run a rosetta enabled app and then parses a sample rosetta file.

In folder ```src/test/resources/rosetta``` you can see two files: 

```types.rosetta``` contains the basic types that a rosetta DSL can contain, like  ```string```, ```int```, ```time``` etc. 

These types are used to bootstrap the rosetta enabled app.

```sample.rosetta``` contains a simple rosetta class with a few attributes of type ```string``` & ```int```

Finally, in  ```src/test/resources/sample/Foo.groovy.sample``` the file contains the correct source code, against which we will compare our results  


### How to contribute
[Read the guide ](/CONTRIBUTING.md)
