from enum import Enum

all = ['DebtClassEnum']
  
class DebtClassEnum(Enum):
  """
  Represents an enumeration list that identifies the type of debt.
  """
  ASSET_BACKED = "ASSET_BACKED"
  """
  Identifies a debt instrument that has periodic income payments and value derived from or backed by a specified pool of underlying assets which could be mortgages or other obligations.
  """
  CONVERTIBLE = "CONVERTIBLE"
  """
  Identifies a debt instrument that can be converted into common shares.
  """
  HOLDER_CONVERTIBLE = "HOLDER_CONVERTIBLE"
  """
  Identifies a debt instrument that can be converted primarily at the election of the holder into common shares of the Issuer.
  """
  HOLDER_EXCHANGEABLE = "HOLDER_EXCHANGEABLE"
  """
  Identifies a debt instrument that can be converted primarily at the election of the holder into common shares of a party other than the Issuer.
  """
  ISSUER_CONVERTIBLE = "ISSUER_CONVERTIBLE"
  """
  Identifies a debt instrument that can be converted at the election of the Issuer into common shares of the Issuer.  Also known as reverse convertible.
  """
  ISSUER_EXCHANGEABLE = "ISSUER_EXCHANGEABLE"
  """
  Identifies a debt instrument that can be converted at the election of the Issuer into common shares of a party other than the Issuer.  Also known as reverse exchangeable.
  """
  REG_CAP = "REG_CAP"
  """
  Identifies a debt instrument as one issued by financial institutions to count towards regulatory capital, including term and perpetual subordinated debt, contingently convertible and others.  Excludes preferred share capital.
  """
  STRUCTURED = "STRUCTURED"
  """
  Identifies a debt instrument athat has non-standard interest or principal features, with full recourse to the issuer.
  """
  VANILLA = "VANILLA"
  """
  Identifies a debt instrument that has a periodic coupon, a defined maturity, and is not backed by any specific asset. The seniority and the structure of the income and principal payments can optionally be defined in DebtType.DebtEconomics.
  """
