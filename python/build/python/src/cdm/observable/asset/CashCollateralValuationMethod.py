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

__all__ = ['CashCollateralValuationMethod']


class CashCollateralValuationMethod(BaseDataClass):
  """
  This type is a generic structure that can represent the parameters of several mid-market valuation and replacement value methods described in the 2021 ISDA Definitions.
  """
  agreedDiscountRate: Optional[AttributeWithMeta[str] | str] = Field(None, description="This may be used to indicate the discount rate to be used for cash collateral for cash settlement purposes.")
  """
  This may be used to indicate the discount rate to be used for cash collateral for cash settlement purposes.
  """
  applicableCsa: Optional[CsaTypeEnum] = Field(None, description="This may be used to specify what type of CSA (credit support annex/agreement) is to be used for cash settlement purposes.")
  """
  This may be used to specify what type of CSA (credit support annex/agreement) is to be used for cash settlement purposes.
  """
  cashCollateralCurrency: Optional[str] = Field(None, description="This may be used to indicate the currency of cash collateral for cash settlement purposes.")
  """
  This may be used to indicate the currency of cash collateral for cash settlement purposes.
  """
  cashCollateralInterestRate: Optional[AttributeWithMeta[str] | str] = Field(None, description="This may be used to indicate the interest rate to be used for cash collateral for cash settlement purposes.")
  """
  This may be used to indicate the interest rate to be used for cash collateral for cash settlement purposes.
  """
  prescribedDocumentationAdjustment: Optional[bool] = Field(None, description="This may be used to indicate that 'prescribed documentation adjustment' is applicable.")
  """
  This may be used to indicate that 'prescribed documentation adjustment' is applicable.
  """
  protectedParty: List[PartyDeterminationEnum] = Field([], description="This may be used to specify which party is protected (e.g. under Replacement Value cash settlement methods).")
  """
  This may be used to specify which party is protected (e.g. under Replacement Value cash settlement methods).
  """
  @rosetta_condition
  def cardinality_protectedParty(self):
    return check_cardinality(self.protectedParty, 0, 2)
  

from cdm.observable.asset.CsaTypeEnum import CsaTypeEnum
from cdm.observable.asset.PartyDeterminationEnum import PartyDeterminationEnum

CashCollateralValuationMethod.update_forward_refs()
