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

__all__ = ['ReferenceBank']


class ReferenceBank(BaseDataClass):
  """
  A class to describe an institution (party) identified by means of a coding scheme and an optional name.
  """
  referenceBankId: AttributeWithMeta[str] | str = Field(..., description="An institution (party) identifier, e.g. a bank identifier code (BIC). FpML specifies a referenceBankIdScheme.")
  """
  An institution (party) identifier, e.g. a bank identifier code (BIC). FpML specifies a referenceBankIdScheme.
  """
  referenceBankName: Optional[str] = Field(None, description="The name of the institution (party). A free format string. FpML does not define usage rules for the element.")
  """
  The name of the institution (party). A free format string. FpML does not define usage rules for the element.
  """


ReferenceBank.update_forward_refs()
