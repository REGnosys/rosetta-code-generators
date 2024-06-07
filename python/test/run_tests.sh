#!/bin/bash
MYPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $MYPATH
./rosetta_tests/run_rosetta_tests.sh
./cdm_tests/run_cdm_tests.sh
./runtime_tests/run_runtime_tests.sh