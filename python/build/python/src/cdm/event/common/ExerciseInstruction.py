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

__all__ = ['ExerciseInstruction']


class ExerciseInstruction(BaseDataClass):
  """
  Specifies the information required to communicate the choices made by the exercising party, in a financial product endowing the party with at least one option.
  """
  exerciseDate: Optional[AdjustableOrAdjustedDate] = Field(None, description="Specifies the date on which an option contained within the financial product would be exercised. The date may be omitted if the contractual product allows for only a single date of exercise (European exercise).")
  """
  Specifies the date on which an option contained within the financial product would be exercised. The date may be omitted if the contractual product allows for only a single date of exercise (European exercise).
  """
  exerciseOption: Optional[AttributeWithReference | OptionPayout] = Field(None, description="Specifies the Option Payout being exercised on the trade.")
  """
  Specifies the Option Payout being exercised on the trade.
  """
  exerciseQuantity: PrimitiveInstruction = Field(..., description="Contains instructions for exercising the option including a quantity change, and optionally a transfer.")
  """
  Contains instructions for exercising the option including a quantity change, and optionally a transfer.
  """
  exerciseTime: Optional[BusinessCenterTime] = Field(None, description="Specifies the time at which an option contained within the financial product woulld be exercised. The time may be omitted if the contractual product allows for only a single time of exercise (European exercise). ")
  """
  Specifies the time at which an option contained within the financial product woulld be exercised. The time may be omitted if the contractual product allows for only a single time of exercise (European exercise). 
  """
  replacementTradeIdentifier: List[Identifier] = Field([], description="Specifies the trade identifier to apply to the replacement trade for physical exercise.")
  """
  Specifies the trade identifier to apply to the replacement trade for physical exercise.
  """

from cdm.base.datetime.AdjustableOrAdjustedDate import AdjustableOrAdjustedDate
from cdm.product.template.OptionPayout import OptionPayout
from cdm.event.common.PrimitiveInstruction import PrimitiveInstruction
from cdm.base.datetime.BusinessCenterTime import BusinessCenterTime
from cdm.base.staticdata.identifier.Identifier import Identifier

ExerciseInstruction.update_forward_refs()
