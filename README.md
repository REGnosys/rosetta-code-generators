# rosetta-code-generators



**Continuous Integration:** [[![Codefresh build status]( https://g.codefresh.io/api/badges/pipeline/regnosysops/REGnosys%2Frosetta-code-generators%2Frosetta-code-generators?branch=master&key=eyJhbGciOiJIUzI1NiJ9.NWE1N2EyYTlmM2JiOTMwMDAxNDRiODMz.ZDeqVUhB-oMlbZGj4tfEiOg0cy6azXaBvoxoeidyL0g&type=cf-1)]( https://g.codefresh.io/pipelines/rosetta-code-generators/builds?repoOwner=REGnosys&repoName=rosetta-code-generators&serviceName=REGnosys%2Frosetta-code-generators&filter=trigger:build~Build;branch:master;pipeline:5d0a15a6a52a3deca9db7236~rosetta-code-generators)] <br/>
**License:** [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)

Did you want to leverage the power of the Rosetta DSL for your project but in a language other than the (Java) default implementation?

You can use this guide and write your own code generator in the language of your choosing.

##### Writing a generator

To provide your own, you simply need to subclass the ``` AbstractExternalGenerator```  class and provide a concrete implementation of its generate method.

```
public abstract Map<String, ? extends CharSequence> generate(RosettaJavaPackages packages, List<RosettaRootElement> elements, String version);
```
 
There is already an example that generates Groovy source code:

```
src/main/java/com/regnosys/rosetta/sample/GroovyCodeGenerator.java
```

You can then test your code with a JUnit test, like 

```
src/test/java/com/regnosys/rosetta/sample/GroovyCodeGeneratorTest.java
```

In package ```src/test/java/com/regnosys/rosetta/sample/framework``` there is some infrastructure code 

that weaves together, using the Google Guice dependency injection mechanism, all the necessary elements to run a rosetta enabled app and then parses a sample rosetta file.

Then we filter the rosetta root elements to get the rosetta classes and then we construct a map,
 
the keys of which are the produced source code file names while the corresponding values contain the actual source for that file name

In folder ```src/test/resources/rosetta``` you can see two files: 

```types.rosetta``` contains the basic types that a rosetta DSL can contain, like  ```string```, ```int```, ```time``` etc. 

These types are used to bootstrap the rosetta enabled app.

```sample.rosetta``` contains a simple rosetta class with a few attributes of type ```string``` & ```int```

Finally, in  ```src/test/resources/groovy/Foo.groovy``` the file contains the correct source code, against which we will compare our results  


##### Clone from github and work on your own branch

You can clone this repository and create your own local branch to work on and set it to upstream, so that it is built in our codefresh CI infrastructure
 
```git clone https://github.com/REGnosys/rosetta-code-generators ```

```git checkout -b your_own_branch``` 

 ```git push --set-upstream origin your_own_branch```
 
Once your are happy with your code, your can open a PR on github and ask for your changes to be included on the master branch

```https://github.com/REGnosys/rosetta-code-generators/pulls```
