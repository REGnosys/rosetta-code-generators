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

__all__ = ['BespokeTransferTiming']


class BespokeTransferTiming(BaseDataClass):
  """
  A class to specify any bespoke Transfer Timing language by each party to the agreement.
  """
  bespokeTransferTimingTerms: Optional[str] = Field(None, description="The bespoke transfer timing terms applicable to the agreement")
  """
  The bespoke transfer timing terms applicable to the agreement
  """
  isApplicable: bool = Field(..., description="A boolean flag to specify whether bespoke transfer terms are applicable or not.")
  """
  A boolean flag to specify whether bespoke transfer terms are applicable or not.
  """


BespokeTransferTiming.update_forward_refs()
