from enum import Enum

all = ['MasterAgreementTypeEnum']
  
class MasterAgreementTypeEnum(Enum):
  """
  The enumerated values to specify the type of the master agreement governing the transaction.
  """
  AFB = "AFB"
  """
  AFB Master Agreement for Foreign Exchange and Derivatives Transactions
  """
  BESPOKE = "BESPOKE"
  """
  A Bespoke (custom) Master Agreement, including one-off agreements for transactions
  """
  CMA = "CMA"
  """
  Clearing Master Agreement
  """
  CMOF = "CMOF"
  """
  Contrato Marco de Operaciones Financieras
  """
  EEI_POWER = "EEI_POWER"
  """
  EEI Master Power Purchase and Sale Agreement
  """
  EFET_ELECTRICITY = "EFET_ELECTRICITY"
  """
  EFET General Agreement Concerning the Delivery and Acceptance of Electricity
  """
  EFET_GAS = "EFET_GAS"
  """
  EFET General Agreement Concerning The Delivery And Acceptance of Natural Gas
  """
  EMA = "EMA"
  """
  European Master Agreement and the Derivatives Annex (Banking Federation of the European Union)
  """
  FBF = "FBF"
  """
  Master Agreement Relating to transactions on Forward Financial Instruments (Federation Bancaire Francaise)
  """
  GMRA = "GMRA"
  """
  ICMA Global Master Agreement for REPO Trades
  """
  GMSLA = "GMSLA"
  """
  ISLA Global Master Agreement for Securities Lending
  """
  GTMA = "GTMA"
  """
  FOA Grid Trade Master Agreement
  """
  GAS_EDI = "GAS_EDI"
  """
  GasEDI Base Contract for Short-term Sale and Purchase of Natural Gas
  """
  GERMAN = "GERMAN"
  """
  German Master Agreement for Financial derivatives and Addendum for Options on Stock Exchange Indices or Securities
  """
  ICOM = "ICOM"
  """
  International Currency Options Market Master Agreement
  """
  IETA_ERPA = "IETA-ERPA"
  """
  International Emissions Trading Association Emissions Reduction Purchase Agreement
  """
  IETA_ETMA = "IETA-ETMA"
  """
  International Emissions Trading Association Emissions Trading Master Agreement
  """
  IETA_IETMA = "IETA-IETMA"
  """
  International Emissions Trading Association International Emissions Trading Master Agreement
  """
  IFEMA = "IFEMA"
  """
  International Foreign Exchange Master Agreement
  """
  IFEOMA = "IFEOMA"
  """
  International Foreign Exchange and Options Master Agreement
  """
  ISDAFIA_CDEA = "ISDAFIA-CDEA"
  """
  ISDA-FIA Cleared Derivatives Execution Agreement
  """
  ISDA_MASTER = "ISDA_MASTER"
  """
  ISDA Master Agreement
  """
  JSCC = "JSCC"
  """
  Master agreement of Japan Securities Clearing Corporation
  """
  LBMA = "LBMA"
  """
  International Bullion Master Agreement Terms published by the London Bullion Market Association
  """
  LEAP = "LEAP"
  """
  Leadership in Energy Automated Processing
  """
  MCPSA = "MCPSA"
  """
  CTA Master Coal Purchase and Sales Agreement
  """
  NAESB_GAS = "NAESB_GAS"
  """
  NAESB Base Contract for Sale and Purchase of Natural Gas
  """
  NBP = "NBP"
  """
  Short Term Flat NBP Trading Terms and Conditions
  """
  RUSSIAN_DERIVATIVES = "RUSSIAN_DERIVATIVES"
  """
  Standard Documentation for Derivative Transactions on the Russian Financial Markets
  """
  RUSSIAN_REPO = "RUSSIAN_REPO"
  """
  Master Agreement and Contractual Terms for Repurchase Agreements on the Russian Financial Market
  """
  S_CO_TA = "S_CO_TA"
  """
  globalCOAL Standard Coal Trading Agreement
  """
  SWISS = "SWISS"
  """
  Swiss Master Agreement for OTC Derivatives Instruments
  """
  TTF = "TTF"
  """
  TTF Hub Natural Gas Trading Terms and Conditions
  """
  ZBT = "ZBT"
  """
  Zeebrugge Hub Natural Gas Trading Terms and Conditions
  """
