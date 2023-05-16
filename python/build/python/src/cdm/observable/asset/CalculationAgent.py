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

__all__ = ['CalculationAgent']


class CalculationAgent(BaseDataClass):
  """
  A class defining the ISDA calculation agent responsible for performing duties as defined in the applicable product definitions.
  """
  calculationAgentBusinessCenter: Optional[AttributeWithMeta[BusinessCenterEnum] | BusinessCenterEnum] = Field(None, description="The city in which the office through which ISDA Calculation Agent is acting for purposes of the transaction is located The short-form confirm for a trade that is executed under a Sovereign or Asia Pacific Master Confirmation Agreement ( MCA ), does not need to specify the Calculation Agent. However, the confirm does need to specify the Calculation Agent City. This is due to the fact that the MCA sets the value for Calculation Agent but does not set the value for Calculation Agent City.")
  """
  The city in which the office through which ISDA Calculation Agent is acting for purposes of the transaction is located The short-form confirm for a trade that is executed under a Sovereign or Asia Pacific Master Confirmation Agreement ( MCA ), does not need to specify the Calculation Agent. However, the confirm does need to specify the Calculation Agent City. This is due to the fact that the MCA sets the value for Calculation Agent but does not set the value for Calculation Agent City.
  """
  calculationAgentParty: Optional[AncillaryRoleEnum] = Field(None, description="Specifies the party which is the ISDA Calculation Agent for the trade. If more than one party is referenced then the parties are assumed to be co-calculation agents, i.e. they have joint responsibility.")
  """
  Specifies the party which is the ISDA Calculation Agent for the trade. If more than one party is referenced then the parties are assumed to be co-calculation agents, i.e. they have joint responsibility.
  """
  calculationAgentPartyEnum: Optional[PartyDeterminationEnum] = Field(None, description="Specifies the ISDA calculation agent responsible for performing duties as defined in the applicable product definitions. For example, the Calculation Agent may be defined as being the Non-exercising Party.")
  """
  Specifies the ISDA calculation agent responsible for performing duties as defined in the applicable product definitions. For example, the Calculation Agent may be defined as being the Non-exercising Party.
  """
  
  @rosetta_condition
  def condition_0_CalculationAgentChoice(self):
    """
    Choice rule to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('calculationAgentParty', 'calculationAgentPartyEnum', necessity=False)

from cdm.base.datetime.BusinessCenterEnum import BusinessCenterEnum
from cdm.base.staticdata.party.AncillaryRoleEnum import AncillaryRoleEnum
from cdm.observable.asset.PartyDeterminationEnum import PartyDeterminationEnum

CalculationAgent.update_forward_refs()
