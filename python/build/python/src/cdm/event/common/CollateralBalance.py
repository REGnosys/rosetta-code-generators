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

__all__ = ['CollateralBalance']


class CollateralBalance(BaseDataClass):
  """
  Represents common attributes to define a collateral balance recorded by the principal as held or posted.
  """
  amountBaseCurrency: Money = Field(..., description="Specifies the collateral balance amount in base currency determined within a collateral legal agreement, or defined for reporting purposes.")
  """
  Specifies the collateral balance amount in base currency determined within a collateral legal agreement, or defined for reporting purposes.
  """
  collateralBalanceStatus: Optional[CollateralStatusEnum] = Field(None, description="Defines the collateral balance breakdown of settlement status.")
  """
  Defines the collateral balance breakdown of settlement status.
  """
  haircutIndicator: Optional[HaircutIndicatorEnum] = Field(None, description="Indicates if the collateral balance amount is based on pre or post haircut, if a haircut is associated with the collateral asset")
  """
  Indicates if the collateral balance amount is based on pre or post haircut, if a haircut is associated with the collateral asset
  """
  payerReceiver: PartyReferencePayerReceiver = Field(..., description="Specifies each of the parties in the collateral balance and its perspective with regards to the direction of the collateral balance, posted or received.")
  """
  Specifies each of the parties in the collateral balance and its perspective with regards to the direction of the collateral balance, posted or received.
  """

from cdm.observable.asset.Money import Money
from cdm.event.common.CollateralStatusEnum import CollateralStatusEnum
from cdm.event.common.HaircutIndicatorEnum import HaircutIndicatorEnum
from cdm.base.staticdata.party.PartyReferencePayerReceiver import PartyReferencePayerReceiver

CollateralBalance.update_forward_refs()
