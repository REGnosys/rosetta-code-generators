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

__all__ = ['Regime']


class Regime(BaseDataClass):
  """
  A class to specify one or more regimes that may be specified as relevant to a legal agreement. 2016/2018 ISDA Credit Support Annex for Initial Margin: Regime.
  """
  applicableRegime: List[ApplicableRegime] = Field([], description="A class to specify the regime(s) that parties to a legal agreement, such as the ISDA 2016 and 2018 CSA for Initial Margin, might agree to apply to one or both parties when acting as collateral taker, and specific terms associated with that application.")
  """
  A class to specify the regime(s) that parties to a legal agreement, such as the ISDA 2016 and 2018 CSA for Initial Margin, might agree to apply to one or both parties when acting as collateral taker, and specific terms associated with that application.
  """
  @rosetta_condition
  def cardinality_applicableRegime(self):
    return check_cardinality(self.applicableRegime, 1, None)
  
  fallbackToMandatoryMethodDays: Optional[Decimal] = Field(None, description="The specification of the number of days after effective delivery of notice that Mandatory method fallback applies. Specification is only required when one or more Regimes have Fall Back to Mandatory Method elected as a SIMM exception.")
  """
  The specification of the number of days after effective delivery of notice that Mandatory method fallback applies. Specification is only required when one or more Regimes have Fall Back to Mandatory Method elected as a SIMM exception.
  """

from cdm.legaldocumentation.csa.ApplicableRegime import ApplicableRegime

Regime.update_forward_refs()
