#!/bin/bash
type -P python > /dev/null && PYEXE=python || PYEXE=python3
if ! $PYEXE -c 'import sys; assert sys.version_info >= (3,10)' > /dev/null 2>&1; then
        echo "Found $($PYEXE -V)"
        echo "Expecting at least python 3.10 - exiting!"
        exit 1
fi

export PYTHONDONTWRITEBYTECODE=1

MYPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

ROSETTARUNTIMEDIR="../../src/main/resources/runtime"
PYTHONUNITTESTDIR="../../target/python_unit_tests"

cd $MYPATH/$PYTHONUNITTESTDIR
$PYEXE -m venv --clear .pytest
ACDIR=$($PYEXE -c "import sys;print('Scripts' if sys.platform.startswith('win') else 'bin')")
source .pytest/$ACDIR/activate

$PYEXE -m pip install 'pydantic>=2.6.1,<2.10'
$PYEXE -m pip install $MYPATH/$ROSETTARUNTIMEDIR/rosetta_runtime-2.1.0-py3-none-any.whl --force-reinstall

$PYEXE -m pip wheel --no-deps --only-binary :all: . || processError
$PYEXE -m pip install python_rosetta_dsl-0.0.0-py3-none-any.whl
$PYEXE -m pip install pytest

# run tests
$PYEXE -m pytest -p no:cacheprovider $MYPATH

rm -rf $MYPATH/.pytest