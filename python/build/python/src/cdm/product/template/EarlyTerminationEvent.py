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

__all__ = ['EarlyTerminationEvent']


class EarlyTerminationEvent(BaseDataClass):
  """
  A data to:  define the adjusted dates associated with an early termination provision.
  """
  adjustedCashSettlementPaymentDate: date = Field(..., description="The date on which the cash settlement amount is paid. This date should already be adjusted for any applicable business date convention.")
  """
  The date on which the cash settlement amount is paid. This date should already be adjusted for any applicable business date convention.
  """
  adjustedCashSettlementValuationDate: date = Field(..., description="The date by which the cash settlement amount must be agreed. This date should already be adjusted for any applicable business day convention.")
  """
  The date by which the cash settlement amount must be agreed. This date should already be adjusted for any applicable business day convention.
  """
  adjustedEarlyTerminationDate: date = Field(..., description="The early termination date that is applicable if an early termination provision is exercised. This date should already be adjusted for any applicable business day convention.")
  """
  The early termination date that is applicable if an early termination provision is exercised. This date should already be adjusted for any applicable business day convention.
  """
  adjustedExerciseDate: date = Field(..., description="The date on which option exercise takes place. This date should already be adjusted for any applicable business day convention.")
  """
  The date on which option exercise takes place. This date should already be adjusted for any applicable business day convention.
  """
  adjustedExerciseFeePaymentDate: Optional[date] = Field(None, description="The date on which the exercise fee amount is paid. This date should already be adjusted for any applicable business day convention.")
  """
  The date on which the exercise fee amount is paid. This date should already be adjusted for any applicable business day convention.
  """
  
  @rosetta_condition
  def condition_0_FpML_ird_39(self):
    """
    FpML validation rule ird-39 - AdjustedExerciseDate must be before or equal to adjustedEarlyTerminationDate.
    """
    return all_elements(self.adjustedExerciseDate, "<=", self.adjustedEarlyTerminationDate)
  
  @rosetta_condition
  def condition_1_FpML_ird_40(self):
    """
    FpML validation rule ird-40 - AdjustedExerciseDate must be before or equal to adjustedCashSettlementValuationDate.
    """
    return all_elements(self.adjustedExerciseDate, "<=", self.adjustedCashSettlementValuationDate)
  
  @rosetta_condition
  def condition_2_FpML_ird_41(self):
    """
    FpML validation rule ird-41 - AdjustedCashSettlementValuationDate must be before or equal to adjustedCashSettlementPaymentDate.
    """
    return all_elements(self.adjustedCashSettlementValuationDate, "<=", self.adjustedCashSettlementPaymentDate)


EarlyTerminationEvent.update_forward_refs()
