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

__all__ = ['BusinessCenters']


class BusinessCenters(BaseDataClass):
  """
  A class for specifying the business day calendar location used in determining whether a day is a business day or not, either by specifying this business center by reference to an enumerated list that is maintained by the FpML standard, or by reference to such specification when it exists elsewhere as part of the instance document. This class corresponds to the FpML BusinessCentersOrReference.model.
  """
  businessCenter: List[AttributeWithMeta[BusinessCenterEnum] | BusinessCenterEnum] = Field([], description="A code identifying one or several business day calendar location(s). The set of business day calendar locations are specified by the business day calendar location enumeration which is maintained by the FpML standard.")
  """
  A code identifying one or several business day calendar location(s). The set of business day calendar locations are specified by the business day calendar location enumeration which is maintained by the FpML standard.
  """
  businessCentersReference: Optional[AttributeWithReference | BusinessCenters] = Field(None, description="A reference to a financial business center location specified elsewhere in the instance document.")
  """
  A reference to a financial business center location specified elsewhere in the instance document.
  """
  
  @rosetta_condition
  def condition_0_BusinessCentersChoice(self):
    """
    Choice rule to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('businessCenter', 'businessCentersReference', necessity=True)

from cdm.base.datetime.BusinessCenterEnum import BusinessCenterEnum
from cdm.base.datetime.BusinessCenters import BusinessCenters

BusinessCenters.update_forward_refs()
