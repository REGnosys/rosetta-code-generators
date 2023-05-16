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

__all__ = ['ExerciseFee']

from cdm.base.staticdata.party.PayerReceiver import PayerReceiver

class ExerciseFee(PayerReceiver):
  """
  A class defining the fee payable on exercise of an option. This fee may be defined as an amount or a percentage of the notional exercised. As a difference with FpML, it extends the BuyerSeller class.
  """
  feeAmount: Optional[Decimal] = Field(None, description="The amount of fee to be paid on exercise. The fee currency is that of the referenced notional.")
  """
  The amount of fee to be paid on exercise. The fee currency is that of the referenced notional.
  """
  feePaymentDate: RelativeDateOffset = Field(..., description="The date on which exercise fee(s) will be paid. It is specified as a relative date.")
  """
  The date on which exercise fee(s) will be paid. It is specified as a relative date.
  """
  feeRate: Optional[Decimal] = Field(None, description="A fee represented as a percentage of some referenced notional. A percentage of 5% would be represented as 0.05.")
  """
  A fee represented as a percentage of some referenced notional. A percentage of 5% would be represented as 0.05.
  """
  notionalReference: AttributeWithReference | Money = Field(..., description="A pointer style reference to the associated notional schedule defined elsewhere in the document.")
  """
  A pointer style reference to the associated notional schedule defined elsewhere in the document.
  """
  
  @rosetta_condition
  def condition_0_ExerciseFeeChoice(self):
    """
    Choice rule to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('feeAmount', 'feeRate', necessity=True)

from cdm.base.datetime.RelativeDateOffset import RelativeDateOffset
from cdm.observable.asset.Money import Money

ExerciseFee.update_forward_refs()
