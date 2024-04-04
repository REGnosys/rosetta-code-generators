'''read and validate trade state specified by cdm_sample'''
import sys
import os
from cdm.event.common.TradeState import TradeState
from cdm_comparison_test import test_trade_state

if __name__ == "__main__":
    cdm_sample = sys.argv[1] if len(sys.argv) > 1 else None
    test_trade_state(cdm_sample)