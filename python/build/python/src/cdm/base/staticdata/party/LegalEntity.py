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

__all__ = ['LegalEntity']


class LegalEntity(BaseDataClass):
  """
  A class to specify a legal entity, with a required name and an optional entity identifier (such as the LEI).
  """
  entityId: List[AttributeWithMeta[str] | str] = Field([], description="A legal entity identifier (e.g. RED entity code).")
  """
  A legal entity identifier (e.g. RED entity code).
  """
  name: AttributeWithMeta[str] | str = Field(..., description="The legal entity name.")
  """
  The legal entity name.
  """


LegalEntity.update_forward_refs()
