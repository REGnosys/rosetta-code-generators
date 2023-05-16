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

__all__ = ['OtherEligibleAndPostedSupport']


class OtherEligibleAndPostedSupport(BaseDataClass):
  """
  A class to specify the Other Eligible Support elections associated Initial and Variation margin agreements.
  """
  applicableTransfer: Optional[bool] = Field(None, description="The definition of 'Transfer' with respect to Other Eligible Support (IM) and Other Posted Support (IM).")
  """
  The definition of 'Transfer' with respect to Other Eligible Support (IM) and Other Posted Support (IM).
  """
  applicableValue: bool = Field(..., description="The definition of 'Value' with respect to Other Eligible Support (IM) and Other Posted Support (IM).")
  """
  The definition of 'Value' with respect to Other Eligible Support (IM) and Other Posted Support (IM).
  """


OtherEligibleAndPostedSupport.update_forward_refs()
