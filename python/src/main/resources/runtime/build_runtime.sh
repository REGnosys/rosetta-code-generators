#!/bin/sh
function processError() {
  echo ""
  echo ""
  echo "***************************************************************************"
  echo "*                                                                         *"
  echo "*                         INITIALISATION FAILED!                          *"
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

MYPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $MYPATH
ACDIR=$($PYEXE -c "import sys;print('Scripts' if sys.platform.startswith('win') else 'bin')")

$PYEXE -m venv --clear .pyenv || processError
source .pyenv/$ACDIR/activate || processError
$PYEXE -m pip install --upgrade pip || processError
$PYEXE -m pip install "setuptools>=62.0" || processError
$PYEXE -m pip install pylint || processError
$PYEXE -m pip install pycodestyle || processError
$PYEXE -m pip install yapf || processError
$PYEXE -m pip install pydantic || processError
$PYEXE -m pip install jsonpickle || processError
rm -rf build
rm rosetta_runtime-1.0.0-py3-none-any.whl
$PYEXE -m pip install -e . || processError
$PYEXE -m pip wheel --no-deps --only-binary :all: . || processError
rm -rf build
echo ""
echo ""
echo "***************************************************************************"
echo "*                                                                         *"
echo "*                                 SUCCESS!!!                              *"
echo "*                                                                         *"
echo "*Finished installing dependencies and building/installing the cdm package!*"
echo "*                                                                         *"
echo "***************************************************************************"
echo ""

