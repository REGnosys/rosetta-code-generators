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

__all__ = ['Instruction']


class Instruction(BaseDataClass):
  """
  Instruction to a function that will be used to perform a business event
  """
  before: Optional[AttributeWithReference | TradeState] = Field(None, description="Specifies the trade state that will be acted on by the primitive event functions.")
  """
  Specifies the trade state that will be acted on by the primitive event functions.
  """
  primitiveInstruction: Optional[PrimitiveInstruction] = Field(None, description="Specifies the primitive instructions that will be used to call primitive event functions.")
  """
  Specifies the primitive instructions that will be used to call primitive event functions.
  """
  
  @rosetta_condition
  def condition_0_ExclusiveSplitPrimitive(self):
    """
    A split primitive is exclusive and cannot be combined with other primitives. Instead, the primitive instructions to be applied to each branch of the split must be specified as breakdowns in the split instruction itself.
    """
    def _then_fn0():
      return self.check_one_of_constraint(self, self.primitiveInstruction.split)
    
    def _else_fn0():
      return True
    
    return if_cond_fn(((self.primitiveInstruction.split) is not None), _then_fn0, _else_fn0)
  
  @rosetta_condition
  def condition_1_NewTrade(self):
    """
    There must be no before trade state if the primitive instructions contain an execution, and vice versa. An instruction only handles 1 trade at a time.
    """
    def _then_fn0():
      return ((self.before) is None)
    
    def _else_fn0():
      return True
    
    def _then_fn0():
      return ((self.primitiveInstruction.execution) is not None)
    
    def _else_fn0():
      return True
    
    return (if_cond_fn(((self.primitiveInstruction.execution) is not None), _then_fn0, _else_fn0) and if_cond_fn(((self.before) is None), _then_fn0, _else_fn0))

from cdm.event.common.TradeState import TradeState
from cdm.event.common.PrimitiveInstruction import PrimitiveInstruction

Instruction.update_forward_refs()
