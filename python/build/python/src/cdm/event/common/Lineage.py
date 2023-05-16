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

__all__ = ['Lineage']


class Lineage(BaseDataClass):
  """
  A class to provide lineage information across lifecycle events through a pointer or set of pointers into the event(s), contract(s) and, possibly, payout components that the event is dependent on or relates to. As an example, if an contractFormation event is corrected, the correction event will have a lineage into the initial event, which takes the form of a globalKey into that initial contract formation event. Two referencing mechanisms are provided as part of the CDM: either the globalKey, which corresponds to the hash value of the CDM class which is referred to, or a reference qualifier which is meant to provide support for the ingestion of xml documents with id/href mechanisms. The CDM recommends the use of the globalKey and provides a default implementation which is accessible in the generated code through org.isda.cdm.globalKey.GlobalKeyHashCalculator. If implementers want to use an alternative hashing mechanism, the API in which they need to plug it is com.rosetta.model.lib.HashFunction.
  """
  eventReference: List[AttributeWithReference | WorkflowStep] = Field([], description="The reference to the instantiation of an Event object, either through a globalKey or an xml-derived id/href mechanism. The definition associated to the Lineage class provides more details with respect to those referencing approaches, their expected usage and available implementation.")
  """
  The reference to the instantiation of an Event object, either through a globalKey or an xml-derived id/href mechanism. The definition associated to the Lineage class provides more details with respect to those referencing approaches, their expected usage and available implementation.
  """
  portfolioStateReference: List[AttributeWithReference | PortfolioState] = Field([], description="The reference to the previous state of a Portfolio, in a chain of Events leading up to a build of that Portfolio as the holding of Product(s) in specific Quantity(ies). As part of the PortfolioState object, a pointer to the previous PortfolioState is provided through a Lineage object, together with pointer(s) to the Event or set of Events leading up to the current (new) state.")
  """
  The reference to the previous state of a Portfolio, in a chain of Events leading up to a build of that Portfolio as the holding of Product(s) in specific Quantity(ies). As part of the PortfolioState object, a pointer to the previous PortfolioState is provided through a Lineage object, together with pointer(s) to the Event or set of Events leading up to the current (new) state.
  """
  tradeReference: List[AttributeWithReference | Trade] = Field([], description="")

from cdm.event.workflow.WorkflowStep import WorkflowStep
from cdm.event.position.PortfolioState import PortfolioState
from cdm.event.common.Trade import Trade

Lineage.update_forward_refs()
