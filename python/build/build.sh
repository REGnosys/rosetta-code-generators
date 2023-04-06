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

ACDIR=$(python -c "import sys;print('Scripts' if sys.platform.startswith('win') else 'bin')")

python -m venv --clear .pyenv || processError
source .pyenv/$ACDIR/activate || processError
python -m pip install --upgrade pip || processError
python -m pip install "setuptools>=62.0" || processError
python -m pip install pylint || processError
python -m pip install pycodestyle || processError
python -m pip install yapf || processError
python -m pip install pytest || processError
python -m pip install pydantic || processError
python -m pip install jsonpickle || processError
python -m pip install -e . || processError
python -m pip wheel --only-binary :all: . || processError
rm -f typing_extensions-*.whl
rm -f pydantic-*.whl

echo ""
echo ""
echo "***************************************************************************"
echo "*                                                                         *"
echo "*                                 SUCCESS!!!                              *"
echo "*                                                                         *"
echo "*             Finished installing dependencies and the cdm module!        *"
echo "*                                                                         *"
echo "***************************************************************************"
echo ""

