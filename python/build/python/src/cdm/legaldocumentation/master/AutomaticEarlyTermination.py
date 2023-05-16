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

__all__ = ['AutomaticEarlyTermination']


class AutomaticEarlyTermination(BaseDataClass):
  """
  A class to specify the Automatic Early Termination provision applicable to a Master Agreement.
  """
  fallbackAET: bool = Field(..., description="A boolean election to specify whether provided that, where a party is governed by a system of law which does not permit the termination of one or more Transactions to occur following an Event of Default specified in Section 5(a)(vii)(1), (3), (4), (5), (6) or, to extent analogous thereto, (8) ,then the Automatic Early Termination provisions of Section 6(a) shall apply to such party.")
  """
  A boolean election to specify whether provided that, where a party is governed by a system of law which does not permit the termination of one or more Transactions to occur following an Event of Default specified in Section 5(a)(vii)(1), (3), (4), (5), (6) or, to extent analogous thereto, (8) ,then the Automatic Early Termination provisions of Section 6(a) shall apply to such party.
  """
  indemnity: bool = Field(..., description="A boolean attribute to specify whether if an Early Termination Date occurs because Automatic Early Termination applies in respect of a party, the Defaulting Party shall indemnify the Non- defaulting Party, on demand, against any losses, costs, expenses or damages that the Non- defaulting Party incurs (to the extent not already taken into account in Section 6(e)) in relation to terminating, liquidating, establishing or re- establishing any hedge or related positions as result of movements of rates, indices, prices, yields, volatilities, spreads or other market data between the Early Termination Date and the Local Business Day on which the Non-defaulting Party becomes aware that the Early Termination Date has occurred")
  """
  A boolean attribute to specify whether if an Early Termination Date occurs because Automatic Early Termination applies in respect of a party, the Defaulting Party shall indemnify the Non- defaulting Party, on demand, against any losses, costs, expenses or damages that the Non- defaulting Party incurs (to the extent not already taken into account in Section 6(e)) in relation to terminating, liquidating, establishing or re- establishing any hedge or related positions as result of movements of rates, indices, prices, yields, volatilities, spreads or other market data between the Early Termination Date and the Local Business Day on which the Non-defaulting Party becomes aware that the Early Termination Date has occurred
  """
  partyElection: List[AutomaticEarlyTerminationElection] = Field([], description="The party election specific to the Automatic Early Termination Clause.")
  """
  The party election specific to the Automatic Early Termination Clause.
  """
  @rosetta_condition
  def cardinality_partyElection(self):
    return check_cardinality(self.partyElection, 0, 2)
  
  
  @rosetta_condition
  def condition_0_FallbackAET(self):
    """
    The fallback Automatic Early Termination provision can only be specified as applicable if the Automatic Early Termination Clause is not applicable to one of the parties.
    """
    def _then_fn0():
      return all_elements(self.partyElection.isApplicable, "=", False)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(all_elements(self.fallbackAET, "=", False), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_Indemnity(self):
    """
    If Automatic Early Termination can never apply then indemnity cannot apply.
    """
    def _then_fn0():
      return all_elements(self.indemnity, "=", False)
    
    def _else_fn0():
      return True
    
    return if_cond_fn((all_elements(self.fallbackAET, "=", False) and all_elements(self.partyElection.isApplicable, "=", False)), _then_fn0, _else_fn0)

from cdm.legaldocumentation.master.AutomaticEarlyTerminationElection import AutomaticEarlyTerminationElection

AutomaticEarlyTermination.update_forward_refs()
