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

__all__ = ['DividendPeriod']


class DividendPeriod(BaseDataClass):
  """
  Time bounded dividend payment periods, each with a dividend payment date per period.
  """
  basketConstituent: Optional[Product] = Field(None, description="For basket undeliers, reference to the basket component which is paying dividends in the specified period.")
  """
  For basket undeliers, reference to the basket component which is paying dividends in the specified period.
  """
  dateAdjustments: BusinessDayAdjustments = Field(..., description="Date adjustments for all unadjusted dates in this dividend period.")
  """
  Date adjustments for all unadjusted dates in this dividend period.
  """
  dividendPaymentDate: DividendPaymentDate = Field(..., description="Specifies when the dividend will be paid to the receiver of the equity return. Has the meaning as defined in the ISDA 2002 Equity Derivatives Definitions. Is not applicable in the case of a dividend reinvestment election.")
  """
  Specifies when the dividend will be paid to the receiver of the equity return. Has the meaning as defined in the ISDA 2002 Equity Derivatives Definitions. Is not applicable in the case of a dividend reinvestment election.
  """
  dividendValuationDate: Optional[AdjustableOrRelativeDate] = Field(None, description="Specifies the dividend valuation dates of the swap.")
  """
  Specifies the dividend valuation dates of the swap.
  """
  endDate: Optional[DividendPaymentDate] = Field(None, description="Dividend period end date.")
  """
  Dividend period end date.
  """
  startDate: Optional[DividendPaymentDate] = Field(None, description="Dividend period start date.")
  """
  Dividend period start date.
  """

from cdm.product.template.Product import Product
from cdm.base.datetime.BusinessDayAdjustments import BusinessDayAdjustments
from cdm.product.asset.DividendPaymentDate import DividendPaymentDate
from cdm.base.datetime.AdjustableOrRelativeDate import AdjustableOrRelativeDate

DividendPeriod.update_forward_refs()
