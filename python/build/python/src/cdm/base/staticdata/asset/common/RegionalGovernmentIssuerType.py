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

__all__ = ['RegionalGovernmentIssuerType']


class RegionalGovernmentIssuerType(BaseDataClass):
  """
  Represents a class to allow specification of different type of Regional government collateral.
  """
  sovereignRecourse: bool = Field(..., description="Applies to regional governments, local authorities or municipals.  True if entity has recourse to sovereign (e.g. debt guaranteed by government).  False if entity does not have recourse to sovereign.")
  """
  Applies to regional governments, local authorities or municipals.  True if entity has recourse to sovereign (e.g. debt guaranteed by government).  False if entity does not have recourse to sovereign.
  """


RegionalGovernmentIssuerType.update_forward_refs()
