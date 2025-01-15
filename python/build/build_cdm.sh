#!/bin/sh
function processError() {
  echo ""
  echo ""
  echo "***************************************************************************"
  echo "*                                                                         *"
  echo "*                         INITIALISATION FAILED!                          *"
  echo "*               -- note: must be run from root directory --               *"
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
MYPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
ROSETTARUNTIMEDIR=$MYPATH/"../src/main/resources/runtime"
PYTHONSOURCEDIR=$MYPATH/"../target/python"
cd $PYTHONSOURCEDIR
$PYEXE -m venv --clear .pybuild || processError
source .pybuild/$ACDIR/activate || processError
rm python_cdm-*.*.*-py3-none-any.whl
$PYEXE -m pip install --upgrade pip || processError
$PYEXE -m pip install "setuptools>=62.0" || processError
$PYEXE -m pip install "pydantic>=2.6.1,<2.10" || processError
$PYEXE -m pip install $ROSETTARUNTIMEDIR/rosetta_runtime-2.1.0-py3-none-any.whl || processError
$PYEXE -m pip wheel --no-deps --only-binary :all: . || processError
rm -rf .pybuild
echo ""
echo ""
echo "***************************************************************************"
echo "*                                                                         *"
echo "*                                 SUCCESS!!!                              *"
echo "*                                                                         *"
echo "*Finished installing dependencies and building/installing the cdm package!*"
echo "*                                                                         *"
echo "*                      package placed in target/python                    !*"
echo "*                                                                         *"
echo "***************************************************************************"
echo ""