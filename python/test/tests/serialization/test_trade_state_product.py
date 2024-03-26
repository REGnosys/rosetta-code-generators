'''read and validate trade state specified by cdm_sample'''
import sys
import os
from cdm.event.common.TradeState import TradeState
from cdm_comparison_test import cdm_comparison_test_from_file

def test_trade_state (cdm_sample_in=None):
    '''read cdm_sample_in and validate '''
    if cdm_sample_in is None:
        dir_path = os.path.dirname(__file__)
        sys.path.append(os.path.join(dir_path))
        cdm_sample_in = os.path.join(dir_path, 'EUR-Vanilla-account.json')
    cdm_comparison_test_from_file (cdm_sample_in, TradeState)

if __name__ == "__main__":
    cdm_sample = sys.argv[1] if len(sys.argv) > 1 else None
    test_trade_state(cdm_sample)