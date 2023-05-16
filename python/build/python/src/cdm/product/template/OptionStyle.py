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

__all__ = ['OptionStyle']


class OptionStyle(BaseDataClass):
  """
  The qualification of the option style: American, Bermuda or European. FpML implements those features as part of a substitution group.
  """
  americanExercise: Optional[AmericanExercise] = Field(None, description="")
  bermudaExercise: Optional[BermudaExercise] = Field(None, description="")
  europeanExercise: Optional[EuropeanExercise] = Field(None, description="")
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('americanExercise', 'bermudaExercise', 'europeanExercise', necessity=True)

from cdm.product.template.AmericanExercise import AmericanExercise
from cdm.product.template.BermudaExercise import BermudaExercise
from cdm.product.template.EuropeanExercise import EuropeanExercise

OptionStyle.update_forward_refs()
