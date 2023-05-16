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

__all__ = ['PartialExercise']


class PartialExercise(BaseDataClass):
  """
  A class defining partial exercise. As defined in the 2000 ISDA Definitions, Section 12.3 Partial Exercise, the buyer of the option may exercise all or less than all the notional amount of the underlying swap but may not be less than the minimum notional amount (if specified) and must be an integral multiple of the integral multiple amount if specified.
  """
  integralMultipleAmount: Optional[Decimal] = Field(None, description="A notional amount which restricts the amount of notional that can be exercised when partial exercise or multiple exercise is applicable. The integral multiple amount defines a lower limit of notional that can be exercised and also defines a unit multiple of notional that can be exercised, i.e. only integer multiples of this amount can be exercised.")
  """
  A notional amount which restricts the amount of notional that can be exercised when partial exercise or multiple exercise is applicable. The integral multiple amount defines a lower limit of notional that can be exercised and also defines a unit multiple of notional that can be exercised, i.e. only integer multiples of this amount can be exercised.
  """
  minimumNotionalAmount: Optional[Decimal] = Field(None, description="The minimum notional amount that can be exercised on a given exercise date. See multipleExercise.")
  """
  The minimum notional amount that can be exercised on a given exercise date. See multipleExercise.
  """
  minimumNumberOfOptions: Optional[int] = Field(None, description="The minimum number of options that can be exercised on a given exercise date.")
  """
  The minimum number of options that can be exercised on a given exercise date.
  """
  notionaReference: AttributeWithReference | Money = Field(..., description="A pointer style reference to the associated notional schedule defined elsewhere in the document. This element has been made optional as part of its integration in the OptionBaseExtended, because not required for the options on securities.")
  """
  A pointer style reference to the associated notional schedule defined elsewhere in the document. This element has been made optional as part of its integration in the OptionBaseExtended, because not required for the options on securities.
  """
  
  @rosetta_condition
  def condition_0_MinimumChoice(self):
    """
    Choice rule to represent an FpML choice construct.
    """
    return self.check_one_of_constraint('minimumNotionalAmount', 'minimumNumberOfOptions', necessity=True)

from cdm.observable.asset.Money import Money

PartialExercise.update_forward_refs()
