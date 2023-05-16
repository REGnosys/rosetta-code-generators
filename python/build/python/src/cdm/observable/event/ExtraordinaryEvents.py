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

__all__ = ['ExtraordinaryEvents']


class ExtraordinaryEvents(BaseDataClass):
  """
  Where the underlying is shares, defines market events affecting the issuer of those shares that may require the terms of the transaction to be adjusted.
  """
  additionalDisruptionEvents: Optional[AdditionalDisruptionEvents] = Field(None, description="2002 ISDA Equity Derivatives Definitions: Additional Disruption Events | 2018 ISDA CDM Equity Confirmation for Security Equity Swap: Additional Disruption Events means each Additional Disruption Event specified in the Confirmation Side Letter. For the avoidance of doubt, each Additional Disruption Event shall be an Extraordinary Event.")
  """
  2002 ISDA Equity Derivatives Definitions: Additional Disruption Events | 2018 ISDA CDM Equity Confirmation for Security Equity Swap: Additional Disruption Events means each Additional Disruption Event specified in the Confirmation Side Letter. For the avoidance of doubt, each Additional Disruption Event shall be an Extraordinary Event.
  """
  compositionOfCombinedConsideration: Optional[bool] = Field(None, description="2002 ISDA Equity Derivatives Definitions: Composition of Combined Consideration | 2018 ISDA CDM Equity Confirmation for Security Equity Swap: Combined Consideration | If present and true, then composition of combined consideration is applicable.")
  """
  2002 ISDA Equity Derivatives Definitions: Composition of Combined Consideration | 2018 ISDA CDM Equity Confirmation for Security Equity Swap: Combined Consideration | If present and true, then composition of combined consideration is applicable.
  """
  delisting: Optional[NationalizationOrInsolvencyOrDelistingEventEnum] = Field(None, description="2002 ISDA Equity Derivatives Definitions: Delisting | 2018 ISDA CDM Equity Confirmation for Security Equity Swap: Delisting means Delisting (Broad Relisting) or Delisting (Narrow Relisting), as specified in the Relationship Supplement.")
  """
  2002 ISDA Equity Derivatives Definitions: Delisting | 2018 ISDA CDM Equity Confirmation for Security Equity Swap: Delisting means Delisting (Broad Relisting) or Delisting (Narrow Relisting), as specified in the Relationship Supplement.
  """
  failureToDeliver: Optional[bool] = Field(None, description="If true, failure to deliver is applicable.")
  """
  If true, failure to deliver is applicable.
  """
  indexAdjustmentEvents: Optional[IndexAdjustmentEvents] = Field(None, description="2002 ISDA Equity Derivatives Definitions: Adjustments to Indices | ")
  """
  2002 ISDA Equity Derivatives Definitions: Adjustments to Indices | 
  """
  mergerEvents: Optional[EquityCorporateEvents] = Field(None, description="2018 ISDA CDM Equity Confirmation for Security Equity Swap: Merger Event shall occur if a Merger occurs and the Merger Date is on or before the final Equity Valuation Date | Occurs when the underlying ceases to exist following a merger between the Issuer and another company.")
  """
  2018 ISDA CDM Equity Confirmation for Security Equity Swap: Merger Event shall occur if a Merger occurs and the Merger Date is on or before the final Equity Valuation Date | Occurs when the underlying ceases to exist following a merger between the Issuer and another company.
  """
  nationalizationOrInsolvency: Optional[NationalizationOrInsolvencyOrDelistingEventEnum] = Field(None, description="2002 ISDA Equity Derivatives Definitions: Nationalization and Insolvency | 2018 ISDA CDM Equity Confirmation for Security Equity Swap: Nationalization shall occur if all the Securities or all or substantially all the assets of an Issuer are nationalized, expropriated or are otherwise required to be transferred to any governmental agency, authority, entity or instrumentality thereof. Insolvency Filing means as defined in the Confirmation Side Letter.")
  """
  2002 ISDA Equity Derivatives Definitions: Nationalization and Insolvency | 2018 ISDA CDM Equity Confirmation for Security Equity Swap: Nationalization shall occur if all the Securities or all or substantially all the assets of an Issuer are nationalized, expropriated or are otherwise required to be transferred to any governmental agency, authority, entity or instrumentality thereof. Insolvency Filing means as defined in the Confirmation Side Letter.
  """
  representations: Optional[Representations] = Field(None, description="")
  tenderOfferEvents: Optional[EquityCorporateEvents] = Field(None, description="2002 ISDA Equity Derivatives Definitions: Tender Offers | 2018 ISDA CDM Equity Confirmation for Security Equity Swap: Tender Offer Event")
  """
  2002 ISDA Equity Derivatives Definitions: Tender Offers | 2018 ISDA CDM Equity Confirmation for Security Equity Swap: Tender Offer Event
  """
  
  @rosetta_condition
  def condition_0_ExtraordinaryEventsChoice(self):
    """
    condition to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('additionalDisruptionEvents', 'failureToDeliver', necessity=True)

from cdm.observable.event.AdditionalDisruptionEvents import AdditionalDisruptionEvents
from cdm.observable.event.NationalizationOrInsolvencyOrDelistingEventEnum import NationalizationOrInsolvencyOrDelistingEventEnum
from cdm.observable.event.IndexAdjustmentEvents import IndexAdjustmentEvents
from cdm.observable.event.EquityCorporateEvents import EquityCorporateEvents
from cdm.observable.event.Representations import Representations

ExtraordinaryEvents.update_forward_refs()
