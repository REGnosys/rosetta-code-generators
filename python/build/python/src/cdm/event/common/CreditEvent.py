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

__all__ = ['CreditEvent']


class CreditEvent(BaseDataClass):
  """
  Specifies the relevant data regarding a credit event.
  """
  auctionDate: Optional[date] = Field(None, description="The date on which the auction is scheduled to occur.")
  """
  The date on which the auction is scheduled to occur.
  """
  creditEventType: CreditEventTypeEnum = Field(..., description="The type of credit event taking place.")
  """
  The type of credit event taking place.
  """
  eventDeterminationDate: date = Field(..., description="The date in which the credit event is determined by the Credit Derivatives Determinations Comitee.")
  """
  The date in which the credit event is determined by the Credit Derivatives Determinations Comitee.
  """
  finalPrice: Optional[Price] = Field(None, description="The final price resulting from the auction.")
  """
  The final price resulting from the auction.
  """
  publiclyAvailableInformation: List[Resource] = Field([], description="A public information source, e.g. a particular newspaper or electronic news service, that may publish relevant information used in the determination of whether or not a credit event has occurred.")
  """
  A public information source, e.g. a particular newspaper or electronic news service, that may publish relevant information used in the determination of whether or not a credit event has occurred.
  """
  recoveryPercent: Optional[Decimal] = Field(None, description="The percentage of the original value of the asset affected by the credit event that can be recovered.")
  """
  The percentage of the original value of the asset affected by the credit event that can be recovered.
  """
  referenceInformation: ReferenceInformation = Field(..., description="The reference entity, part of a credit basket, impacted by the credit event.")
  """
  The reference entity, part of a credit basket, impacted by the credit event.
  """

from cdm.event.common.CreditEventTypeEnum import CreditEventTypeEnum
from cdm.observable.asset.Price import Price
from cdm.legaldocumentation.common.Resource import Resource
from cdm.product.asset.ReferenceInformation import ReferenceInformation

CreditEvent.update_forward_refs()
