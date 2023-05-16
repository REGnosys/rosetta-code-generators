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

__all__ = ['IndexReferenceInformation']


class IndexReferenceInformation(BaseDataClass):
  """
  A class defining a Credit Default Swap Index.
  """
  excludedReferenceEntity: List[ReferenceInformation] = Field([], description="Excluded reference entity.")
  """
  Excluded reference entity.
  """
  indexAnnexDate: Optional[date] = Field(None, description="A CDS index series annex date.")
  """
  A CDS index series annex date.
  """
  indexAnnexSource: Optional[AttributeWithMeta[IndexAnnexSourceEnum] | IndexAnnexSourceEnum] = Field(None, description="A CDS index series annex source.")
  """
  A CDS index series annex source.
  """
  indexAnnexVersion: Optional[int] = Field(None, description="A CDS index series version identifier, e.g. 1, 2, 3 etc.")
  """
  A CDS index series version identifier, e.g. 1, 2, 3 etc.
  """
  indexFactor: Optional[Decimal] = Field(None, description="Index Factor is the index version factor or percent, expressed as an absolute decimal value between 0 and 1, that multiplied by the original notional amount yields the notional amount covered by the seller of protection.")
  """
  Index Factor is the index version factor or percent, expressed as an absolute decimal value between 0 and 1, that multiplied by the original notional amount yields the notional amount covered by the seller of protection.
  """
  indexId: List[AttributeWithMeta[str] | str] = Field([], description="A CDS index identifier (e.g. RED pair code).")
  """
  A CDS index identifier (e.g. RED pair code).
  """
  indexName: Optional[AttributeWithMeta[str] | str] = Field(None, description="The name of the index expressed as a free format string with an associated scheme.")
  """
  The name of the index expressed as a free format string with an associated scheme.
  """
  indexSeries: Optional[int] = Field(None, description="A CDS index series identifier, e.g. 1, 2, 3 etc.")
  """
  A CDS index series identifier, e.g. 1, 2, 3 etc.
  """
  seniority: Optional[CreditSeniorityEnum] = Field(None, description="Seniority of debt instruments comprising the index.")
  """
  Seniority of debt instruments comprising the index.
  """
  settledEntityMatrix: Optional[SettledEntityMatrix] = Field(None, description="Used to specify the Relevant Settled Entity Matrix when there are settled entities at the time of the trade.")
  """
  Used to specify the Relevant Settled Entity Matrix when there are settled entities at the time of the trade.
  """
  tranche: Optional[Tranche] = Field(None, description="This element contains CDS tranche terms.")
  """
  This element contains CDS tranche terms.
  """
  
  @rosetta_condition
  def condition_0_IndexSeries(self):
    """
    FpML specifies the type associated to indexSeries as a positive integer.
    """
    def _then_fn0():
      return all_elements(self.indexSeries, ">=", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.indexSeries) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_IndexAnnexVersion(self):
    """
    FpML specifies the type associated to indexVersion as a positive integer.
    """
    def _then_fn0():
      return all_elements(self.indexAnnexVersion, ">=", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.indexAnnexVersion) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_2_IndexFactor(self):
    """
    Index factor is expressed as a decimal and should be a positive number between o and 1.
    """
    def _then_fn0():
      return (all_elements(self.indexFactor, ">=", 0) and all_elements(self.indexFactor, "<=", 1))
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.indexFactor) is not None), _then_fn0, _else_fn0)

from cdm.product.asset.ReferenceInformation import ReferenceInformation
from cdm.product.asset.IndexAnnexSourceEnum import IndexAnnexSourceEnum
from cdm.product.asset.CreditSeniorityEnum import CreditSeniorityEnum
from cdm.product.asset.SettledEntityMatrix import SettledEntityMatrix
from cdm.product.asset.Tranche import Tranche

IndexReferenceInformation.update_forward_refs()
