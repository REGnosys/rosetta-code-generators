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

__all__ = ['ContractualDefinition']


class ContractualDefinition(BaseDataClass):
  contractualDefinitionIdentifier: Optional[ContractualDefinitionIdentifier] = Field(None, description="Contractual Definition Identifier in which the code is published. Includes Document Type and Document Version")
  """
  Contractual Definition Identifier in which the code is published. Includes Document Type and Document Version
  """
  identifier: Optional[Identifier] = Field(None, description="Corresponds to the unique identifier of the Contractual Definition in which the code is published")
  """
  Corresponds to the unique identifier of the Contractual Definition in which the code is published
  """
  publicationDate: Optional[date] = Field(None, description="2021-06-11")
  """
  2021-06-11
  """
  
  @rosetta_condition
  def condition_0_Choice(self):
    """
    Choice between document uuid or document type and version
    """
    return self.check_one_of_constraint('identifier', 'contractualDefinitionIdentifier', necessity=True)

from cdm.observable.asset.fro.ContractualDefinitionIdentifier import ContractualDefinitionIdentifier
from cdm.base.staticdata.identifier.Identifier import Identifier

ContractualDefinition.update_forward_refs()
