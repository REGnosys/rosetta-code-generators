#!/bin/sh

cd /Users/dls/projects/isda-cdm-code-gen/github/REGnosys/rosetta-code-generators/python/dist
find . > /Users/dls/projects/isda-cdm-code-gen/github/REGnosys/rosetta-code-generators/python/dev/FTAdvisory/new_dir_list.txt 
cd /Users/dls/projects/isda-cdm-code-gen/github/REGnosys/rosetta-code-generators/python-bu/dist
find . >  /Users/dls/projects/isda-cdm-code-gen/github/REGnosys/rosetta-code-generators/python/dev/FTAdvisory/orig_dir_list.txt
cd  /Users/dls/projects/isda-cdm-code-gen/github/REGnosys/rosetta-code-generators/python/dev/FTAdvisory/
diff orig_dir_list.txt new_dir_list.txt > compare.txt 