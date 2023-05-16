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

__all__ = ['EquityUnderlierProvisions']


class EquityUnderlierProvisions(BaseDataClass):
  componentSecurityIndexAnnexFallback: Optional[bool] = Field(None, description="For an index option or swap transaction, a flag to indicate whether a relevant Component Security Index Annex is applicable to the transaction.")
  """
  For an index option or swap transaction, a flag to indicate whether a relevant Component Security Index Annex is applicable to the transaction.
  """
  localJurisdiction: Optional[AttributeWithMeta[str] | str] = Field(None, description="The ISO 3166 standard code for the country within which the postal address is located.")
  """
  The ISO 3166 standard code for the country within which the postal address is located.
  """
  multipleExchangeIndexAnnexFallback: Optional[bool] = Field(None, description="For an index option or swap transaction, a flag to indicate whether a relevant Multiple Exchange Index Annex is applicable to the transaction. This annex defines additional provisions which are applicable where an index is comprised of component securities that are traded on multiple exchanges.")
  """
  For an index option or swap transaction, a flag to indicate whether a relevant Multiple Exchange Index Annex is applicable to the transaction. This annex defines additional provisions which are applicable where an index is comprised of component securities that are traded on multiple exchanges.
  """
  relevantJurisdiction: Optional[AttributeWithMeta[str] | str] = Field(None, description="The ISO 3166 standard code for the country within which the postal address is located.")
  """
  The ISO 3166 standard code for the country within which the postal address is located.
  """
  
  @rosetta_condition
  def condition_0_ComponentSecurityOrMultipleExchange(self):
    """
    If multipleExchangeIndexAnnexFallback is present then componentSecurityIndexAnnexFallback must be absent and vice versa.
    """
    return self.check_one_of_constraint('multipleExchangeIndexAnnexFallback', 'componentSecurityIndexAnnexFallback', necessity=False)


EquityUnderlierProvisions.update_forward_refs()
