# pylint: disable=line-too-long, invalid-name, missing-function-docstring, missing-module-docstring, superfluous-parens
# pylint: disable=wrong-import-position, unused-import, unused-wildcard-import, wildcard-import, wrong-import-order, missing-class-docstring
from __future__ import annotations
from typing import List, Optional
from datetime import date
from datetime import time
from datetime import datetime
from decimal import Decimal
from pydantic import Field
from rosetta.runtime.utils import *

__all__ = ['ValuationSource']


class ValuationSource(BaseDataClass):
  """
  A class describing the method for obtaining a settlement rate, specified through either an information source (page), a settlement rate option (fixing) or by using quotes from reference banks.
  """
  dealerOrCCP: Optional[AncillaryEntity] = Field(None, description="Holds an identifier for the reference entity that is agreed by both parties as a basis for cash settlement calculations. This could be a dealer from whom quotations are obtained by the calculation agent on the reference obligation for purposes of cash settlement in a credit event. ISDA 2003 Term: Dealer. This could be the clearing organization (CCP, DCO) to which the trade should be cleared, as applicable for cash-settled swaptions.")
  """
  Holds an identifier for the reference entity that is agreed by both parties as a basis for cash settlement calculations. This could be a dealer from whom quotations are obtained by the calculation agent on the reference obligation for purposes of cash settlement in a credit event. ISDA 2003 Term: Dealer. This could be the clearing organization (CCP, DCO) to which the trade should be cleared, as applicable for cash-settled swaptions.
  """
  informationSource: Optional[FxSpotRateSource] = Field(None, description="The information source where a published or displayed market rate will be obtained, e.g. Telerate Page 3750.")
  """
  The information source where a published or displayed market rate will be obtained, e.g. Telerate Page 3750.
  """
  quotedCurrencyPair: Optional[AttributeWithAddress[QuotedCurrencyPair] | QuotedCurrencyPair] = Field(None, description="Defines the two currencies for an FX trade and the quotation relationship between the two currencies.  This attribute was formerly part of 'fxSettlementTerms', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.")
  """
  Defines the two currencies for an FX trade and the quotation relationship between the two currencies.  This attribute was formerly part of 'fxSettlementTerms', which is now being harmonised into a common 'CashSettlementTerms' that includes a 'ValuationDate'.
  """
  referenceBanks: Optional[ReferenceBanks] = Field(None, description="A container for a set of reference institutions that may be called upon to provide rate quotations as part of the method to determine the applicable cash settlement amount. If institutions are not specified, it is assumed that reference institutions will be agreed between the parties on the exercise date, or in the case of swap transaction to which mandatory early termination is applicable, the cash settlement valuation date.")
  """
  A container for a set of reference institutions that may be called upon to provide rate quotations as part of the method to determine the applicable cash settlement amount. If institutions are not specified, it is assumed that reference institutions will be agreed between the parties on the exercise date, or in the case of swap transaction to which mandatory early termination is applicable, the cash settlement valuation date.
  """
  settlementRateOption: Optional[SettlementRateOption] = Field(None, description="The rate option to use for the fixing. Currently only applicable to foreign exchange fixing in case of cross-currency settlement.")
  """
  The rate option to use for the fixing. Currently only applicable to foreign exchange fixing in case of cross-currency settlement.
  """
  
  @rosetta_condition
  def condition_0_InformationSource(self):
    """
    An information source must be provided.
    """
    return self.check_one_of_constraint('informationSource', 'settlementRateOption', 'referenceBanks', 'dealerOrCCP', necessity=True)

from cdm.base.staticdata.party.AncillaryEntity import AncillaryEntity
from cdm.observable.asset.FxSpotRateSource import FxSpotRateSource
from cdm.observable.asset.QuotedCurrencyPair import QuotedCurrencyPair
from cdm.base.staticdata.party.ReferenceBanks import ReferenceBanks
from cdm.observable.asset.SettlementRateOption import SettlementRateOption

ValuationSource.update_forward_refs()
