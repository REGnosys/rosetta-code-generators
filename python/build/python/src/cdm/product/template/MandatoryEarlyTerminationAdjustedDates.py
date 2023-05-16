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

__all__ = ['MandatoryEarlyTerminationAdjustedDates']


class MandatoryEarlyTerminationAdjustedDates(BaseDataClass):
  """
  A data defining:  the adjusted dates associated with a mandatory early termination provision.
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
  
  @rosetta_condition
  def condition_0_FpML_ird_44(self):
    """
    FpML validation rule ird-44 - AdjustedEarlyTerminationDate must be before or equal to adjustedCashSettlementValuationDate must be before or the same as adjustedCashSettlementPaymentDate
    """
    return (all_elements(self.adjustedEarlyTerminationDate, "<=", self.adjustedCashSettlementValuationDate) and all_elements(self.adjustedCashSettlementValuationDate, "<=", self.adjustedCashSettlementPaymentDate))


MandatoryEarlyTerminationAdjustedDates.update_forward_refs()
