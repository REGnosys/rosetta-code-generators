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

__all__ = ['ValuationMethod']


class ValuationMethod(BaseDataClass):
  """
  Specifies the parameters required to obtain a valuation, including the source, quotation method (bid, mid etc.) and any applicable quotation amount.
  """
  cashCollateralValuationMethod: Optional[CashCollateralValuationMethod] = Field(None, description="Specifies the parameters representing several mid-market valuation and replacement value methods.")
  """
  Specifies the parameters representing several mid-market valuation and replacement value methods.
  """
  minimumQuotationAmount: Optional[Money] = Field(None, description="In the determination of a cash settlement amount, if weighted average quotations are to be obtained, the minimum quotation amount specifies a minimum intended threshold amount of outstanding principal balance of the reference obligation for which the quote should be obtained. If not specified, the ISDA definitions provide for a fallback amount of the lower of either USD 1,000,000 (or its equivalent in the relevant obligation currency) or the quotation amount. ISDA 2003 Term: Minimum Quotation Amount.")
  """
  In the determination of a cash settlement amount, if weighted average quotations are to be obtained, the minimum quotation amount specifies a minimum intended threshold amount of outstanding principal balance of the reference obligation for which the quote should be obtained. If not specified, the ISDA definitions provide for a fallback amount of the lower of either USD 1,000,000 (or its equivalent in the relevant obligation currency) or the quotation amount. ISDA 2003 Term: Minimum Quotation Amount.
  """
  quotationAmount: Optional[Money] = Field(None, description="In the determination of a cash settlement amount, if weighted average quotations are to be obtained, the quotation amount specifies an upper limit to the outstanding principal balance of the reference obligation for which the quote should be obtained. If not specified, the ISDA definitions provide for a fallback amount equal to the floating rate payer calculation amount. ISDA 2003 Term: Quotation Amount.")
  """
  In the determination of a cash settlement amount, if weighted average quotations are to be obtained, the quotation amount specifies an upper limit to the outstanding principal balance of the reference obligation for which the quote should be obtained. If not specified, the ISDA definitions provide for a fallback amount equal to the floating rate payer calculation amount. ISDA 2003 Term: Quotation Amount.
  """
  quotationMethod: Optional[QuotationRateTypeEnum] = Field(None, description="The type of price quotations to be requested from dealers when determining the market value of the reference obligation for purposes of cash settlement, or which rate quote is to be observed for a fixing. For example, Bid, Offer, Mid-market or Exercising Party Pays. ISDA 2003 Term: Quotation Method. The meaning of Exercising Party Pays is defined in the 2000 ISDA Definitions, Section 17.2. Certain Definitions Relating to Cash Settlement, paragraph (j).")
  """
  The type of price quotations to be requested from dealers when determining the market value of the reference obligation for purposes of cash settlement, or which rate quote is to be observed for a fixing. For example, Bid, Offer, Mid-market or Exercising Party Pays. ISDA 2003 Term: Quotation Method. The meaning of Exercising Party Pays is defined in the 2000 ISDA Definitions, Section 17.2. Certain Definitions Relating to Cash Settlement, paragraph (j).
  """
  valuationMethod: Optional[ValuationMethodEnum] = Field(None, description="The ISDA defined methodology for determining the final price of the reference obligation for purposes of cash settlement. (ISDA 2003 Term: Valuation Method). For example, Market, Highest etc.")
  """
  The ISDA defined methodology for determining the final price of the reference obligation for purposes of cash settlement. (ISDA 2003 Term: Valuation Method). For example, Market, Highest etc.
  """
  valuationSource: ValuationSource = Field(..., description="The source for obtaining a valuation. This may come from some information source (e.g. Reuters), from a rate option fixing (e.g. FX fixing for cross-currency settlement), or from a set of reference banks. This is a mandatory attribute as the valuation method relies on one of those sources to be specified.")
  """
  The source for obtaining a valuation. This may come from some information source (e.g. Reuters), from a rate option fixing (e.g. FX fixing for cross-currency settlement), or from a set of reference banks. This is a mandatory attribute as the valuation method relies on one of those sources to be specified.
  """
  
  @rosetta_condition
  def condition_0_FpML_cd_37(self):
    """
    FpML validation rule cd-37 - If condition quotationAmount is true, and if condition minimumQuotationAmount is true, and if both amounts have the same-currency, then quotationAmount/amount must be greater or equal to minimumQuotationAmount/amount.
    """
    def _then_fn0():
      return all_elements(self.quotationAmount.value, ">", self.minimumQuotationAmount.value)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((((self.quotationAmount) is not None) and ((self.minimumQuotationAmount) is not None)) and all_elements(self.quotationAmount.unit.currency, "=", self.minimumQuotationAmount.unit.currency)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_Dealer(self):
    """
    When a quotation amount is specified, the dealer from which to obtain the quotation must be specified in the valuation source. This is typically applicable to determine the recovery amount in a credit event.
    """
    def _then_fn0():
      return ((self.valuationSource.dealerOrCCP.legalEntity) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.quotationAmount) is not None) or ((self.minimumQuotationAmount) is not None)), _then_fn0, _else_fn0)

from cdm.observable.asset.CashCollateralValuationMethod import CashCollateralValuationMethod
from cdm.observable.asset.Money import Money
from cdm.observable.asset.QuotationRateTypeEnum import QuotationRateTypeEnum
from cdm.observable.asset.ValuationMethodEnum import ValuationMethodEnum
from cdm.observable.asset.ValuationSource import ValuationSource

ValuationMethod.update_forward_refs()
