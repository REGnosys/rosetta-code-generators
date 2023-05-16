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

__all__ = ['CreditSupportProviderElection']


class CreditSupportProviderElection(BaseDataClass):
  """
  The party election of Credit Support Provider(s), if any.
  """
  bespokeCreditSuppportProvider: Optional[str] = Field(None, description="...")
  """
  ...
  """
  creditSupportProvider: List[LegalEntity] = Field([], description="The specified Credit Support Provider(s), if any.")
  """
  The specified Credit Support Provider(s), if any.
  """
  creditSupportProviderTerms: CreditSupportProviderTermsEnum = Field(..., description="Specification of the Credit Support Provider terms.")
  """
  Specification of the Credit Support Provider terms.
  """
  party: Party = Field(..., description="The elective party")
  """
  The elective party
  """
  
  @rosetta_condition
  def condition_0_CreditSupportProvider(self):
    """
    A validation rule to ensure that a Credit Support Provider is specified when required.
    """
    def _then_fn0():
      return ((self.creditSupportProvider) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.creditSupportProviderTerms, "=", CreditSupportProviderTermsEnum.SPECIFIED), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.LegalEntity import LegalEntity
from cdm.legaldocumentation.common.CreditSupportProviderTermsEnum import CreditSupportProviderTermsEnum
from cdm.base.staticdata.party.Party import Party

CreditSupportProviderElection.update_forward_refs()
