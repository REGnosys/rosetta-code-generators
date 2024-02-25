# pylint: disable=unused-import,missing-function-docstring,invalid-name
from datetime import date
import logging
import os
from pathlib import Path
from cdm.event.common.Trade import Trade
from cdm.event.common.TradeIdentifier import TradeIdentifier
from cdm.product.template.TradableProduct import TradableProduct
from cdm.product.template.Product import Product
from cdm.product.template.TradeLot import TradeLot
from cdm.product.common.settlement.PriceQuantity import PriceQuantity
from cdm.base.staticdata.party.Party import Party
from cdm.base.staticdata.party.PartyIdentifier import PartyIdentifier
from cdm.base.staticdata.party.Counterparty import Counterparty
from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum
from cdm.base.staticdata.asset.common.Index import Index
from cdm.base.staticdata.identifier.AssignedIdentifier import AssignedIdentifier
from cdm.event.common.TradeState import TradeState


def test_trade():
    priceQuantity = PriceQuantity()
    tradeLot = TradeLot(priceQuantity=[priceQuantity])
    product = Product(index=Index())
    counterparty = [
        Counterparty(role=CounterpartyRoleEnum.PARTY_1,
                     partyReference=Party(
                         partyId=[PartyIdentifier(identifier='Acme Corp')])),
        Counterparty(
            role=CounterpartyRoleEnum.PARTY_2,
            partyReference=Party(
                partyId=[PartyIdentifier(identifier='Wile E. Coyote')]))
    ]
    tradableProduct = TradableProduct(product=product,
                                      tradeLot=[tradeLot],
                                      counterparty=counterparty)
    assignedIdentifier = AssignedIdentifier(identifier='BIG DEAL!')
    tradeIdentifier = [
        TradeIdentifier(issuer='Acme Corp',
                        assignedIdentifier=[assignedIdentifier])
    ]

    t = Trade(tradeDate=date(2023, 1, 1),
              tradableProduct=tradableProduct,
              tradeIdentifier=tradeIdentifier)
    exceptions = t.validate_model(raise_exc=False)
    print(exceptions)
    print('Done!')


def test_fx():
    path = os.path.join(os.path.dirname(__file__), '..', 'serialization',
                        'fx-ex03-fx-fwd.json')
    json_str = Path(path).read_text()
    ts = TradeState.model_validate_json(json_str)
    print(repr(ts))

    exceptions = ts.validate_model(raise_exc=False)
    print(exceptions)
    print('Done!')


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.DEBUG)
    # test_trade()
    test_fx()

# EOF
