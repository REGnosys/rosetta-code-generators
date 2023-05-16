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

__all__ = ['ReferenceBanks']


class ReferenceBanks(BaseDataClass):
  """
  A class defining the list of reference institutions polled for relevant rates or prices when determining the cash settlement amount for a product where cash settlement is applicable.
  """
  referenceBank: List[ReferenceBank] = Field([], description="An institution (party) identified by means of a coding scheme and an optional name.")
  """
  An institution (party) identified by means of a coding scheme and an optional name.
  """
  @rosetta_condition
  def cardinality_referenceBank(self):
    return check_cardinality(self.referenceBank, 1, None)
  

from cdm.base.staticdata.party.ReferenceBank import ReferenceBank

ReferenceBanks.update_forward_refs()
