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

__all__ = ['Equity']

from cdm.base.staticdata.asset.common.IdentifiedProduct import IdentifiedProduct

class Equity(IdentifiedProduct):
  """
  A class to specify an equity as having a product identifier. As a difference versus the FpML standard, the CDM structure of this class only includes the productIdentifier class, which consists of an identifier, productTaxonomy, and source of the identifier. The reason for this approach is to avoid the potential for conflicting information between the information associated with the contractual product and the reference information maintained by the relevant service provider.
  """
  pass


Equity.update_forward_refs()
