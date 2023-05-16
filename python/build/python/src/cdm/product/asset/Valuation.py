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

__all__ = ['Valuation']


class Valuation(BaseDataClass):
  componentSecurityIndexAnnexFallback: Optional[bool] = Field(None, description="For an index option transaction, a flag to indicate whether a relevant Component Security Index Annex is applicable to the transaction.")
  """
  For an index option transaction, a flag to indicate whether a relevant Component Security Index Annex is applicable to the transaction.
  """
  dividendValuationDates: Optional[AdjustableRelativeOrPeriodicDates] = Field(None, description="Specifies the dividend valuation dates of the swap.")
  """
  Specifies the dividend valuation dates of the swap.
  """
  fPVFinalPriceElectionFallback: Optional[FPVFinalPriceElectionFallbackEnum] = Field(None, description="Specifies the fallback provisions for Hedging Party in the determination of the Final Price.")
  """
  Specifies the fallback provisions for Hedging Party in the determination of the Final Price.
  """
  futuresPriceValuation: Optional[bool] = Field(None, description="The official settlement price as announced by the related exchange is applicable, in accordance with the ISDA 2002 definitions.")
  """
  The official settlement price as announced by the related exchange is applicable, in accordance with the ISDA 2002 definitions.
  """
  multipleExchangeIndexAnnexFallback: Optional[bool] = Field(None, description="For an index option transaction, a flag to indicate whether a relevant Multiple Exchange Index Annex is applicable to the transaction. This annex defines additional provisions which are applicable where an index is comprised of component securities that are traded on multiple exchanges.")
  """
  For an index option transaction, a flag to indicate whether a relevant Multiple Exchange Index Annex is applicable to the transaction. This annex defines additional provisions which are applicable where an index is comprised of component securities that are traded on multiple exchanges.
  """
  numberOfValuationDates: Optional[int] = Field(None, description="The number of valuation dates between valuation start date and valuation end date.")
  """
  The number of valuation dates between valuation start date and valuation end date.
  """
  optionsPriceValuation: Optional[bool] = Field(None, description="The official settlement price as announced by the related exchange is applicable, in accordance with the ISDA 2002 definitions")
  """
  The official settlement price as announced by the related exchange is applicable, in accordance with the ISDA 2002 definitions
  """
  
  @rosetta_condition
  def condition_0_PositiveNumberOfValuationDates(self):
    """
    The number of valuation dates must be positive.
    """
    def _then_fn0():
      return all_elements(self.numberOfValuationDates, ">", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.numberOfValuationDates) is not None), _then_fn0, _else_fn0)

from cdm.base.datetime.AdjustableRelativeOrPeriodicDates import AdjustableRelativeOrPeriodicDates
from cdm.product.asset.FPVFinalPriceElectionFallbackEnum import FPVFinalPriceElectionFallbackEnum

Valuation.update_forward_refs()
