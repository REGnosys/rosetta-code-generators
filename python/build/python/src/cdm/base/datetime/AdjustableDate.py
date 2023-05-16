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

__all__ = ['AdjustableDate']


class AdjustableDate(BaseDataClass):
  """
  A class for defining a date that shall be subject to adjustment if it would otherwise fall on a day that is not a business day in the specified business centers, together with the convention for adjusting the date.
  """
  adjustedDate: Optional[AttributeWithMeta[date] | date] = Field(None, description="The date once the adjustment has been performed. (Note that this date may change if the business center holidays change).")
  """
  The date once the adjustment has been performed. (Note that this date may change if the business center holidays change).
  """
  dateAdjustments: Optional[BusinessDayAdjustments] = Field(None, description="The business day convention and financial business centers used for adjusting the date if it would otherwise fall on a day that is not a business date in the specified business centers.")
  """
  The business day convention and financial business centers used for adjusting the date if it would otherwise fall on a day that is not a business date in the specified business centers.
  """
  dateAdjustmentsReference: Optional[AttributeWithReference | BusinessDayAdjustments] = Field(None, description="A pointer style reference to date adjustments defined elsewhere in the document.")
  """
  A pointer style reference to date adjustments defined elsewhere in the document.
  """
  unadjustedDate: Optional[date] = Field(None, description="A date subject to adjustment. While in FpML this date is required, this cardinality constraint has been relaxed as part of the CDM in order to support the FRA representation, which effective and termination dates are specified in FpML as adjusted dates.")
  """
  A date subject to adjustment. While in FpML this date is required, this cardinality constraint has been relaxed as part of the CDM in order to support the FRA representation, which effective and termination dates are specified in FpML as adjusted dates.
  """
  
  @rosetta_condition
  def condition_0_AdjustableDateChoice(self):
    """
    Choice rule to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('dateAdjustments', 'dateAdjustmentsReference', necessity=False)

from cdm.base.datetime.BusinessDayAdjustments import BusinessDayAdjustments

AdjustableDate.update_forward_refs()
