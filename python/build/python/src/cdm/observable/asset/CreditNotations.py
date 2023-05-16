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

__all__ = ['CreditNotations']


class CreditNotations(BaseDataClass):
  """
  Represents the credit rating notation higher level construct, which provides the ability to specify multiple rating notations.
  """
  creditNotation: Optional[CreditNotation] = Field(None, description="Specifies only one credit notation is determined.")
  """
  Specifies only one credit notation is determined.
  """
  creditNotations: Optional[MultipleCreditNotations] = Field(None, description="Specifies if several credit notations exist, alongside an 'any' or 'all' or all condition.")
  """
  Specifies if several credit notations exist, alongside an 'any' or 'all' or all condition.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('creditNotation', 'creditNotations', necessity=True)

from cdm.observable.asset.CreditNotation import CreditNotation
from cdm.observable.asset.MultipleCreditNotations import MultipleCreditNotations

CreditNotations.update_forward_refs()
