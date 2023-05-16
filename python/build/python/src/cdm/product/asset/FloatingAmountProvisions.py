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

__all__ = ['FloatingAmountProvisions']


class FloatingAmountProvisions(BaseDataClass):
  stepUpProvision: Optional[bool] = Field(None, description="As specified by the ISDA Standard Terms Supplement for use with trades on mortgage-backed securities. The presence of the element with value set to 'true' signifies that the provision is applicable. If applicable, the applicable step-up terms are specified as part of that ISDA Standard Terms Supplement. From a usage standpoint, this provision is typically applicable in the case of RMBS and not applicable in case of CMBS trades.")
  """
  As specified by the ISDA Standard Terms Supplement for use with trades on mortgage-backed securities. The presence of the element with value set to 'true' signifies that the provision is applicable. If applicable, the applicable step-up terms are specified as part of that ISDA Standard Terms Supplement. From a usage standpoint, this provision is typically applicable in the case of RMBS and not applicable in case of CMBS trades.
  """
  wacCapInterestProvision: Optional[bool] = Field(None, description="As specified by the ISDA Supplement for use with trades on mortgage-backed securities, 'WAC Cap' means a weighted average coupon or weighted average rate cap provision (however defined in the Underlying Instruments) of the Underlying Instruments that limits, increases or decreases the interest rate or interest entitlement, as set out in the Underlying Instruments on the Effective Date without regard to any subsequent amendment The presence of the element with value set to 'true' signifies that the provision is applicable. From a usage standpoint, this provision is typically applicable in the case of CMBS and not applicable in case of RMBS trades.")
  """
  As specified by the ISDA Supplement for use with trades on mortgage-backed securities, 'WAC Cap' means a weighted average coupon or weighted average rate cap provision (however defined in the Underlying Instruments) of the Underlying Instruments that limits, increases or decreases the interest rate or interest entitlement, as set out in the Underlying Instruments on the Effective Date without regard to any subsequent amendment The presence of the element with value set to 'true' signifies that the provision is applicable. From a usage standpoint, this provision is typically applicable in the case of CMBS and not applicable in case of RMBS trades.
  """


FloatingAmountProvisions.update_forward_refs()
