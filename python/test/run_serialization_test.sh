#!/bin/bash
function processError() {
  echo ""
  echo ""
  echo "***************************************************************************"
  echo "*                                                                         *"
  echo "*                             TESTING FAILED!                             *"
  echo "*                  -- must be run from root directory --                  *"
  echo "*                                                                         *"
  echo "***************************************************************************"
  echo ""
  exit 1
}

type -P python > /dev/null && PYEXE=python || PYEXE=python3
if ! $PYEXE -c 'import sys; assert sys.version_info >= (3,10)' > /dev/null 2>&1; then
        echo "Found $($PYEXE -V)"
        echo "Expecting at least python 3.10 - exiting!"
        exit 1
fi

ACDIR=$($PYEXE -c "import sys;print('Scripts' if sys.platform.startswith('win') else 'bin')")

$PYEXE -m venv --clear .pydevenv || processError
source .pydevenv/$ACDIR/activate || processError

MYPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo $MYPATH
ROSETTARUNTIMEDIR="../src/main/resources/runtime"
PYTHONCDMDIR="../target/python"
$PYEXE -m pip install pydantic
$PYEXE -m pip install pytest
$PYEXE -m pip install $MYPATH/$ROSETTARUNTIMEDIR/rosetta_runtime-2.0.0-py3-none-any.whl 
$PYEXE -m pip install $MYPATH/$PYTHONCDMDIR/python_cdm-0.0.0-py3-none-any.whl
$PYEXE $MYPATH/tests/serialization/test_trade_state_product.py