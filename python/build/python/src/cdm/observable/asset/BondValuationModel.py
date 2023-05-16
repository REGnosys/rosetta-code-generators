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

__all__ = ['BondValuationModel']


class BondValuationModel(BaseDataClass):
  """
   Bond valuation model for the security leg in a securities financing transaction, closely modelled onto the BondCollateral.model in FpML.
  """
  accrualsAmount: Optional[Money] = Field(None, description="Accruals amount for the bond in the security leg")
  """
  Accruals amount for the bond in the security leg
  """
  bondPriceAndYieldModel: BondPriceAndYieldModel = Field(..., description="Price and yield model for valuing a bond security leg.")
  """
  Price and yield model for valuing a bond security leg.
  """
  nominalAmount: Money = Field(..., description="The quantity of the underlier expressed as a nominal amount.")
  """
  The quantity of the underlier expressed as a nominal amount.
  """

from cdm.observable.asset.Money import Money
from cdm.observable.asset.BondPriceAndYieldModel import BondPriceAndYieldModel

BondValuationModel.update_forward_refs()
