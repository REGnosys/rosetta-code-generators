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

__all__ = ['Administrator']


class Administrator(BaseDataClass):
  """
  The administrator for that rate or benchmark or, if there is no administrator, the provider of that rate or benchmark.
  """
  name: Optional[str] = Field(None, description="e.g. Reserve Bank of Australia")
  """
  e.g. Reserve Bank of Australia
  """
  website: Optional[str] = Field(None, description="e.g. https://www.bloomberg.com/")
  """
  e.g. https://www.bloomberg.com/
  """


Administrator.update_forward_refs()
