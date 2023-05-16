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

__all__ = ['Reset']


class Reset(BaseDataClass):
  """
  Defines the reset value or fixing value produced in cashflow calculations, during the life-cycle of a financial instrument. The reset process defined in Create_Reset function joins product definition details with observations to compute the reset value.
  """
  averagingMethodology: Optional[AveragingCalculation] = Field(None, description="Identifies the aggregation method to use in the case where multiple observations are used to compute the reset value and the method is not defined in a payout.")
  """
  Identifies the aggregation method to use in the case where multiple observations are used to compute the reset value and the method is not defined in a payout.
  """
  observations: List[AttributeWithReference | Observation] = Field([], description="Represents an audit of the observations used to produce the reset value. If multiple observations were necessary to produce the reset value, the aggregation method should be defined on the payout.")
  """
  Represents an audit of the observations used to produce the reset value. If multiple observations were necessary to produce the reset value, the aggregation method should be defined on the payout.
  """
  @rosetta_condition
  def cardinality_observations(self):
    return check_cardinality(self.observations, 1, None)
  
  rateRecordDate: Optional[date] = Field(None, description="Specifies the 'Rate Record Day' for a Fallback rate.  Fallback rate fixing processes typically set the fixing rate in arrears, i.e., the Fallback Rate corresponding to a Rate Record Date is set at the end of the interest accural period.  When this applies, Reset->resetDate occurs at the end of the interest period, and the Reset->rateRecordDate occurs near the start of the interest period.  The Reset->rateRecordDate and Reset->observations->observationIdentifier->observationDate will differ if a Fallback rate is unavailable on the Rate Record Date, and the latest previous available rate is used as the observation.")
  """
  Specifies the 'Rate Record Day' for a Fallback rate.  Fallback rate fixing processes typically set the fixing rate in arrears, i.e., the Fallback Rate corresponding to a Rate Record Date is set at the end of the interest accural period.  When this applies, Reset->resetDate occurs at the end of the interest period, and the Reset->rateRecordDate occurs near the start of the interest period.  The Reset->rateRecordDate and Reset->observations->observationIdentifier->observationDate will differ if a Fallback rate is unavailable on the Rate Record Date, and the latest previous available rate is used as the observation.
  """
  resetDate: date = Field(..., description="Specifies the date on which the reset occurred.")
  """
  Specifies the date on which the reset occurred.
  """
  resetValue: Price = Field(..., description="Specifies the reset or fixing value. The fixing value could be a cash price, interest rate, or other value.")
  """
  Specifies the reset or fixing value. The fixing value could be a cash price, interest rate, or other value.
  """
  
  @rosetta_condition
  def condition_0_AveragingMethodologyExists(self):
    """
    Ensures an averaging method is defined when more than one observation is used to compute the reset.
    """
    def _then_fn0():
      return ((self.averagingMethodology) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(len(self.observations), ">", 1), _then_fn0, _else_fn0)

from cdm.product.template.AveragingCalculation import AveragingCalculation
from cdm.observable.event.Observation import Observation
from cdm.observable.asset.Price import Price

Reset.update_forward_refs()
