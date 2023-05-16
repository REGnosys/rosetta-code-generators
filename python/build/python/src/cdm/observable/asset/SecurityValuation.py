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

__all__ = ['SecurityValuation']


class SecurityValuation(BaseDataClass):
  """
   Terms defining the security valuation method as part of a security leg in a securities fianncing transaction and closely modelled onto the CollateralValuation type in FpML.
  """
  securityValuationModel: SecurityValuationModel = Field(..., description="The security valuation model choice, based on either a nominal amount or a number of units.")
  """
  The security valuation model choice, based on either a nominal amount or a number of units.
  """
  underlier: Security = Field(..., description="The underlying security of the security leg.")
  """
  The underlying security of the security leg.
  """

from cdm.observable.asset.SecurityValuationModel import SecurityValuationModel
from cdm.base.staticdata.asset.common.Security import Security

SecurityValuation.update_forward_refs()
