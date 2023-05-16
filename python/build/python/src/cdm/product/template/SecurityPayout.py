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

__all__ = ['SecurityPayout']


class SecurityPayout(BaseDataClass):
  """
   Security payout specification in case the product payout involves some form of security collateral, as in a securities financing transaction.
  """
  initialMargin: Optional[InitialMargin] = Field(None, description="RepoDurationEnum.")
  """
  RepoDurationEnum.
  """
  repoDuration: Optional[RepoDurationEnum] = Field(None, description="A duration code for the repo transaction. This defines a type of a repo transaction with fixed duration.")
  """
  A duration code for the repo transaction. This defines a type of a repo transaction with fixed duration.
  """
  securityLeg: List[SecurityLeg] = Field([], description="Each SecurityLeg represent a buy/sell at different dates, typically 1 near leg and 1 far leg in a securities financing transaction.")
  """
  Each SecurityLeg represent a buy/sell at different dates, typically 1 near leg and 1 far leg in a securities financing transaction.
  """
  @rosetta_condition
  def cardinality_securityLeg(self):
    return check_cardinality(self.securityLeg, 1, None)
  
  securityValuation: List[SecurityValuation] = Field([], description="The underlying securities and their valuation for the security leg.")
  """
  The underlying securities and their valuation for the security leg.
  """
  @rosetta_condition
  def cardinality_securityValuation(self):
    return check_cardinality(self.securityValuation, 1, None)
  

from cdm.product.template.InitialMargin import InitialMargin
from cdm.product.template.RepoDurationEnum import RepoDurationEnum
from cdm.product.template.SecurityLeg import SecurityLeg
from cdm.observable.asset.SecurityValuation import SecurityValuation

SecurityPayout.update_forward_refs()
