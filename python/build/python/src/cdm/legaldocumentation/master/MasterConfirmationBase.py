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

__all__ = ['MasterConfirmationBase']


class MasterConfirmationBase(BaseDataClass):
  """
  Legal agreement specification for General Terms and Elections that are applicable across multiple confirmations and are referenced by these confirmations.
  """
  pass


MasterConfirmationBase.update_forward_refs()
