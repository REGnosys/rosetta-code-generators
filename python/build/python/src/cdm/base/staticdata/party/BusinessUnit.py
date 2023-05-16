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

__all__ = ['BusinessUnit']


class BusinessUnit(BaseDataClass):
  """
  A class to specify an organizational unit.
  """
  contactInformation: Optional[ContactInformation] = Field(None, description="The contact information for such business unit, when different from the contact information associated with the party.")
  """
  The contact information for such business unit, when different from the contact information associated with the party.
  """
  identifier: Optional[Identifier] = Field(None, description="An identifier used to uniquely identify the organizational unit")
  """
  An identifier used to uniquely identify the organizational unit
  """
  name: str = Field(..., description="A name used to describe the organizational unit")
  """
  A name used to describe the organizational unit
  """

from cdm.base.staticdata.party.ContactInformation import ContactInformation
from cdm.base.staticdata.identifier.Identifier import Identifier

BusinessUnit.update_forward_refs()
