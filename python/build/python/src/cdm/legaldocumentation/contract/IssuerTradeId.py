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

__all__ = ['IssuerTradeId']


class IssuerTradeId(BaseDataClass):
  """
  A class for a two-parts identifier, such as a USI.
  """
  identifier: Optional[AttributeWithMeta[str] | str] = Field(None, description="The identifier value. The CDM uses a neutral identifier attribute name rather than the FpML trade qualifier because of the focus that includes the pre-execution lifecycle, at which point a trade doesn't exist yet.")
  """
  The identifier value. The CDM uses a neutral identifier attribute name rather than the FpML trade qualifier because of the focus that includes the pre-execution lifecycle, at which point a trade doesn't exist yet.
  """
  issuer: AttributeWithMeta[str] | str = Field(..., description="The party that assigns the trade identifier.")
  """
  The party that assigns the trade identifier.
  """


IssuerTradeId.update_forward_refs()
