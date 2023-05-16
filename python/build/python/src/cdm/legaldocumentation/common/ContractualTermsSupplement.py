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

__all__ = ['ContractualTermsSupplement']


class ContractualTermsSupplement(BaseDataClass):
  """
  A contractual supplement (such as those published by ISDA) and its publication date that will apply to the trade.
  """
  contractualTermsSupplementType: AttributeWithMeta[ContractualSupplementTypeEnum] | ContractualSupplementTypeEnum = Field(..., description="Identifies the form of applicable contractual supplement.")
  """
  Identifies the form of applicable contractual supplement.
  """
  publicationDate: Optional[date] = Field(None, description="Specifies the publication date of the applicable version of the contractual supplement.")
  """
  Specifies the publication date of the applicable version of the contractual supplement.
  """

from cdm.legaldocumentation.common.ContractualSupplementTypeEnum import ContractualSupplementTypeEnum

ContractualTermsSupplement.update_forward_refs()
