# Rosetta Code Generators


**License:** [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)

Did you want to leverage the power of the Rosetta DSL for your project but in a language other than the (Java) default implementation?

You can use this guide and write your own code generator in the language of your choosing.

### What is it

 It is a tool to translate Ecore model instances, created by parsing rosetta files, to any programming language

 Here is an illustration of how code generation works
 
 [[https://github.com/REGnosys/rosetta-code-generators/blob/master/images/rosetta-language-code-generation.png|alt=how code generation works]]

### Writing a generator

To provide your own, simply create a new package under ``` src/main/java/com/regnosys/rosetta/generators/``` 
and subclass the ``` AbstractExternalGenerator```  class and provide a concrete implementation of its generate method.

```
public abstract Map<String, ? extends CharSequence> generate(RosettaJavaPackages packages, List<RosettaRootElement> elements, String version);
```

There is already an example that generates some sample source code (it is valid Groovy code):

```
src/main/java/com/regnosys/rosetta/generators/sample/SampleCodeGenerator.java
```

You can then test your code with a JUnit test, like

```
src/test/java/com/regnosys/rosetta/generators/sample/SampleCodeGeneratorTest.java
```

In package ```src/test/java/com/regnosys/rosetta/generators/framework``` there is some infrastructure code

that weaves together, using the Google Guice dependency injection mechanism, all the necessary elements to run a rosetta enabled app and then parses a sample rosetta file.

In folder ```src/test/resources/rosetta``` you can see two files:

```types.rosetta``` contains the basic types that a rosetta DSL can contain, like  ```string```, ```int```, ```time``` etc.

These types are used to bootstrap the rosetta enabled app.

```sample.rosetta``` contains a simple rosetta class with a few attributes of type ```string``` & ```int```

Finally, in  ```src/test/resources/sample/Foo.groovy.sample``` the file contains the correct source code, against which we will compare our results  


### How to contribute
[Please read the guide ](/CONTRIBUTING.md)
