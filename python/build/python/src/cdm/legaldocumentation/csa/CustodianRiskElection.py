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

__all__ = ['CustodianRiskElection']


class CustodianRiskElection(BaseDataClass):
  """
  A class to specify the Custodian Risk (English Law and New York Law ISDA CSA) and the Collateral Manager Risk (Japanese Law ISDA CSA) election. | ISDA 2016 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (n)(ii): Custodian (IM) Risk. | ISDA 2018 English Law Credit Support Deed for Initial Margin, paragraph 13, General Principles, (n)(ii): Custodian (IM) Risk. | ISDA 2016 Japanese Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (m)(i): Collateral Manager Risk. | ISDA 2016 New York Law Credit Support Annex for Initial Margin, paragraph 13, General Principles, (n)(ii): Custodian (IM) Risk.
  """
  isSpecified: bool = Field(..., description="The qualification as to whether the risk is deemed as Specified.")
  """
  The qualification as to whether the risk is deemed as Specified.
  """
  party: Optional[CounterpartyRoleEnum] = Field(None, description="The elective party.")
  """
  The elective party.
  """
  qualification: Optional[str] = Field(None, description="The Custodian Risk (English Law and New York Law ISDA CSA) or Collateral Manager Risk (Japanese Law ISDA CSA) qualification. This attribute is optional because the Custodian Risk provision can be deemed as 'Specified', although not be qualified through this attribute.")
  """
  The Custodian Risk (English Law and New York Law ISDA CSA) or Collateral Manager Risk (Japanese Law ISDA CSA) qualification. This attribute is optional because the Custodian Risk provision can be deemed as 'Specified', although not be qualified through this attribute.
  """
  
  @rosetta_condition
  def condition_0_Specified(self):
    """
    The Custodian Risk (English Law and New York Law ISDA CSA) or Collateral Manager Risk (Japanese Law ISDA CSA) should only be qualified if that risk is deemed 'specified'.
    """
    def _then_fn0():
      return ((self.qualification) is None)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.isSpecified, "=", False), _then_fn0, _else_fn0)

from cdm.base.staticdata.party.CounterpartyRoleEnum import CounterpartyRoleEnum

CustodianRiskElection.update_forward_refs()
