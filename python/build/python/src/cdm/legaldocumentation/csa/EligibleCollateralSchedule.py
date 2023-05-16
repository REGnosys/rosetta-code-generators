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

__all__ = ['EligibleCollateralSchedule']


class EligibleCollateralSchedule(BaseDataClass):
  """
  Represents a set of criteria used to specify an eligible collateral schedule.
  """
  criteria: List[EligibleCollateralCriteria] = Field([], description="Represents a set of criteria used to specify eligible collateral.")
  """
  Represents a set of criteria used to specify eligible collateral.
  """
  @rosetta_condition
  def cardinality_criteria(self):
    return check_cardinality(self.criteria, 1, None)
  
  scheduleIdentifier: List[Identifier] = Field([], description="Specifies the identifier(s) to uniquely identify an eligible collateral schedule for an identity issuer.")
  """
  Specifies the identifier(s) to uniquely identify an eligible collateral schedule for an identity issuer.
  """

from cdm.legaldocumentation.csa.EligibleCollateralCriteria import EligibleCollateralCriteria
from cdm.base.staticdata.identifier.Identifier import Identifier

EligibleCollateralSchedule.update_forward_refs()
