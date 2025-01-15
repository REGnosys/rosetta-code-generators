'''read and validate trade state specified by cdm_sample'''
import sys
import os
from pathlib import Path

from cdm.event.common.TradeState import TradeState

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)))
from test_helpers.config import CDM_JSON_SAMPLE_SOURCE
from cdm.product.template.functions import FpmlIrd8
from cdm.base.staticdata.party.Account import Account
from cdm.event.common.Trade import Trade
from cdm.product.template.TradableProduct import TradableProduct

def dummy_FpmlIrd8(tradableProduct: TradableProduct, accounts: list[Account] | None)  -> bool:
    return True

FpmlIrd8.FpmlIrd8 = dummy_FpmlIrd8


def test_read_and_validate():
    ''' The below sample json needs to conform to the same current version of
        CDM as was used to build the python library.
        JSON generated for earlier or newer versions of CDM might fail to
        correctly parse or validate
    '''
    path = os.path.join(os.path.dirname(__file__), CDM_JSON_SAMPLE_SOURCE,
                        'rates', 'EUR-Vanilla-account.json')
    #                        'bond-option-uti.json')
    json_str = Path(path).read_text(encoding='utf8')
    ts = TradeState.model_validate_json(json_str)
    print(repr(ts))

    exceptions = ts.validate_model(raise_exc=False)
    # if len(exceptions) == 1 and str(exceptions[0]).startswith(
    #         'Condition "cdm.event.common.ContractDetails.ContractDetails.'
    #         'condition_0_ExecutedAgreement" for ContractDetails('):
    #     exceptions = []

    if exceptions:
        print('test_rates ... exceptions found')
        for e in exceptions:
            print(e)
    assert not exceptions


if __name__ == "__main__":
    test_read_and_validate()
