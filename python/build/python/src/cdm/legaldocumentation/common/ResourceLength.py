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

__all__ = ['ResourceLength']


class ResourceLength(BaseDataClass):
  """
  A class to indicate the length of the resource.
  """
  lengthUnit: LengthUnitEnum = Field(..., description="The length unit of the resource. For example, pages (pdf, text documents) or time (audio, video files).")
  """
  The length unit of the resource. For example, pages (pdf, text documents) or time (audio, video files).
  """
  lengthValue: Decimal = Field(..., description="The length value of the resource.")
  """
  The length value of the resource.
  """

from cdm.legaldocumentation.common.LengthUnitEnum import LengthUnitEnum

ResourceLength.update_forward_refs()
