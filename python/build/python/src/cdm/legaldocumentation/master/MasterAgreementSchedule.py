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

__all__ = ['MasterAgreementSchedule']


class MasterAgreementSchedule(BaseDataClass):
  """
  The set of elections which specify a Master Agreement.
  """
  addressForNotices: AddressForNotices = Field(..., description="Specification of the address and other details for notices.")
  """
  Specification of the address and other details for notices.
  """
  automaticEarlyTermination: AutomaticEarlyTermination = Field(..., description="The specification of whether there is an automatic occurrence of an Early Termination Date in respect of Transactions upon the occurrence of certain bankruptcy / insolvency related events.")
  """
  The specification of whether there is an automatic occurrence of an Early Termination Date in respect of Transactions upon the occurrence of certain bankruptcy / insolvency related events.
  """
  creditSupportDocument: CreditSupportDocument = Field(..., description="Identification of party specific Credit Support Documents applicable to the document.")
  """
  Identification of party specific Credit Support Documents applicable to the document.
  """
  creditSupportProvider: CreditSupportProvider = Field(..., description="Identification of party specific Credit Support Providers applicable to the document.")
  """
  Identification of party specific Credit Support Providers applicable to the document.
  """
  nonContractualObligations: bool = Field(..., description="Specification of whether the Governing Law clause extends to Non-Contractual Obligations (True) or does not extend to Non-Contractual Obligations (False).")
  """
  Specification of whether the Governing Law clause extends to Non-Contractual Obligations (True) or does not extend to Non-Contractual Obligations (False).
  """
  specifiedEntities: List[SpecifiedEntities] = Field([], description="A provision that allows each party to specify its Specified Entities for certain Events of Default and Termination Events")
  """
  A provision that allows each party to specify its Specified Entities for certain Events of Default and Termination Events
  """
  @rosetta_condition
  def cardinality_specifiedEntities(self):
    return check_cardinality(self.specifiedEntities, 4, 4)
  
  terminationCurrency: TerminationCurrency = Field(..., description="Specification of the currency in which the termination payment is made (including the process by which such currency is determined).")
  """
  Specification of the currency in which the termination payment is made (including the process by which such currency is determined).
  """

from cdm.legaldocumentation.common.AddressForNotices import AddressForNotices
from cdm.legaldocumentation.master.AutomaticEarlyTermination import AutomaticEarlyTermination
from cdm.legaldocumentation.master.CreditSupportDocument import CreditSupportDocument
from cdm.legaldocumentation.master.CreditSupportProvider import CreditSupportProvider
from cdm.legaldocumentation.master.SpecifiedEntities import SpecifiedEntities
from cdm.legaldocumentation.master.TerminationCurrency import TerminationCurrency

MasterAgreementSchedule.update_forward_refs()
