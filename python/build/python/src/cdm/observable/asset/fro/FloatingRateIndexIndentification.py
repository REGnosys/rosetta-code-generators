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

__all__ = ['FloatingRateIndexIndentification']


class FloatingRateIndexIndentification(BaseDataClass):
  currency: Optional[ISOCurrencyCodeEnum] = Field(None, description="FRO currency - 3 character ISO currrency code")
  """
  FRO currency - 3 character ISO currrency code
  """
  floatingRateIndex: Optional[AttributeWithMeta[FloatingRateIndexEnum] | FloatingRateIndexEnum] = Field(None, description="The reference index that is used to specify the floating interest rate. The FpML standard maintains the list of such indices, which are positioned as enumeration values as part of the CDM.")
  """
  The reference index that is used to specify the floating interest rate. The FpML standard maintains the list of such indices, which are positioned as enumeration values as part of the CDM.
  """
  froType: Optional[str] = Field(None, description="FRO type (e.g. OIS)")
  """
  FRO type (e.g. OIS)
  """

from cdm.base.staticdata.asset.common.ISOCurrencyCodeEnum import ISOCurrencyCodeEnum
from cdm.base.staticdata.asset.rates.FloatingRateIndexEnum import FloatingRateIndexEnum

FloatingRateIndexIndentification.update_forward_refs()
