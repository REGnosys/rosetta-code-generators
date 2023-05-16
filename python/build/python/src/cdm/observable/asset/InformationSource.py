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

__all__ = ['InformationSource']


class InformationSource(BaseDataClass):
  """
  A class defining the source for a piece of information (e.g. a rate fix or an FX fixing). The attribute names have been adjusted from FpML to address the fact that the information is not limited to rates.
  """
  sourcePage: Optional[AttributeWithMeta[str] | str] = Field(None, description="A specific page for the source for obtaining a market data point. In FpML, this is specified as a scheme, rateSourcePageScheme, for which no coding Scheme or URI is specified.")
  """
  A specific page for the source for obtaining a market data point. In FpML, this is specified as a scheme, rateSourcePageScheme, for which no coding Scheme or URI is specified.
  """
  sourcePageHeading: Optional[str] = Field(None, description="The heading for the source on a given source page.")
  """
  The heading for the source on a given source page.
  """
  sourceProvider: AttributeWithMeta[InformationProviderEnum] | InformationProviderEnum = Field(..., description="An information source for obtaining a market data point. For example Bloomberg, Reuters, Telerate, etc.")
  """
  An information source for obtaining a market data point. For example Bloomberg, Reuters, Telerate, etc.
  """

from cdm.observable.asset.InformationProviderEnum import InformationProviderEnum

InformationSource.update_forward_refs()
