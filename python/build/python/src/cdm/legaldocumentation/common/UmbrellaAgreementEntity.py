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

__all__ = ['UmbrellaAgreementEntity']

from cdm.base.staticdata.party.LegalEntity import LegalEntity

class UmbrellaAgreementEntity(LegalEntity):
  """
  A class to specify the legal entities that are part of the umbrella agreement.
  """
  terms: Optional[str] = Field(None, description="The terms that might be associated with each party to the umbrella agreement.")
  """
  The terms that might be associated with each party to the umbrella agreement.
  """


UmbrellaAgreementEntity.update_forward_refs()
