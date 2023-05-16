from enum import Enum

all = ['EU_EMIR_EligibleCollateralEnum']
  
class EU_EMIR_EligibleCollateralEnum(Enum):
  """
  Identifies European Union Eligible Collateral Assets classification categories based on EMIR Uncleared Margin Rules. Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities. Please note: EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM.
  """
  EU_EMIR_TYPE_A = "EU_EMIR_TYPE_A"
  """
  Denotes Cash in the form of money credited to an account in any currency, or similar claims for the repayment of money, such as money market deposits.
  """
  EU_EMIR_TYPE_B = "EU_EMIR_TYPE_B"
  """
   Denotes gold in the form of allocated pure gold bullion of recognised good delivery.
  """
  EU_EMIR_TYPE_C = "EU_EMIR_TYPE_C"
  """
   Denotes debt securities issued by Member States' central governments or central banks.
  """
  EU_EMIR_TYPE_D = "EU_EMIR_TYPE_D"
  """
   Denotes debt securities issued by Member States' regional governments or local authorities whose exposures are treated as exposures to the central government of that Member State in accordance with Article 115(2) of Regulation (EU) No 575/2013.
  """
  EU_EMIR_TYPE_E = "EU_EMIR_TYPE_E"
  """
   Denotes debt securities issued by Member States' public sector entities whose exposures are treated as exposures to the central government, regional government or local authority of that Member State in accordance with Article 116(4) of Regulation (EU) No 575/2013.
  """
  EU_EMIR_TYPE_F = "EU_EMIR_TYPE_F"
  """
   Denotes debt securities issued by Member States' regional governments or local authorities other than those referred to in (TypeD.)
  """
  EU_EMIR_TYPE_G = "EU_EMIR_TYPE_G"
  """
   Denotes debt securities issued by Member States' public sector entities other than those referred to in (TypeE).
  """
  EU_EMIR_TYPE_H = "EU_EMIR_TYPE_H"
  """
   Denotes debt securities issued by multilateral development banks listed in Article 117(2) of Regulation (EU) No 575/2013.
  """
  EU_EMIR_TYPE_I = "EU_EMIR_TYPE_I"
  """
   Denotes debt securities issued by the international organisations listed in Article 118 of Regulation (EU) No 575/2013.
  """
  EU_EMIR_TYPE_J = "EU_EMIR_TYPE_J"
  """
   Denotes debt securities issued by third countries' governments or central banks.
  """
  EU_EMIR_TYPE_K = "EU_EMIR_TYPE_K"
  """
   Denotes debt securities issued by third countries' regional governments or local authorities that meet the requirements of (TypeD) and (TypeE).
  """
  EU_EMIR_TYPE_L = "EU_EMIR_TYPE_L"
  """
   Denotes debt securities issued by third countries' regional governments or local authorities other than those referred to in (TypeD) and (TypeE).
  """
  EU_EMIR_TYPE_M = "EU_EMIR_TYPE_M"
  """
   Denotes debt securities issued by credit institutions or investment firms including bonds referred to in Article 52(4) of Directive 2009/65/EC of the European Parliament and of the Council.
  """
  EU_EMIR_TYPE_N = "EU_EMIR_TYPE_N"
  """
   Denotes corporate bonds.
  """
  EU_EMIR_TYPE_O = "EU_EMIR_TYPE_O"
  """
   Denotes the most senior tranche of a securitisation, as defined in Article 4(61) of Regulation (EU) No 575/2013, that is not a re-securitisation as defined in Article 4(63) of that Regulation.
  """
  EU_EMIR_TYPE_P = "EU_EMIR_TYPE_P"
  """
   Denotes convertible bonds provided that they can be converted only into equities which are included in an index specified pursuant to point (a) of Article 197 (8) of Regulation (EU) No 575/2013.
  """
  EU_EMIR_TYPE_Q = "EU_EMIR_TYPE_Q"
  """
   Denotes equities included in an index specified pursuant to point (a) of Article 197(8) of Regulation (EU) No 575/2013.
  """
  EU_EMIR_TYPE_R = "EU_EMIR_TYPE_R"
  """
   Denotes shares or units in undertakings for collective investments in transferable securities (UCITS), provided that the conditions set out in Article 5 of EU Regulation 2016/2251 are met.
  """
