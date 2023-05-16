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

__all__ = ['PremiumExpression']


class PremiumExpression(BaseDataClass):
  """
  This class corresponds to the FpML Premium.model group for representing the option premium when expressed in a way other than an amount.
  """
  percentageOfNotional: Optional[Decimal] = Field(None, description="The amount of premium to be paid expressed as a percentage of the notional value of the transaction. A percentage of 5% would be expressed as 0.05.")
  """
  The amount of premium to be paid expressed as a percentage of the notional value of the transaction. A percentage of 5% would be expressed as 0.05.
  """
  premiumType: Optional[PremiumTypeEnum] = Field(None, description="Forward start premium type")
  """
  Forward start premium type
  """
  pricePerOption: Optional[Money] = Field(None, description="The amount of premium to be paid expressed as a function of the number of options.")
  """
  The amount of premium to be paid expressed as a function of the number of options.
  """

from cdm.observable.asset.PremiumTypeEnum import PremiumTypeEnum
from cdm.observable.asset.Money import Money

PremiumExpression.update_forward_refs()
