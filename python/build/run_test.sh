#!/bin/bash
type -P python > /dev/null && PYEXE=python || PYEXE=python3
if ! $PYEXE -c 'import sys; assert sys.version_info >= (3,10)' > /dev/null 2>&1; then
        echo "Found $($PYEXE -V)"
        echo "Expecting at least python 3.10 - exiting!"
        exit 1
fi

MYPATH="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $MYPATH

ACDIR=$($PYEXE -c "import sys;print('Scripts' if sys.platform.startswith('win') else 'bin')")

rm *.whl
rm -rf testenv -rf

bash build.sh

$PYEXE -m venv --clear testenv
source testenv/$ACDIR/activate

$PYEXE -m pip install pytest
$PYEXE -m pip install rosetta.runtime-1.0.0-py3-none-any.whl
$PYEXE -m pip install python_cdm-3.3.2-py3-none-any.whl

$PYEXE test/serialization/test_party.py
$PYEXE test/serialization/test_trade_state_product_3_2_2.py
