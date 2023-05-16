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

__all__ = ['LegalAgreementIdentification']


class LegalAgreementIdentification(BaseDataClass):
  """
  Specifies the type of legal agreement, identified via a set of composable attributes: agreementName, publisher, governing law and version, e.g. ISDA 2013 Standard Credit Support Annex English Law.
  """
  agreementName: AgreementName = Field(..., description="The legal agreement name, e.g. Credit Support Annex for Variation Margin.")
  """
  The legal agreement name, e.g. Credit Support Annex for Variation Margin.
  """
  governingLaw: Optional[GoverningLawEnum] = Field(None, description="The law governing the legal agreement, e.g. English Law, New York Law or Japanese Law.")
  """
  The law governing the legal agreement, e.g. English Law, New York Law or Japanese Law.
  """
  publisher: Optional[LegalAgreementPublisherEnum] = Field(None, description="The legal agreement publisher, e.g. ISDA.")
  """
  The legal agreement publisher, e.g. ISDA.
  """
  vintage: Optional[int] = Field(None, description="In the case where successive definitions of the legal agreement have been developed, the vintage identification. This is typically (but not necessarily) done by referencing the year, e.g. 2013 in the case of the ISDA 2013 Standard Credit Support Annex.")
  """
  In the case where successive definitions of the legal agreement have been developed, the vintage identification. This is typically (but not necessarily) done by referencing the year, e.g. 2013 in the case of the ISDA 2013 Standard Credit Support Annex.
  """
  
  @rosetta_condition
  def condition_0_CSAMarginType(self):
    """
    A condition to ensure that CSA margin type is only specified if a credit support agreemnt type is specified and its published vintage year is equal to or after 2016.
    """
    def _then_fn0():
      return (((self.agreementName.creditSupportAgreementType) is not None) and all_elements(self.vintage, ">=", 2016))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.agreementName.creditSupportAgreementMarginType) is not None), _then_fn0, _else_fn0)

from cdm.legaldocumentation.common.AgreementName import AgreementName
from cdm.legaldocumentation.common.GoverningLawEnum import GoverningLawEnum
from cdm.legaldocumentation.common.LegalAgreementPublisherEnum import LegalAgreementPublisherEnum

LegalAgreementIdentification.update_forward_refs()
