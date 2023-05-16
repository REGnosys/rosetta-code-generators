from enum import Enum

all = ['ExerciseNoticeGiverEnum']
  
class ExerciseNoticeGiverEnum(Enum):
  """
  Defines the principal party to the trade that has the right to exercise.
  """
  AS_SPECIFIED_IN_MASTER_AGREEMENT = "AS_SPECIFIED_IN_MASTER_AGREEMENT"
  """
  Specifies that the Master Agreement defines the principal party to the trade that has the right to exercise.
  """
  BOTH = "BOTH"
  """
  Specifies that both the option buyer and option seller has the right to exercise.
  """
  BUYER = "BUYER"
  """
  Specifies that only the option buyer has the right to exercise.
  """
  SELLER = "SELLER"
  """
  Specifies that only the option seller has the right to exercise.
  """
