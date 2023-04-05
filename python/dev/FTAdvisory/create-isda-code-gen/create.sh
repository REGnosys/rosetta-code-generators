#!/bin/sh
mkdir isda-cdm-code-gen-5.5.1 ./isda-cdm-code-gen-5.5.1/.m2 ./isda-cdm-code-gen-5.5.1/github ./isda-cdm-code-gen-5.5.1/github/REGnosys
cp ./create-isda-code-gen/settings.xml ./isda-cdm-code-gen-5.5.1/.m2/
cd ./isda-cdm-code-gen-5.5.1/github/REGnosys
git clone https://github.com/REGnosys/rosetta-code-generators.git -b 5.5.1
cp ../../../create-isda-code-gen/pom.xml ./rosetta-code-generators/
cd rosetta-code-generators
mvn -s ../../../.m2/settings.xml clean install
mvn archetype:generate -DgroupId="com.regnosys.rosetta.code-generators"  -DartifactId=python
rm -rf ./python
git clone --branch version_7.1.1 https://github.com/Cloudrisk/isda-cdm-python.git
mv isda-cdm-python python
rm -rf ./python/build/src/python_cdm.egg-info
rm ./python/build/src/cdm/__init__.py
rm ./python/build/src/cdm/version.py
rm -rf ./python/build/src/cdm/base
rm -rf ./python/build/src/cdm/event
rm -rf ./python/build/src/cdm/observable
rm -rf ./python/build/src/cdm/regulation
rm -rf ./python/build/src/cdm/legaldocumentation
rm -rf ./python/build/src/cdm/product
mvn -s ../../../.m2/settings.xml clean install
cd ./python/build
./run_test.sh
