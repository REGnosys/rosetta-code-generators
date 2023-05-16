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

__all__ = ['CalculationDateLocationElection']


class CalculationDateLocationElection(BaseDataClass):
  """
  A class to specify each of the party elections with respect to the Calculation Date Location. ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (d)(i): Calculation Date Location. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (e)(i): Calculation Date Location. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (d)(i): Calculation Date Location.
  """
  businessCenter: Optional[AttributeWithMeta[BusinessCenterEnum] | BusinessCenterEnum] = Field(None, description="The Calculation Date Location when specified as a business center which corresponds to the FpML list of business centers or can be mapped to it.")
  """
  The Calculation Date Location when specified as a business center which corresponds to the FpML list of business centers or can be mapped to it.
  """
  customLocation: Optional[str] = Field(None, description="The Calculation Date Location when specified a location which doesn't correspond to the FpML list of business centers or cannot be mapped to it.")
  """
  The Calculation Date Location when specified a location which doesn't correspond to the FpML list of business centers or cannot be mapped to it.
  """
  party: CounterpartyRoleEnum = Field(..., description="The elective party.")
  """
  The elective party.
  """
  
  @rosetta_condition
  def condition_0_Choice(self):
    """
    The Calculation Date Location is specified either as a standard business center or as a custom location.
    """
    return self.check_one_of_constraint('businessCenter', 'customLocation', necessity=True)

from cdm.base.datetime.BusinessCenterEnum import BusinessCenterEnum
from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

CalculationDateLocationElection.update_forward_refs()
