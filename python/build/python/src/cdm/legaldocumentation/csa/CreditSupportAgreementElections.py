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

__all__ = ['CreditSupportAgreementElections']


class CreditSupportAgreementElections(BaseDataClass):
  """
  The set of elections which specify a Credit Support Annex or Deed.
  """
  additionalAmendments: Optional[str] = Field(None, description="Any additional amendments that might be specified by the parties to the agreement.")
  """
  Any additional amendments that might be specified by the parties to the agreement.
  """
  additionalBespokeTerms: Optional[str] = Field(None, description="Any additional terms that might be specified applicable.")
  """
  Any additional terms that might be specified applicable.
  """
  additionalObligations: Optional[str] = Field(None, description="The additional obligations that might be specified by the parties to a Credit Support Agreement.")
  """
  The additional obligations that might be specified by the parties to a Credit Support Agreement.
  """
  additionalRepresentations: AdditionalRepresentations = Field(..., description="The specification Additional Representations that may be applicable to the agreement.")
  """
  The specification Additional Representations that may be applicable to the agreement.
  """
  addressesForTransfer: Optional[ContactElection] = Field(None, description="The optional specification of address for transfer as specified by the respective parties to the agreement.")
  """
  The optional specification of address for transfer as specified by the respective parties to the agreement.
  """
  appropriatedCollateralValuation: Optional[AppropriatedCollateralValuation] = Field(None, description="The election for the Valuation of Appropriate Collateral.")
  """
  The election for the Valuation of Appropriate Collateral.
  """
  baseAndEligibleCurrency: BaseAndEligibleCurrency = Field(..., description="The base and eligible currency(ies) for the document as specified by the parties to the agreement.")
  """
  The base and eligible currency(ies) for the document as specified by the parties to the agreement.
  """
  calculationAndTiming: CalculationAndTiming = Field(..., description="The set of elections for determining Valuation and Timing terms specific to the agreement")
  """
  The set of elections for determining Valuation and Timing terms specific to the agreement
  """
  conditionsPrecedent: Optional[ConditionsPrecedent] = Field(None, description="The set of elections that may overwrite the default Condition Precedent provision, and the set of provisions that are deemed Access Condition.")
  """
  The set of elections that may overwrite the default Condition Precedent provision, and the set of provisions that are deemed Access Condition.
  """
  coveredTransactions: CoveredTransactions = Field(..., description="The specification of transactions covered by the terms of the agreement.")
  """
  The specification of transactions covered by the terms of the agreement.
  """
  creditSupportObligations: CreditSupportObligations = Field(..., description="The Credit Support Obligations applicable to the agreement. ")
  """
  The Credit Support Obligations applicable to the agreement. 
  """
  creditSupportOffsets: bool = Field(..., description="The specification of whether the standard Credit Support Offset provisions are applicable (true) or not applicable (false).")
  """
  The specification of whether the standard Credit Support Offset provisions are applicable (true) or not applicable (false).
  """
  custodyArrangements: Optional[CustodyArrangements] = Field(None, description="The Custodian and Segregated Account details in respect of each party to the agreement.")
  """
  The Custodian and Segregated Account details in respect of each party to the agreement.
  """
  demandsAndNotices: Optional[ContactElection] = Field(None, description="The optional specification of address where the demands, specifications and notices will be communicated to for each of the parties to the agreement.")
  """
  The optional specification of address where the demands, specifications and notices will be communicated to for each of the parties to the agreement.
  """
  disputeResolution: DisputeResolution = Field(..., description="The election terms under which a party disputes (i) the Calculation Agent’s calculation of a Delivery Amount or a Return Amount, or (ii) the Value of any Transfer of Eligible Credit Support or Posted Credit Support.")
  """
  The election terms under which a party disputes (i) the Calculation Agent’s calculation of a Delivery Amount or a Return Amount, or (ii) the Value of any Transfer of Eligible Credit Support or Posted Credit Support.
  """
  distributionAndInterestPayment: Optional[DistributionAndInterestPayment] = Field(None, description="The Distributions and Interest Payment terms specified as part of the agreement.")
  """
  The Distributions and Interest Payment terms specified as part of the agreement.
  """
  exchangeDate: Optional[str] = Field(None, description="The bespoke exchange date terms that might be specified by the parties to the agreement.")
  """
  The bespoke exchange date terms that might be specified by the parties to the agreement.
  """
  fxHaircutCurrency: Optional[FxHaircutCurrency] = Field(None, description="The reference currency for the purpose of specifying the FX Haircut relating to a posting obligation, as being either the Termination Currency or an FX Designated Currency.")
  """
  The reference currency for the purpose of specifying the FX Haircut relating to a posting obligation, as being either the Termination Currency or an FX Designated Currency.
  """
  generalSimmElections: Optional[GeneralSimmElections] = Field(None, description="The specification of the ISDA SIMM Method for all Covered Transactions with respect to all Regimes.")
  """
  The specification of the ISDA SIMM Method for all Covered Transactions with respect to all Regimes.
  """
  holdingAndUsingPostedCollateral: HoldingAndUsingPostedCollateral = Field(..., description="The elections for the holding and using of posted collateral by the respective parties to the Credit Support Annex for Variation Margin.")
  """
  The elections for the holding and using of posted collateral by the respective parties to the Credit Support Annex for Variation Margin.
  """
  identifiedCrossCurrencySwap: Optional[bool] = Field(None, description="The qualification of whether cross-currency swaps need to be identified in the Confirmation so that the obligations to exchange principal be disregarded for the purpose of determining the Delivery Amount or Return Amount.")
  """
  The qualification of whether cross-currency swaps need to be identified in the Confirmation so that the obligations to exchange principal be disregarded for the purpose of determining the Delivery Amount or Return Amount.
  """
  interpretationTerms: Optional[str] = Field(None, description="The bespoke provision that might be specified by the parties to the agreement applicable to Interpretations.")
  """
  The bespoke provision that might be specified by the parties to the agreement applicable to Interpretations.
  """
  jurisdictionRelatedTerms: Optional[JurisdictionRelatedTerms] = Field(None, description="The jurisdiction specific terms relevant to the agreement.")
  """
  The jurisdiction specific terms relevant to the agreement.
  """
  minimumTransferAmountAmendment: MinimumTransferAmountAmendment = Field(..., description="The bespoke provision that might be specified by the parties to the agreement applicable to Minimum Transfer Amount.  Unless specified the definition of Minimum Transfer Amount in any Other Regulatory CSA has the meaning specified in such Other Regulatory CSA.")
  """
  The bespoke provision that might be specified by the parties to the agreement applicable to Minimum Transfer Amount.  Unless specified the definition of Minimum Transfer Amount in any Other Regulatory CSA has the meaning specified in such Other Regulatory CSA.
  """
  oneWayProvisions: OneWayProvisions = Field(..., description="The determination of whether the One Way Provisions are applicable (true) or not applicable (false).")
  """
  The determination of whether the One Way Provisions are applicable (true) or not applicable (false).
  """
  otherAgreements: Optional[OtherAgreements] = Field(None, description="The bespoke definition of other agreement terms as specified by the parties to the agreement.")
  """
  The bespoke definition of other agreement terms as specified by the parties to the agreement.
  """
  otherEligibleAndPostedSupport: OtherEligibleAndPostedSupport = Field(..., description="The Other Eligible Support elections associated with margin agreements.")
  """
  The Other Eligible Support elections associated with margin agreements.
  """
  postingObligations: PostingObligations = Field(..., description="The security providers posting obligations.")
  """
  The security providers posting obligations.
  """
  processAgent: Optional[ProcessAgent] = Field(None, description="The Process Agent that might be appointed by the parties to the agreement.")
  """
  The Process Agent that might be appointed by the parties to the agreement.
  """
  regime: Regime = Field(..., description="The Regime Table provision , which determines the regulatory regime(s) applicable to each of the parties to the agreement.")
  """
  The Regime Table provision , which determines the regulatory regime(s) applicable to each of the parties to the agreement.
  """
  rightsEvents: RightsEvents = Field(..., description="The bespoke provisions that might be specified by the parties to the agreement to specify the rights of Security Taker and/or Security Provider when an Early Termination or Access Condition event has occurred..")
  """
  The bespoke provisions that might be specified by the parties to the agreement to specify the rights of Security Taker and/or Security Provider when an Early Termination or Access Condition event has occurred..
  """
  sensitivityMethodologies: SensitivityMethodologies = Field(..., description="The specification of methodologies to compute sensitivities specific to the agreement.")
  """
  The specification of methodologies to compute sensitivities specific to the agreement.
  """
  substitutedRegime: List[SubstitutedRegime] = Field([], description="The specification of Additional regimes for purposes of determining whether a Regulatory Event has occurred.")
  """
  The specification of Additional regimes for purposes of determining whether a Regulatory Event has occurred.
  """
  substitution: Substitution = Field(..., description="The conditions under which the Security Provider can substitute posted collateral.")
  """
  The conditions under which the Security Provider can substitute posted collateral.
  """
  terminationCurrencyAmendment: TerminationCurrencyAmendment = Field(..., description="The bespoke provision that might be specified by the parties to the agreement applicable to Termination Currency.  Unless specified the definition of Termination Currency has the meaning specified in the Schedule to the ISDA Master Agreement.")
  """
  The bespoke provision that might be specified by the parties to the agreement applicable to Termination Currency.  Unless specified the definition of Termination Currency has the meaning specified in the Schedule to the ISDA Master Agreement.
  """
  trustSchemeAddendum: bool = Field(..., description="The qualification of whether Trust Scheme Addendum is applicable (True) or not applicable (False).")
  """
  The qualification of whether Trust Scheme Addendum is applicable (True) or not applicable (False).
  """

