from enum import Enum

all = ['CollateralAssetDefinitionsEnum']
  
class CollateralAssetDefinitionsEnum(Enum):
  """
  The ISDA Collateral Assets Definitions as published by ISDA in the 2003 ISDA Collateral Asset Definitions.
  """
  AU_CASH = "AU_CASH"
  """
  Australian Dollar (AUD) Cash.
  """
  AU_CIB = "AU-CIB"
  """
  Australian Government Securities Capital-Indexed Bonds.
  """
  AU_FIB = "AU-FIB"
  """
  Australian Semi-Government Securities Fixed Interest Bonds.
  """
  AU_FRB = "AU-FRB"
  """
  Australian Government Securities Fixed Rate Bonds.
  """
  AU_ILB = "AU-ILB"
  """
  Australian Semi-Government Securities Index Linked Bonds.
  """
  AU_NOTE = "AU-NOTE"
  """
  Australian Government Securities Treasury Notes.
  """
  AU_STATENOTE = "AU-STATENOTE"
  """
  Australian Semi-Government Securities Treasury Notes.
  """
  AU_TAB = "AU-TAB"
  """
  Australian Government Securities Treasury Adjustable Rate Bonds.
  """
  BE_BEL20 = "BE-BEL20"
  """
  BEL20 Equity Securities.
  """
  BE_CERT = "BE-CERT"
  """
  Belgian Treasury Certificates.
  """
  BE_LINEAR = "BE-LINEAR"
  """
  Belgian Linear Obligations.
  """
  BE_NOTE = "BE-NOTE"
  """
  Belgian Treasury notes.
  """
  BE_REGIONGT = "BE-REGIONGT"
  """
  Public sector issues guaranteed by Regional Authorities.
  """
  BE_STATEGT = "BE-STATEGT"
  """
  Public sector issues guaranteed by the Belgian State.
  """
  BE_STATELOAN = "BE-STATELOAN"
  """
  Belgian State Loans.
  """
  CA_BOND = "CA-BOND"
  """
  Canada Bonds.
  """
  CA_CASH = "CA-CASH"
  """
  Canadian Dollar (CAD) Cash.
  """
  CA_RRB = "CA-RRB"
  """
  Government of Canada Real Return Bonds.
  """
  CA_TBILL = "CA-TBILL"
  """
  Government of Canada Treasury Bills.
  """
  CH_CANTON = "CH-CANTON"
  """
  Public Authority Bond.
  """
  CH_CASH = "CH-CASH"
  """
  Swiss Franc (CHF) Cash.
  """
  CH_FEDBOND = "CH-FEDBOND"
  """
  Federal Bond.
  """
  DE_BILL = "DE-BILL"
  """
  Unverzinsliche Schatzanweisungen (Bills).
  """
  DE_BOND = "DE-BOND"
  """
  Bundesanleihen (Bonds).
  """
  DE_ERBLAST = "DE-ERBLAST"
  """
  Negotiable Debt Obligations issued by or taken over and since serviced and managed by the Erblasttilgungsfond (Redemption Fund for Inherited Liabilities) backed by Federal Republic of Germany, including but not limited to former issues of the Treuhandanstalt, the Bundesbahn, the Bundespost, the Economic Recovery Program (ERP), the privatised Federal Railway (Bahn AG), the telecommunications element of the Federal Post Office (Telekom) and the German Unity Fund.
  """
  DE_MUNI = "DE-MUNI"
  """
  Kommunalschuldverschreib  ungen (Municipal Bonds).
  """
  DE_NOTE2 = "DE-NOTE2"
  """
  Bundesschatzanweisungen (Notes).
  """
  DE_NOTE5_5 = "DE-NOTE5.5"
  """
  Bundesobligationen (Notes).
  """
  DE_PFAND = "DE-PFAND"
  """
  Hypothekenpfandbriefe (Mortgage Bonds).
  """
  DK_BILL = "DK-BILL"
  """
  Skatkammerbeviser (Treasury Bills).
  """
  DK_BOLIGX = "DK-BOLIGX"
  """
  BoligX obligationer.
  """
  DK_BOND = "DK-BOND"
  """
  Statsobligationer (Government Bonds).
  """
  DK_CALLMORT = "DK-CALLMORT"
  """
  Callable Mortgage Bonds.
  """
  DK_CASH = "DK-CASH"
  """
  Danish Krone (DKK) Cash.
  """
  DK_KFX = "DK-KFX"
  """
  KFX Equity Securities.
  """
  DK_MORT = "DK-MORT"
  """
  Non-callable Mortgage Bonds.
  """
  DK_NOTE = "DK-NOTE"
  """
  Statsgaeldsbeviser (Treasury Notes).
  """
  ES_BILL = "ES-BILL"
  """
  Treasury Bills - Letras del Tesoro.
  """
  ES_BOND = "ES-BOND"
  """
  Public Government Debt.
  """
  ES_CEDULAS = "ES-CEDULAS"
  """
  Cedulas.
  """
  ES_CORP = "ES-CORP"
  """
  Corporate Bonds.
  """
  ES_EQUITY = "ES-EQUITY"
  """
  Equity securities issued by a Spanish company, and listed as an IBEX 35 constituent company as reported by the Sociedad de Bolsas, each share representing the minimum unit of participation of a shareholder in the stock capital of the company.
  """
  EU_CASH = "EU-CASH"
  """
  Euro (EUR) Cash.
  """
  EU_EURO100 = "EU-EURO100"
  """
  FTSE Euro 100 Index Equity Securities.
  """
  EU_EUROTOP300 = "EU-EUROTOP300"
  """
  FTSE Eurotop 300 Index Equity Securities.
  """
  EU_STOXX50 = "EU-STOXX50"
  """
  EuroSTOXX 50 Index Equity Securities.
  """
  EU_STOXX600 = "EU-STOXX600"
  """
  STOXX 600 Index Equity Securities.
  """
  FI_BILL = "FI-BILL"
  """
  Treasury bills.
  """
  FI_BOND = "FI-BOND"
  """
  Serial bonds (Finnish Government Bond).
  """
  FI_HEX = "FI-HEX"
  """
  HEX Equity Securities.
  """
  FR_BDT = "FR-BDT"
  """
  Commercial Paper: (Billet de Trésorerie).
  """
  FR_BTAN = "FR-BTAN"
  """
  Treasury Notes: Bons du Trésor à Taux Annuel (BTAN).
  """
  FR_BTF = "FR-BTF"
  """
  Treasury Bills: Bons du Trésor à Taux Fixe (BTF).
  """
  FR_OAT = "FR-OAT"
  """
  Government bonds: Obligations Assimilables du Trésor (OAT).
  """
  FR_STRIP = "FR-STRIP"
  """
  STRIPS.
  """
  GA_AU_GOV = "GA-AU-GOV"
  """
  Generally Accepted Australian Government Obligations.
  """
  GA_BE_GOV = "GA-BE-GOV"
  """
  Generally Accepted Belgian Government Obligations.
  """
  GA_CA_GOV = "GA-CA-GOV"
  """
  Generally Accepted Canadian Government Obligations.
  """
  GA_CH_GOV = "GA-CH-GOV"
  """
  Generally Accepted Swiss Government Obligations.
  """
  GA_DE_GOV = "GA-DE-GOV"
  """
  Generally Accepted German Government Obligations.
  """
  GA_DK_GOV = "GA-DK-GOV"
  """
  Generally Accepted Danish Government Obligations.
  """
  GA_ES_GOV = "GA-ES-GOV"
  """
  Generally Accepted Spanish Government Obligations.
  """
  GA_EUROZONE_GOV = "GA-EUROZONE-GOV"
  """
  Generally Accepted Euro Zone Government Securities.
  """
  GA_EU_GOV = "GA-EU-GOV"
  """
  Generally Accepted EU Member State Government Securities.
  """
  GA_FI_GOV = "GA-FI-GOV"
  """
  Generally Accepted Finnish Government Obligations.
  """
  GA_FR_GOV = "GA-FR-GOV"
  """
  Generally Accepted French Government Obligations.
  """
  GA_G5_GOV = "GA-G5-GOV"
  """
  Generally Accepted G5 Government Obligations.
  """
  GA_GB_GOV = "GA-GB-GOV"
  """
  Generally Accepted British Government Obligations.
  """
  GA_HK_GOV = "GA-HK-GOV"
  """
  Generally Accepted Hong Kong Government Obligations.
  """
  GA_IT_GOV = "GA-IT-GOV"
  """
  Generally Accepted Italian Government Obligations.
  """
  GA_JP_GOV = "GA-JP-GOV"
  """
  Generally Accepted Japanese Government Obligations.
  """
  GA_KR_GOV = "GA-KR-GOV"
  """
  Generally Accepted Korean Government Obligations.
  """
  GA_NL_GOV = "GA-NL-GOV"
  """
  Generally Accepted Netherlands Government Obligations.
  """
  GA_NO_GOV = "GA-NO-GOV"
  """
  Generally Accepted Norwegian Government Obligations.
  """
  GA_NZ_GOV = "GA-NZ-GOV"
  """
  Generally Accepted New Zealand Government Obligations.
  """
  GA_SE_GOV = "GA-SE-GOV"
  """
  Generally Accepted Swedish Government Obligations.
  """
  GA_SG_GOV = "GA-SG-GOV"
  """
  Generally Accepted Singaporean Government Obligations.
  """
  GA_US_AGENCY = "GA-US-AGENCY"
  """
  Generally Accepted US Agency Obligations.
  """
  GA_US_GOV = "GA-US-GOV"
  """
  Generally Accepted US Government Obligations.
  """
  GA_US_MORTGAGES = "GA-US-MORTGAGES"
  """
  Generally Accepted US Mortgage-Backed Obligations.
  """
  GB_CASH = "GB-CASH"
  """
  British Pound Sterling (GBP) Cash.
  """
  GB_DDGILT = "GB-DDGILT"
  """
  Double-dated Gilts.
  """
  GB_FT100 = "GB-FT100"
  """
  FTSE 100 Equity Securities.
  """
  GB_FT250 = "GB-FT250"
  """
  FTSE 250 Equity Securities.
  """
  GB_FT350 = "GB-FT350"
  """
  FTSE 350 Equity Securities.
  """
  GB_GILT = "GB-GILT"
  """
  Conventional Gilts.
  """
  GB_INDEXGILT = "GB-INDEXGILT"
  """
  Index-Linked Gilts.
  """
  GB_PERPGILT = "GB-PERPGILT"
  """
  Undated or Perpetual Gilts.
  """
  GB_RUMPGILT = "GB-RUMPGILT"
  """
  Rump Stock.
  """
  GB_SUPR1 = "GB-SUPR1"
  """
  Bank of England Euro Bills.
  """
  GB_SUPR2 = "GB-SUPR2"
  """
  Bank of England Euro Notes.
  """
  GB_TBILL = "GB-TBILL"
  """
  UK Treasury Bills.
  """
  GB_ZEROGILT = "GB-ZEROGILT"
  """
  Gilt Strips or Zero Coupon Gilts.
  """
  HK_BILL = "HK-BILL"
  """
  Hong Kong Government Exchange Fund Bills.
  """
  HK_CASH = "HK-CASH"
  """
  Hong Kong Dollar (HKD) Cash.
  """
  HK_NOTE = "HK-NOTE"
  """
  Hong Kong Government Exchange Fund Notes.
  """
  IT_BOT = "IT-BOT"
  """
  Botbuoni Ordinari del Tesoro (BOT) zero coupon debt securities issued by the Italian Treasury with maturities up to 365 days.
  """
  IT_BTP = "IT-BTP"
  """
  Buoni del Tesoro Poliennali fixed interest semi-annual debt securities issued by the Italian Treasury with original maturities between 3 and 30 years.
  """
  IT_CCT = "IT-CCT"
  """
  Certificati di Credito del Tesoro a Cedola Variable (CCT) or floating rate interest bearing debt securities issued by the Italian Treasury.
  """
  IT_CORP = "IT-CORP"
  """
  Corporate bonds.
  """
  IT_CTZ = "IT-CTZ"
  """
  Certificati del Tesoro zero coupon debt securities issued by the Italian Treasury with maturities between 18 and 24 months.
  """
  IT_MIB30 = "IT-MIB30"
  """
  MIB30 Equity Securities.
  """
  IT_REP = "IT-REP"
  """
  Debt securities issued and marketed by the Republic of Italy outside the Italian market, traded as Eurobonds.
  """
  JP_CASH = "JP-CASH"
  """
  Japanese Yen (JPY) Cash.
  """
  JP_CORPORATE = "JP-CORPORATE"
  """
  Corporate bonds including straight bonds.
  """
  JP_CP = "JP-CP"
  """
  Commercial Paper.
  """
  JP_EQUITY = "JP-EQUITY"
  """
  Equity securities issued by a Japanese company, each share representing the minimum unit of participation of a partner in the stock capital of the company.
  """
  JP_EUROBOND = "JP-EUROBOND"
  """
  Yen-denominated foreign bonds.
  """
  JP_JGB = "JP-JGB"
  """
  Japanese Government Bonds.
  """
  KR_BOND = "KR-BOND"
  """
  Korean Treasury Bonds.
  """
  KR_CASH = "KR-CASH"
  """
  Korean Won (KRW) Cash.
  """
  KR_EXIM = "KR-EXIM"
  """
  Non Korean Won denominated Export-Import Bank of Korea bonds.
  """
  KR_KDICKRW = "KR-KDICKRW"
  """
  Korean Development Insurance Corporation Bonds (Korean Won denominated).
  """
  KR_KDR = "KR-KDR"
  """
  Non-Korean Won denominated Korea Development Bank bonds (KDBs).
  """
  KR_KEPCO = "KR-KEPCO"
  """
  KEPCO bonds.
  """
  KR_MSB = "KR-MSB"
  """
  Monetary Stabilisation Bonds.
  """
  KR_NHC = "KR-NHC"
  """
  Non Korean Won denominated Korea National Housing Corporation bonds (KNHCs).
  """
  KR_ROK = "KR-ROK"
  """
  Non-Korean Won denominated Republic of Korea bonds (ROKs).
  """
  NL_AEX = "NL-AEX"
  """
  AEX Equity Securities.
  """
  NL_BILL = "NL-BILL"
  """
  Dutch Treasury Certificates.
  """
  NL_BOND = "NL-BOND"
  """
  Dutch State Loans.
  """
  NO_BOND = "NO-BOND"
  """
  Norwegian Government Bonds.
  """
  NO_CASH = "NO-CASH"
  """
  Norwegian Krone (NOK) Cash.
  """
  NO_OBX = "NO-OBX"
  """
  OBX Equity Securities.
  """
  NO_TBILL = "NO-TBILL"
  """
  Norwegian T-Bills.
  """
  NZ_BOND = "NZ-BOND"
  """
  New Zealand Government Bonds.
  """
  NZ_CASH = "NZ-CASH"
  """
  New Zealand Dollar (NZD) Cash.
  """
  NZ_TBILL = "NZ-TBILL"
  """
  New Zealand Government Treasury Bills.
  """
  SE_CASH = "SE-CASH"
  """
  Swedish Krona (SEK) Cash.
  """
  SE_GOVT = "SE-GOVT"
  """
  Swedish Government Bonds (SGB).
  """
  SE_ILGOVT = "SE-ILGOVT"
  """
  Swedish Index Linked Government bonds.
  """
  SE_MORT = "SE-MORT"
  """
  Swedish Mortgage Bonds.
  """
  SE_OMX = "SE-OMX"
  """
  OMX Equity Securities.
  """
  SE_TBILL = "SE-TBILL"
  """
  Swedish Treasury Bills (STB).
  """
  SG_BOND = "SG-BOND"
  """
  Singapore Government (SGS) Bonds.
  """
  SG_CASH = "SG-CASH"
  """
  Singapore Dollar (SGD) Cash.
  """
  SG_TBILL = "SG-TBILL"
  """
  Singapore Government T-Bills (T-Bills).
  """
  SU_IADB = "SU-IADB"
  """
  Inter-American Development Bank Bonds.
  """
  SU_IBRDDN = "SU-IBRDDN"
  """
  International Bank for Reconstruction and Development (World Bank) Discount Notes.
  """
  SU_IBRDGB = "SU-IBRDGB"
  """
  International Bank for Reconstruction and Development (World Bank or IBRD) Global Benchmark Bonds.
  """
  US_ARM = "US-ARM"
  """
  Adjustable Rate Mortgage (ARM) Bonds.
  """
  US_CASH = "US-CASH"
  """
  United States of America Dollar (USD) Cash.
  """
  US_DERIV = "US-DERIV"
  """
  REMICs, CMOs and other derivative structures.
  """
  US_DOW = "US-DOW"
  """
  Dow Jones Industrial Average Equity Securities.
  """
  US_DOW_COMP = "US-DOW-COMP"
  """
  Dow Jones Composite Average Equity Securities.
  """
  US_DOW_TRAN = "US-DOW-TRAN"
  """
  Dow Jones Transportation  Average Equity Securities.
  """
  US_DOW_UTIL = "US-DOW-UTIL"
  """
  Dow Jones Utilities Average Equity Securities.
  """
  US_FAMC = "US-FAMC"
  """
  Federal Agricultural Mortgage Corp (Farmer Mac) Bonds.
  """
  US_FCS = "US-FCS"
  """
  Farm Credit System (FCS) Bonds.
  """
  US_FCSFAC = "US-FCSFAC"
  """
  Farm Credit System Financial Assistance Corporation (FCSFAC) Bonds.
  """
  US_FHLB = "US-FHLB"
  """
  Callable Agency Debt – Federal Home Loan Bank (FHLB).
  """
  US_FHLBNC = "US-FHLBNC"
  """
  Non-Callable Federal Home Loan Bank Debt.
  """
  US_FHLBNCDN = "US-FHLBNCDN"
  """
  Non-Callable Federal Home Loan Bank Discount Notes.
  """
  US_FHLMC = "US-FHLMC"
  """
  Callable Agency Debt – the Federal Home Loan Mortgage Corporation (FHLMC or Freddie Mac).
  """
  US_FHLMCMBS = "US-FHLMCMBS"
  """
  Federal Home Loan Mortgage Corporation Certificates – Mortgage Backed Securities.
  """
  US_FICO = "US-FICO"
  """
  Financing Corp (FICO) Bonds.
  """
  US_FNMA = "US-FNMA"
  """
  Callable Agency Debt – Federal National Mortgage Association (FNMA or Fannie Mae).
  """
  US_FNMAMBS = "US-FNMAMBS"
  """
  Federal National Mortgage Association Certificates – Mortgage Backed Securities.
  """
  US_GNMA = "US-GNMA"
  """
  Callable Agency Debt – Government National Mortgage Association (GNMA).
  """
  US_GNMAMBS = "US-GNMAMBS"
  """
  Government National Mortgage Association Certificates – Mortgage Backed Securities (GNMA or Ginnie Mae)
  """
  US_LEHM_BOND = "US-LEHM-BOND"
  """
  Lehman Brothers Credit Bond Index Debt Securities.
  """
  US_NAS_100 = "US-NAS-100"
  """
  NASDAQ-100 Index Equity Securities.
  """
  US_NAS_COMP = "US-NAS-COMP"
  """
  NASDAQ Composite Index Equity Securities.
  """
  US_NCAD = "US-NCAD"
  """
  Non-Callable Agency Debt – Various Issuers.
  """
  US_NCADN = "US-NCADN"
  """
  Non-Callable Agency Discount Notes – Various Issuers.
  """
  US_NYSE_COMP = "US-NYSE-COMP"
  """
  NYSE Composite Index Equity Securities.
  """
  US_REFCORP = "US-REFCORP"
  """
  Resolution Funding Corp (REFCorp) Bonds.
  """
  US_SLMA = "US-SLMA"
  """
  Student Loan Marketing Association (Sallie Mae) Bonds.
  """
  US_STRIP = "US-STRIP"
  """
  US Treasury Strips.
  """
  US_S_P100 = "US-S&P100"
  """
  Standard & Poor’s 100 Index Equity Securities.
  """
  US_S_P400 = "US-S&P400"
  """
  Standard & Poor’s Midcap 400 Equity Securities. corporations that are included within the Standard And Poor's Midcap 400 Index published by Standard And Poor's, a division of The McGraw-Hill Companies, Inc.
  """
  US_S_P500 = "US-S&P500"
  """
  Standard & Poor’s 500 Index Equity Securities.
  """
  US_S_P600 = "US-S&P600"
  """
  Standard & Poor’s Smallcap 600 Index Equity Securities.
  """
  US_TBILL = "US-TBILL"
  """
  US Treasury Bills.
  """
  US_TBOND = "US-TBOND"
  """
  US Treasury Bonds.
  """
  US_TIPS = "US-TIPS"
  """
  US Treasury Inflation Protected Issues (TIPS).
  """
  US_TNOTE = "US-TNOTE"
  """
  US Treasury Notes.
  """
  US_TVA = "US-TVA"
  """
  Tennessee Valley Authority (TVA) Bonds.
  """
