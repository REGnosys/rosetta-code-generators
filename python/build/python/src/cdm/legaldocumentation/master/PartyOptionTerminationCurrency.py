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

__all__ = ['PartyOptionTerminationCurrency']


class PartyOptionTerminationCurrency(BaseDataClass):
  """
  Specifies mechanism for Termination currency to be selected by the Non-defaulting Party/party which is not the Affected Party.
  """
  bothAffectedTermCurrencyOption: Optional[str] = Field(None, description="Specifies termination currency where there are two Affected Parties and they cannot agree on the termination currency.")
  """
  Specifies termination currency where there are two Affected Parties and they cannot agree on the termination currency.
  """
  terminationCurrencyCondition: TerminationCurrencyConditionEnum = Field(..., description="Specifies the enumerated conditions for selection of the termination currency.")
  """
  Specifies the enumerated conditions for selection of the termination currency.
  """
  terminationCurrencySpecifiedCondition: Optional[str] = Field(None, description="Specifies alternative conditions for selection of the termination currency.")
  """
  Specifies alternative conditions for selection of the termination currency.
  """
  
  @rosetta_condition
  def condition_0_TerminationCurrencyCondition(self):
    """
    A validation rule to ensure that Termination Currency alternative conditions are specified when required.
    """
    def _then_fn0():
      return ((self.terminationCurrencySpecifiedCondition) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.terminationCurrencyCondition, "=", TerminationCurrencyConditionEnum.SPECIFIED), _then_fn0, _else_fn0)

from cdm.legaldocumentation.common.TerminationCurrencyConditionEnum import TerminationCurrencyConditionEnum

PartyOptionTerminationCurrency.update_forward_refs()
