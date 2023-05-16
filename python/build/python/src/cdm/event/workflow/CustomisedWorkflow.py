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

__all__ = ['CustomisedWorkflow']


class CustomisedWorkflow(BaseDataClass):
  """
  In its initial iteration, this class is meant to support the DTCC TIW workflow information.
  """
  itemName: str = Field(..., description="In this initial iteration, this corresponds to the DTCC TIW element name.")
  """
  In this initial iteration, this corresponds to the DTCC TIW element name.
  """
  itemValue: str = Field(..., description="In this initial iteration, this corresponds to the DTCC value.")
  """
  In this initial iteration, this corresponds to the DTCC value.
  """


CustomisedWorkflow.update_forward_refs()
