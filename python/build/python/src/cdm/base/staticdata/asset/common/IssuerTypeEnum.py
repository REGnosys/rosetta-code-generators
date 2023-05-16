from enum import Enum

all = ['IssuerTypeEnum']
  
class IssuerTypeEnum(Enum):
  """
  Represents an enumeration list to identify the type of entity issuing the asset.
  """
  CORPORATE = "CORPORATE"
  """
  Specifies debt issued Securities by corporate bodies including Banks.
  """
  FUND = "FUND"
  """
  Specifies a vehicle (with or without separate legal personality) designed for the purposes of collective investment towards a defined investment goal.
  """
  QUASI_GOVERNMENT = "QUASI_GOVERNMENT"
  """
  Specifies debt issues by institutions or bodies, typically constituted by statute, with a function mandated by the government and subject to government supervision inclusive of profit- and non-profit making bodies. Includes the US Agencies and GSEs and the EU concept of public sector entities. Excluding any entities which are also Regional Government.
  """
  REGIONAL_GOVERNMENT = "REGIONAL_GOVERNMENT"
  """
  Specifies Regional Government Issued Debt including states within countries, local authorities and municipalities.
  """
  SOVEREIGN_CENTRAL_BANK = "SOVEREIGN_CENTRAL_BANK"
  """
  Specifies Sovereign, Government Debt Securities including Central Banks.
  """
  SPECIAL_PURPOSE_VEHICLE = "SPECIAL_PURPOSE_VEHICLE"
  """
  Specifies a vehicle setup for the purpose of acquisition and financing of specific assets on a limited recourse basis. E.g. asset backed securities, including securitisations.
  """
  SUPRA_NATIONAL = "SUPRA_NATIONAL"
  """
  Specifies debt issued by international organisations and multilateral banks, entities constituted by treaties or with multiple sovereign members includes Multilateral development Banks.
  """
