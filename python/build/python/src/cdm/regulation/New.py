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

__all__ = ['New']


class New(BaseDataClass):
  addtlAttrbts: AddtlAttrbts = Field(..., description="")
  buyr: Buyr = Field(..., description="")
  exctgPrsn: ExctgPrsn = Field(..., description="")
  exctgPty: str = Field(..., description="")
  finInstrm: FinInstrm = Field(..., description="")
  invstmtDcsnPrsn: InvstmtDcsnPrsn = Field(..., description="")
  invstmtPtyInd: str = Field(..., description="")
  ordrTrnsmssn: OrdrTrnsmssn = Field(..., description="")
  sellr: Sellr = Field(..., description="")
  submitgPty: str = Field(..., description="")
  tx: Tx = Field(..., description="")
  txId: str = Field(..., description="")

from cdm.regulation.AddtlAttrbts import AddtlAttrbts
from cdm.regulation.Buyr import Buyr
from cdm.regulation.ExctgPrsn import ExctgPrsn
from cdm.regulation.FinInstrm import FinInstrm
from cdm.regulation.InvstmtDcsnPrsn import InvstmtDcsnPrsn
from cdm.regulation.OrdrTrnsmssn import OrdrTrnsmssn
from cdm.regulation.Sellr import Sellr
from cdm.regulation.Tx import Tx

New.update_forward_refs()
