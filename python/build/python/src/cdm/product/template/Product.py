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

__all__ = ['Product']


class Product(BaseDataClass):
  """
  Defines the product that is the subject of a tradable product definition, an underlying product definition, a physical exercise, a position, or other purposes.
  """
  basket: Optional[Basket] = Field(None, description="Identifies a custom basket by referencing a product identifier and its constituents.")
  """
  Identifies a custom basket by referencing a product identifier and its constituents.
  """
  commodity: Optional[AttributeWithAddress[Commodity] | Commodity] = Field(None, description="Identifies a commodity by referencing a product identifier.")
  """
  Identifies a commodity by referencing a product identifier.
  """
  contractualProduct: Optional[ContractualProduct] = Field(None, description="Specifies the contractual product's economic terms, product identifier, and product taxonomy.")
  """
  Specifies the contractual product's economic terms, product identifier, and product taxonomy.
  """
  foreignExchange: Optional[ForeignExchange] = Field(None, description="Defines a foreign exchange spot or forward transaction.")
  """
  Defines a foreign exchange spot or forward transaction.
  """
  index: Optional[Index] = Field(None, description="Identifies an index by referencing a product identifier.")
  """
  Identifies an index by referencing a product identifier.
  """
  loan: Optional[Loan] = Field(None, description="Identifies a loan by referencing a product identifier and an optional set of attributes.")
  """
  Identifies a loan by referencing a product identifier and an optional set of attributes.
  """
  security: Optional[Security] = Field(None, description="Identifies a security by referencing a product identifier and a security type, plus an optional set of attributes.")
  """
  Identifies a security by referencing a product identifier and a security type, plus an optional set of attributes.
  """
  
  @rosetta_condition
  def condition_0_(self):
    return self.check_one_of_constraint('contractualProduct', 'index', 'loan', 'foreignExchange', 'commodity', 'security', 'basket', necessity=True)

from cdm.product.template.Basket import Basket
from cdm.base.staticdata.asset.common.Commodity import Commodity
from cdm.product.template.ContractualProduct import ContractualProduct
from cdm.product.asset.ForeignExchange import ForeignExchange
from cdm.base.staticdata.asset.common.Index import Index
from cdm.base.staticdata.asset.common.Loan import Loan
from cdm.base.staticdata.asset.common.Security import Security

Product.update_forward_refs()
