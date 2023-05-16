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

__all__ = ['Address']


class Address(BaseDataClass):
  """
  A class to specify a post or street address.
  """
  city: Optional[str] = Field(None, description="The city component of the postal address.")
  """
  The city component of the postal address.
  """
  country: Optional[AttributeWithMeta[str] | str] = Field(None, description="The ISO 3166 standard code for the country within which the postal address is located.")
  """
  The ISO 3166 standard code for the country within which the postal address is located.
  """
  postalCode: Optional[str] = Field(None, description="The code, required for computerized mail sorting systems, that is allocated to a physical address by a national postal authority.")
  """
  The code, required for computerized mail sorting systems, that is allocated to a physical address by a national postal authority.
  """
  state: Optional[str] = Field(None, description="A country subdivision used in postal addresses in some countries. For example, US states, Canadian provinces, Swiss cantons, ...")
  """
  A country subdivision used in postal addresses in some countries. For example, US states, Canadian provinces, Swiss cantons, ...
  """
  street: List[str] = Field([], description="The set of street and building number information that identifies a postal address within a city.")
  """
  The set of street and building number information that identifies a postal address within a city.
  """
  @rosetta_condition
  def cardinality_street(self):
    return check_cardinality(self.street, 1, None)
  


Address.update_forward_refs()
