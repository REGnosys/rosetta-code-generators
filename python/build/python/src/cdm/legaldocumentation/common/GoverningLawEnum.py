from enum import Enum

all = ['GoverningLawEnum']
  
class GoverningLawEnum(Enum):
  """
  The enumerated values to specify the law governing the contract or legal document.
  """
  AS_SPECIFIED_IN_MASTER_AGREEMENT = "AS_SPECIFIED_IN_MASTER_AGREEMENT"
  """
  The Governing Law is determined by reference to the relevant master agreement.
  """
  BE = "BE"
  """
  Belgian law
  """
  CAAB = "CAAB"
  """
  Alberta law
  """
  CABC = "CABC"
  """
  British Columbia Law
  """
  CAMN = "CAMN"
  """
  Manitoba law
  """
  CAON = "CAON"
  """
  Ontario law
  """
  CAQC = "CAQC"
  """
  Quebec law
  """
  DE = "DE"
  """
  German law
  """
  FR = "FR"
  """
  French law
  """
  GBEN = "GBEN"
  """
  English law
  """
  GBGY = "GBGY"
  """
  The law of the island of Guernsey
  """
  GBIM = "GBIM"
  """
  The law of the Isle of Man
  """
  GBJY = "GBJY"
  """
  The law of the island of Jersey
  """
  GBSC = "GBSC"
  """
  Scottish law
  """
  IE = "IE"
  """
  Irish law
  """
  JP = "JP"
  """
  Japanese law
  """
  LU = "LU"
  """
  Luxembourg law
  """
  RELATED_MASTER_AGREEMENT = "RELATED_MASTER_AGREEMENT"
  """
  As agreed in the ISDA Master Agreement
  """
  USCA = "USCA"
  """
  Californian law
  """
  USDE = "USDE"
  """
  Delaware law
  """
  USIL = "USIL"
  """
  Illinois law
  """
  USNY = "USNY"
  """
  New York law
  """
