#!/bin/sh
python -m venv .pyenv || processError
pip uninstall -y python_cdm-3.3.2-py3-none-any.whl
rm python_cdm-3.3.2-py3-none-any.whl
./build.sh
python -m pip install --force-reinstall python_cdm-3.3.2-py3-none-any.whl
python test/serialization/test_party.py
python test/serialization/test_trade_state_product_3_2_2.py
