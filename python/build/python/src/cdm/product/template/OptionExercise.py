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

__all__ = ['OptionExercise']


class OptionExercise(BaseDataClass):
  """
   A class to represent the applicable terms to qualify an option exercise: the option style (e.g. American style option), the exercise procedure (e.g. manual exercise) and the settlement terms (e.g. physical vs. cash).
  """
  exerciseProcedure: Optional[ExerciseProcedure] = Field(None, description="The set of parameters defining the procedure associated with the exercise, e.g. manual exercise.")
  """
  The set of parameters defining the procedure associated with the exercise, e.g. manual exercise.
  """
  optionStyle: OptionStyle = Field(..., description="The option exercise can be of American style, Bermuda style or European style. The FpML implementation makes use of a substitution group.")
  """
  The option exercise can be of American style, Bermuda style or European style. The FpML implementation makes use of a substitution group.
  """
  strike: Optional[OptionStrike] = Field(None, description="Specifies the strike of the option on credit default swap.")
  """
  Specifies the strike of the option on credit default swap.
  """

from cdm.product.template.ExerciseProcedure import ExerciseProcedure
from cdm.product.template.OptionStyle import OptionStyle
from cdm.product.template.OptionStrike import OptionStrike

OptionExercise.update_forward_refs()
