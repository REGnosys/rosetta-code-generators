# ISDA CDM Python Implementation

This repository contains both a Python CDM implementation and the code to generate the package from Regnosys' Rosetta specifications.  
 
The Python package can both deserialize CDM into objects and serialize objects with a caveat.  Ingestion of CDM flattens any use of metadata abstraction and, as a result, serialized CDM will not match a source which makes use of metadata objects.

The implementation follows the same approach as those completed for other languages such as C# in that it does not include the complete scope of functionality available in the Java implementation.

The Python package supports CDM version XXX and requires Python version 3.9+.

The code to create the Python package supports Rosetta DSL version 4.44.0 and Rosetta Bundle version 3.13.0.

## License

[License terms](<https://portal.cdm.rosetta-technology.io/#/terms-isda>) 

## Contributors
- [CloudRisk](https://www.cloudrisk.uk)
- [TradeHeader SL](https://www.tradeheader.com)
- FT Advisory LLC

## Repository Organization

Root (this README, project configuration files)
  - dist (Python code to read and write CDM, Unit and Functional tests)
  - docker 
  - documentation 
  - src  (Java code to generate Python from the Rosetta CDM definitions) 

# Python Package

The dist directory contains the generated Python code in the src subdirectory, a script to build the Python package (build.sh), unit tests in the test directory and a script to execute these tests. 

The unit tests in the pytests directory leverage the pytest package to confirm that the implementation successfully supports Rosetta semantics.  Additionally, the pytests directory contain tests that confirm that certain CDM functionality works as expected.

## Installation, Unit and Functional Tests 

Executing build.sh will create a python package (i.e., python_cdm-2.182.3-py3-none-any.whl) which can then be instaalled using pip.
Executing pytests.sh will run the above unit tests. 

The scripts assume access to Python (ver 3.9+).

## Containerized build and tests of the Python package

The Root directory contains Dockerfile definition to containerize the build, intallation and testing processes of the generated Python code.

Requires generated python code under dist/src
From Root directory:
- Run 'docker build -t image:tag .'
- Run 'docker run -it image:tag sh' to enter the container in interactive mode
- Run 'docker run image:tag

For example:

```
docker build -t rosetta-codegen:0.0.1 .
docker run rosetta-codegen:0.0.1
```
This should result in the unit tests having been sucessfully run.

## Example

See To demonstrate usage 

An example of how to create a swap ...

# Generation 

At present, the only way to generate the Python code itself is by running a unit test in a development environment.

The following instructions are based on directions found at:

[https://github.com/REGnosys/rosetta-code-generators](https://github.com/REGnosys/rosetta-code-generators)

[https://github.com/REGnosys/rosetta-code-generators/issues/149](https://github.com/REGnosys/rosetta-code-generators/issues/149)

## Prerequisites

[Eclipse 2021 (JSEE) + xtend support Eclipse IDE for Java and DSL Developers](https://www.eclipse.org/downloads/packages/release/2021-12/r/eclipse-ide-java-and-dsl-developers)

[Git](https://git-scm.com/)

[Maven](http://maven.apache.org/)

## Installation Steps

1. Create a directory structure hereafter referred to as [CODEGEN]
```
mkdir [CODEGEN]
mkdir [CODEGEN]/.m2
mkdir [CODEGEN]/github
mkdir [CODEGEN]/github/REGnosys
```

2. Fork and clone the Rosetta CDM repository 

Fork a copy from https://github.com/REGnosys/rosetta-code-generators ([MYREPO])

```
cd [CODEGEN]/github/REGnosys/
git clone https://github.com/[MYREPO]/rosetta-code-generators.git
```

3. Download settings.xml from the below link to .m2 directory and update for your repository path

[settings.xml](https://github.com/REGnosys/rosetta-code-generators/issues/149#issuecomment-1151680983)

save to [CODEGEN]/.m2/settings.xml

Edit settings.xml and update <localRepository> to [CODEGEN]/.m2/repository. 

```
<localRepository>[CODEGEN]/.m2/repository</localRepository>
```

4. Run a clean maven install 

```
cd [CODEGEN]/github/REGnosys/rosetta-code-generators
mvn -s [CODEGEN]/.m2/settings.xml clean install
```
All the tests should pass.

5. Create a Python project

```
mvn archetype:generate -DgroupId=com.regnosys.rosetta.code-generators  -DartifactId=python
```
Take the defaults for all of the prompts

6. Fork and clone the Python codebase and run a maven clean install

Fork a copy from https://github.com/Cloudrisk/isda-cdm-python.git to your own repo referred to as [MYPYTHONREPO] 

```
cd [CODEGEN]/github/REGnosys/rosetta-code-generators/python
git clone https://github.com/[MYPYTHONREPO]/isda-cdm-python.git
```
Copy the contents of the repo to the working directory

```
cp -Rf ./isda-cdm-python/***** ./
cp -Rf ./isda-cdm-python/.***** ./
```

Run a maven clean install
```
mvn -s [CODEGEN]/.m2/settings.xml clean install
```
(tbc but likely to fail)

7. Update properties in the parent pom.xml (located in [CODEGEN]/github/REGnosys/rosetta-code-generators)

Change the Rosetta versions to those currently supported in the Python code:

- set rosetta.dsl.version to 4.44.0 in all places
  <rosetta.dsl.version>4.44.0</rosetta.dsl.version>
        
- set rosetta.bundle.version to 3.13.0  
  <rosetta.bundle.version>3.13.0</rosetta.bundle.version>

Optionally comment out modules for other languages to speed up compilation and runtime

```
    <!--mdule>sample</!module-->
    <!--module>daml</!module-->
    <!--mdule>default-cdm-generators</!module-->
    <!--module>typescript</module-->
    <!--module>scala</module-->
    <!--module>golang</module-->
    <!--module>c-sharp</module-->
```
8. Open in eclipse  

- Import an existing maven project
- Update maven user preferences to use settings.xml as created above: [CODEGEN]/.m2/settings.xml
- Update java version to 11

8. To generate the Python implementation of CDM

Run PythonFilesGeneratorTest.xtend as a JUnit test

There should be one test which passes