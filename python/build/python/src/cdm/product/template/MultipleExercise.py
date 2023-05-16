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

__all__ = ['MultipleExercise']

from cdm.product.template.PartialExercise import PartialExercise

class MultipleExercise(PartialExercise):
  """
  A class defining multiple exercises. As defined in the 2000 ISDA Definitions, Section 12.4. Multiple Exercise, the buyer of the option has the right to exercise all or less than all the unexercised notional amount of the underlying swap on one or more days in the exercise period, but on any such day may not exercise less than the minimum notional amount or more than the maximum notional amount, and if an integral multiple amount is specified, the notional exercised must be equal to or, be an integral multiple of, the integral multiple amount. In FpML, MultipleExercise is built upon the PartialExercise.model.
  """
  maximumNotionalAmount: Optional[Decimal] = Field(None, description="The maximum notional amount that can be exercised on a given exercise date.")
  """
  The maximum notional amount that can be exercised on a given exercise date.
  """
  maximumNumberOfOptions: Optional[int] = Field(None, description="The maximum number of options that can be exercised on a given exercise date. If the number is not specified, it means that the maximum number of options corresponds to the remaining unexercised options.")
  """
  The maximum number of options that can be exercised on a given exercise date. If the number is not specified, it means that the maximum number of options corresponds to the remaining unexercised options.
  """
  
  @rosetta_condition
  def condition_0_MaximumChoice(self):
    """
    Choice rule to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('maximumNotionalAmount', 'maximumNumberOfOptions', necessity=True)
  
  @rosetta_condition
  def condition_1_MaximumNumberOfOptions(self):
    """
    FpML MultipleExercise construct specifies the maximumNumberOfOptions as a positive integer.
    """
    def _then_fn0():
      return all_elements(self.maximumNotionalAmount, ">=", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.maximumNumberOfOptions) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_MinimumNumberOfOptions(self):
    """
    FpML MultipleExercise construct specifies the minimumNumberOfOptions as a positive integer.
    """
    def _then_fn0():
      return all_elements(self.minimumNumberOfOptions, ">=", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.minimumNumberOfOptions) is not None), _then_fn0, _else_fn0)


MultipleExercise.update_forward_refs()
