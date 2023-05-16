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

__all__ = ['ContractDetails']


class ContractDetails(BaseDataClass):
  """
  Defines specific attributes that relate to contractual details of trades.
  """
  documentation: List[LegalAgreement] = Field([], description="Represents the legal document(s) that governs a trade and associated contractual product terms, either as a reference to such documents when specified as part of the CDM, or through identification of some of the key terms of those documents, such as the type of document, the document identifier, the publisher, the document vintage and the agreement date.")
  """
  Represents the legal document(s) that governs a trade and associated contractual product terms, either as a reference to such documents when specified as part of the CDM, or through identification of some of the key terms of those documents, such as the type of document, the document identifier, the publisher, the document vintage and the agreement date.
  """
  governingLaw: Optional[AttributeWithMeta[GoverningLawEnum] | GoverningLawEnum] = Field(None, description="Represents the law governing the trade and associated contractual product terms.")
  """
  Represents the law governing the trade and associated contractual product terms.
  """
  
  @rosetta_condition
  def condition_0_ExecutedAgreement(self):
    """
    Contract details can only only point to  executed legal agreements.
    """
    def _then_fn0():
      return ((self.documentation.agreementDate) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.documentation) is not None), _then_fn0, _else_fn0)

from cdm.legaldocumentation.common.LegalAgreement import LegalAgreement
from cdm.legaldocumentation.common.GoverningLawEnum import GoverningLawEnum

ContractDetails.update_forward_refs()
