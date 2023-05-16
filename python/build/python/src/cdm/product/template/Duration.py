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

__all__ = ['Duration']


class Duration(BaseDataClass):
  """
  Specifies the Duration Terms of the Security Financing Transaction, and optionally any Evergreen terms.
  """
  durationType: DurationTypeEnum = Field(..., description="Specifies the Duration Terms of the Security Financing transaction. e.g. Open or Term.")
  """
  Specifies the Duration Terms of the Security Financing transaction. e.g. Open or Term.
  """
  evergreenProvision: Optional[EvergreenProvision] = Field(None, description="A data defining: the right of a party to exercise an Evergreen option")
  """
  A data defining: the right of a party to exercise an Evergreen option
  """

from cdm.product.template.DurationTypeEnum import DurationTypeEnum
from cdm.product.template.EvergreenProvision import EvergreenProvision

Duration.update_forward_refs()
