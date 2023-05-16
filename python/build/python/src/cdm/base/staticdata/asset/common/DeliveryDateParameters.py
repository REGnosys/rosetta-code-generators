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

__all__ = ['DeliveryDateParameters']


class DeliveryDateParameters(BaseDataClass):
  """
  Specifies a specific date or the parameters for identifying the relevant contract date when the commodity reference price is a futures contract.
  """
  deliveryDate: Optional[AdjustableDate] = Field(None, description="Specifies the specific contract date for the contract that should be referenced for a price.")
  """
  Specifies the specific contract date for the contract that should be referenced for a price.
  """
  deliveryDateExpirationConvention: Optional[Offset] = Field(None, description="Specifies, for a Commodity Transaction that references a listed future, the day on which the specified future will expire ahead of the actual expiration of the referenced future. For example: Z21 Contract expires on 19Nov21, with an adjust of 2D the 'expire' will be 16Nov21. DeliveryDateRollConvention takes precedence. Example: Pricing on the Z21 Contract with NearbyContractDay and a deliveryDateRoll of 10D, Sampling of the F22 Contract will occur on 8Nov21 through the last Date of the Z21 Contract. With an ExpConvention of 5D, the last sampling date on the F22 contract will be 12Nov21.")
  """
  Specifies, for a Commodity Transaction that references a listed future, the day on which the specified future will expire ahead of the actual expiration of the referenced future. For example: Z21 Contract expires on 19Nov21, with an adjust of 2D the 'expire' will be 16Nov21. DeliveryDateRollConvention takes precedence. Example: Pricing on the Z21 Contract with NearbyContractDay and a deliveryDateRoll of 10D, Sampling of the F22 Contract will occur on 8Nov21 through the last Date of the Z21 Contract. With an ExpConvention of 5D, the last sampling date on the F22 contract will be 12Nov21.
  """
  deliveryDateRollConvention: Optional[Offset] = Field(None, description="Specifies, for a Commodity Transaction that references a listed future, the day on which the specified future will roll to the next nearby month prior to the expiration of the referenced future. If the future will not roll at all - i.e. the price will be taken from the expiring contract, 0 days should be specified here. If the future will roll to the next nearby on the last trading day - i.e. the price will be taken from the next nearby on the last trading day, then 1 business day should be specified and so on.")
  """
  Specifies, for a Commodity Transaction that references a listed future, the day on which the specified future will roll to the next nearby month prior to the expiration of the referenced future. If the future will not roll at all - i.e. the price will be taken from the expiring contract, 0 days should be specified here. If the future will roll to the next nearby on the last trading day - i.e. the price will be taken from the next nearby on the last trading day, then 1 business day should be specified and so on.
  """
  deliveryNearby: Optional[Offset] = Field(None, description="Provides a container for the parametric representation that specifies which nearby contract date would be used as a refrence for a price .")
  """
  Provides a container for the parametric representation that specifies which nearby contract date would be used as a refrence for a price .
  """
  
  @rosetta_condition
  def condition_0_DeliveryDateParametersChoice(self):
    """
    Requires definition of a delivery date or delieryNearby parameters.
    """
    return self.check_one_of_constraint('deliveryNearby', 'deliveryDate', necessity=False)

from cdm.base.datetime.AdjustableDate import AdjustableDate
from cdm.base.datetime.Offset import Offset

DeliveryDateParameters.update_forward_refs()
