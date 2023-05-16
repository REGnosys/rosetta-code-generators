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

__all__ = ['EarlyTerminationProvision']


class EarlyTerminationProvision(BaseDataClass):
  """
  A data defining:  an early termination provision for a swap. This early termination is at fair value, i.e. on termination the fair value of the product must be settled between the parties.
  """
  mandatoryEarlyTermination: Optional[MandatoryEarlyTermination] = Field(None, description="A mandatory early termination provision to terminate the swap at fair value.")
  """
  A mandatory early termination provision to terminate the swap at fair value.
  """
  mandatoryEarlyTerminationDateTenor: Optional[Period] = Field(None, description="Period after trade date of the mandatory early termination date.")
  """
  Period after trade date of the mandatory early termination date.
  """
  optionalEarlyTermination: Optional[OptionalEarlyTermination] = Field(None, description="An option for either or both parties to terminate the swap at fair value.")
  """
  An option for either or both parties to terminate the swap at fair value.
  """
  optionalEarlyTerminationParameters: Optional[ExercisePeriod] = Field(None, description="Definition of the first early termination date and the frequency of the termination dates subsequent to that. American exercise is defined by having a frequency of one day.")
  """
  Definition of the first early termination date and the frequency of the termination dates subsequent to that. American exercise is defined by having a frequency of one day.
  """
  
  @rosetta_condition
  def condition_0_MandatoryEarlyTermination(self):
    """
    The FpML MandatoryEarlyTermination.model specifies a required choice node. The choice node associated with the FpML EarlyTerminationProvision is quite complex and using the data rule provides a more flexible approach than adding complexity to the condition grammar.
    """
    return ((((self.mandatoryEarlyTermination) is not None) or ((self.optionalEarlyTermination) is not None)) or (((self.mandatoryEarlyTermination) is not None) and ((self.optionalEarlyTermination) is not None)))

from cdm.product.template.MandatoryEarlyTermination import MandatoryEarlyTermination
from cdm.base.datetime.Period import Period
from cdm.product.template.OptionalEarlyTermination import OptionalEarlyTermination
from cdm.product.template.ExercisePeriod import ExercisePeriod

EarlyTerminationProvision.update_forward_refs()
