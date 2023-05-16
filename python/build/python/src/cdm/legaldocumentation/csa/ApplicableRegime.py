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

__all__ = ['ApplicableRegime']


class ApplicableRegime(BaseDataClass):
  """
  A class to specify the applicable regulatory regime(s) that parties to a legal agreement, such as the ISDA 2016 and 2018 CSA for Initial Margin, might be subject to.
  """
  additionalRegime: Optional[str] = Field(None, description="The additional regulatory regime as specified by the parties.")
  """
  The additional regulatory regime as specified by the parties.
  """
  additionalTerms: Optional[str] = Field(None, description="The bespoke Additional Type for the purposes of Covered Transactions (IM).")
  """
  The bespoke Additional Type for the purposes of Covered Transactions (IM).
  """
  additionalType: Optional[AdditionalTypeEnum] = Field(None, description="The Additional Type of transaction that can require the collection or delivery of initial margin under the specified regulatory regime for the purposes of Covered Transactions, as specified in ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (b)(B).")
  """
  The Additional Type of transaction that can require the collection or delivery of initial margin under the specified regulatory regime for the purposes of Covered Transactions, as specified in ISDA 2016 Credit Support Annex for Initial Margin, paragraph 13, General Principles, (b)(B).
  """
  regime: Optional[RegulatoryRegimeEnum] = Field(None, description="The applicable regulatory regime, as specified through an enumeration.")
  """
  The applicable regulatory regime, as specified through an enumeration.
  """
  regimeTerms: List[RegimeTerms] = Field([], description="A class that is used by the ApplicableRegime and the AdditionalRegime classes to specify the terms that are specific to each party and regime which are referred to in the Regime Table as part of certain legal agreements, such as such as the ISDA 2016 and 2018 CSA for Initial Margin.")
  """
  A class that is used by the ApplicableRegime and the AdditionalRegime classes to specify the terms that are specific to each party and regime which are referred to in the Regime Table as part of certain legal agreements, such as such as the ISDA 2016 and 2018 CSA for Initial Margin.
  """
  @rosetta_condition
  def cardinality_regimeTerms(self):
    return check_cardinality(self.regimeTerms, 2, 2)
  
  
  @rosetta_condition
  def condition_0_ApplicableRegimeChoice(self):
    """
    The applicable regime should be specified either as an enumeration or as an additional regime specified by the parties.
    """
    return self.check_one_of_constraint('regime', 'additionalRegime', necessity=True)

from cdm.legaldocumentation.csa.AdditionalTypeEnum import AdditionalTypeEnum
from cdm.legaldocumentation.csa.RegulatoryRegimeEnum import RegulatoryRegimeEnum
from cdm.legaldocumentation.csa.RegimeTerms import RegimeTerms

ApplicableRegime.update_forward_refs()