from cdm.legaldocumentation.csa.AdditionalRepresentations import AdditionalRepresentations
from cdm.legaldocumentation.csa.ContactElection import ContactElection
from cdm.legaldocumentation.csa.AppropriatedCollateralValuation import AppropriatedCollateralValuation
from cdm.legaldocumentation.csa.BaseAndEligibleCurrency import BaseAndEligibleCurrency
from cdm.legaldocumentation.csa.CalculationAndTiming import CalculationAndTiming
from cdm.legaldocumentation.csa.ConditionsPrecedent import ConditionsPrecedent
from cdm.legaldocumentation.csa.CoveredTransactions import CoveredTransactions
from cdm.legaldocumentation.csa.CreditSupportObligations import CreditSupportObligations
from cdm.legaldocumentation.csa.CustodyArrangements import CustodyArrangements
from cdm.legaldocumentation.csa.DisputeResolution import DisputeResolution
from cdm.legaldocumentation.csa.DistributionAndInterestPayment import DistributionAndInterestPayment
from cdm.legaldocumentation.csa.FxHaircutCurrency import FxHaircutCurrency
from cdm.legaldocumentation.csa.GeneralSimmElections import GeneralSimmElections
from cdm.legaldocumentation.csa.HoldingAndUsingPostedCollateral import HoldingAndUsingPostedCollateral
from cdm.legaldocumentation.csa.JurisdictionRelatedTerms import JurisdictionRelatedTerms
from cdm.legaldocumentation.csa.MinimumTransferAmountAmendment import MinimumTransferAmountAmendment
from cdm.legaldocumentation.csa.OneWayProvisions import OneWayProvisions
from cdm.legaldocumentation.csa.OtherAgreements import OtherAgreements
from cdm.legaldocumentation.csa.OtherEligibleAndPostedSupport import OtherEligibleAndPostedSupport
from cdm.legaldocumentation.csa.PostingObligations import PostingObligations
from cdm.legaldocumentation.csa.ProcessAgent import ProcessAgent
from cdm.legaldocumentation.csa.Regime import Regime
from cdm.legaldocumentation.csa.RightsEvents import RightsEvents
from cdm.legaldocumentation.csa.SensitivityMethodologies import SensitivityMethodologies
from cdm.legaldocumentation.csa.SubstitutedRegime import SubstitutedRegime
from cdm.legaldocumentation.csa.Substitution import Substitution
from cdm.legaldocumentation.csa.TerminationCurrencyAmendment import TerminationCurrencyAmendment

CreditSupportAgreementElections.update_forward_refs()
