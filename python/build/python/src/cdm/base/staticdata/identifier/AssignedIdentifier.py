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

__all__ = ['AssignedIdentifier']


class AssignedIdentifier(BaseDataClass):
  """
  A class to specify the identifier value and its associated version.
  """
  identifier: AttributeWithMeta[str] | str = Field(..., description="The identifier value.")
  """
  The identifier value.
  """
  identifierType: Optional[TradeIdentifierTypeEnum] = Field(None, description="The enumerated classification of the identifier.")
  """
  The enumerated classification of the identifier.
  """
  version: Optional[int] = Field(None, description="The identifier version, which is specified as an integer and is meant to be incremented each time the transaction terms (whether contract or event) change. This version is made option to support the use case where the identifier is referenced without the version. The constraint that a contract and a lifecycle event need to have an associated version is enforced through data rules.")
  """
  The identifier version, which is specified as an integer and is meant to be incremented each time the transaction terms (whether contract or event) change. This version is made option to support the use case where the identifier is referenced without the version. The constraint that a contract and a lifecycle event need to have an associated version is enforced through data rules.
  """

from cdm.base.staticdata.identifier.TradeIdentifierTypeEnum import TradeIdentifierTypeEnum

AssignedIdentifier.update_forward_refs()
