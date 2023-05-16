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

__all__ = ['BondPriceAndYieldModel']


class BondPriceAndYieldModel(BaseDataClass):
  """
   Bond price and yield valuation model for the security leg in a securities financing transaction, closely modelled onto the BondPriceAndYield.model in FpML.
  """
  allInPrice: Optional[Decimal] = Field(None, description="Bond all-in-price which is a price that includes all relevant price adjustments (i.e. accrued interest, haircut or margin ratio, inflation factor,etc.). It expresses a price in terms of percentage of nominal amount.")
  """
  Bond all-in-price which is a price that includes all relevant price adjustments (i.e. accrued interest, haircut or margin ratio, inflation factor,etc.). It expresses a price in terms of percentage of nominal amount.
  """
  cleanOrDirtyPrice: Optional[CleanOrDirtyPrice] = Field(None, description="Either the clean or dirty price of the bond.")
  """
  Either the clean or dirty price of the bond.
  """
  inflationFactor: Optional[Decimal] = Field(None, description="The inflation factor is specified for inflation-linked products which require some additional elements to calculate prices correctly.")
  """
  The inflation factor is specified for inflation-linked products which require some additional elements to calculate prices correctly.
  """
  relativePrice: Optional[RelativePrice] = Field(None, description="Bond price relative to a Benchmark.")
  """
  Bond price relative to a Benchmark.
  """
  yieldToMaturity: Optional[Decimal] = Field(None, description="Price specified as a yield to maturity.")
  """
  Price specified as a yield to maturity.
  """

from cdm.observable.asset.CleanOrDirtyPrice import CleanOrDirtyPrice
from cdm.observable.asset.RelativePrice import RelativePrice

BondPriceAndYieldModel.update_forward_refs()
