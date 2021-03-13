# Kotlin code generator

setup JAVA_HOME

> echo $JAVA_HOME 
> /home/vincent/.jdks/adopt-openjdk-1.8.0_275


To launch a unit test:

`mvn test -pl kotlin -Dtest=KotlinModelObjectGeneratorTest#shouldGenerateEnums`

into /home/vincent/devel/vjuge/rosetta-code-generators:

 `mvn -pl kotlin clean test -Dtest=com.regnosys.rosetta.generator.kotlin.KotlinModelObjectGeneratorTest && cp kotlin/cdm/*.kt ../../kotlin-pure-cdm/src/commonMain/kotlin/org/isda/cdm`
