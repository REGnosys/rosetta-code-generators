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

__all__ = ['LegalAgreement']

from cdm.legaldocumentation.common.LegalAgreementBase import LegalAgreementBase

class LegalAgreement(LegalAgreementBase):
  """
  The specification of a legal agreement between two parties, being negotiated or having been executed. This includes the baseline information and the optional specialised elections
  """
  agreementTerms: Optional[AgreementTerms] = Field(None, description="Specification of the content of the legal agreement.")
  """
  Specification of the content of the legal agreement.
  """
  relatedAgreements: List[LegalAgreement] = Field([], description="Specifies the agreement(s) that govern the agreement, either as a reference to such agreements when specified as part of the CDM, or through identification of some of the key terms of those agreements, such as the type of agreement, the publisher, the vintage, the agreement identifier and the agreement date.")
  """
  Specifies the agreement(s) that govern the agreement, either as a reference to such agreements when specified as part of the CDM, or through identification of some of the key terms of those agreements, such as the type of agreement, the publisher, the vintage, the agreement identifier and the agreement date.
  """
  umbrellaAgreement: Optional[UmbrellaAgreement] = Field(None, description="The determination of whether Umbrella Agreement terms are applicable (True) or Not Applicable (False).")
  """
  The determination of whether Umbrella Agreement terms are applicable (True) or Not Applicable (False).
  """
  
  @rosetta_condition
  def condition_0_ConsistentlyExecutedAgreements(self):
    """
    An executed agreement can only point to executed related agreements if any.
    """
    def _then_fn0():
      return ((self.relatedAgreements.agreementDate) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((self.relatedAgreements) is not None) and ((self.agreementDate) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_AgreementVerification(self):
    """
    A validation rule to ensure that the agreement elections are associated with the correct legal agreement type as specified.
    """
    def _then_fn3():
      return all_elements(self.legalAgreementIdentification.agreementName.agreementType, "=", LegalAgreementTypeEnum.MASTER_AGREEMENT)
    
    def _else_fn3():
      return True
    
    def _then_fn2():
      return all_elements(self.legalAgreementIdentification.agreementName.creditSupportAgreementType, "=", CreditSupportAgreementTypeEnum.COLLATERAL_TRANSFER_AGREEMENT)
    
    def _else_fn2():
      return if_cond_fn(((self.agreementTerms.agreement.masterAgreementSchedule) is not None), _then_fn3, _else_fn3)
    
    def _then_fn1():
      return (all_elements(self.legalAgreementIdentification.agreementName.creditSupportAgreementType, "=", CreditSupportAgreementTypeEnum.CREDIT_SUPPORT_ANNEX) or all_elements(self.legalAgreementIdentification.agreementName.creditSupportAgreementType, "=", CreditSupportAgreementTypeEnum.CREDIT_SUPPORT_DEED))
    
    def _else_fn1():
      return if_cond_fn(((self.agreementTerms.agreement.collateralTransferAgreementElections) is not None), _then_fn2, _else_fn2)
    
    def _then_fn0():
      return all_elements(self.legalAgreementIdentification.agreementName.agreementType, "=", LegalAgreementTypeEnum.SECURITY_AGREEMENT)
    
    def _else_fn0():
      return if_cond_fn(((self.agreementTerms.agreement.creditSupportAgreementElections) is not None), _then_fn1, _else_fn1)
    
    return if_cond_fn(((self.agreementTerms.agreement.securityAgreementElections) is not None), _then_fn0, _else_fn0)

from cdm.legaldocumentation.common.AgreementTerms import AgreementTerms
from cdm.legaldocumentation.common.LegalAgreement import LegalAgreement
from cdm.legaldocumentation.common.UmbrellaAgreement import UmbrellaAgreement
from cdm.legaldocumentation.common.LegalAgreementTypeEnum import LegalAgreementTypeEnum
from cdm.legaldocumentation.csa.CreditSupportAgreementTypeEnum import CreditSupportAgreementTypeEnum

LegalAgreement.update_forward_refs()
