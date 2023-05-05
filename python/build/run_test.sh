#!/bin/sh
ACDIR=$(python -c "import sys;print('Scripts' if sys.platform.startswith('win') else 'bin')")
pip uninstall -y python_cdm-3.3.2-py3-none-any.whl
rm python_cdm-3.3.2-py3-none-any.whl
./build.sh
source .pyenv/$ACDIR/activate
python -m pip install --force-reinstall python_cdm-3.3.2-py3-none-any.whl
python test/serialization/test_party.py
python test/serialization/test_trade_state_product_3_2_2.py
