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

__all__ = ['MultipleDebtTypes']


class MultipleDebtTypes(BaseDataClass):
  """
  Represents a class to specify multiple credit debt types alongside a conditional 'any' or 'all' qualifier.
  """
  condition: QuantifierEnum = Field(..., description="An enumerated attribute, to qualify whether All or Any debt type applies.")
  """
  An enumerated attribute, to qualify whether All or Any debt type applies.
  """
  debtType: List[AttributeWithMeta[str] | str] = Field([], description="The type of debt, e.g. long term debt, deposit, ... FpML doesn't specific a scheme value, hence no enumeration is specified as part of the CDM. At least two debt types much be specified.")
  """
  The type of debt, e.g. long term debt, deposit, ... FpML doesn't specific a scheme value, hence no enumeration is specified as part of the CDM. At least two debt types much be specified.
  """
  @rosetta_condition
  def cardinality_debtType(self):
    return check_cardinality(self.debtType, 2, None)
  

from cdm.base.math.QuantifierEnum import QuantifierEnum

MultipleDebtTypes.update_forward_refs()
