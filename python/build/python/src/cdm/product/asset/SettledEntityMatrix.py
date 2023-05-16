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

__all__ = ['SettledEntityMatrix']


class SettledEntityMatrix(BaseDataClass):
  """
  A class to specify the Relevant Settled Entity Matrix.
  """
  matrixSource: AttributeWithMeta[SettledEntityMatrixSourceEnum] | SettledEntityMatrixSourceEnum = Field(..., description="Relevant settled entity matrix source.")
  """
  Relevant settled entity matrix source.
  """
  publicationDate: Optional[date] = Field(None, description="Specifies the publication date of the applicable version of the matrix. When this element is omitted, the Standard Terms Supplement defines rules for which version of the matrix is applicable.")
  """
  Specifies the publication date of the applicable version of the matrix. When this element is omitted, the Standard Terms Supplement defines rules for which version of the matrix is applicable.
  """

from cdm.product.asset.SettledEntityMatrixSourceEnum import SettledEntityMatrixSourceEnum

SettledEntityMatrix.update_forward_refs()
