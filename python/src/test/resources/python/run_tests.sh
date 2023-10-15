#!/bin/bash
type -P python > /dev/null && PYEXE=python || PYEXE=python3
if ! $PYEXE -c 'import sys; assert sys.version_info >= (3,10)' > /dev/null 2>&1; then
        echo "Found $($PYEXE -V)"
        echo "Expecting at least python 3.10 - exiting!"
        exit 1
fi

MYPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROSETTARUNTIMEDIR=" ../../../main/resources/runtime"
cd $MYPATH

ACDIR=$(python -c "import sys;print('Scripts' if sys.platform.startswith('win') else 'bin')")

rm -rf testenv
$PYEXE -m venv --clear testenv
source testenv/$ACDIR/activate

$PYEXE -m pip install "pydantic==1.*"
$PYEXE -m pip install pytest
$PYEXE -m pip install $MYPATH/$ROSETTARUNTIMEDIR/rosetta_runtime-2.0.0-py3-none-any.whl 
pytest
rm -rf testenv .pytest_cache __pycache__ build