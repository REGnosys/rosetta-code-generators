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

__all__ = ['CollateralTransferAgreementElections']


class CollateralTransferAgreementElections(BaseDataClass):
  """
  The set of elections which specify a Collateral Transfer Agreement
  """
  additionalAmendments: Optional[str] = Field(None, description="Any additional amendments that might be specified by the parties to the agreement.")
  """
  Any additional amendments that might be specified by the parties to the agreement.
  """
  additionalBespokeTerms: Optional[str] = Field(None, description="Any additional terms that might be specified applicable.")
  """
  Any additional terms that might be specified applicable.
  """
  additionalRepresentations: AdditionalRepresentations = Field(..., description="The specification Additional Representations that may be applicable to the agreement.")
  """
  The specification Additional Representations that may be applicable to the agreement.
  """
  addressesForTransfer: Optional[ContactElection] = Field(None, description="The optional specification of address for transfer as specified by the respective parties to the agreement.")
  """
  The optional specification of address for transfer as specified by the respective parties to the agreement.
  """
  baseAndEligibleCurrency: BaseAndEligibleCurrency = Field(..., description="The base and eligible currency(ies) for the document as specified by the parties to the agreement.")
  """
  The base and eligible currency(ies) for the document as specified by the parties to the agreement.
  """
  calculationAndTiming: CalculationAndTiming = Field(..., description="The set of elections for determining Valuation and Timing terms specific to the agreement")
  """
  The set of elections for determining Valuation and Timing terms specific to the agreement
  """
  conditionsPrecedent: ConditionsPrecedent = Field(..., description="The set of elections that may overwrite the default Condition Precedent provision, and the set of provisions that are deemed Access Condition.")
  """
  The set of elections that may overwrite the default Condition Precedent provision, and the set of provisions that are deemed Access Condition.
  """
  creditSupportObligations: CreditSupportObligations = Field(..., description="The Credit Support Obligations applicable to the agreement. ")
  """
  The Credit Support Obligations applicable to the agreement. 
  """
  custodyArrangements: CustodyArrangements = Field(..., description="The Custodian and Segregated Account details in respect of each party to the agreement.")
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
  fxHaircutCurrency: Optional[FxHaircutCurrency] = Field(None, description="The reference currency for the purpose of specifying the FX Haircut relating to a posting obligation, as being either the Termination Currency or an FX Designated Currency.")
  """
  The reference currency for the purpose of specifying the FX Haircut relating to a posting obligation, as being either the Termination Currency or an FX Designated Currency.
  """
  generalSimmElections: GeneralSimmElections = Field(..., description="The specification of the ISDA SIMM Method for all Covered Transactions with respect to all Regimes.")
  """
  The specification of the ISDA SIMM Method for all Covered Transactions with respect to all Regimes.
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
  minimumTransferAmountAmendment: Optional[MinimumTransferAmountAmendment] = Field(None, description="The bespoke provision that might be specified by the parties to the agreement applicable to Minimum Transfer Amount.  Unless specified the definition of Minimum Transfer Amount in any Other Regulatory CSA has the meaning specified in such Other Regulatory CSA.")
  """
  The bespoke provision that might be specified by the parties to the agreement applicable to Minimum Transfer Amount.  Unless specified the definition of Minimum Transfer Amount in any Other Regulatory CSA has the meaning specified in such Other Regulatory CSA.
  """
  oneWayProvisions: OneWayProvisions = Field(..., description="The determination of whether the One Way Provisions are applicable (true) or not applicable (false).")
  """
  The determination of whether the One Way Provisions are applicable (true) or not applicable (false).
  """
  otherCsa: Optional[str] = Field(None, description="The bespoke definition of Other CSA as specified by the parties to the agreement.")
  """
  The bespoke definition of Other CSA as specified by the parties to the agreement.
  """
  pledgeeRepresentativeRider: Optional[PledgeeRepresentativeRider] = Field(None, description="The terms of the Rider for the ISDA Euroclear 2019 Collateral Transfer Agreement with respect to the use of a Pledgee Representative attached to this Agreement.")
  """
  The terms of the Rider for the ISDA Euroclear 2019 Collateral Transfer Agreement with respect to the use of a Pledgee Representative attached to this Agreement.
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
  rightsEvents: Optional[RightsEvents] = Field(None, description="The bespoke provisions that might be specified by the parties to the agreement to specify the rights of Security Taker and/or Security Provider when an Early Termination or Access Condition event has occurred..")
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
  @rosetta_condition
  def cardinality_substitutedRegime(self):
    return check_cardinality(self.substitutedRegime, 1, None)
  
  substitution: Optional[Substitution] = Field(None, description="The conditions under which the Security Provider can substitute posted collateral.")
  """
  The conditions under which the Security Provider can substitute posted collateral.
  """
  terminationCurrencyAmendment: TerminationCurrencyAmendment = Field(..., description="The bespoke provision that might be specified by the parties to the agreement applicable to Termination Currency.  Unless specified the definition of Termination Currency has the meaning specified in the Schedule to the ISDA Master Agreement.")
  """
  The bespoke provision that might be specified by the parties to the agreement applicable to Termination Currency.  Unless specified the definition of Termination Currency has the meaning specified in the Schedule to the ISDA Master Agreement.
  """

from cdm.legaldocumentation.csa.AdditionalRepresentations import AdditionalRepresentations
from cdm.legaldocumentation.csa.ContactElection import ContactElection
from cdm.legaldocumentation.csa.BaseAndEligibleCurrency import BaseAndEligibleCurrency
from cdm.legaldocumentation.csa.CalculationAndTiming import CalculationAndTiming
from cdm.legaldocumentation.csa.ConditionsPrecedent import ConditionsPrecedent
from cdm.legaldocumentation.csa.CreditSupportObligations import CreditSupportObligations
from cdm.legaldocumentation.csa.CustodyArrangements import CustodyArrangements
from cdm.legaldocumentation.csa.DisputeResolution import DisputeResolution
from cdm.legaldocumentation.csa.FxHaircutCurrency import FxHaircutCurrency
from cdm.legaldocumentation.csa.GeneralSimmElections import GeneralSimmElections
from cdm.legaldocumentation.csa.JurisdictionRelatedTerms import JurisdictionRelatedTerms
from cdm.legaldocumentation.csa.MinimumTransferAmountAmendment import MinimumTransferAmountAmendment
from cdm.legaldocumentation.csa.OneWayProvisions import OneWayProvisions
from cdm.legaldocumentation.csa.PledgeeRepresentativeRider import PledgeeRepresentativeRider
from cdm.legaldocumentation.csa.PostingObligations import PostingObligations
from cdm.legaldocumentation.csa.ProcessAgent import ProcessAgent
from cdm.legaldocumentation.csa.Regime import Regime
from cdm.legaldocumentation.csa.RightsEvents import RightsEvents
from cdm.legaldocumentation.csa.SensitivityMethodologies import SensitivityMethodologies
from cdm.legaldocumentation.csa.SubstitutedRegime import SubstitutedRegime
from cdm.legaldocumentation.csa.Substitution import Substitution
from cdm.legaldocumentation.csa.TerminationCurrencyAmendment import TerminationCurrencyAmendment

CollateralTransferAgreementElections.update_forward_refs()
