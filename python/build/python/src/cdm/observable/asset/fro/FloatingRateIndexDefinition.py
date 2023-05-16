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

__all__ = ['FloatingRateIndexDefinition']


class FloatingRateIndexDefinition(BaseDataClass):
  administrator: Optional[Administrator] = Field(None, description="The administrator for that rate or benchmark or, if there is no administrator, the provider of that rate or benchmark.")
  """
  The administrator for that rate or benchmark or, if there is no administrator, the provider of that rate or benchmark.
  """
  calculationDefaults: Optional[FloatingRateIndexCalculationDefaults] = Field(None, description="Any calculation default values.")
  """
  Any calculation default values.
  """
  definitionalSource: Optional[str] = Field(None, description="The source of an FRO, particularly if not a Contractual Definition (e.g. the broker rates matrix).")
  """
  The source of an FRO, particularly if not a Contractual Definition (e.g. the broker rates matrix).
  """
  deprecationReason: Optional[str] = Field(None, description="Deprecation and Code Descriptions")
  """
  Deprecation and Code Descriptions
  """
  designatedMaturityApplicable: Optional[bool] = Field(None, description="")
  externalMappings: Optional[FloatingRateIndexExternalMappings] = Field(None, description="Any mappings to other codes for this index.")
  """
  Any mappings to other codes for this index.
  """
  fpmlDescription: Optional[str] = Field(None, description="FpML Description")
  """
  FpML Description
  """
  fro: FloatingRateIndexIndentification = Field(..., description="The underlying FRO name and designated maturity.")
  """
  The underlying FRO name and designated maturity.
  """
  history: Optional[FroHistory] = Field(None, description="FRO History")
  """
  FRO History
  """
  inLoan: Optional[bool] = Field(None, description="YES / NO to flag FROs identified by the FpML Syndicated Loan WG as having underlying benchmark that may also be referenced in syndicated loans.")
  """
  YES / NO to flag FROs identified by the FpML Syndicated Loan WG as having underlying benchmark that may also be referenced in syndicated loans.
  """
  mappings: Optional[FloatingRateIndexMappings] = Field(None, description="Any mappings to other FRos.")
  """
  Any mappings to other FRos.
  """
  supportedDefinition: List[ContractualDefinition] = Field([], description="The definition version or versions supported by the FRO.")
  """
  The definition version or versions supported by the FRO.
  """

from cdm.observable.asset.fro.Administrator import Administrator
from cdm.observable.asset.fro.FloatingRateIndexCalculationDefaults import FloatingRateIndexCalculationDefaults
from cdm.observable.asset.fro.FloatingRateIndexExternalMappings import FloatingRateIndexExternalMappings
from cdm.observable.asset.fro.FloatingRateIndexIndentification import FloatingRateIndexIndentification
from cdm.observable.asset.fro.FroHistory import FroHistory
from cdm.observable.asset.fro.FloatingRateIndexMappings import FloatingRateIndexMappings
from cdm.observable.asset.fro.ContractualDefinition import ContractualDefinition

FloatingRateIndexDefinition.update_forward_refs()
