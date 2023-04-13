#!/bin/sh

parent=$(dirname $PWD)
abs_parent=$(realpath "$parent")
rm -rf "$abs_parent/isda-cdm-code-gen-5.5.1/github/REGnosys/rosetta-code-generators/python/dev/FTAdvisory/create-isda-code-gen"
cp -Rf  "$abs_parent/create-isda-code-gen" "$abs_parent/isda-cdm-code-gen-5.5.1/github/REGnosys/rosetta-code-generators/python/dev/FTAdvisory/create-isda-code-gen"