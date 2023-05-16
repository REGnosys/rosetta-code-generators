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

__all__ = ['FloatingRateOption']


class FloatingRateOption(BaseDataClass):
  """
  Specification of a floating rate option as a floating rate index and tenor.
  """
  floatingRateIndex: Optional[AttributeWithMeta[FloatingRateIndexEnum] | FloatingRateIndexEnum] = Field(None, description="The reference index that is used to specify the floating interest rate. The FpML standard maintains the list of such indices, which are positioned as enumeration values as part of the CDM.")
  """
  The reference index that is used to specify the floating interest rate. The FpML standard maintains the list of such indices, which are positioned as enumeration values as part of the CDM.
  """
  indexTenor: Optional[Period] = Field(None, description="The ISDA Designated Maturity, i.e. the floating rate tenor.")
  """
  The ISDA Designated Maturity, i.e. the floating rate tenor.
  """
  inflationRateIndex: Optional[AttributeWithMeta[InflationRateIndexEnum] | InflationRateIndexEnum] = Field(None, description="The reference index that is used to specify the inflation interest rate. The FpML standard maintains the list of such indices, which are positioned as enumeration values as part of the CDM.")
  """
  The reference index that is used to specify the inflation interest rate. The FpML standard maintains the list of such indices, which are positioned as enumeration values as part of the CDM.
  """
  
  @rosetta_condition
  def condition_0_FloatingRateIndex(self):
    """
    A required choice condition for either a floating rate or inflation rate index.
    """
    return self.check_one_of_constraint('floatingRateIndex', 'inflationRateIndex', necessity=True)

from cdm.base.staticdata.asset.rates.FloatingRateIndexEnum import FloatingRateIndexEnum
from cdm.base.datetime.Period import Period
from cdm.base.staticdata.asset.rates.InflationRateIndexEnum import InflationRateIndexEnum

FloatingRateOption.update_forward_refs()
