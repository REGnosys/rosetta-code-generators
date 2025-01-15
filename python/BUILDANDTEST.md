# _Build and testing instructions_

1. To build the generator
##
        bash mvn clean install

2. Run the core Python Unit Tests
- Assuming the build successfully completes and all JUnit tests pass.
##
        bash test/run_tests.sh

3. To Generate CDM from Rosetta / Rune
- Update the attribute <cdm.rosetta.source.path> in python/pom.xml to point to the Rune/Rosetta files
- In PythonFilesGeneratorTest.xtend, comment the line "@Disabled("Generate CDM from Rosetta Files") (immediately before `def void generateCDMPythonFromRosetta`)
- Run the build and execute the Java Unit Test
##
        bash mvn clean install

4. To rebuild the runtime package
##
        bash src/main/resources/build_runtime.sh

5. To package the generated CDM Python
##
        bash build/build_cdm.sh

6. To test whether the generated code can read and validate a CDM JSON file

##
        bash test/cdm_tests/run_serialization_test.sh
