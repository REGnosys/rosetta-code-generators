from enum import Enum

all = ['UK_EMIR_EligibleCollateralEnum']
  
class UK_EMIR_EligibleCollateralEnum(Enum):
  """
  Identifies United Kingdom Eligible Collateral Assets classification categories based on UK Onshored EMIR Uncleared Margin Rules. Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities. Please note: UK EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM.
  """
  UK_EMIR_TYPE_A = "UK_EMIR_TYPE_A"
  """
  Denotes cash in the form of money credited to an account in any currency, or similar claims for the repayment of money, such as money market deposits.
  """
  UK_EMIR_TYPE_B = "UK_EMIR_TYPE_B"
  """
  Denotes gold in the form of allocated pure gold bullion of recognised good delivery.
  """
  UK_EMIR_TYPE_C = "UK_EMIR_TYPE_C"
  """
  Denotes debt securities issued by the central government of the United Kingdom or the Bank of England.
  """
  UK_EMIR_TYPE_D = "UK_EMIR_TYPE_D"
  """
  Denotes debt securities issued by United Kingdom regional governments or local authorities whose exposures are treated as exposures to the central government of the United Kingdom in accordance with Article 115(2) of Regulation (EU) No 575/2013.
  """
  UK_EMIR_TYPE_E = "UK_EMIR_TYPE_E"
  """
  Denotes debt securities issued by United Kingdom public sector entities whose exposures are treated as exposures to the central government, regional government or local authority of the United Kingdom in accordance with Article 116(4) of Regulation (EU) No 575/2013.
  """
  UK_EMIR_TYPE_F = "UK_EMIR_TYPE_F"
  """
  Denotes debt securities issued by United Kingdom regional governments or local authorities other than those referred to in (TypeD).
  """
  UK_EMIR_TYPE_G = "UK_EMIR_TYPE_G"
  """
  Denotes debt securities issued by United Kingdom public sector entities other than those referred to in (TypeE).
  """
  UK_EMIR_TYPE_H = "UK_EMIR_TYPE_H"
  """
  Denotes debt securities issued by multilateral development banks listed in Article 117(2) of Regulation (EU) No 575/2013.
  """
  UK_EMIR_TYPE_I = "UK_EMIR_TYPE_I"
  """
  Denotes debt securities issued by the international organisations listed in Article 118 of Regulation (EU) No 575/2013.
  """
  UK_EMIR_TYPE_J = "UK_EMIR_TYPE_J"
  """
  Denotes debt securities issued by third countries' governments or central banks.
  """
  UK_EMIR_TYPE_K = "UK_EMIR_TYPE_K"
  """
  Denotes debt securities issued by third countries' regional governments or local authorities that meet the requirements of (TypeD) and (TypeE).
  """
  UK_EMIR_TYPE_L = "UK_EMIR_TYPE_L"
  """
  Denotes debt securities issued by third countries' regional governments or local authorities other than those referred to in (TypeD) and (TypeE).
  """
  UK_EMIR_TYPE_M = "UK_EMIR_TYPE_M"
  """
  Denotes debt securities issued by credit institutions or investment firms including bonds admitted to the register of regulated covered bonds maintained under Regulation 7(1)(b) of the Regulated Covered Bonds Regulations 2008 (SI 2008/346).
  """
  UK_EMIR_TYPE_N = "UK_EMIR_TYPE_N"
  """
  Denotes corporate bonds.
  """
  UK_EMIR_TYPE_O = "UK_EMIR_TYPE_O"
  """
  Denotes the most senior tranche of a securitisation, as defined in Article 4(61) of Regulation (EU) No 575/2013, that is not a re-securitisation as defined in Article 4(63) of that Regulation.
  """
  UK_EMIR_TYPE_P = "UK_EMIR_TYPE_P"
  """
  Denotes convertible bonds provided that they can be converted only into equities which are included in an index specified pursuant to point (a) of Article 197 (8) of Regulation (EU) No 575/2013.
  """
  UK_EMIR_TYPE_Q = "UK_EMIR_TYPE_Q"
  """
  Denotes equities included in an index specified pursuant to point (a) of Article 197(8) of Regulation (EU) No 575/2013.
  """
  UK_EMIR_TYPE_R = "UK_EMIR_TYPE_R"
  """
  Denotes shares or units in undertakings for UK UCITS, provided that the conditions set out in Article 5 of EU Regulation 2016/2251 (as modified by the Technical Standards (European Market Infrastructure) (EU Exit) (No. 3) Instrument 2019) are met.
  """
