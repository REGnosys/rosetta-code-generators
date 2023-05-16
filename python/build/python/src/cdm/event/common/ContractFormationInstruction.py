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

__all__ = ['ContractFormationInstruction']


class ContractFormationInstruction(BaseDataClass):
  """
  Specifies instructions to create a fully formed contract, with optional legal agreements.
  """
  legalAgreement: List[LegalAgreement] = Field([], description="Optional legal agreements associated to the contract being formed, for instance a master agreement.")
  """
  Optional legal agreements associated to the contract being formed, for instance a master agreement.
  """
  
  @rosetta_condition
  def condition_0_ExecutedAgreements(self):
    """
    The full formation of a contract can only be completed with executed legal agreements.
    """
    def _then_fn0():
      return ((self.legalAgreement.agreementDate) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.legalAgreement) is not None), _then_fn0, _else_fn0)

from cdm.legaldocumentation.common.LegalAgreement import LegalAgreement

ContractFormationInstruction.update_forward_refs()
