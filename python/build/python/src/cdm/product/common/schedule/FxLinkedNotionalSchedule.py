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

__all__ = ['FxLinkedNotionalSchedule']


class FxLinkedNotionalSchedule(BaseDataClass):
  """
  A data to:  describe a notional schedule where each notional that applies to a calculation period is calculated with reference to a notional amount or notional amount schedule in a different currency by means of a spot currency exchange rate which is normally observed at the beginning of each period.
  """
  fixingTime: Optional[BusinessCenterTime] = Field(None, description="The time at which the spot currency exchange rate will be observed. It is specified as a time in a business day calendar location, e.g. 11:00am London time.")
  """
  The time at which the spot currency exchange rate will be observed. It is specified as a time in a business day calendar location, e.g. 11:00am London time.
  """
  fxSpotRateSource: FxSpotRateSource = Field(..., description="The information source and time at which the spot currency exchange rate will be observed.")
  """
  The information source and time at which the spot currency exchange rate will be observed.
  """
  varyingNotionalCurrency: AttributeWithMeta[str] | str = Field(..., description="The currency of the varying notional amount, i.e. the notional amount being determined periodically based on observation of a spot currency exchange rate. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.")
  """
  The currency of the varying notional amount, i.e. the notional amount being determined periodically based on observation of a spot currency exchange rate. The list of valid currencies is not presently positioned as an enumeration as part of the CDM because that scope is limited to the values specified by ISDA and FpML. As a result, implementers have to make reference to the relevant standard, such as the ISO 4217 standard for currency codes.
  """
  varyingNotionalFixingDates: RelativeDateOffset = Field(..., description="The dates on which spot currency exchange rates are observed for purposes of determining the varying notional currency amount that will apply to a calculation period.")
  """
  The dates on which spot currency exchange rates are observed for purposes of determining the varying notional currency amount that will apply to a calculation period.
  """
  varyingNotionalInterimExchangePaymentDates: RelativeDateOffset = Field(..., description="The dates on which interim exchanges of notional are paid. Interim exchanges will arise as a result of changes in the spot currency exchange amount or changes in the constant notional schedule (e.g. amortisation).")
  """
  The dates on which interim exchanges of notional are paid. Interim exchanges will arise as a result of changes in the spot currency exchange amount or changes in the constant notional schedule (e.g. amortisation).
  """

from cdm.base.datetime.BusinessCenterTime import BusinessCenterTime
from cdm.observable.asset.FxSpotRateSource import FxSpotRateSource
from cdm.base.datetime.RelativeDateOffset import RelativeDateOffset

FxLinkedNotionalSchedule.update_forward_refs()
