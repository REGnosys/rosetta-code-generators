# rosetta-code-generators
====

**Latest release: [x.y.z](https://github.com/REGnosys/rosetta-code-generators)**

**Documentation:** [User Guide](...)(...) <br/>
**Continuous Integration:** [[![Codefresh build status]( https://g.codefresh.io/api/badges/pipeline/regnosysops/REGnosys%2Frosetta-code-generators%2Frosetta-code-generators?branch=master&key=eyJhbGciOiJIUzI1NiJ9.NWE1N2EyYTlmM2JiOTMwMDAxNDRiODMz.ZDeqVUhB-oMlbZGj4tfEiOg0cy6azXaBvoxoeidyL0g&type=cf-1)]( https://g.codefresh.io/pipelines/rosetta-code-generators/builds?repoOwner=REGnosys&repoName=rosetta-code-generators&serviceName=REGnosys%2Frosetta-code-generators&filter=trigger:build~Build;branch:master;pipeline:5d0a15a6a52a3deca9db7236~rosetta-code-generators)](...) <br/>
**Mailing Lists:** [User Mailing List](...) <br/>
**License:** [Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)

Did you want to leverage the power of the Rosetta DSL for your project but in a language other than the (Java) default implementation?

You can use this guide and write your own code generator in the language of your choosing.

To provide your own, you simply need to implement the ``` ExternalGenerator```  interface.

This interface contains two methods:

The ``` getOutputConfiguration ``` method provides infrastructure for when the code is compiled, so all that is required is to return 
an ```ExternalOutputConfiguration``` object with a suitable name and description.

The actual generation is done in the ```generate``` method:

First we filter the rosetta root elements to get the rosetta classes and then we construct a map,
 
the keys of which are the produced source code file names while the corresponding values contain the actual source for that file name
 
There is already an example that generates Groovy source code:

```
src/main/java/com/regnosys/rosetta/sample/GroovyCodeGenerator.java
```

You can then test your code with a JUnit test

```
src/test/java/com/regnosys/rosetta/sample/GroovyCodeGeneratorTest.java
```
In package ```src/test/java/com/regnosys/rosetta/sample/framework``` there is some infrastructure code 

that weaves together, using the Google Guice dependency injection mechanism, all the necessary elements to run a rosetta enabled app.

In folder ```src/test/resources/rosetta``` you can see three files: 

```types.rosetta``` contains the basic types that a rosetta DSL can contain, 
like  ```string```, ```int```, ```time``` etc. 

These types are used to bootstrap the rosetta enabled app.

```sample.rosetta``` contains a simple rosetta class with a few attributes of type ```string``` & ```int```

Finally, the ```Foo.groovy``` class contains the correct source code, against which we will compare our results  

You can check out this repository using 
```git clone https://github.com/REGnosys/rosetta-code-generators ```

Create your own local branch to work on and set it to upstream, so that it is built in our codefresh CI infrastructure

```git checkout -b your_own_branch``` 

 ```git push --set-upstream origin your_own_branch```
 
...and once your are happy with your code, your can open a PR on github and ask for your changes to be included on the master branch

```https://github.com/REGnosys/rosetta-code-generators/pulls```
