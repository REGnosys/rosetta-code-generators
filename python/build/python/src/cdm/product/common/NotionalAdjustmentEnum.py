from enum import Enum

all = ['NotionalAdjustmentEnum']
  
class NotionalAdjustmentEnum(Enum):
  """
  The enumerated values to specify the conditions that govern the adjustment to the number of units of the return swap.
  """
  EXECUTION = "EXECUTION"
  """
  The adjustments to the number of units are governed by an execution clause.
  """
  PORTFOLIO_REBALANCING = "PORTFOLIO_REBALANCING"
  """
  The adjustments to the number of units are governed by a portfolio rebalancing clause.
  """
  STANDARD = "STANDARD"
  """
  The adjustments to the number of units are not governed by any specific clause.
  """
