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

__all__ = ['PaymentCalculationPeriod']


class PaymentCalculationPeriod(BaseDataClass):
  """
  A data defining:  the adjusted payment date and associated calculation period parameters required to calculate the actual or projected payment amount. This data forms:  part of the cashflow representation of a swap stream.
  """
  adjustedPaymentDate: Optional[date] = Field(None, description="The adjusted payment date. This date should already be adjusted for any applicable business day convention. This component is not intended for use in trade confirmation but may be specified to allow the fee structure to also serve as a cashflow type component.")
  """
  The adjusted payment date. This date should already be adjusted for any applicable business day convention. This component is not intended for use in trade confirmation but may be specified to allow the fee structure to also serve as a cashflow type component.
  """
  calculationPeriod: List[CalculationPeriod] = Field([], description="The parameters used in the calculation of a fixed or floating rate calculation period amount. A list of calculation period elements may be ordered in the document by ascending start date. An FpML document which contains an unordered list of calculation periods is still regarded as a conformant document.")
  """
  The parameters used in the calculation of a fixed or floating rate calculation period amount. A list of calculation period elements may be ordered in the document by ascending start date. An FpML document which contains an unordered list of calculation periods is still regarded as a conformant document.
  """
  @rosetta_condition
  def cardinality_calculationPeriod(self):
    return check_cardinality(self.calculationPeriod, 1, None)
  
  discountFactor: Optional[Decimal] = Field(None, description="A decimal value representing the discount factor used to calculate the present value of cash flow.")
  """
  A decimal value representing the discount factor used to calculate the present value of cash flow.
  """
  fixedPaymentAmount: Optional[Money] = Field(None, description="A known fixed payment amount.")
  """
  A known fixed payment amount.
  """
  forecastPaymentAmount: Optional[Money] = Field(None, description="A monetary amount representing the forecast of the future value of the payment.")
  """
  A monetary amount representing the forecast of the future value of the payment.
  """
  presentValueAmount: Optional[Money] = Field(None, description="A monetary amount representing the present value of the forecast payment.")
  """
  A monetary amount representing the present value of the forecast payment.
  """
  unadjustedPaymentDate: Optional[date] = Field(None, description="The unadjusted payment date.")
  """
  The unadjusted payment date.
  """
  
  @rosetta_condition
  def condition_0_CalculationPeriodNumberOfDays(self):
    """
    FpML specifies calculationPeriodNumberOfDays as a positive integer.
    """
    def _then_fn0():
      return all_elements(self.calculationPeriod.calculationPeriodNumberOfDays, ">=", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.calculationPeriod.calculationPeriodNumberOfDays) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_PaymentCalculationPeriodChoice(self):
    """
    condition to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('calculationPeriod', 'fixedPaymentAmount', necessity=True)
  
  @rosetta_condition
  def condition_2_FpML_ird_34(self):
    """
    FpML validation rule ird-34 - Either unadjustedPaymentDate or adjustedPaymentDate must exist.
    """
    return (((self.unadjustedPaymentDate) is not None) or ((self.adjustedPaymentDate) is not None))

from cdm.product.common.schedule.CalculationPeriod import CalculationPeriod
from cdm.observable.asset.Money import Money

PaymentCalculationPeriod.update_forward_refs()
