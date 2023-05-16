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

__all__ = ['AutomaticExercise']


class AutomaticExercise(BaseDataClass):
  """
  A type to define automatic exercise of a swaption. With automatic exercise the option is deemed to have exercised if it is in the money by more than the threshold amount on the exercise date.
  """
  thresholdRate: Decimal = Field(..., description="A threshold rate. The threshold of 0.10% would be represented as 0.001")
  """
  A threshold rate. The threshold of 0.10% would be represented as 0.001
  """


AutomaticExercise.update_forward_refs()
