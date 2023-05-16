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

__all__ = ['FxInformationSource']

from cdm.observable.asset.InformationSource import InformationSource

class FxInformationSource(InformationSource):
  """
  Information source specific to Foreign Exchange products.
  """
  fixingTime: Optional[BusinessCenterTime] = Field(None, description="The time that the fixing will be taken along with a business center to define the time zone.")
  """
  The time that the fixing will be taken along with a business center to define the time zone.
  """

from cdm.base.datetime.BusinessCenterTime import BusinessCenterTime

FxInformationSource.update_forward_refs()
