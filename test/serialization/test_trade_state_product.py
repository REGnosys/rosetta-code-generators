import sys
import pytest

from cdm.event.common.TradeState import TradeState
import sys,os

from cdm_comparison_test import cdm_comparison_test_from_file

def test_trade_state (version="4_0_0"):
	dirPath = os.path.dirname(__file__)
	sys.path.append(os.path.join(dirPath))
	cdm_comparison_test_from_file (dirPath + '/cdm_samples/' + version + '/EUR-Vanilla-account.json', TradeState)

if __name__ == "__main__":
	version = sys.argv[1] if len(sys.argv) > 1 else '3_3_2'
	test_trade_state(version)