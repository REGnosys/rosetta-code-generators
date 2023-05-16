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

__all__ = ['OtherAgreement']


class OtherAgreement(BaseDataClass):
  """
  A class for defining an agreement executed between parties.
  """
  date: Optional[date] = Field(None, description="The date on which the agreement was signed.")
  """
  The date on which the agreement was signed.
  """
  identifier: Optional[AttributeWithMeta[str] | str] = Field(None, description="An identifier that has been created to identify the agreement.")
  """
  An identifier that has been created to identify the agreement.
  """
  otherAgreementType: AttributeWithMeta[str] | str = Field(..., description="The agreement executed between the parties and intended to govern product-specific derivatives transactions between those parties.")
  """
  The agreement executed between the parties and intended to govern product-specific derivatives transactions between those parties.
  """
  version: Optional[AttributeWithMeta[str] | str] = Field(None, description="The version of the agreement.")
  """
  The version of the agreement.
  """


OtherAgreement.update_forward_refs()
