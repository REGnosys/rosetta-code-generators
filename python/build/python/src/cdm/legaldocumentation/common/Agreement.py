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

__all__ = ['Agreement']


class Agreement(BaseDataClass):
  """
  Specification of the standard set of terms that define a legal agreement.
  """
  collateralTransferAgreementElections: Optional[CollateralTransferAgreementElections] = Field(None, description="Elections to specify a Collateral Transfer Agreement.")
  """
  Elections to specify a Collateral Transfer Agreement.
  """
  creditSupportAgreementElections: Optional[CreditSupportAgreementElections] = Field(None, description="Elections to specify a Credit Support Annex or Credit Support Deed for Intial or Variation Margin.")
  """
  Elections to specify a Credit Support Annex or Credit Support Deed for Intial or Variation Margin.
  """
  masterAgreementSchedule: Optional[MasterAgreementSchedule] = Field(None, description="Elections to specify a Master Agreement Schedule.")
  """
  Elections to specify a Master Agreement Schedule.
  """
  securityAgreementElections: Optional[SecurityAgreementElections] = Field(None, description="Elections to specify a Security agreement.")
  """
  Elections to specify a Security agreement.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('creditSupportAgreementElections', 'collateralTransferAgreementElections', 'securityAgreementElections', 'masterAgreementSchedule', necessity=True)

from cdm.legaldocumentation.csa.CollateralTransferAgreementElections import CollateralTransferAgreementElections
from cdm.legaldocumentation.csa.CreditSupportAgreementElections import CreditSupportAgreementElections
from cdm.legaldocumentation.master.MasterAgreementSchedule import MasterAgreementSchedule
from cdm.legaldocumentation.csa.SecurityAgreementElections import SecurityAgreementElections

Agreement.update_forward_refs()
