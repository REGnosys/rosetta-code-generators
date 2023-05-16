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

__all__ = ['CalculationCurrencyElection']


class CalculationCurrencyElection(BaseDataClass):
  """
  A class to specify the ISDA SIMM Calculation Currency as either the Base Currency or an alternative currency. ISDA 2016 CSA for Initial Margin, Paragraph 13, General Principles (ee)(3). | ISDA 2018 CSA for Initial Margin, Paragraph 13, General Principles (ee)(3).
  """
  currency: Optional[AttributeWithMeta[str] | str] = Field(None, description="The currency in which the ISDA SIMM Calculation is denominated, when different from the Base Currency. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
  """
  The currency in which the ISDA SIMM Calculation is denominated, when different from the Base Currency. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.
  """
  isBaseCurrency: bool = Field(..., description="The SIMM Calculation Currency (also known as SIMM Reporting Currency) means the Base Currency when True. It means a different currency when False. In that latter case, the SIMM Calculation Currency is specified as part of the currency attribute.")
  """
  The SIMM Calculation Currency (also known as SIMM Reporting Currency) means the Base Currency when True. It means a different currency when False. In that latter case, the SIMM Calculation Currency is specified as part of the currency attribute.
  """
  party: CounterpartyRoleEnum = Field(..., description="The party which the SIMM Calculation Currency qualification applies to.")
  """
  The party which the SIMM Calculation Currency qualification applies to.
  """
  
  @rosetta_condition
  def condition_0_BaseCurrency(self):
    """
    A data rule to enforce that, when the SIMM calculation currency is specified as the Base Currency and vice versa
    """
    def _then_fn0():
      return ((self.currency) is None)
    
    def _else_fn0():
      return ((self.currency) is not None)
    
    return if_cond_fn(all_elements(self.isBaseCurrency, "=", False), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

CalculationCurrencyElection.update_forward_refs()
