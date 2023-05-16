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

__all__ = ['EuropeanExercise']


class EuropeanExercise(BaseDataClass):
  """
  A class defining the exercise period for a European style option together with any rules governing the notional amount of the underlying which can be exercised on any given exercise date and any associated exercise fees.
  """
  earliestExerciseTime: Optional[BusinessCenterTime] = Field(None, description="The earliest time at which notice of exercise can be given by the buyer to the seller (or seller's agent) on the expiration date.")
  """
  The earliest time at which notice of exercise can be given by the buyer to the seller (or seller's agent) on the expiration date.
  """
  exerciseFee: Optional[ExerciseFee] = Field(None, description="A fee to be paid on exercise. This could be represented as an amount or a rate and notional reference on which to apply the rate.")
  """
  A fee to be paid on exercise. This could be represented as an amount or a rate and notional reference on which to apply the rate.
  """
  expirationDate: List[AdjustableOrRelativeDate] = Field([], description="The last day within an exercise period for an American style option. For a European style option it is the only day within the exercise period.")
  """
  The last day within an exercise period for an American style option. For a European style option it is the only day within the exercise period.
  """
  @rosetta_condition
  def cardinality_expirationDate(self):
    return check_cardinality(self.expirationDate, 1, None)
  
  expirationTime: BusinessCenterTime = Field(..., description="The latest time for exercise on expirationDate.")
  """
  The latest time for exercise on expirationDate.
  """
  expirationTimeType: Optional[ExpirationTimeTypeEnum] = Field(None, description="The time of day at which the equity option expires, for example the official closing time of the exchange.")
  """
  The time of day at which the equity option expires, for example the official closing time of the exchange.
  """
  partialExercise: Optional[PartialExercise] = Field(None, description="As defined in the 2000 ISDA Definitions, Section 12.3. Partial Exercise, the buyer of the option has the right to exercise all or less than all the notional amount of the underlying swap on the expiration date, but may not exercise less than the minimum notional amount, and if an integral multiple amount is specified, the notional amount exercised must be equal to, or be an integral multiple of, the integral multiple amount.")
  """
  As defined in the 2000 ISDA Definitions, Section 12.3. Partial Exercise, the buyer of the option has the right to exercise all or less than all the notional amount of the underlying swap on the expiration date, but may not exercise less than the minimum notional amount, and if an integral multiple amount is specified, the notional amount exercised must be equal to, or be an integral multiple of, the integral multiple amount.
  """
  relevantUnderlyingDate: Optional[AdjustableOrRelativeDates] = Field(None, description="The effective date on the underlying product if the option is exercised.  For example, for a swaption it is the swap effective date, for an option on an FX spot or forward it is the value date for settlement, and in an extendible/cancelable provision it is the swap termination date, which is the date on which the termination is effective.")
  """
  The effective date on the underlying product if the option is exercised.  For example, for a swaption it is the swap effective date, for an option on an FX spot or forward it is the value date for settlement, and in an extendible/cancelable provision it is the swap termination date, which is the date on which the termination is effective.
  """

from cdm.base.datetime.BusinessCenterTime import BusinessCenterTime
from cdm.product.template.ExerciseFee import ExerciseFee
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate
from cdm.product.template.ExpirationTimeTypeEnum import ExpirationTimeTypeEnum
from cdm.product.template.PartialExercise import PartialExercise
from cdm.base.datetime.AdjustableOrRelativeDates import AdjustableOrRelativeDates

EuropeanExercise.update_forward_refs()
