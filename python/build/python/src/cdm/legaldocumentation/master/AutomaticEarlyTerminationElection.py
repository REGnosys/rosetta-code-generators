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

__all__ = ['AutomaticEarlyTerminationElection']


class AutomaticEarlyTerminationElection(BaseDataClass):
  """
  A class to specify the party elections specific to the Automatic Early Termination Clause.
  """
  isApplicable: bool = Field(..., description="A boolean election to specify whether the Automatic Early Termination provisions of Section 6(a) are applicable (True) or not applicable (False).")
  """
  A boolean election to specify whether the Automatic Early Termination provisions of Section 6(a) are applicable (True) or not applicable (False).
  """
  party: Party = Field(..., description="The party for which the Automatic Early Termination provisions are being specified.")
  """
  The party for which the Automatic Early Termination provisions are being specified.
  """

from cdm.base.staticdata.party.Party import Party

AutomaticEarlyTerminationElection.update_forward_refs()
