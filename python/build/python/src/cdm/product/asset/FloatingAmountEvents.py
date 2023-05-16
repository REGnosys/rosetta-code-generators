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

__all__ = ['FloatingAmountEvents']


class FloatingAmountEvents(BaseDataClass):
  """
  A class to specify the ISDA terms relating to the floating rate payment events and the implied additional fixed payments, applicable to the credit derivatives transactions on mortgage-backed securities with pay-as-you-go or physical settlement.
  """
  additionalFixedPayments: Optional[AdditionalFixedPayments] = Field(None, description="Specifies the events that will give rise to the payment additional fixed payments.")
  """
  Specifies the events that will give rise to the payment additional fixed payments.
  """
  failureToPayPrincipal: Optional[bool] = Field(None, description="A floating rate payment event. Corresponds to the failure by the Reference Entity to pay an expected principal amount or the payment of an actual principal amount that is less than the expected principal amount. ISDA 2003 Term: Failure to Pay Principal.")
  """
  A floating rate payment event. Corresponds to the failure by the Reference Entity to pay an expected principal amount or the payment of an actual principal amount that is less than the expected principal amount. ISDA 2003 Term: Failure to Pay Principal.
  """
  floatingAmountProvisions: Optional[FloatingAmountProvisions] = Field(None, description="Specifies the floating amount provisions associated with the floatingAmountEvents.")
  """
  Specifies the floating amount provisions associated with the floatingAmountEvents.
  """
  impliedWritedown: Optional[bool] = Field(None, description="A floating rate payment event. Results from the fact that losses occur to the underlying instruments that do not result in reductions of the outstanding principal of the reference obligation.")
  """
  A floating rate payment event. Results from the fact that losses occur to the underlying instruments that do not result in reductions of the outstanding principal of the reference obligation.
  """
  interestShortfall: Optional[InterestShortFall] = Field(None, description="A floating rate payment event. With respect to any Reference Obligation Payment Date, either (a) the non-payment of an Expected Interest Amount or (b) the payment of an Actual Interest Amount that is less than the Expected Interest Amount. ISDA 2003 Term: Interest Shortfall.")
  """
  A floating rate payment event. With respect to any Reference Obligation Payment Date, either (a) the non-payment of an Expected Interest Amount or (b) the payment of an Actual Interest Amount that is less than the Expected Interest Amount. ISDA 2003 Term: Interest Shortfall.
  """
  writedown: Optional[bool] = Field(None, description="A floating rate payment event. Results from the fact that the underlier writes down its outstanding principal amount. ISDA 2003 Term: Writedown.")
  """
  A floating rate payment event. Results from the fact that the underlier writes down its outstanding principal amount. ISDA 2003 Term: Writedown.
  """

from cdm.product.asset.AdditionalFixedPayments import AdditionalFixedPayments
from cdm.product.asset.FloatingAmountProvisions import FloatingAmountProvisions
from cdm.product.asset.InterestShortFall import InterestShortFall

FloatingAmountEvents.update_forward_refs()
