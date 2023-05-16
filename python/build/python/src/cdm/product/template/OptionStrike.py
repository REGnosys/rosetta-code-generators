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

__all__ = ['OptionStrike']


class OptionStrike(BaseDataClass):
  """
  Defines the strike price of an option.
  """
  averagingStrikeFeature: Optional[AveragingStrikeFeature] = Field(None, description="Defines an  option strike that is calculated from an average of observed market prices.")
  """
  Defines an  option strike that is calculated from an average of observed market prices.
  """
  referenceSwapCurve: Optional[ReferenceSwapCurve] = Field(None, description="Defines the strike of an option when expressed by reference to a swap curve (Typically the case for a convertible bond option).")
  """
  Defines the strike of an option when expressed by reference to a swap curve (Typically the case for a convertible bond option).
  """
  strikePrice: Optional[Price] = Field(None, description="Defines the strike of an option in the form of a price that could be a cash price, interestRate, or other types.")
  """
  Defines the strike of an option in the form of a price that could be a cash price, interestRate, or other types.
  """
  strikeReference: Optional[AttributeWithReference | FixedRateSpecification] = Field(None, description="Defines the strike of an option in reference to the spread of the underlying swap (typical practice in the case of an option on a credit single name swaps).")
  """
  Defines the strike of an option in reference to the spread of the underlying swap (typical practice in the case of an option on a credit single name swaps).
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('strikePrice', 'strikeReference', 'referenceSwapCurve', 'averagingStrikeFeature', necessity=True)

from cdm.product.template.AveragingStrikeFeature import AveragingStrikeFeature
from cdm.observable.asset.ReferenceSwapCurve import ReferenceSwapCurve
from cdm.observable.asset.Price import Price
from cdm.product.asset.FixedRateSpecification import FixedRateSpecification

OptionStrike.update_forward_refs()
