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

__all__ = ['CalculationPeriod']

from cdm.product.common.schedule.CalculationPeriodBase import CalculationPeriodBase

class CalculationPeriod(CalculationPeriodBase):
  """
  A data defining:  the parameters used in the calculation of a fixed or floating rate calculation period amount. This data forms:  part of cashflows representation of a swap stream.
  """
  calculationPeriodNumberOfDays: Optional[int] = Field(None, description="The number of days from the adjusted effective / start date to the adjusted termination / end date calculated in accordance with the applicable day count fraction.")
  """
  The number of days from the adjusted effective / start date to the adjusted termination / end date calculated in accordance with the applicable day count fraction.
  """
  dayCountYearFraction: Optional[Decimal] = Field(None, description="The year fraction value of the calculation period, result of applying the ISDA rules for day count fraction defined in the ISDA Annex.")
  """
  The year fraction value of the calculation period, result of applying the ISDA rules for day count fraction defined in the ISDA Annex.
  """
  fixedRate: Optional[Decimal] = Field(None, description="The calculation period fixed rate. A per annum rate, expressed as a decimal. A fixed rate of 5% would be represented as 0.05.")
  """
  The calculation period fixed rate. A per annum rate, expressed as a decimal. A fixed rate of 5% would be represented as 0.05.
  """
  floatingRateDefinition: Optional[FloatingRateDefinition] = Field(None, description="The floating rate reset information for the calculation period.")
  """
  The floating rate reset information for the calculation period.
  """
  forecastAmount: Optional[Money] = Field(None, description="The amount representing the forecast of the accrued value of the calculation period. An intermediate value used to generate the forecastPaymentAmount in the PaymentCalculationPeriod.")
  """
  The amount representing the forecast of the accrued value of the calculation period. An intermediate value used to generate the forecastPaymentAmount in the PaymentCalculationPeriod.
  """
  forecastRate: Optional[Decimal] = Field(None, description="A value representing the forecast rate used to calculate the forecast future value of the accrual period. This is a calculated rate determined based on averaging the rates in the rateObservation elements, and incorporates all of the rate treatment and averaging rules. A value of 1% should be represented as 0.01.")
  """
  A value representing the forecast rate used to calculate the forecast future value of the accrual period. This is a calculated rate determined based on averaging the rates in the rateObservation elements, and incorporates all of the rate treatment and averaging rules. A value of 1% should be represented as 0.01.
  """
  fxLinkedNotionalAmount: Optional[FxLinkedNotionalAmount] = Field(None, description="The amount that a cashflow will accrue interest on. This is the calculated amount of the FX linked - i.e. the other currency notional amount multiplied by the appropriate FX spot rate.")
  """
  The amount that a cashflow will accrue interest on. This is the calculated amount of the FX linked - i.e. the other currency notional amount multiplied by the appropriate FX spot rate.
  """
  notionalAmount: Optional[Decimal] = Field(None, description="The amount that a cashflow will accrue interest on.")
  """
  The amount that a cashflow will accrue interest on.
  """
  unadjustedEndDate: Optional[date] = Field(None, description="The calculation end date, unadjusted.")
  """
  The calculation end date, unadjusted.
  """
  unadjustedStartDate: Optional[date] = Field(None, description="The calculation start date, unadjusted.")
  """
  The calculation start date, unadjusted.
  """
  
  @rosetta_condition
  def condition_0_NotionalChoice(self):
    """
    condition to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('notionalAmount', 'fxLinkedNotionalAmount', necessity=True)
  
  @rosetta_condition
  def condition_1_RateChoice(self):
    """
    condition to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('floatingRateDefinition', 'fixedRate', necessity=True)
  
  @rosetta_condition
  def condition_2_StartDateChoice(self):
    """
    FpML validation rule ird-30 - Context: CalculationPeriod (complex type). unadjustedStartDate exists or adjustedStartDate exists.
    """
    return self.check_one_of_constraint('adjustedStartDate', 'unadjustedStartDate', necessity=True)
  
  @rosetta_condition
  def condition_3_EndDateChoice(self):
    """
    FpML validation rule ird-31 - Context: CalculationPeriod (complex type). unadjustedEndDate exists or adjustedEndDate exists.
    """
    return self.check_one_of_constraint('adjustedEndDate', 'unadjustedEndDate', necessity=True)

from cdm.product.asset.FloatingRateDefinition import FloatingRateDefinition
from cdm.observable.asset.Money import Money
from cdm.product.common.schedule.FxLinkedNotionalAmount import FxLinkedNotionalAmount

CalculationPeriod.update_forward_refs()
