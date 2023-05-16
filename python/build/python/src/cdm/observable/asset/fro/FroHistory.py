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

__all__ = ['FroHistory']


class FroHistory(BaseDataClass):
  """
  FRO History
  """
  endDate: Optional[date] = Field(None, description="The date the Floating Rate Option was removed from the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. 2014/01/01)")
  """
  The date the Floating Rate Option was removed from the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. 2014/01/01)
  """
  firstDefinedIn: Optional[ContractualDefinition] = Field(None, description="The supplement or version the FRO was first added to the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. S52)")
  """
  The supplement or version the FRO was first added to the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. S52)
  """
  lastUpdateIn: Optional[ContractualDefinition] = Field(None, description="The supplement or version the FRO was last updated in the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. FRO-M-V1)")
  """
  The supplement or version the FRO was last updated in the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. FRO-M-V1)
  """
  startDate: Optional[date] = Field(None, description="The date the Floating Rate Option was added to the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. 2017/04/06)")
  """
  The date the Floating Rate Option was added to the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. 2017/04/06)
  """
  updateDate: Optional[date] = Field(None, description="The date the Floating Rate Option was last updated in the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. 2021/06/11)")
  """
  The date the Floating Rate Option was last updated in the 2006 Definitions or 2021 Floating Rate Matrix. (e.g. 2021/06/11)
  """

from cdm.observable.asset.fro.ContractualDefinition import ContractualDefinition

FroHistory.update_forward_refs()
