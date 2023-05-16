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

__all__ = ['AgreementName']


class AgreementName(BaseDataClass):
  """
  Specifies the agreement name through an agreement type and optional detailed sub agreement type.
  """
  agreementType: LegalAgreementTypeEnum = Field(..., description="Specification of the legal agreement type.")
  """
  Specification of the legal agreement type.
  """
  brokerConfirmationType: Optional[BrokerConfirmationTypeEnum] = Field(None, description="Specification of the broker confirmation type.")
  """
  Specification of the broker confirmation type.
  """
  contractualDefinitionsType: List[AttributeWithMeta[ContractualDefinitionsEnum] | ContractualDefinitionsEnum] = Field([], description="The definitions such as those published by ISDA that will define the terms of the trade.")
  """
  The definitions such as those published by ISDA that will define the terms of the trade.
  """
  contractualMatrix: List[ContractualMatrix] = Field([], description="A reference to a contractual matrix of elected terms/values (such as those published by ISDA) that shall be deemed to apply to the trade. The applicable matrix is identified by reference to a name and optionally a publication date. Depending on the structure of the matrix, an additional term (specified in the matrixTerm element) may be required to further identify a subset of applicable terms/values within the matrix.")
  """
  A reference to a contractual matrix of elected terms/values (such as those published by ISDA) that shall be deemed to apply to the trade. The applicable matrix is identified by reference to a name and optionally a publication date. Depending on the structure of the matrix, an additional term (specified in the matrixTerm element) may be required to further identify a subset of applicable terms/values within the matrix.
  """
  contractualTermsSupplement: List[ContractualTermsSupplement] = Field([], description="A contractual supplement (such as those published by ISDA) that will apply to the trade.")
  """
  A contractual supplement (such as those published by ISDA) that will apply to the trade.
  """
  creditSupportAgreementMarginType: Optional[CreditSupportAgreementMarginTypeEnum] = Field(None, description="specifies the type of margin for which a legal agreement is named.")
  """
  specifies the type of margin for which a legal agreement is named.
  """
  creditSupportAgreementType: Optional[AttributeWithMeta[CreditSupportAgreementTypeEnum] | CreditSupportAgreementTypeEnum] = Field(None, description="Specification of the credit support agreement type.")
  """
  Specification of the credit support agreement type.
  """
  masterAgreementType: Optional[AttributeWithMeta[MasterAgreementTypeEnum] | MasterAgreementTypeEnum] = Field(None, description="Specification of the master agreement type.")
  """
  Specification of the master agreement type.
  """
  masterConfirmationAnnexType: Optional[AttributeWithMeta[MasterConfirmationAnnexTypeEnum] | MasterConfirmationAnnexTypeEnum] = Field(None, description="The type of master confirmation annex executed between the parties.")
  """
  The type of master confirmation annex executed between the parties.
  """
  masterConfirmationType: Optional[AttributeWithMeta[MasterConfirmationTypeEnum] | MasterConfirmationTypeEnum] = Field(None, description="The type of master confirmation executed between the parties.")
  """
  The type of master confirmation executed between the parties.
  """
  otherAgreement: Optional[str] = Field(None, description="Definition of an agreement that is not enumerated in the CDM.")
  """
  Definition of an agreement that is not enumerated in the CDM.
  """
  
  @rosetta_condition
  def condition_0_AgreementType(self):
    """
    A condition to ensure that the agreement type specified is consistent with the detailed documentation identified.
    """
    def _then_fn4():
      return ((((self.contractualDefinitionsType) is None) and ((self.contractualTermsSupplement) is None)) and ((self.contractualMatrix) is None))
    
    def _else_fn4():
      return True
    
    def _then_fn3():
      return (((self.masterConfirmationType) is None) and ((self.masterConfirmationAnnexType) is None))
    
    def _else_fn3():
      return if_cond_fn(any_elements(self.agreementType, "<>", LegalAgreementTypeEnum.CONFIRMATION), _then_fn4, _else_fn4)
    
    def _then_fn2():
      return ((self.brokerConfirmationType) is None)
    
    def _else_fn2():
      return if_cond_fn(any_elements(self.agreementType, "<>", LegalAgreementTypeEnum.MASTER_CONFIRMATION), _then_fn3, _else_fn3)
    
    def _then_fn1():
      return ((self.masterAgreementType) is None)
    
    def _else_fn1():
      return if_cond_fn(any_elements(self.agreementType, "<>", LegalAgreementTypeEnum.BROKER_CONFIRMATION), _then_fn2, _else_fn2)
    
    def _then_fn0():
      return ((self.otherAgreement) is None)
    
    def _else_fn0():
      return if_cond_fn(any_elements(self.agreementType, "<>", LegalAgreementTypeEnum.MASTER_AGREEMENT), _then_fn1, _else_fn1)
    
    return if_cond_fn(any_elements(self.agreementType, "<>", LegalAgreementTypeEnum.OTHER), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_CreditSupportAgreement(self):
    """
    A condition to ensure that the credit supoort agreement type is specified when required.
    """
    def _then_fn0():
      return ((self.creditSupportAgreementType) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.agreementType, "=", LegalAgreementTypeEnum.CREDIT_SUPPORT_AGREEMENT), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_MasterConfirmation(self):
    """
    If a master confirmation annex type is specified a master confirmation type must exist.
    """
    def _then_fn0():
      return ((self.masterConfirmationType) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.masterConfirmationAnnexType) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_CSAMarginType(self):
    """
    A condition to ensure that CSA margin type is only specified if a credit support agreemnt type is specified.
    """
    def _then_fn0():
      return ((self.creditSupportAgreementType) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.creditSupportAgreementMarginType) is not None), _then_fn0, _else_fn0)

from cdm.legaldocumentation.common.LegalAgreementTypeEnum import LegalAgreementTypeEnum
from cdm.legaldocumentation.contract.BrokerConfirmationTypeEnum import BrokerConfirmationTypeEnum
from cdm.legaldocumentation.common.ContractualDefinitionsEnum import ContractualDefinitionsEnum
from cdm.legaldocumentation.common.ContractualMatrix import ContractualMatrix
from cdm.legaldocumentation.common.ContractualTermsSupplement import ContractualTermsSupplement
from cdm.legaldocumentation.common.CreditSupportAgreementMarginTypeEnum import CreditSupportAgreementMarginTypeEnum
from cdm.legaldocumentation.csa.CreditSupportAgreementTypeEnum import CreditSupportAgreementTypeEnum
from cdm.legaldocumentation.master.MasterAgreementTypeEnum import MasterAgreementTypeEnum
from cdm.legaldocumentation.master.MasterConfirmationAnnexTypeEnum import MasterConfirmationAnnexTypeEnum
from cdm.legaldocumentation.master.MasterConfirmationTypeEnum import MasterConfirmationTypeEnum

AgreementName.update_forward_refs()
