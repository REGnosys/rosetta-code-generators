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

__all__ = ['SubstitutedRegime']


class SubstitutedRegime(BaseDataClass):
  """
  A class to specify each party's election with respect to the Substituted Regimes that will be applicable...
  """
  additionalRegime: Optional[str] = Field(None, description="The additional regulatory regime as specified by the parties.")
  """
  The additional regulatory regime as specified by the parties.
  """
  regime: Optional[RegulatoryRegimeEnum] = Field(None, description="The applicable regulatory regime, as specified through an enumeration.")
  """
  The applicable regulatory regime, as specified through an enumeration.
  """
  regimeTerms: List[SubstitutedRegimeTerms] = Field([], description="Specifies the applicability of the Substituted Regime as denoted in the Substituted Regime Table as part of certain legal agreements, such as such as the ISDA 2016 and 2018 CSA for Initial Margin.")
  """
  Specifies the applicability of the Substituted Regime as denoted in the Substituted Regime Table as part of certain legal agreements, such as such as the ISDA 2016 and 2018 CSA for Initial Margin.
  """
  @rosetta_condition
  def cardinality_regimeTerms(self):
    return check_cardinality(self.regimeTerms, 2, 2)
  
  
  @rosetta_condition
  def condition_0_SubstitutedRegimeChoice(self):
    """
    The applicable regime should be specified either as an enumeration or as an additional regime specified by the parties.
    """
    return self.check_one_of_constraint('regime', 'additionalRegime', necessity=True)

from cdm.legaldocumentation.csa.RegulatoryRegimeEnum import RegulatoryRegimeEnum
from cdm.legaldocumentation.csa.SubstitutedRegimeTerms import SubstitutedRegimeTerms

SubstitutedRegime.update_forward_refs()
