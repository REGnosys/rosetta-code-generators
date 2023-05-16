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

__all__ = ['DividendReturnTerms']


class DividendReturnTerms(BaseDataClass):
  """
  A class describing the conditions governing the payment of dividends to the receiver of the equity return, with the exception of the dividend payout ratio, which is defined for each of the underlying components.
  """
  dividendAmountType: Optional[DividendAmountTypeEnum] = Field(None, description="Specifies whether the dividend is paid with respect to the Dividend Period.")
  """
  Specifies whether the dividend is paid with respect to the Dividend Period.
  """
  dividendComposition: Optional[DividendCompositionEnum] = Field(None, description="Specifies how the composition of Dividends is to be determined.")
  """
  Specifies how the composition of Dividends is to be determined.
  """
  dividendCurrency: Optional[DividendCurrency] = Field(None, description="Specifies the currency in which the dividend will be denominated, e.g. the dividend currency, or a specified currency. This class is not specified as such in FpML, which makes use of the CurrencyAndDeterminationMethod.model to specify such terms.")
  """
  Specifies the currency in which the dividend will be denominated, e.g. the dividend currency, or a specified currency. This class is not specified as such in FpML, which makes use of the CurrencyAndDeterminationMethod.model to specify such terms.
  """
  dividendEntitlement: Optional[DividendEntitlementEnum] = Field(None, description="Defines the date on which the receiver of the equity return is entitled to the dividend.")
  """
  Defines the date on which the receiver of the equity return is entitled to the dividend.
  """
  dividendPayoutRatio: List[DividendPayoutRatio] = Field([], description="Specifies the dividend payout ratio associated with each underlier. In FpML 5.10 the payout is positioned at the underlier level, although there is an intent to reconsider this approach and position it at the leg level. This is approach adopted by the CDM.")
  """
  Specifies the dividend payout ratio associated with each underlier. In FpML 5.10 the payout is positioned at the underlier level, although there is an intent to reconsider this approach and position it at the leg level. This is approach adopted by the CDM.
  """
  dividendPeriod: List[DividendPeriod] = Field([], description="One to many time bounded dividend payment periods, each with a dividend payment date per period.")
  """
  One to many time bounded dividend payment periods, each with a dividend payment date per period.
  """
  dividendReinvestment: Optional[bool] = Field(None, description="Boolean element that defines whether the dividend will be reinvested or not.")
  """
  Boolean element that defines whether the dividend will be reinvested or not.
  """
  excessDividendAmount: Optional[DividendAmountTypeEnum] = Field(None, description="Determination of Gross Cash Dividend per Share.")
  """
  Determination of Gross Cash Dividend per Share.
  """
  extraordinaryDividendsParty: Optional[AncillaryRoleEnum] = Field(None, description="Specifies the party which determines if dividends are extraordinary in relation to normal levels.")
  """
  Specifies the party which determines if dividends are extraordinary in relation to normal levels.
  """
  firstOrSecondPeriod: Optional[DividendPeriodEnum] = Field(None, description="2002 ISDA Equity Derivatives Definitions: Dividend Period as either the First Period or the Second Period. | ")
  """
  2002 ISDA Equity Derivatives Definitions: Dividend Period as either the First Period or the Second Period. | 
  """
  materialDividend: Optional[bool] = Field(None, description="If present and true, then material non cash dividends are applicable.")
  """
  If present and true, then material non cash dividends are applicable.
  """
  nonCashDividendTreatment: Optional[NonCashDividendTreatmentEnum] = Field(None, description="Specifies the treatment of Non-Cash Dividends.")
  """
  Specifies the treatment of Non-Cash Dividends.
  """
  performance: Optional[str] = Field(None, description="Performance calculation, in accordance with Part 1 Section 12 of the 2018 ISDA CDM Equity Confirmation for Security Equity Swap, Para 75. 'Equity Performance'. Cumulative performance is used as a notional multiplier factor on both legs of an Equity Swap.")
  """
  Performance calculation, in accordance with Part 1 Section 12 of the 2018 ISDA CDM Equity Confirmation for Security Equity Swap, Para 75. 'Equity Performance'. Cumulative performance is used as a notional multiplier factor on both legs of an Equity Swap.
  """
  specialDividends: Optional[bool] = Field(None, description="Specifies the method according to which special dividends are determined.")
  """
  Specifies the method according to which special dividends are determined.
  """
  
  @rosetta_condition
  def condition_0_DividendPeriod(self):
    """
    FpML specifies a choice between dividendPeriod on one end, and dividendPeriodEffectiveDate and dividendPeriodEndDate on the other end.
    """
    def _then_fn0():
      return (((self.dividendPeriod.startDate) is None) and ((self.dividendPeriod.endDate) is None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.firstOrSecondPeriod) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_ExtraordinaryDividendsParty(self):
    def _then_fn0():
      return all_elements(self.extraordinaryDividendsParty, "=", AncillaryRoleEnum.EXTRAORDINARY_DIVIDENDS_PARTY)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.extraordinaryDividendsParty) is not None), _then_fn0, _else_fn0)

from cdm.product.asset.DividendAmountTypeEnum import DividendAmountTypeEnum
from cdm.product.asset.DividendCompositionEnum import DividendCompositionEnum
from cdm.product.asset.DividendCurrency import DividendCurrency
from cdm.product.asset.DividendEntitlementEnum import DividendEntitlementEnum
from cdm.product.asset.DividendPayoutRatio import DividendPayoutRatio
from cdm.product.asset.DividendPeriod import DividendPeriod
from cdm.base.staticdata.party.AncillaryRoleEnum import AncillaryRoleEnum
from cdm.product.asset.DividendPeriodEnum import DividendPeriodEnum
from cdm.product.asset.NonCashDividendTreatmentEnum import NonCashDividendTreatmentEnum

DividendReturnTerms.update_forward_refs()
