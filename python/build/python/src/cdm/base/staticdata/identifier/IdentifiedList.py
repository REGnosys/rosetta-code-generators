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

__all__ = ['IdentifiedList']


class IdentifiedList(BaseDataClass):
  """
  Attaches an identifier to a collection of objects, when those objects themselves can each be represented by an identifier. One use case is the representation of package transactions, where each component is a separate trade with its own identifier, and those trades are linked together as a package with its own identifier. The data type has been named generically rather than referring to 'packages' as it may have a number of other uses.
  """
  componentId: List[Identifier] = Field([], description="Identifiers for each component of the list. Since the data type is used to link multiple identified objects together, at least 2 components are required in the list. Creating an identified list with only 1 identified component has been deemed unnecessary, because it would just create a redundant identifier.")
  """
  Identifiers for each component of the list. Since the data type is used to link multiple identified objects together, at least 2 components are required in the list. Creating an identified list with only 1 identified component has been deemed unnecessary, because it would just create a redundant identifier.
  """
  @rosetta_condition
  def cardinality_componentId(self):
    return check_cardinality(self.componentId, 2, None)
  
  listId: Identifier = Field(..., description="The identifier for the list. In the case of a package transaction, this would be the package identifier. This attribute is mandatory to allow the list itself to be identified.")
  """
  The identifier for the list. In the case of a package transaction, this would be the package identifier. This attribute is mandatory to allow the list itself to be identified.
  """
  price: Optional[Price] = Field(None, description="The price of the package.")
  """
  The price of the package.
  """

from cdm.base.staticdata.identifier.Identifier import Identifier
from cdm.observable.asset.Price import Price

IdentifiedList.update_forward_refs()
