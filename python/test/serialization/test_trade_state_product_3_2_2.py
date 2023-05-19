import pytest

from cdm.event.common.TradeState import TradeState
import sys,os
dirPath = os.path.dirname(__file__)
sys.path.append(os.path.join(dirPath))

from cdm_comparison_test import cdm_comparison_test_from_file

def test_trade_state ():
	cdm_comparison_test_from_file (dirPath + '/3.3.2/fpml-5-10/products/rates/EUR-Vanilla-account.json', TradeState)

if __name__ == "__main__":
	test_trade_state()