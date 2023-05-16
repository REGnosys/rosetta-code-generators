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

__all__ = ['SecurityAgreementElections']


class SecurityAgreementElections(BaseDataClass):
  """
  The set of elections which specify a Security Agremeent
  """
  additionalAmendments: Optional[str] = Field(None, description="Any additional amendments that might be specified by the parties to the agreement.")
  """
  Any additional amendments that might be specified by the parties to the agreement.
  """
  additionalBespokeTerms: Optional[str] = Field(None, description="Any additional terms that might be specified applicable.")
  """
  Any additional terms that might be specified applicable.
  """
  appropriatedCollateralValuation: Optional[AppropriatedCollateralValuation] = Field(None, description="The election for the Valuation of Appropriate Collateral.")
  """
  The election for the Valuation of Appropriate Collateral.
  """
  deliveryInLieuRight: Optional[bool] = Field(None, description="Delivery In Lieu rights")
  """
  Delivery In Lieu rights
  """
  enforcementEvent: Optional[EnforcementEvent] = Field(None, description="Enforcement Events specific to the agreement")
  """
  Enforcement Events specific to the agreement
  """
  executionTerms: Optional[ExecutionTerms] = Field(None, description="The location and language of execution to determine duty to be paid.")
  """
  The location and language of execution to determine duty to be paid.
  """
  fullDischarge: Optional[bool] = Field(None, description="Full Discharge condition")
  """
  Full Discharge condition
  """
  jurisdictionRelatedTerms: Optional[JurisdictionRelatedTerms] = Field(None, description="The jurisdiction specific terms")
  """
  The jurisdiction specific terms
  """
  pledgedAccount: Optional[Account] = Field(None, description="The pledged account associated with the agreement")
  """
  The pledged account associated with the agreement
  """
  processAgent: Optional[ProcessAgent] = Field(None, description="The Process Agent that might be appointed by the parties to the agreement.")
  """
  The Process Agent that might be appointed by the parties to the agreement.
  """

from cdm.legaldocumentation.csa.AppropriatedCollateralValuation import AppropriatedCollateralValuation
from cdm.legaldocumentation.csa.EnforcementEvent import EnforcementEvent
from cdm.legaldocumentation.csa.ExecutionTerms import ExecutionTerms
from cdm.legaldocumentation.csa.JurisdictionRelatedTerms import JurisdictionRelatedTerms
from cdm.base.staticdata.party.Account import Account
from cdm.legaldocumentation.csa.ProcessAgent import ProcessAgent

SecurityAgreementElections.update_forward_refs()
