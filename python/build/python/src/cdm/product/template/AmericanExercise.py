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

__all__ = ['AmericanExercise']


class AmericanExercise(BaseDataClass):
  """
  A class defining the exercise period for an American style option together with any rules governing the notional amount of the underlying which can be exercised on any given exercise date and any associated exercise fees.
  """
  commencementDate: AdjustableOrRelativeDate = Field(..., description="The first day of the exercise period for an American style option.")
  """
  The first day of the exercise period for an American style option.
  """
  earliestExerciseTime: Optional[BusinessCenterTime] = Field(None, description="The earliest time at which notice of exercise can be given by the buyer to the seller (or seller's agent) to, and including, the expiration date.")
  """
  The earliest time at which notice of exercise can be given by the buyer to the seller (or seller's agent) to, and including, the expiration date.
  """
  exerciseFeeSchedule: Optional[ExerciseFeeSchedule] = Field(None, description="The fees associated with an exercise date. The fees are conditional on the exercise occurring. The fees can be specified as actual currency amounts or as percentages of the notional amount being exercised.")
  """
  The fees associated with an exercise date. The fees are conditional on the exercise occurring. The fees can be specified as actual currency amounts or as percentages of the notional amount being exercised.
  """
  expirationDate: AdjustableOrRelativeDate = Field(..., description="The last day within an exercise period for an American style option. For a European style option it is the only day within the exercise period.")
  """
  The last day within an exercise period for an American style option. For a European style option it is the only day within the exercise period.
  """
  expirationTime: BusinessCenterTime = Field(..., description="The latest time for exercise on expirationDate.")
  """
  The latest time for exercise on expirationDate.
  """
  expirationTimeType: Optional[ExpirationTimeTypeEnum] = Field(None, description="The time of day at which the equity option expires, for example the official closing time of the exchange.")
  """
  The time of day at which the equity option expires, for example the official closing time of the exchange.
  """
  latestExerciseTime: Optional[BusinessCenterTime] = Field(None, description="For a Bermuda or American style option, the latest time on an exercise business day (excluding the expiration date) within the exercise period that notice can be given by the buyer to the seller or seller's agent. Notice of exercise given after this time will be deemed to have been given on the next exercise business day.")
  """
  For a Bermuda or American style option, the latest time on an exercise business day (excluding the expiration date) within the exercise period that notice can be given by the buyer to the seller or seller's agent. Notice of exercise given after this time will be deemed to have been given on the next exercise business day.
  """
  multipleExercise: Optional[MultipleExercise] = Field(None, description="As defined in the 2000 ISDA Definitions, Section 12.4. Multiple Exercise, the buyer of the option has the right to exercise all or less than all the unexercised notional amount of the underlying swap on one or more days in the exercise period, but on any such day may not exercise less than the minimum notional amount or more that the maximum notional amount, and if an integral multiple amount is specified, the notional amount exercised must be equal to, or be an integral multiple of, the integral multiple amount.")
  """
  As defined in the 2000 ISDA Definitions, Section 12.4. Multiple Exercise, the buyer of the option has the right to exercise all or less than all the unexercised notional amount of the underlying swap on one or more days in the exercise period, but on any such day may not exercise less than the minimum notional amount or more that the maximum notional amount, and if an integral multiple amount is specified, the notional amount exercised must be equal to, or be an integral multiple of, the integral multiple amount.
  """
  relevantUnderlyingDate: Optional[AdjustableOrRelativeDates] = Field(None, description="The effective date on the underlying product if the option is exercised.  For example, for a swaption it is the swap effective date, for an option on an FX spot or forward it is the value date for settlement, and in an extendible/cancelable provision it is the swap termination date, which is the date on which the termination is effective.'")
  """
  The effective date on the underlying product if the option is exercised.  For example, for a swaption it is the swap effective date, for an option on an FX spot or forward it is the value date for settlement, and in an extendible/cancelable provision it is the swap termination date, which is the date on which the termination is effective.'
  """

from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate
from cdm.base.datetime.BusinessCenterTime import BusinessCenterTime
from cdm.product.template.ExerciseFeeSchedule import ExerciseFeeSchedule
from cdm.product.template.ExpirationTimeTypeEnum import ExpirationTimeTypeEnum
from cdm.product.template.MultipleExercise import MultipleExercise
from cdm.base.datetime.AdjustableOrRelativeDates import AdjustableOrRelativeDates

AmericanExercise.update_forward_refs()
