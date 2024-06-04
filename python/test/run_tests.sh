#!/bin/bash
type -P python > /dev/null && PYEXE=python || PYEXE=python3
if ! $PYEXE -c 'import sys; assert sys.version_info >= (3,10)' > /dev/null 2>&1; then
        echo "Found $($PYEXE -V)"
        echo "Expecting at least python 3.10 - exiting!"
        exit 1
fi

export PYTHONDONTWRITEBYTECODE=1

ACDIR=$($PYEXE -c "import sys;print('Scripts' if sys.platform.startswith('win') else 'bin')")
$PYEXE -m venv --clear .pydevenv
source .pydevenv/$ACDIR/activate

MYPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROSETTARUNTIMEDIR="../src/main/resources/runtime"
PYTHONUNITTESTDIR="../target/python_unit_tests"
PYTHONCDMDIR="../target/python"
$PYEXE -m pip install pydantic
$PYEXE -m pip install pytest
$PYEXE -m pip install $MYPATH/$ROSETTARUNTIMEDIR/rosetta_runtime-2.0.0-py3-none-any.whl 

cd $MYPATH
# build and install unit test package
cd $PYTHONUNITTESTDIR
$PYEXE -m pip wheel --no-deps --only-binary :all: . || processError
$PYEXE -m pip install python_rosetta-0.0.0-py3-none-any.whl
# install cdm package
$PYEXE -m pip install $MYPATH/$PYTHONCDMDIR/python_cdm-*-py3-none-any.whl

# run tests
pytest -p no:cacheprovider $MYPATH
