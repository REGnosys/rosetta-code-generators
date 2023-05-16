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

__all__ = ['CalculationAgentModel']


class CalculationAgentModel(BaseDataClass):
  """
  This class corresponds to the FpML CalculationAgent.model.
  """
  calculationAgent: Optional[CalculationAgent] = Field(None, description="The ISDA calculation agent responsible for performing duties as defined in the applicable product definitions.")
  """
  The ISDA calculation agent responsible for performing duties as defined in the applicable product definitions.
  """
  calculationAgentBusinessCenter: Optional[BusinessCenterEnum] = Field(None, description="The city in which the office through which ISDA Calculation Agent is acting for purposes of the transaction is located. The short-form confirm for a trade that is executed under a Sovereign or Asia-Pacific Master Confirmation Agreement (MCA), does not need to specify the Calculation Agent. However, the confirm does need to specify the Calculation Agent city. This is due to the fact that the MCA sets the value for Calculation Agent but does not set the value for Calculation Agent city.")
  """
  The city in which the office through which ISDA Calculation Agent is acting for purposes of the transaction is located. The short-form confirm for a trade that is executed under a Sovereign or Asia-Pacific Master Confirmation Agreement (MCA), does not need to specify the Calculation Agent. However, the confirm does need to specify the Calculation Agent city. This is due to the fact that the MCA sets the value for Calculation Agent but does not set the value for Calculation Agent city.
  """

from cdm.observable.asset.CalculationAgent import CalculationAgent
from cdm.base.datetime.BusinessCenterEnum import BusinessCenterEnum

CalculationAgentModel.update_forward_refs()
