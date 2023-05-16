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

__all__ = ['FloatingRateIndexMap']


class FloatingRateIndexMap(BaseDataClass):
  """
  A map for a single FRO to or from an equivalent or similar FRO in a different contractual definitions version.
  """
  contractualDefinitionIdentifier: Optional[ContractualDefinitionIdentifier] = Field(None, description="Contractual Definition to which the map applies. Includes Document Type and Document Version")
  """
  Contractual Definition to which the map applies. Includes Document Type and Document Version
  """
  identifier: Optional[Identifier] = Field(None, description="Corresponds to the unique identifier of the Contractual Definition to which the map applies")
  """
  Corresponds to the unique identifier of the Contractual Definition to which the map applies
  """
  index: FloatingRateIndexEnum = Field(..., description=" The FRO name that is being mapped to/from.")
  """
   The FRO name that is being mapped to/from.
  """
  
  @rosetta_condition
  def condition_0_Choice(self):
    """
    Choice between document uuid or document type and version
    """
    return self.check_one_of_constraint('identifier', 'contractualDefinitionIdentifier', necessity=True)

from cdm.observable.asset.fro.ContractualDefinitionIdentifier import ContractualDefinitionIdentifier
from cdm.base.staticdata.identifier.Identifier import Identifier
from cdm.base.staticdata.asset.rates.FloatingRateIndexEnum import FloatingRateIndexEnum

FloatingRateIndexMap.update_forward_refs()
