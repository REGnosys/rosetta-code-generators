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

__all__ = ['ContactInformation']


class ContactInformation(BaseDataClass):
  """
  A class to specify contact information associated with a party: telephone, postal/street address, email and web page.
  """
  address: List[Address] = Field([], description="The street/postal address.")
  """
  The street/postal address.
  """
  email: List[str] = Field([], description="The email address.")
  """
  The email address.
  """
  telephone: List[TelephoneNumber] = Field([], description="The telephone number.")
  """
  The telephone number.
  """
  webPage: List[str] = Field([], description="The web page. This attribute is not specified as part of the FpML ContactInformation complex type.")
  """
  The web page. This attribute is not specified as part of the FpML ContactInformation complex type.
  """

from cdm.base.staticdata.party.Address import Address
from cdm.base.staticdata.party.TelephoneNumber import TelephoneNumber

ContactInformation.update_forward_refs()
