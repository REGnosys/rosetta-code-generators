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

__all__ = ['PersonIdentifier']


class PersonIdentifier(BaseDataClass):
  """
  Comprises an identifier and a source. The associated metadata key denotes the ability to associate a hash value to the PersonIdentifier instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage.
  """
  country: Optional[AttributeWithMeta[str] | str] = Field(None, description="The ISO 3166 standard code for the country issuing the identifier.")
  """
  The ISO 3166 standard code for the country issuing the identifier.
  """
  identifier: AttributeWithMeta[str] | str = Field(..., description="Provides an identifier associated with a person. The identifier is unique within the public source specified in the source attribute.")
  """
  Provides an identifier associated with a person. The identifier is unique within the public source specified in the source attribute.
  """
  identifierType: Optional[PersonIdentifierTypeEnum] = Field(None, description="Defines the source of the identifier.")
  """
  Defines the source of the identifier.
  """

from cdm.base.staticdata.party.PersonIdentifierTypeEnum import PersonIdentifierTypeEnum

PersonIdentifier.update_forward_refs()
