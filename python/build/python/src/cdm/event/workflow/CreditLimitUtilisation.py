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

__all__ = ['CreditLimitUtilisation']


class CreditLimitUtilisation(BaseDataClass):
  """
  Credit limit utilisation breakdown by executed trades and pending orders.
  """
  executed: Optional[CreditLimitUtilisationPosition] = Field(None, description="Credit limit utilisation attributable to executed trades.")
  """
  Credit limit utilisation attributable to executed trades.
  """
  pending: Optional[CreditLimitUtilisationPosition] = Field(None, description="Credit limit utilisation attributable to pending unexecuted orders.")
  """
  Credit limit utilisation attributable to pending unexecuted orders.
  """

from cdm.event.workflow.CreditLimitUtilisationPosition import CreditLimitUtilisationPosition

CreditLimitUtilisation.update_forward_refs()
