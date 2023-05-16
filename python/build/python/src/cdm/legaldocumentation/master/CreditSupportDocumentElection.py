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

__all__ = ['CreditSupportDocumentElection']


class CreditSupportDocumentElection(BaseDataClass):
  """
  The party election of Credit Support Provider(s), if any.
  """
  bespokeCreditSuppportDocument: Optional[str] = Field(None, description="Specification of a document when not captured under RelatedAgreement")
  """
  Specification of a document when not captured under RelatedAgreement
  """
  creditSupportDocument: List[LegalAgreement] = Field([], description="The specified Credit Support Document(s), if any.")
  """
  The specified Credit Support Document(s), if any.
  """
  creditSupportDocumentTerms: CreditSupportDocumentTermsEnum = Field(..., description="Specification of the Credit Support Document terms.")
  """
  Specification of the Credit Support Document terms.
  """
  party: Party = Field(..., description="The elective party")
  """
  The elective party
  """
  
  @rosetta_condition
  def condition_0_CreditSupportDocument(self):
    """
    A validation rule to ensure that a Credit Support Document is specified when required.
    """
    def _then_fn0():
      return ((self.creditSupportDocument) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.creditSupportDocumentTerms, "=", CreditSupportDocumentTermsEnum.SPECIFIED), _then_fn0, _else_fn0)

from cdm.legaldocumentation.common.LegalAgreement import LegalAgreement
from cdm.legaldocumentation.common.CreditSupportDocumentTermsEnum import CreditSupportDocumentTermsEnum
from cdm.base.staticdata.party.Party import Party

CreditSupportDocumentElection.update_forward_refs()
