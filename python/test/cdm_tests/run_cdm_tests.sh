#!/bin/bash
type -P python > /dev/null && PYEXE=python || PYEXE=python3
if ! $PYEXE -c 'import sys; assert sys.version_info >= (3,10)' > /dev/null 2>&1; then
        echo "Found $($PYEXE -V)"
        echo "Expecting at least python 3.10 - exiting!"
        exit 1
fi

export PYTHONDONTWRITEBYTECODE=1

ACDIR=$($PYEXE -c "import sys;print('Scripts' if sys.platform.startswith('win') else 'bin')")
$PYEXE -m venv --clear .pytest
source .pytest/$ACDIR/activate

MYPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROSETTARUNTIMEDIR="../../src/main/resources/runtime"
PYTHONCDMDIR="../../target/python"
$PYEXE -m pip install 'pydantic==2.6.1,<2.10'
$PYEXE -m pip install pytest
$PYEXE -m pip install $MYPATH/$ROSETTARUNTIMEDIR/rosetta_runtime-2.1.0-py3-none-any.whl 

# install cdm package
$PYEXE -m pip install $MYPATH/$PYTHONCDMDIR/python_cdm-*-py3-none-any.whl

# run tests
$PYEXE -m pytest -p no:cacheprovider $MYPATH
rm -rf .pytest