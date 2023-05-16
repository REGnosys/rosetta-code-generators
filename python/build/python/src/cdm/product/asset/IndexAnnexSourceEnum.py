from enum import Enum

all = ['IndexAnnexSourceEnum']
  
class IndexAnnexSourceEnum(Enum):
  """
  The enumerated values to specify the CDX index annex source.
  """
  MASTER_CONFIRMATION = "MASTER_CONFIRMATION"
  """
  As defined in the relevant form of Master Confirmation applicable to the confirmation of Dow Jones CDX indices.
  """
  PUBLISHER = "PUBLISHER"
  """
  As defined in the relevant form of Master Confirmation applicable to the confirmation of Dow Jones CDX indices.
  """
