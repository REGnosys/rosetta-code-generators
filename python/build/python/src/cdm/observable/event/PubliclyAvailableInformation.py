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

__all__ = ['PubliclyAvailableInformation']


class PubliclyAvailableInformation(BaseDataClass):
  publicSource: List[str] = Field([], description="A public information source, e.g. a particular newspaper or electronic news service, that may publish relevant information used in the determination of whether or not a credit event has occurred. ISDA 2003 Term: Public Source.")
  """
  A public information source, e.g. a particular newspaper or electronic news service, that may publish relevant information used in the determination of whether or not a credit event has occurred. ISDA 2003 Term: Public Source.
  """
  specifiedNumber: Optional[int] = Field(None, description="The minimum number of the specified public information sources that must publish information that reasonably confirms that a credit event has occurred. The market convention is two. ISDA 2003 Term: Specified Number.")
  """
  The minimum number of the specified public information sources that must publish information that reasonably confirms that a credit event has occurred. The market convention is two. ISDA 2003 Term: Specified Number.
  """
  standardPublicSources: Optional[bool] = Field(None, description="If this element is specified and set to 'true', indicates that ISDA defined Standard Public Sources are applicable.")
  """
  If this element is specified and set to 'true', indicates that ISDA defined Standard Public Sources are applicable.
  """
  
  @rosetta_condition
  def condition_0_SourceChoice(self):
    """
     FpML validation rule cd-36 - Context: PubliclyAvailableInformation (complex type). Either standardPublicSources or at least one publicSource element must exist.
    """
    return self.check_one_of_constraint('standardPublicSources', 'publicSource', necessity=True)
  
  @rosetta_condition
  def condition_1_PositiveSpecifiedNumber(self):
    """
     FpML specifies specifiedNumber as a positiveInteger.
    """
    def _then_fn0():
      return all_elements(self.specifiedNumber, ">=", 0)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.specifiedNumber) is not None), _then_fn0, _else_fn0)


PubliclyAvailableInformation.update_forward_refs()
