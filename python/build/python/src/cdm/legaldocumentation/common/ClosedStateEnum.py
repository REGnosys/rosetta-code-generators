from enum import Enum

all = ['ClosedStateEnum']
  
class ClosedStateEnum(Enum):
  """
  The enumerated values to specify what led to the contract or execution closure.
  """
  ALLOCATED = "ALLOCATED"
  """
  The execution or contract has been allocated.
  """
  CANCELLED = "CANCELLED"
  """
  The execution or contract has been cancelled.
  """
  EXERCISED = "EXERCISED"
  """
  The (option) contract has been exercised.
  """
  EXPIRED = "EXPIRED"
  """
  The (option) contract has expired without being exercised.
  """
  MATURED = "MATURED"
  """
  The contract has reached its contractual termination date.
  """
  NOVATED = "NOVATED"
  """
  The contract has been novated. This state applies to the stepped-out contract component of the novation event.
  """
  TERMINATED = "TERMINATED"
  """
  The contract has been subject of an early termination event.
  """
