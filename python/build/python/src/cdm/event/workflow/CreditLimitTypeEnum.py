from enum import Enum

all = ['CreditLimitTypeEnum']
  
class CreditLimitTypeEnum(Enum):
  """
  The enumeration values to qualify the type of credit limits.
  """
  CS01 = "CS01"
  """
  The type of credit line expressed in CS01. The sensitivity with respect to changes in the CDS spread.
  """
  DV01 = "DV01"
  """
  The type of credit line expressed in DV01. The dollar value of a one basis point decrease in interest rates. It shows the change in a bond's price compared to a decrease in the bond's yield.
  """
  IM = "IM"
  """
  The type of credit line expressed in Initial Margin value.
  """
  NPV = "NPV"
  """
  The type of credit line expressed as a Net Present Value.
  """
  NOTIONAL = "NOTIONAL"
  """
  The type of credit line expressed in Notional amount.
  """
  PV01 = "PV01"
  """
  The type of credit line expressed in PV01. The value of a one dollar or one basis point annuity.
  """
