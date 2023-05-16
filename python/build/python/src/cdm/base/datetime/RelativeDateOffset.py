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

__all__ = ['RelativeDateOffset']

from cdm.base.datetime.Offset import Offset

class RelativeDateOffset(Offset):
  """
  A class defining a date (referred to as the derived date) as a relative offset from another date (referred to as the anchor date). If the anchor date is itself an adjustable date then the offset is assumed to be calculated from the adjusted anchor date. A number of different scenarios can be supported, namely; 1) the derived date may simply be a number of calendar periods (days, weeks, months or years) preceding or following the anchor date; 2) the unadjusted derived date may be a number of calendar periods (days, weeks, months or years) preceding or following the anchor date with the resulting unadjusted derived date subject to adjustment in accordance with a specified business day convention, i.e. the derived date must fall on a good business day; 3) the derived date may be a number of business days preceding or following the anchor date. Note that the businessDayConvention specifies any required adjustment to the unadjusted derived date. A negative or positive value in the periodMultiplier indicates whether the unadjusted derived precedes or follows the anchor date. The businessDayConvention should contain a value NONE if the day type element contains a value of Business (since specifying a negative or positive business days offset would already guarantee that the derived date would fall on a good business day in the specified business centers).
  """
  adjustedDate: Optional[date] = Field(None, description="The date once the adjustment has been performed. (Note that this date may change if the business center holidays change).")
  """
  The date once the adjustment has been performed. (Note that this date may change if the business center holidays change).
  """
  businessCenters: Optional[BusinessCenters] = Field(None, description="")
  businessCentersReference: Optional[AttributeWithReference | BusinessCenters] = Field(None, description="A pointer style reference to a set of financial business centers defined elsewhere in the document. This set of business centers is used to determine whether a particular day is a business day or not.")
  """
  A pointer style reference to a set of financial business centers defined elsewhere in the document. This set of business centers is used to determine whether a particular day is a business day or not.
  """
  businessDayConvention: BusinessDayConventionEnum = Field(..., description="The convention for adjusting a date if it would otherwise fall on a day that is not a business day, as specified by an ISDA convention (e.g. Following, Precedent).")
  """
  The convention for adjusting a date if it would otherwise fall on a day that is not a business day, as specified by an ISDA convention (e.g. Following, Precedent).
  """
  dateRelativeTo: Optional[AttributeWithReference | date] = Field(None, description="Specifies the anchor as an href attribute. The href attribute value is a pointer style reference to the element or component elsewhere in the document where the anchor date is defined.")
  """
  Specifies the anchor as an href attribute. The href attribute value is a pointer style reference to the element or component elsewhere in the document where the anchor date is defined.
  """

from cdm.base.datetime.BusinessCenters import BusinessCenters
from cdm.base.datetime.BusinessDayConventionEnum import BusinessDayConventionEnum

RelativeDateOffset.update_forward_refs()
