#!/bin/sh
function processError() {
  echo ""
  echo ""
  echo "***************************************************************************"
  echo "*                                                                         *"
  echo "*                          PYTHON TESTS FAILED!                           *"
  echo "*                                                                         *"
  echo "***************************************************************************"
  echo ""
  exit 1
}

echo ""
echo ""
echo "***************************************************************************"
echo "*                                                                         *"
echo "*                              PYTHON TESTS!!!                            *"
echo "*                                                                         *"
echo "*                Install wheel and test python-cdm package!               *"
echo "*                                                                         *"
echo "***************************************************************************"
echo ""

# install the .whl package using pip
python -m pip install python_cdm-*-py3-none-any.whl || processError

# navigate to the folder containing pytests
cd test

# run all pytests
python -m pytest || processError

echo ""
echo ""
echo "***************************************************************************"
echo "*                                                                         *"
echo "*                                 SUCCESS!!!                              *"
echo "*                                                                         *"
echo "*                   Finished testing python-cdm module!                   *"
echo "*                                                                         *"
echo "***************************************************************************"
echo ""