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

__all__ = ['ContractualMatrix']


class ContractualMatrix(BaseDataClass):
  matrixTerm: Optional[AttributeWithMeta[MatrixTermEnum] | MatrixTermEnum] = Field(None, description="Defines any applicable key into the relevant matrix. For example, the Transaction Type would be the single term required for the Credit Derivatives Physical Settlement Matrix. This element should be omitted in the case of the 2000 ISDA Definitions Settlement Matrix for Early Termination and Swaptions.")
  """
  Defines any applicable key into the relevant matrix. For example, the Transaction Type would be the single term required for the Credit Derivatives Physical Settlement Matrix. This element should be omitted in the case of the 2000 ISDA Definitions Settlement Matrix for Early Termination and Swaptions.
  """
  matrixType: AttributeWithMeta[MatrixTypeEnum] | MatrixTypeEnum = Field(..., description="Identifies the form of applicable matrix.")
  """
  Identifies the form of applicable matrix.
  """

from cdm.legaldocumentation.common.MatrixTermEnum import MatrixTermEnum
from cdm.legaldocumentation.common.MatrixTypeEnum import MatrixTypeEnum

ContractualMatrix.update_forward_refs()
