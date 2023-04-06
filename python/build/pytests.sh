#!/bin/bash
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
echo "*                       test the python-cdm package!                      *"
echo "*                                                                         *"
echo "***************************************************************************"
echo ""

ACDIR=$(python -c "import sys;print('Scripts' if sys.platform.startswith('win') else 'bin')")

# It is assumed, that the build.sh script has been run (it installs the cdm package
# in the local virtual environment)
source .pyenv/$ACDIR/activate || processError

# navigate to the folder containing pytests
cd test || processError

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