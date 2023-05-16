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

__all__ = ['FutureValueAmount']


class FutureValueAmount(BaseDataClass):
  """
  A class defining a currency and a future value date.
  """
  calculationPeriodNumberOfDays: int = Field(..., description="The number of days from the adjusted calculation period start date to the adjusted value date, calculated in accordance with the applicable day count fraction.")
  """
  The number of days from the adjusted calculation period start date to the adjusted value date, calculated in accordance with the applicable day count fraction.
  """
  currency: AttributeWithMeta[str] | str = Field(..., description="The currency in which the an amount is denominated. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
  """
  The currency in which the an amount is denominated. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.
  """
  quantity: Optional[AttributeWithAddress[NonNegativeQuantitySchedule] | NonNegativeQuantitySchedule] = Field(None, description="")
  valueDate: date = Field(..., description="Adjusted value date of the future value amount.")
  """
  Adjusted value date of the future value amount.
  """
  
  @rosetta_condition
  def condition_0_PositiveCalculationPeriodNumberOfDays(self):
    """
    FpML specifies calculationPeriodNumberOfDays as a positiveInteger.
    """
    return all_elements(self.calculationPeriodNumberOfDays, ">=", 0)

from cdm.base.math.NonNegativeQuantitySchedule import NonNegativeQuantitySchedule

FutureValueAmount.update_forward_refs()
