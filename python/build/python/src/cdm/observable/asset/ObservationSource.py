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

__all__ = ['ObservationSource']


class ObservationSource(BaseDataClass):
  """
  The observation source can be composed of an curve and/or and information source.
  """
  curve: Optional[Curve] = Field(None, description="")
  informationSource: Optional[InformationSource] = Field(None, description="")
  
  @rosetta_condition
  def condition_0_CurveInformationSource(self):
    """
    ObservationSource should not be empty, although the attribute cardinality would allow that.
    """
    return (((((self.curve) is not None) and ((self.informationSource) is not None)) or ((self.curve) is not None)) or ((self.informationSource) is not None))

from cdm.observable.asset.Curve import Curve
from cdm.observable.asset.InformationSource import InformationSource

ObservationSource.update_forward_refs()
