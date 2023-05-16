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

__all__ = ['Observable']


class Observable(BaseDataClass):
  """
  Specifies the object to be observed for a price, it could be an asset or a reference.
  """
  commodity: Optional[AttributeWithMeta[Commodity] | Commodity] = Field(None, description="Identifies a commodity by referencing a product identifier.")
  """
  Identifies a commodity by referencing a product identifier.
  """
  currencyPair: Optional[AttributeWithMeta[QuotedCurrencyPair] | QuotedCurrencyPair] = Field(None, description="Describes the composition of a rate that has been quoted or is to be quoted, including the two currencies and the quotation relationship between the two currencies.")
  """
  Describes the composition of a rate that has been quoted or is to be quoted, including the two currencies and the quotation relationship between the two currencies.
  """
  optionReferenceType: Optional[OptionReferenceTypeEnum] = Field(None, description="The underlying contract which is referenced when determining the final settlement price of the instrument. Eg. Rolling Front Month Future; Spot etc.")
  """
  The underlying contract which is referenced when determining the final settlement price of the instrument. Eg. Rolling Front Month Future; Spot etc.
  """
  productIdentifier: List[AttributeWithMeta[ProductIdentifier] | ProductIdentifier] = Field([], description="Comprises of an identifier and a source. The associated metadata key denotes the ability to associate a hash value to the ProductIdentifier instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage.")
  """
  Comprises of an identifier and a source. The associated metadata key denotes the ability to associate a hash value to the ProductIdentifier instantiations for the purpose of model cross-referencing, in support of functionality such as the event effect and the lineage.
  """
  rateOption: Optional[AttributeWithMeta[FloatingRateOption] | FloatingRateOption] = Field(None, description="Specifies a floating rate index and tenor.")
  """
  Specifies a floating rate index and tenor.
  """
  
  @rosetta_condition
  def condition_0_ObservableChoice(self):
    """
    An observable can only be composed of one type any time.
    """
    return self.check_one_of_constraint('rateOption', 'commodity', 'productIdentifier', 'currencyPair', necessity=True)

from cdm.base.staticdata.asset.common.Commodity import Commodity
from cdm.observable.asset.QuotedCurrencyPair import QuotedCurrencyPair
from cdm.observable.asset.OptionReferenceTypeEnum import OptionReferenceTypeEnum
from cdm.base.staticdata.asset.common.ProductIdentifier import ProductIdentifier
from cdm.observable.asset.FloatingRateOption import FloatingRateOption

Observable.update_forward_refs()
