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

__all__ = ['DebtEconomics']


class DebtEconomics(BaseDataClass):
  """
  Specifies selected economics of a debt instrument.
  """
  debtInterest: Optional[DebtInterestEnum] = Field(None, description="Specifies the general rule for periodic interest rate payment.")
  """
  Specifies the general rule for periodic interest rate payment.
  """
  debtPrincipal: Optional[DebtPrincipalEnum] = Field(None, description="Specifies the general rule for repayment of principal.")
  """
  Specifies the general rule for repayment of principal.
  """
  debtSeniority: Optional[DebtSeniorityEnum] = Field(None, description="Specifies the order of repayment in the event of a sale or bankruptcy of the issuer or a related party (eg guarantor).")
  """
  Specifies the order of repayment in the event of a sale or bankruptcy of the issuer or a related party (eg guarantor).
  """

from cdm.base.staticdata.asset.common.DebtInterestEnum import DebtInterestEnum
from cdm.base.staticdata.asset.common.DebtPrincipalEnum import DebtPrincipalEnum
from cdm.base.staticdata.asset.common.DebtSeniorityEnum import DebtSeniorityEnum

DebtEconomics.update_forward_refs()
