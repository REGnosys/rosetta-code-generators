#!/bin/sh
function processError() {
  rm -rf .pydevenv
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

$PYEXE -m venv --clear .pybuild || processError
source .pybuild/$ACDIR/activate || processError
$PYEXE -m pip install --upgrade pip || processError
$PYEXE -m pip install "setuptools>=62.0" || processError
$PYEXE -m pip install pylint || processError
$PYEXE -m pip install pycodestyle || processError
$PYEXE -m pip install yapf || processError
$PYEXE -m pip install "pydantic>=2.6.1,<2.10" || processError
$PYEXE -m pip install jsonpickle || processError
rm -rf build
rm rosetta_runtime-*-py3-none-any.whl
$PYEXE -m pip install -e . || processError
$PYEXE -m pip wheel --no-deps --only-binary :all: . || processError
rm -rf build .pybuild
echo ""
echo ""
echo "***************************************************************************"
echo "*                                                                         *"
echo "*                                 SUCCESS!!!                              *"
echo "*                                                                         *"
echo "*Finished installing dependencies and building the rosetta runtime       !*"
echo "*                                                                         *"
echo "***************************************************************************"
echo ""

