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

__all__ = ['Knock']


class Knock(BaseDataClass):
  """
  Knock In means option to exercise comes into existence. Knock Out means option to exercise goes out of existence.
  """
  knockIn: Optional[TriggerEvent] = Field(None, description="The knock in.")
  """
  The knock in.
  """
  knockOut: Optional[TriggerEvent] = Field(None, description="The knock out.")
  """
  The knock out.
  """

from cdm.observable.event.TriggerEvent import TriggerEvent

Knock.update_forward_refs()
