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

__all__ = ['TimeZone']


class TimeZone(BaseDataClass):
  """
  The time alongside with the timezone location information. This class makes use of the FpML TimezoneLocation construct.
  """
  location: Optional[AttributeWithMeta[str] | str] = Field(None, description="FpML specifies the timezoneLocationScheme by reference to the Time Zone Database (a.k.a. tz database) maintained by IANA, the Internet Assigned Numbers Authority.")
  """
  FpML specifies the timezoneLocationScheme by reference to the Time Zone Database (a.k.a. tz database) maintained by IANA, the Internet Assigned Numbers Authority.
  """
  time: time = Field(..., description="The observation time.")
  """
  The observation time.
  """


TimeZone.update_forward_refs()
