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

__all__ = ['Trade']


class Trade(BaseDataClass):
  """
  Defines the output of a financial transaction between parties - a Business Event. A Trade impacts the financial position (i.e. the balance sheet) of involved parties.
  """
  account: List[Account] = Field([], description="Represents a party's granular account information, which may be used in subsequent internal processing.")
  """
  Represents a party's granular account information, which may be used in subsequent internal processing.
  """
  clearedDate: Optional[date] = Field(None, description="Specifies the date on which a trade is cleared (novated) through a central counterparty clearing service.")
  """
  Specifies the date on which a trade is cleared (novated) through a central counterparty clearing service.
  """
  collateral: Optional[Collateral] = Field(None, description="Represents the collateral obligations of a party.")
  """
  Represents the collateral obligations of a party.
  """
  contractDetails: Optional[ContractDetails] = Field(None, description="Represents information specific to trades involving contractual products.")
  """
  Represents information specific to trades involving contractual products.
  """
  executionDetails: Optional[ExecutionDetails] = Field(None, description="Represents information specific to trades that arose from executions.")
  """
  Represents information specific to trades that arose from executions.
  """
  party: List[Party] = Field([], description="Represents the parties to the trade. The cardinality is optional to address the case where the trade is defined within a BusinessEvent data type, in which case the party is specified in BusinessEvent.")
  """
  Represents the parties to the trade. The cardinality is optional to address the case where the trade is defined within a BusinessEvent data type, in which case the party is specified in BusinessEvent.
  """
  partyRole: List[PartyRole] = Field([], description="Represents the role each specified party takes in the trade. further to the principal roles, payer and receiver.")
  """
  Represents the role each specified party takes in the trade. further to the principal roles, payer and receiver.
  """
  tradableProduct: TradableProduct = Field(..., description="Represents the financial instrument The corresponding FpML construct is the product abstract element and the associated substitution group.")
  """
  Represents the financial instrument The corresponding FpML construct is the product abstract element and the associated substitution group.
  """
  tradeDate: AttributeWithMeta[date] | date = Field(..., description="Specifies the date which the trade was agreed.")
  """
  Specifies the date which the trade was agreed.
  """
  tradeIdentifier: List[Identifier] = Field([], description="Represents the identifier(s) that uniquely identify a trade for an identity issuer. A trade can include multiple identifiers, for example a trade that is reportable to both the CFTC and ESMA, and then has an associated USI (Unique Swap Identifier) UTI (Unique Trade Identifier).")
  """
  Represents the identifier(s) that uniquely identify a trade for an identity issuer. A trade can include multiple identifiers, for example a trade that is reportable to both the CFTC and ESMA, and then has an associated USI (Unique Swap Identifier) UTI (Unique Trade Identifier).
  """
  @rosetta_condition
  def cardinality_tradeIdentifier(self):
    return check_cardinality(self.tradeIdentifier, 1, None)
  
  
  @rosetta_condition
  def condition_0_SecurityPartyRole(self):
    """
    When the executed product is a security, both ExecutingEntity and Counterparty party roles must exist.
    """
    def _then_fn0():
      return (contains(self.partyRole.role, PartyRoleEnum.EXECUTING_ENTITY) and contains(self.partyRole.role, PartyRoleEnum.COUNTERPARTY))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.tradableProduct.product.security) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_SecurityPartyRoleBuyerSeller(self):
    """
    When the executed product is a security, both buyer and seller party roles must exist.
    """
    def _then_fn0():
      return (contains(self.partyRole.role, PartyRoleEnum.BUYER) and contains(self.partyRole.role, PartyRoleEnum.SELLER))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.tradableProduct.product.security) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_SecurityPrice(self):
    """
    When the executed product is a security, the price must be specified.
    """
    def _then_fn0():
      return ((self.tradableProduct.tradeLot.priceQuantity.price) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.tradableProduct.product.security) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_3_SettlementTerms(self):
    """
    When the executed product is a security, the settlement terms must be specified.
    """
    def _then_fn0():
      return (((self.tradableProduct.tradeLot).priceQuantity.settlementTerms) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.tradableProduct.product.security) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_4_PackageTrade(self):
    """
    When the trade is part of a package as specified in the execution details, the trade identifier must be found as one of the package components.
    """
    def _then_fn0():
      return contains(self.executionDetails.packageReference.componentId, self.tradeIdentifier)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.executionDetails.packageReference) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_5_DeliverableObligationsPhysicalSettlementMatrix(self):
    """
    The below set of credit deliverable obligation provisions are specified as optional boolean in FpML and the CDM because they would be specified as part of the Physical Settlement Matrix when such document governs the contract terms. As a result, this data rule specifies that those provisions cannot be omitted if the Credit Derivatives Physical Settlement Matrix doesn't governs the terms of the contract.
    """
    def _then_fn0():
      return ((((((((((((((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.notSubordinated) is not None) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.specifiedCurrency) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.notSovereignLender) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.notDomesticCurrency) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.notDomesticLaw) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.notContingent) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.notDomesticIssuance) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.assignableLoan) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.consentRequiredLoan) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.transferable) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.maximumMaturity) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.notBearer) is not None)) and ((((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.fullFaithAndCreditObLiability) is not None) or ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.generalFundObligationLiability) is not None)) or ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.revenueObligationLiability) is not None)))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((any_elements(self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix.matrixType, "<>", MatrixTypeEnum.CREDIT_DERIVATIVES_PHYSICAL_SETTLEMENT_MATRIX) or ((self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix.matrixType) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_6_ObligationsPhysicalSettlementMatrix(self):
    """
    The below set of obligation of the reference entity are specified as optional boolean in FpML and the CDM because they would be specified as part of the Physical Settlement Matrix when such document governs the contract terms. As a result, this data rule specifies that those provisions cannot be omitted if the Physical Settlement Matrix governs the terms of the contract. This data rule also applies to cash settled contracts because those could still end-up being physically settled, in case the case where an auction could not take place because of, say, liquidity considerations.
    """
    def _then_fn0():
      return ((((((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.obligations.notSubordinated) is not None) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.obligations.notSovereignLender) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.obligations.notDomesticLaw) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.obligations.notDomesticIssuance) is not None)) and ((((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.obligations.fullFaithAndCreditObLiability) is not None) or ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.obligations.generalFundObligationLiability) is not None)) or ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.obligations.revenueObligationLiability) is not None)))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((any_elements(self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix.matrixType, "<>", MatrixTypeEnum.CREDIT_DERIVATIVES_PHYSICAL_SETTLEMENT_MATRIX) or ((self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix.matrixType) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.obligations) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_7_CreditEventsPhysicalSettlementMatrix(self):
    """
    The below set of credit events are specified as optional boolean in FpML and the CDM because they would be specified as part of the Physical Settlement Matrix when such document governs the contract terms. As a result, this data rule specifies that those provisions can only be omitted if the Physical Settlement Matrix governs the terms of the contract. This data rule also applies to cash settled contracts because those could still end-up being physically settled, in the case where an auction could not take place because of, say, liquidity considerations.
    """
    def _then_fn0():
      return ((((((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.bankruptcy) is not None) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.obligationDefault) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.obligationAcceleration) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.repudiationMoratorium) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.governmentalIntervention) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((any_elements(self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix.matrixType, "<>", MatrixTypeEnum.CREDIT_DERIVATIVES_PHYSICAL_SETTLEMENT_MATRIX) or ((self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix.matrixType) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_8_RestructuringPhysicalSettlementMatrix(self):
    """
    The below multiple holder obligation restructuring provisions is specified as optional boolean in FpML and the CDM because they would be specified as part of the Physical Settlement Matrix when such document governs the contract terms. As a result, this data rule specifies that this provision can only be omitted if the Physical Settlement Matrix governs the terms of the contract. This data rule also applies to cash settled contracts because those could still end-up being physically settled, in the case where an auction could not take place because of, say, liquidity considerations.
    """
    def _then_fn0():
      return ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.restructuring.multipleHolderObligation) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((any_elements(self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix.matrixType, "<>", MatrixTypeEnum.CREDIT_DERIVATIVES_PHYSICAL_SETTLEMENT_MATRIX) or ((self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix.matrixType) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.restructuring) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_9_AdditionalFixedPaymentsMortgages(self):
    """
    The below set of additional fixed payment provisions are specified as optional boolean in FpML and the CDM because they only apply to mortgage credit default swaps. As a result, this data rule specifies that those provisions are required if the contract corresponds to a mortgage credit default swap. The provision related to the existence of the Contractual Term Supplement is meant to address the case where the underlier is a mortgage index.
    """
    def _then_fn0():
      return ((((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.floatingAmountEvents.additionalFixedPayments.interestShortfallReimbursement) is not None) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.floatingAmountEvents.additionalFixedPayments.principalShortfallReimbursement) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.floatingAmountEvents.additionalFixedPayments.writedownReimbursement) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((all_elements(self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation.referenceObligation.security.securityType, "=", SecurityTypeEnum.DEBT) and all_elements(self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation.referenceObligation.security.debtType.debtClass, "=", DebtClassEnum.ASSET_BACKED)) or contains(self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualTermsSupplement.contractualTermsSupplementType, ContractualSupplementTypeEnum.CD_SON_MBS)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.floatingAmountEvents) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_10_FloatingAmountEventsMortgages(self):
    """
    The below set of floating amount events provisions are specified as optional boolean in FpML and the CDM because they only apply to mortgage credit default swaps. As a result, this data rule specifies that those provisions are required if the contract corresponds to a mortgage credit default swap. The provision related to the existence of the Contractual Term Supplement is meant to address the case where the underlier is a mortgage index.
    """
    def _then_fn0():
      return ((((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.floatingAmountEvents.failureToPayPrincipal) is not None) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.floatingAmountEvents.writedown) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.floatingAmountEvents.impliedWritedown) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((all_elements(self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation.referenceObligation.security.securityType, "=", SecurityTypeEnum.DEBT) and all_elements(self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation.referenceObligation.security.debtType.debtClass, "=", DebtClassEnum.ASSET_BACKED)) or contains(self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualTermsSupplement.contractualTermsSupplementType, ContractualSupplementTypeEnum.CD_SON_MBS)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.floatingAmountEvents) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_11_CreditEventsMortgages(self):
    """
    The below set of credit events provisions are specified as optional boolean in FpML and the CDM because they only apply to mortgage credit default swaps. As a result, this data rule specifies that those provisions are required if the contract corresponds to a mortgage credit default swap. The provision related to the existence of the Contractual Term Supplement is meant to address the case where the underlier is a mortgage index.
    """
    def _then_fn0():
      return (((((((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.failureToPayPrincipal) is not None) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.failureToPayInterest) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.distressedRatingsDowngrade) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.maturityExtension) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.writedown) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.impliedWritedown) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((all_elements(self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation.referenceObligation.security.securityType, "=", SecurityTypeEnum.DEBT) and all_elements(self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation.referenceObligation.security.debtType.debtClass, "=", DebtClassEnum.ASSET_BACKED)) or contains(self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualTermsSupplement.contractualTermsSupplementType, ContractualSupplementTypeEnum.CD_SON_MBS)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_12_HedgingParty(self):
    """
    FpML specifies that there cannot be more than 2 hedging parties.
    """
    def _then_fn0():
      return all_elements(len(FilterPartyRole(self.partyRole, PartyRoleEnum.HEDGING_PARTY)), "<=", 2)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(contains(self.partyRole.role, PartyRoleEnum.HEDGING_PARTY), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_13_DeterminingParty(self):
    """
    FpML specifies that there cannot be more than 2 determining parties.
    """
    def _then_fn0():
      return all_elements(len(FilterPartyRole(self.partyRole, PartyRoleEnum.DETERMINING_PARTY)), "<=", 2)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(contains(self.partyRole.role, PartyRoleEnum.DETERMINING_PARTY), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_14_BarrierDerterminationAgent(self):
    """
    FpML specifies that there cannot be more than 1 barrier determination agent.
    """
    def _then_fn0():
      return all_elements(len(FilterPartyRole(self.partyRole, PartyRoleEnum.BARRIER_DETERMINATION_AGENT)), "<=", 1)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(contains(self.partyRole.role, PartyRoleEnum.BARRIER_DETERMINATION_AGENT), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_15_ClearedDate(self):
    """
    If the cleared date exists, it needs to be on or after the trade date.
    """
    def _then_fn0():
      return all_elements(self.clearedDate, ">=", self.tradeDate)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.clearedDate) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_16_FpML_cd_1(self):
    """
    FpML validation rule cd-1 - If referenceInformation exists, tradeDate must be before effectiveDate/unadjustedDate.
    """
    def _then_fn0():
      return (all_elements(self.tradeDate, "<", self.tradableProduct.product.contractualProduct.economicTerms.effectiveDate.adjustableDate.unadjustedDate) or all_elements(self.tradeDate, "<", self.tradableProduct.product.contractualProduct.economicTerms.effectiveDate.adjustableDate.adjustedDate))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_17_FpML_cd_7(self):
    """
    FpML validation rule cd-7 - If condition LongForm is true, then effectiveDate/dateAdjustments exists.
    """
    def _then_fn0():
      return (((self.tradableProduct.product.contractualProduct.economicTerms.payout.interestRatePayout.calculationPeriodDates.effectiveDate.adjustableDate.dateAdjustments) is not None) or all_elements(self.tradeDate, "<", self.tradableProduct.product.contractualProduct.economicTerms.effectiveDate.adjustableDate.adjustedDate))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((((self.contractDetails.documentation.legalAgreementIdentification.agreementName.masterConfirmationType) is None) and ((self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_18_FpML_cd_8(self):
    """
    FpML validation rule cd-8 - If condition LongForm is true, and if scheduledTerminationDate exists then scheduledTerminationDate/dateAdjustments exists.
    """
    def _then_fn0():
      return ((self.tradableProduct.product.contractualProduct.economicTerms.terminationDate.adjustableDate.dateAdjustments) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((((self.contractDetails.documentation.legalAgreementIdentification.agreementName.masterConfirmationType) is None) and ((self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_19_FpML_cd_11(self):
    """
    FpML validation rule cd-11 - If condition LongForm is true, and if condition ISDA2003 is true, then allGuarantees must exist.
    """
    def _then_fn0():
      return ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation.allGuarantees) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((((self.contractDetails.documentation.legalAgreementIdentification.agreementName.masterConfirmationType) is None) and ((self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation) is not None)) and all_elements(self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualDefinitionsType, "=", ContractualDefinitionsEnum.ISDA_2003_CREDIT)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_20_FpML_cd_19(self):
    """
    FpML validation rule cd-19 - If the condition ISDA1999Credit is true, then the following elements must not exist: protectionTerms/creditEvents/creditEventNotice/businessCenter, protectionTerms/creditEvents/restructuring/multipleHolderObligation, protectionTerms/creditEvents/restructuring/multipleCreditEventNotices, generalTerms/referenceInformation/allGuarantees, generalTerms/indexReferenceInformation, generalTerms/substitution, generalTerms/modifiedEquityDelivery.
    """
    def _then_fn0():
      return ((((((((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.creditEventNotice.businessCenter) is None) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.restructuring.multipleHolderObligation) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.restructuring.multipleCreditEventNotices) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation.allGuarantees) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.indexReferenceInformation) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.substitution) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.modifiedEquityDelivery) is None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualDefinitionsType, "=", ContractualDefinitionsEnum.ISDA_1999_CREDIT), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_21_FpML_cd_20(self):
    """
    FpML validation rule cd-20 - If the condition ISDA2003 is true, then protectionTerms/obligations/notContingent must not exist.
    """
    def _then_fn0():
      return ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.obligations.notContingent) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualDefinitionsType, "=", ContractualDefinitionsEnum.ISDA_2003_CREDIT), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_22_FpML_cd_23(self):
    """
    FpML validation rule cd-23 - If the condition LongForm is true, then cashSettlementTerms or physicalSettlementTerms must exist.
    """
    def _then_fn0():
      return (((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.cashSettlementTerms) is not None) or ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((((self.contractDetails.documentation.legalAgreementIdentification.agreementName.masterConfirmationType) is None) and ((self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_23_FpML_cd_24(self):
    """
    FpML validation rule cd-24 - If the condition LongForm is true, then the following elements must exist: protectionTerms/creditEvents/creditEventNotice, protectionTerms/obligations, generalTerms/referenceInformation/referencePrice.
    """
    def _then_fn0():
      return ((((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.creditEvents.creditEventNotice) is not None) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.protectionTerms.obligations) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation.referencePrice) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((((self.contractDetails.documentation.legalAgreementIdentification.agreementName.masterConfirmationType) is None) and ((self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_24_FpML_cd_25(self):
    """
    FpML validation rule cd-25 - If the condition LongForm is true, and if physicalSettlementTerms exists, then physicalSettlementTerms must contain settlementCurrency, physicalSettlementPeriod, escrow and deliverableObligations/accruedInterest.
    """
    def _then_fn0():
      return (((((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.settlementCurrency) is not None) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.physicalSettlementPeriod) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.escrow) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms.deliverableObligations.accruedInterest) is not None))
    
    def _else_fn0():
      return True
    
    return if_cond_fn((((((self.contractDetails.documentation.legalAgreementIdentification.agreementName.masterConfirmationType) is None) and ((self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.settlementTerms.physicalSettlementTerms) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_25_FpML_cd_32(self):
    """
    FpML validation rule cd-32 - If condition LongForm is true, and if fixedAmountCalculation/calculationAmount exists, then fixedAmountCalculation/dayCountFraction must exist.
    """
    def _then_fn0():
      return ((self.tradableProduct.product.contractualProduct.economicTerms.payout.interestRatePayout.dayCountFraction) is not None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((((((self.contractDetails.documentation.legalAgreementIdentification.agreementName.masterConfirmationType) is None) and ((self.contractDetails.documentation.legalAgreementIdentification.agreementName.contractualMatrix) is None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.creditDefaultPayout.generalTerms.referenceInformation) is not None)) and ((self.tradableProduct.product.contractualProduct.economicTerms.payout.interestRatePayout.priceQuantity) is not None)) and ((self.tradableProduct.tradeLot.priceQuantity.quantity.value) is not None)), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_26_FpML_ird_8(self):
    """
    FpML validation rule ird-8 - If the same party is specified as the payer and receiver, then different accounts must be specified.
    """
    def _then_fn0():
      return all_elements(FpmlIrd8(self.tradableProduct, self.account), "=", False)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.tradableProduct.product.contractualProduct.economicTerms.payout.interestRatePayout) is not None), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.Account import Account
from cdm.legaldocumentation.csa.Collateral import Collateral
from cdm.event.common.ContractDetails import ContractDetails
from cdm.event.common.ExecutionDetails import ExecutionDetails
from cdm.base.staticdata.party.Party import Party
from cdm.base.staticdata.party.PartyRole import PartyRole
from cdm.product.template.TradableProduct import TradableProduct
from cdm.base.staticdata.identifier.Identifier import Identifier
from cdm.base.staticdata.party.PartyRoleEnum import PartyRoleEnum
from cdm.legaldocumentation.common.MatrixTypeEnum import MatrixTypeEnum
from cdm.base.staticdata.asset.common.SecurityTypeEnum import SecurityTypeEnum
from cdm.base.staticdata.asset.common.DebtClassEnum import DebtClassEnum
from cdm.legaldocumentation.common.ContractualSupplementTypeEnum import ContractualSupplementTypeEnum
from cdm.base.staticdata.party.functions.FilterPartyRole import FilterPartyRole
from cdm.legaldocumentation.common.ContractualDefinitionsEnum import ContractualDefinitionsEnum
from cdm.product.template.functions.FpmlIrd8 import FpmlIrd8

Trade.update_forward_refs()
