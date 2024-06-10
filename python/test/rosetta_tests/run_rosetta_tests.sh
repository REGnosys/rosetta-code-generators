#!/bin/bash
type -P python > /dev/null && PYEXE=python || PYEXE=python3
if ! $PYEXE -c 'import sys; assert sys.version_info >= (3,10)' > /dev/null 2>&1; then
        echo "Found $($PYEXE -V)"
        echo "Expecting at least python 3.10 - exiting!"
        exit 1
fi

export PYTHONDONTWRITEBYTECODE=1

MYPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $MYPATH
$PYEXE -m venv --clear .pydevenv

ACDIR=$($PYEXE -c "import sys;print('Scripts' if sys.platform.startswith('win') else 'bin')")
source .pydevenv/$ACDIR/activate

ROSETTARUNTIMEDIR="../../src/main/resources/runtime"
PYTHONUNITTESTDIR="../../target/python_unit_tests"

$PYEXE -m pip install pydantic
$PYEXE -m pip install pytest
$PYEXE -m pip install $MYPATH/$ROSETTARUNTIMEDIR/rosetta_runtime-2.1.0-py3-none-any.whl --force-reinstall

cd $MYPATH/$PYTHONUNITTESTDIR
$PYEXE -m pip wheel --no-deps --only-binary :all: . || processError
$PYEXE -m pip install python_rosetta-0.0.0-py3-none-any.whl

# run tests
pytest -p no:cacheprovider $MYPATH