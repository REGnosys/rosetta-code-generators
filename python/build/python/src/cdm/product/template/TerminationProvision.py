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

__all__ = ['TerminationProvision']


class TerminationProvision(BaseDataClass):
  """
  A class for defining option provisions.
  """
  cancelableProvision: Optional[CancelableProvision] = Field(None, description="A provision that allows the specification of an embedded option within a swap giving the buyer of the option the right to terminate the swap, in whole or in part, on the early termination date.")
  """
  A provision that allows the specification of an embedded option within a swap giving the buyer of the option the right to terminate the swap, in whole or in part, on the early termination date.
  """
  earlyTerminationProvision: Optional[EarlyTerminationProvision] = Field(None, description="Parameters specifying provisions relating to the optional and mandatory early termination of a swap transaction.")
  """
  Parameters specifying provisions relating to the optional and mandatory early termination of a swap transaction.
  """
  evergreenProvision: Optional[EvergreenProvision] = Field(None, description="A data defining: the right of a party to exercise an Evergreen option")
  """
  A data defining: the right of a party to exercise an Evergreen option
  """
  extendibleProvision: Optional[ExtendibleProvision] = Field(None, description="A provision that allows the specification of an embedded option with a swap giving the buyer of the option the right to extend the swap, in whole or in part, to the extended termination date.")
  """
  A provision that allows the specification of an embedded option with a swap giving the buyer of the option the right to extend the swap, in whole or in part, to the extended termination date.
  """
  
  @rosetta_condition
  def condition_0_TerminationProvisionChoice(self):
    return self.check_one_of_constraint('cancelableProvision', 'extendibleProvision', 'evergreenProvision', 'earlyTerminationProvision', necessity=True)

from cdm.product.template.CancelableProvision import CancelableProvision
from cdm.product.template.EarlyTerminationProvision import EarlyTerminationProvision
from cdm.product.template.EvergreenProvision import EvergreenProvision
from cdm.product.template.ExtendibleProvision import ExtendibleProvision

TerminationProvision.update_forward_refs()
