from enum import Enum

all = ['FloatingRateIndexEnum']
  
class FloatingRateIndexEnum(Enum):
  """
  The enumerated values to specify the list of floating rate index.
  """
  AED_EBOR_REUTERS = "AED-EBOR-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AED_EIBOR = "AED-EIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  AUD_AONIA = "AUD-AONIA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_AONIA_OIS_COMPOUND = "AUD-AONIA-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_AONIA_OIS_COMPOUND_SWAP_MARKER = "AUD-AONIA-OIS-COMPOUND-SwapMarker"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_AONIA_OIS_COMPOUND_1 = "AUD-AONIA-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  AUD_BBR_AUBBSW = "AUD-BBR-AUBBSW"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_BBR_BBSW = "AUD-BBR-BBSW"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_BBR_BBSW_BLOOMBERG = "AUD-BBR-BBSW-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_BBR_BBSY__BID_ = "AUD-BBR-BBSY (BID)"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_BBR_ISDC = "AUD-BBR-ISDC"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_BBSW = "AUD-BBSW"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  AUD_BBSW_QUARTERLY_SWAP_RATE_ICAP = "AUD-BBSW Quarterly Swap Rate ICAP"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  AUD_BBSW_SEMI_ANNUAL_SWAP_RATE_ICAP = "AUD-BBSW Semi Annual Swap Rate ICAP"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  AUD_BBSY_BID = "AUD-BBSY Bid"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  AUD_LIBOR_BBA = "AUD-LIBOR-BBA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_LIBOR_BBA_BLOOMBERG = "AUD-LIBOR-BBA-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_LIBOR_REFERENCE_BANKS = "AUD-LIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_QUARTERLY_SWAP_RATE_ICAP = "AUD-Quarterly Swap Rate-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_QUARTERLY_SWAP_RATE_ICAP_REFERENCE_BANKS = "AUD-Quarterly Swap Rate-ICAP-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_SEMI_ANNUAL_SWAP_RATE_11_00_BGCANTOR = "AUD-Semi-Annual Swap Rate-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_SEMI_ANNUAL_SWAP_RATE_BGCANTOR_REFERENCE_BANKS = "AUD-Semi-Annual Swap Rate-BGCANTOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_SEMI_ANNUAL_SWAP_RATE_ICAP_REFERENCE_BANKS = "AUD-Semi-Annual Swap Rate-ICAP-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_SEMI_ANNUAL_SWAP_RATE_ICAP = "AUD-Semi-annual Swap Rate-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  AUD_SWAP_RATE_REUTERS = "AUD-Swap Rate-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  BRL_CDI = "BRL-CDI"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CAD_BA_CDOR = "CAD-BA-CDOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_BA_CDOR_BLOOMBERG = "CAD-BA-CDOR-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_BA_ISDD = "CAD-BA-ISDD"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_BA_REFERENCE_BANKS = "CAD-BA-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_BA_REUTERS = "CAD-BA-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_BA_TELERATE = "CAD-BA-Telerate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_CDOR = "CAD-CDOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CAD_CORRA = "CAD-CORRA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_CORRA_OIS_COMPOUND = "CAD-CORRA-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_CORRA_OIS_COMPOUND_1 = "CAD-CORRA-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CAD_ISDA_SWAP_RATE = "CAD-ISDA-Swap Rate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_LIBOR_BBA = "CAD-LIBOR-BBA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_LIBOR_BBA_BLOOMBERG = "CAD-LIBOR-BBA-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_LIBOR_BBA_SWAP_MARKER = "CAD-LIBOR-BBA-SwapMarker"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_LIBOR_REFERENCE_BANKS = "CAD-LIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_REPO_CORRA = "CAD-REPO-CORRA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_TBILL_ISDD = "CAD-TBILL-ISDD"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_TBILL_REFERENCE_BANKS = "CAD-TBILL-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_TBILL_REUTERS = "CAD-TBILL-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CAD_TBILL_TELERATE = "CAD-TBILL-Telerate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_3_M_LIBOR_SWAP_CME_VS_LCH_ICAP = "CHF-3M LIBOR SWAP-CME vs LCH-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_3_M_LIBOR_SWAP_CME_VS_LCH_ICAP_BLOOMBERG = "CHF-3M LIBOR SWAP-CME vs LCH-ICAP-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_3_M_LIBOR_SWAP_EUREX_VS_LCH_ICAP = "CHF-3M LIBOR SWAP-EUREX vs LCH-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_3_M_LIBOR_SWAP_EUREX_VS_LCH_ICAP_BLOOMBERG = "CHF-3M LIBOR SWAP-EUREX vs LCH-ICAP-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_6_M_LIBORSWAP_CME_VS_LCH_ICAP_BLOOMBERG = "CHF-6M LIBORSWAP-CME vs LCH-ICAP-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_6_M_LIBOR_SWAP_CME_VS_LCH_ICAP = "CHF-6M LIBOR SWAP-CME vs LCH-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_6_M_LIBOR_SWAP_EUREX_VS_LCH_ICAP = "CHF-6M LIBOR SWAP-EUREX vs LCH-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_6_M_LIBOR_SWAP_EUREX_VS_LCH_ICAP_BLOOMBERG = "CHF-6M LIBOR SWAP-EUREX vs LCH-ICAP-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_ANNUAL_SWAP_RATE = "CHF-Annual Swap Rate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_ANNUAL_SWAP_RATE_11_00_ICAP = "CHF-Annual Swap Rate-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "CHF-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_BASIS_SWAP_3_M_VS_6_M_LIBOR_11_00_ICAP = "CHF-Basis Swap-3m vs 6m-LIBOR-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_ISDAFIX_SWAP_RATE = "CHF-ISDAFIX-Swap Rate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_LIBOR = "CHF-LIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CHF_LIBOR_BBA = "CHF-LIBOR-BBA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_LIBOR_BBA_BLOOMBERG = "CHF-LIBOR-BBA-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_LIBOR_ISDA = "CHF-LIBOR-ISDA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_LIBOR_REFERENCE_BANKS = "CHF-LIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_OIS_11_00_ICAP = "CHF-OIS-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_SARON = "CHF-SARON"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_SARON_OIS_COMPOUND = "CHF-SARON-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_SARON_OIS_COMPOUND_1 = "CHF-SARON-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CHF_TOIS_OIS_COMPOUND = "CHF-TOIS-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CHF_USD_BASIS_SWAPS_11_00_ICAP = "CHF USD-Basis Swaps-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CLP_ICP = "CLP-ICP"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CLP_TNA = "CLP-TNA"
  """
  Refers to the Indice Camara Promedio ('ICP') rate for Chilean Pesos which, for a Reset Date, is determined and published by the Asociacion de Bancos e Instituciones Financieras de Chile A.G. ('ABIF') in accordance with the 'Reglamento Indice de Camara Promedio' of the ABIF as published in the Diario Oficial de la Republica de Chile (the 'ICP Rules') and which is reported on the ABIF website by not later than 10:00 a.m., Santiago time, on that Reset Date.
  """
  CL_CLICP_BLOOMBERG = "CL-CLICP-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CNH_HIBOR = "CNH-HIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CNH_HIBOR_REFERENCE_BANKS = "CNH-HIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CNH_HIBOR_TMA = "CNH-HIBOR-TMA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CNY_7_REPO_COMPOUNDING_DATE = "CNY 7-Repo Compounding Date"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CNY_CNREPOFIX_CFXS_REUTERS = "CNY-CNREPOFIX=CFXS-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CNY_DEPOSIT_RATE = "CNY-Deposit Rate"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CNY_FIXING_REPO_RATE = "CNY-Fixing Repo Rate"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CNY_LPR = "CNY-LPR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CNY_PBOCB_REUTERS = "CNY-PBOCB-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CNY_QUARTERLY_7_D_REPO_NDS_RATE_TRADITION = "CNY-Quarterly 7D Repo NDS Rate Tradition"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CNY_QUARTERLY_7_DAY_REPO_NON_DELIVERABLE_SWAP_RATE_TRADITION = "CNY-Quarterly 7 day Repo Non Deliverable Swap Rate-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CNY_QUARTERLY_7_DAY_REPO_NON_DELIVERABLE_SWAP_RATE_TRADITION_REFERENCE_BANKS = "CNY-Quarterly 7 day Repo Non Deliverable Swap Rate-TRADITION-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CNY_SHIBOR = "CNY-SHIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CNY_SHIBOR_OIS_COMPOUND = "CNY-SHIBOR-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CNY_SHIBOR_REUTERS = "CNY-SHIBOR-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction..
  """
  CNY_SEMI_ANNUAL_SWAP_RATE_11_00_BGCANTOR = "CNY-Semi-Annual Swap Rate-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CNY_SEMI_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "CNY-Semi-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CNY_SHIBOR_OIS_COMPOUNDING = "CNY-Shibor-OIS-Compounding"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  COP_IBR_OIS_COMPOUND = "COP-IBR-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  COP_IBR_OIS_COMPOUND_1 = "COP-IBR-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CZK_ANNUAL_SWAP_RATE_11_00_BGCANTOR = "CZK-Annual Swap Rate-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CZK_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "CZK-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CZK_CZEONIA = "CZK-CZEONIA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CZK_CZEONIA_OIS_COMPOUND = "CZK-CZEONIA-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CZK_PRIBOR = "CZK-PRIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  CZK_PRIBOR_PRBO = "CZK-PRIBOR-PRBO"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  CZK_PRIBOR_REFERENCE_BANKS = "CZK-PRIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  DKK_CIBOR = "DKK-CIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  DKK_CIBOR2 = "DKK-CIBOR2"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  DKK_CIBOR_2_BLOOMBERG = "DKK-CIBOR2-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  DKK_CIBOR2_DKNA13 = "DKK-CIBOR2-DKNA13"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  DKK_CIBOR_DKNA13 = "DKK-CIBOR-DKNA13"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  DKK_CIBOR_DKNA_13_BLOOMBERG = "DKK-CIBOR-DKNA13-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  DKK_CIBOR_REFERENCE_BANKS = "DKK-CIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  DKK_CITA = "DKK-CITA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  DKK_CITA_DKNA14_COMPOUND = "DKK-CITA-DKNA14-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  DKK_DESTR = "DKK-DESTR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  DKK_DESTR_COMPOUNDED_INDEX = "DKK-DESTR Compounded Index"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  DKK_DESTR_OIS_COMPOUND = "DKK-DESTR-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  DKK_DKKOIS_OIS_COMPOUND = "DKK-DKKOIS-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  DKK_TOM_NEXT_OIS_COMPOUND = "DKK-Tom Next-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  EUR_3_M_EURIBOR_SWAP_CME_VS_LCH_ICAP = "EUR-3M EURIBOR SWAP-CME vs LCH-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_3_M_EURIBOR_SWAP_CME_VS_LCH_ICAP_BLOOMBERG = "EUR-3M EURIBOR SWAP-CME vs LCH-ICAP-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_3_M_EURIBOR_SWAP_EUREX_VS_LCH_ICAP = "EUR-3M EURIBOR SWAP-EUREX vs LCH-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_3_M_EURIBOR_SWAP_EUREX_VS_LCH_ICAP_BLOOMBERG = "EUR-3M EURIBOR SWAP-EUREX vs LCH-ICAP-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_6_M_EURIBOR_SWAP_CME_VS_LCH_ICAP = "EUR-6M EURIBOR SWAP-CME vs LCH-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_6_M_EURIBOR_SWAP_CME_VS_LCH_ICAP_BLOOMBERG = "EUR-6M EURIBOR SWAP-CME vs LCH-ICAP-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_6_M_EURIBOR_SWAP_EUREX_VS_LCH_ICAP = "EUR-6M EURIBOR SWAP-EUREX vs LCH-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_6_M_EURIBOR_SWAP_EUREX_VS_LCH_ICAP_BLOOMBERG = "EUR-6M EURIBOR SWAP-EUREX vs LCH-ICAP-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ANNUAL_SWAP_RATE_10_00 = "EUR-Annual Swap Rate-10:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ANNUAL_SWAP_RATE_10_00_BGCANTOR = "EUR-Annual Swap Rate-10:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ANNUAL_SWAP_RATE_10_00_BLOOMBERG = "EUR-Annual Swap Rate-10:00-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ANNUAL_SWAP_RATE_10_00_ICAP = "EUR-Annual Swap Rate-10:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ANNUAL_SWAP_RATE_10_00_SWAP_MARKER = "EUR-Annual Swap Rate-10:00-SwapMarker"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ANNUAL_SWAP_RATE_10_00_TRADITION = "EUR-Annual Swap Rate-10:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ANNUAL_SWAP_RATE_11_00 = "EUR-Annual Swap Rate-11:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ANNUAL_SWAP_RATE_11_00_BLOOMBERG = "EUR-Annual Swap Rate-11:00-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ANNUAL_SWAP_RATE_11_00_ICAP = "EUR-Annual Swap Rate-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ANNUAL_SWAP_RATE_11_00_SWAP_MARKER = "EUR-Annual Swap Rate-11:00-SwapMarker"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ANNUAL_SWAP_RATE_3_MONTH = "EUR-Annual Swap Rate-3 Month"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ANNUAL_SWAP_RATE_3_MONTH_SWAP_MARKER = "EUR-Annual Swap Rate-3 Month-SwapMarker"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ANNUAL_SWAP_RATE_4_15_TRADITION = "EUR-Annual Swap Rate-4:15-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "EUR-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_BASIS_SWAP_EONIA_VS_3_M_EUR_IBOR_SWAP_RATES_A_360_10_00_ICAP = "EUR Basis Swap-EONIA vs 3m EUR+IBOR Swap Rates-A/360-10:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_CNO_TEC10 = "EUR-CNO TEC10"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  EUR_EONIA = "EUR-EONIA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  EUR_EONIA_AVERAGE_1 = "EUR-EONIA-AVERAGE"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EONIA_AVERAGE = "EUR-EONIA-Average"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  EUR_EONIA_OIS_10_00_BGCANTOR = "EUR-EONIA-OIS-10:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EONIA_OIS_10_00_ICAP = "EUR-EONIA-OIS-10:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EONIA_OIS_10_00_TRADITION = "EUR-EONIA-OIS-10:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EONIA_OIS_11_00_ICAP = "EUR-EONIA-OIS-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EONIA_OIS_4_15_TRADITION = "EUR-EONIA-OIS-4:15-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EONIA_OIS_COMPOUND = "EUR-EONIA-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EONIA_OIS_COMPOUND_BLOOMBERG = "EUR-EONIA-OIS-COMPOUND-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EONIA_OIS_COMPOUND_1 = "EUR-EONIA-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  EUR_EONIA_SWAP_INDEX = "EUR-EONIA-Swap-Index"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURIBOR = "EUR-EURIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  EUR_EURIBOR_ACT_365 = "EUR-EURIBOR-Act/365"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURIBOR_ACT_365_BLOOMBERG = "EUR-EURIBOR-Act/365-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURIBOR_ANNUAL_BOND_SWAP_VS_1_M_11_00_ICAP = "EUR EURIBOR-Annual Bond Swap vs 1m-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURIBOR_BASIS_SWAP_1_M_VS_3_M_EURIBOR_11_00_ICAP = "EUR EURIBOR-Basis Swap-1m vs 3m-Euribor-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURIBOR_BASIS_SWAP_3_M_VS_6_M_11_00_ICAP = "EUR EURIBOR-Basis Swap-3m vs 6m-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURIBOR_ICE_SWAP_RATE_11_00 = "EUR-EURIBOR ICE Swap Rate-11:00"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  EUR_EURIBOR_ICE_SWAP_RATE_12_00 = "EUR-EURIBOR ICE Swap Rate-12:00"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  EUR_EURIBOR_REFERENCE_BANKS = "EUR-EURIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURIBOR_REUTERS = "EUR-EURIBOR-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURIBOR_TELERATE = "EUR-EURIBOR-Telerate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURONIA_OIS_COMPOUND = "EUR-EURONIA-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURONIA_OIS_COMPOUND_1 = "EUR-EURONIA-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR = "EUR-EuroSTR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR_AVERAGE_12_M = "EUR-EuroSTR Average 12M"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR_AVERAGE_1_M = "EUR-EuroSTR Average 1M"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR_AVERAGE_1_W = "EUR-EuroSTR Average 1W"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR_AVERAGE_3_M = "EUR-EuroSTR Average 3M"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR_AVERAGE_6_M = "EUR-EuroSTR Average 6M"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR_COMPOUND = "EUR-EuroSTR-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR_COMPOUNDED_INDEX = "EUR-EuroSTR Compounded Index"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR_ICE_COMPOUNDED_INDEX = "EUR-EuroSTR ICE Compounded Index"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR_ICE_COMPOUNDED_INDEX_0_FLOOR = "EUR-EuroSTR ICE Compounded Index 0 Floor"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR_ICE_COMPOUNDED_INDEX_0_FLOOR_2_D_LAG = "EUR-EuroSTR ICE Compounded Index 0 Floor 2D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR_ICE_COMPOUNDED_INDEX_0_FLOOR_5_D_LAG = "EUR-EuroSTR ICE Compounded Index 0 Floor 5D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR_ICE_COMPOUNDED_INDEX_2_D_LAG = "EUR-EuroSTR ICE Compounded Index 2D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR_ICE_COMPOUNDED_INDEX_5_D_LAG = "EUR-EuroSTR ICE Compounded Index 5D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_EURO_STR_OIS_COMPOUND = "EUR-EuroSTR-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  EUR_ISDA_EURIBOR_SWAP_RATE_11_00 = "EUR-ISDA-EURIBOR Swap Rate-11:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ISDA_EURIBOR_SWAP_RATE_12_00 = "EUR-ISDA-EURIBOR Swap Rate-12:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ISDA_LIBOR_SWAP_RATE_10_00 = "EUR-ISDA-LIBOR Swap Rate-10:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_ISDA_LIBOR_SWAP_RATE_11_00 = "EUR-ISDA-LIBOR Swap Rate-11:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_LIBOR = "EUR-LIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  EUR_LIBOR_BBA = "EUR-LIBOR-BBA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_LIBOR_BBA_BLOOMBERG = "EUR-LIBOR-BBA-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_LIBOR_REFERENCE_BANKS = "EUR-LIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_TAM_CDC = "EUR-TAM-CDC"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_TEC10_CNO = "EUR-TEC10-CNO"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_TEC_10_CNO_SWAP_MARKER = "EUR-TEC10-CNO-SwapMarker"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_TEC_10_REFERENCE_BANKS = "EUR-TEC10-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_TEC5_CNO = "EUR-TEC5-CNO"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_TEC_5_CNO_SWAP_MARKER = "EUR-TEC5-CNO-SwapMarker"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_TEC_5_REFERENCE_BANKS = "EUR-TEC5-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_TMM_CDC_COMPOUND = "EUR-TMM-CDC-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  EUR_USD_BASIS_SWAPS_11_00_ICAP = "EUR USD-Basis Swaps-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_6_M_LIBOR_SWAP_CME_VS_LCH_ICAP = "GBP-6M LIBOR SWAP-CME vs LCH-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_6_M_LIBOR_SWAP_CME_VS_LCH_ICAP_BLOOMBERG = "GBP-6M LIBOR SWAP-CME vs LCH-ICAP-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_6_M_LIBOR_SWAP_EUREX_VS_LCH_ICAP = "GBP-6M LIBOR SWAP-EUREX vs LCH-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_6_M_LIBOR_SWAP_EUREX_VS_LCH_ICAP_BLOOMBERG = "GBP-6M LIBOR SWAP-EUREX vs LCH-ICAP-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_ISDA_SWAP_RATE = "GBP-ISDA-Swap Rate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_LIBOR = "GBP-LIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  GBP_LIBOR_BBA = "GBP-LIBOR-BBA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_LIBOR_BBA_BLOOMBERG = "GBP-LIBOR-BBA-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_LIBOR_ICE_SWAP_RATE = "GBP-LIBOR ICE Swap Rate"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  GBP_LIBOR_ISDA = "GBP-LIBOR-ISDA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_LIBOR_REFERENCE_BANKS = "GBP-LIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_RONIA = "GBP-RONIA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  GBP_RONIA_OIS_COMPOUND = "GBP-RONIA-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA = "GBP-SONIA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_COMPOUND = "GBP-SONIA-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_COMPOUNDED_INDEX = "GBP-SONIA Compounded Index"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_ICE_COMPOUNDED_INDEX = "GBP-SONIA ICE Compounded Index"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_ICE_COMPOUNDED_INDEX_0_FLOOR = "GBP-SONIA ICE Compounded Index 0 Floor"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_ICE_COMPOUNDED_INDEX_0_FLOOR_2_D_LAG = "GBP-SONIA ICE Compounded Index 0 Floor 2D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_ICE_COMPOUNDED_INDEX_0_FLOOR_5_D_LAG = "GBP-SONIA ICE Compounded Index 0 Floor 5D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_ICE_COMPOUNDED_INDEX_2_D_LAG = "GBP-SONIA ICE Compounded Index 2D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_ICE_COMPOUNDED_INDEX_5_D_LAG = "GBP-SONIA ICE Compounded Index 5D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_ICE_SWAP_RATE = "GBP-SONIA ICE Swap Rate"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_ICE_TERM = "GBP-SONIA ICE Term"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_OIS_11_00_ICAP = "GBP-SONIA-OIS-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_OIS_11_00_TRADITION = "GBP-SONIA-OIS-11:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_OIS_4_15_TRADITION = "GBP-SONIA-OIS-4:15-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_OIS_COMPOUND = "GBP-SONIA-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_REFINITIV_TERM = "GBP-SONIA Refinitiv Term"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SONIA_SWAP_RATE = "GBP-SONIA Swap Rate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SEMI_ANNUAL_SWAP_RATE = "GBP-Semi-Annual Swap Rate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SEMI_ANNUAL_SWAP_RATE_11_00_ICAP = "GBP-Semi-Annual Swap Rate-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SEMI_ANNUAL_SWAP_RATE_11_00_TRADITION = "GBP-Semi Annual Swap Rate-11:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SEMI_ANNUAL_SWAP_RATE_4_15_TRADITION = "GBP-Semi Annual Swap Rate-4:15-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SEMI_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "GBP-Semi-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_SEMI_ANNUAL_SWAP_RATE_SWAP_MARKER_26 = "GBP-Semi-Annual Swap Rate-SwapMarker26"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_UK_BASE_RATE = "GBP-UK Base Rate"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  GBP_USD_BASIS_SWAPS_11_00_ICAP = "GBP USD-Basis Swaps-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_WMBA_RONIA_COMPOUND = "GBP-WMBA-RONIA-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GBP_WMBA_SONIA_COMPOUND = "GBP-WMBA-SONIA-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GRD_ATHIBOR_ATHIBOR = "GRD-ATHIBOR-ATHIBOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GRD_ATHIBOR_REFERENCE_BANKS = "GRD-ATHIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GRD_ATHIBOR_TELERATE = "GRD-ATHIBOR-Telerate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GRD_ATHIMID_REFERENCE_BANKS = "GRD-ATHIMID-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  GRD_ATHIMID_REUTERS = "GRD-ATHIMID-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_HIBOR = "HKD-HIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  HKD_HIBOR_HIBOR_ = "HKD-HIBOR-HIBOR="
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_HIBOR_HIBOR_BLOOMBERG = "HKD-HIBOR-HIBOR-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_HIBOR_HKAB = "HKD-HIBOR-HKAB"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_HIBOR_HKAB_BLOOMBERG = "HKD-HIBOR-HKAB-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_HIBOR_ISDC = "HKD-HIBOR-ISDC"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_HIBOR_REFERENCE_BANKS = "HKD-HIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_HONIA = "HKD-HONIA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_HONIA_OIS_COMPOUND = "HKD-HONIA-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  HKD_HONIX_OIS_COMPOUND = "HKD-HONIX-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_ISDA_SWAP_RATE_11_00 = "HKD-ISDA-Swap Rate-11:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_ISDA_SWAP_RATE_4_00 = "HKD-ISDA-Swap Rate-4:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_QUARTERLY_ANNUAL_SWAP_RATE_11_00_BGCANTOR = "HKD-Quarterly-Annual Swap Rate-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_QUARTERLY_ANNUAL_SWAP_RATE_11_00_TRADITION = "HKD-Quarterly-Annual Swap Rate-11:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_QUARTERLY_ANNUAL_SWAP_RATE_4_00_BGCANTOR = "HKD-Quarterly-Annual Swap Rate-4:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_QUARTERLY_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "HKD-Quarterly-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_QUARTERLY_QUARTERLY_SWAP_RATE_11_00_ICAP = "HKD-Quarterly-Quarterly Swap Rate-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_QUARTERLY_QUARTERLY_SWAP_RATE_4_00_ICAP = "HKD-Quarterly-Quarterly Swap Rate-4:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HKD_QUARTERLY_QUARTERLY_SWAP_RATE_REFERENCE_BANKS = "HKD-Quarterly-Quarterly Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HUF_BUBOR = "HUF-BUBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  HUF_BUBOR_REFERENCE_BANKS = "HUF-BUBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HUF_BUBOR_REUTERS = "HUF-BUBOR-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  HUF_HUFONIA = "HUF-HUFONIA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  IDR_IDMA_BLOOMBERG = "IDR-IDMA-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  IDR_IDRFIX = "IDR-IDRFIX"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  IDR_JIBOR = "IDR-JIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  IDR_JIBOR_REUTERS = "IDR-JIBOR-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  IDR_SBI_REUTERS = "IDR-SBI-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  IDR_SOR_REFERENCE_BANKS = "IDR-SOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  IDR_SOR_REUTERS = "IDR-SOR-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  IDR_SOR_TELERATE = "IDR-SOR-Telerate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  IDR_SEMI_ANNUAL_SWAP_RATE_11_00_BGCANTOR = "IDR-Semi-Annual Swap Rate-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  IDR_SEMI_ANNUAL_SWAP_RATE_NON_DELIVERABLE_16_00_TULLETT_PREBON = "IDR-Semi Annual Swap Rate-Non-deliverable-16:00-Tullett Prebon"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  IDR_SEMI_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "IDR-Semi-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  ILS_TELBOR = "ILS-TELBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  ILS_TELBOR_01_REUTERS = "ILS-TELBOR01-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  ILS_TELBOR_REFERENCE_BANKS = "ILS-TELBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  INR_BMK = "INR-BMK"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  INR_CMT = "INR-CMT"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  INR_FBIL_MIBOR_OIS_COMPOUND = "INR-FBIL-MIBOR-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  INR_INBMK_REUTERS = "INR-INBMK-REUTERS"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  INR_MIBOR_OIS = "INR-MIBOR OIS"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  INR_MIBOR_OIS_COMPOUND = "INR-MIBOR-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  INR_MIBOR_OIS_COMPOUND_1 = "INR-MIBOR-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  INR_MIFOR = "INR-MIFOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  INR_MIOIS = "INR-MIOIS"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  INR_MITOR_OIS_COMPOUND = "INR-MITOR-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  INR_MODIFIED_MIFOR = "INR-Modified MIFOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  INR_REFERENCE_BANKS = "INR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  INR_SEMI_ANNUAL_SWAP_RATE_11_30_BGCANTOR = "INR-Semi-Annual Swap Rate-11:30-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  INR_SEMI_ANNUAL_SWAP_RATE_NON_DELIVERABLE_16_00_TULLETT_PREBON = "INR-Semi Annual Swap Rate-Non-deliverable-16:00-Tullett Prebon"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  INR_SEMI_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "INR-Semi-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  ISK_REIBOR = "ISK-REIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  ISK_REIBOR_REFERENCE_BANKS = "ISK-REIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  ISK_REIBOR_REUTERS = "ISK-REIBOR-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_ANNUAL_SWAP_RATE_11_00_TRADITION = "JPY-Annual Swap Rate-11:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_ANNUAL_SWAP_RATE_3_00_TRADITION = "JPY-Annual Swap Rate-3:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_BBSF_BLOOMBERG_10_00 = "JPY-BBSF-Bloomberg-10:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_BBSF_BLOOMBERG_15_00 = "JPY-BBSF-Bloomberg-15:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_EUROYEN_TIBOR = "JPY-Euroyen TIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  JPY_ISDA_SWAP_RATE_10_00 = "JPY-ISDA-Swap Rate-10:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_ISDA_SWAP_RATE_15_00 = "JPY-ISDA-Swap Rate-15:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_LIBOR = "JPY-LIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  JPY_LIBOR_BBA = "JPY-LIBOR-BBA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_LIBOR_BBA_BLOOMBERG = "JPY-LIBOR-BBA-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_LIBOR_FRASETT = "JPY-LIBOR-FRASETT"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_LIBOR_ISDA = "JPY-LIBOR-ISDA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_LIBOR_REFERENCE_BANKS = "JPY-LIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_LIBOR_TSR_10_00 = "JPY-LIBOR TSR-10:00"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  JPY_LIBOR_TSR_15_00 = "JPY-LIBOR TSR-15:00"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  JPY_LTPR_MHBK = "JPY-LTPR MHBK"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  JPY_LTPR_MHCB = "JPY-LTPR-MHCB"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_LTPR_TBC = "JPY-LTPR-TBC"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_MUTANCALL_TONAR = "JPY-MUTANCALL-TONAR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_OIS_11_00_ICAP = "JPY-OIS-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_OIS_11_00_TRADITION = "JPY-OIS-11:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_OIS_3_00_TRADITION = "JPY-OIS-3:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_QUOTING_BANKS_LIBOR = "JPY-Quoting Banks-LIBOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_STPR_QUOTING_BANKS = "JPY-STPR-Quoting Banks"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TIBOR = "JPY-TIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  JPY_TIBOR_17096 = "JPY-TIBOR-17096"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TIBOR_17097 = "JPY-TIBOR-17097"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TIBOR_DTIBOR01 = "JPY-TIBOR-DTIBOR01"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TIBOR_TIBM = "JPY-TIBOR-TIBM"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TIBOR_TIBM_REFERENCE_BANKS = "JPY-TIBOR-TIBM-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TIBOR_TIBM_10_BANKS = "JPY-TIBOR-TIBM (10 Banks)"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TIBOR_TIBM_5_BANKS = "JPY-TIBOR-TIBM (5 Banks)"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TIBOR_TIBM_ALL_BANKS = "JPY-TIBOR-TIBM (All Banks)"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TIBOR_TIBM_ALL_BANKS_BLOOMBERG = "JPY-TIBOR-TIBM (All Banks)-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TIBOR_ZTIBOR = "JPY-TIBOR-ZTIBOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA = "JPY-TONA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA_AVERAGE_180_D = "JPY-TONA Average 180D"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA_AVERAGE_30_D = "JPY-TONA Average 30D"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA_AVERAGE_90_D = "JPY-TONA Average 90D"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA_COMPOUNDED_INDEX = "JPY-TONA Compounded Index"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA_ICE_COMPOUNDED_INDEX = "JPY-TONA ICE Compounded Index"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA_ICE_COMPOUNDED_INDEX_0_FLOOR = "JPY-TONA ICE Compounded Index 0 Floor"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA_ICE_COMPOUNDED_INDEX_0_FLOOR_2_D_LAG = "JPY-TONA ICE Compounded Index 0 Floor 2D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA_ICE_COMPOUNDED_INDEX_0_FLOOR_5_D_LAG = "JPY-TONA ICE Compounded Index 0 Floor 5D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA_ICE_COMPOUNDED_INDEX_2_D_LAG = "JPY-TONA ICE Compounded Index 2D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA_ICE_COMPOUNDED_INDEX_5_D_LAG = "JPY-TONA ICE Compounded Index 5D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA_OIS_COMPOUND = "JPY-TONA-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA_OIS_COMPOUND_1 = "JPY-TONA-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA_TSR_10_00 = "JPY-TONA TSR-10:00"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TONA_TSR_15_00 = "JPY-TONA TSR-15:00"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TORF_QUICK = "JPY-TORF QUICK"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TSR_REFERENCE_BANKS = "JPY-TSR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TSR_REUTERS_10_00 = "JPY-TSR-Reuters-10:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TSR_REUTERS_15_00 = "JPY-TSR-Reuters-15:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TSR_TELERATE_10_00 = "JPY-TSR-Telerate-10:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_TSR_TELERATE_15_00 = "JPY-TSR-Telerate-15:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  JPY_USD_BASIS_SWAPS_11_00_ICAP = "JPY USD-Basis Swaps-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  KRW_BOND_3222 = "KRW-Bond-3222"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  KRW_CD_3220 = "KRW-CD-3220"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  KRW_CD_91D = "KRW-CD 91D"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  KRW_CD_KSDA_BLOOMBERG = "KRW-CD-KSDA-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  KRW_QUARTERLY_ANNUAL_SWAP_RATE_3_30_ICAP = "KRW-Quarterly Annual Swap Rate-3:30-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  MXN_TIIE = "MXN-TIIE"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  MXN_TIIE_BANXICO = "MXN-TIIE-Banxico"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  MXN_TIIE_BANXICO_BLOOMBERG = "MXN-TIIE-Banxico-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  MXN_TIIE_BANXICO_REFERENCE_BANKS = "MXN-TIIE-Banxico-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  MXN_TIIE_REFERENCE_BANKS = "MXN-TIIE-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  MYR_KLIBOR = "MYR-KLIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  MYR_KLIBOR_BNM = "MYR-KLIBOR-BNM"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  MYR_KLIBOR_REFERENCE_BANKS = "MYR-KLIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  MYR_QUARTERLY_SWAP_RATE_11_00_TRADITION = "MYR-Quarterly Swap Rate-11:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  MYR_QUARTERLY_SWAP_RATE_TRADITION_REFERENCE_BANKS = "MYR-Quarterly Swap Rate-TRADITION-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NOK_NIBOR = "NOK-NIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  NOK_NIBOR_NIBR = "NOK-NIBOR-NIBR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NOK_NIBOR_NIBR_BLOOMBERG = "NOK-NIBOR-NIBR-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NOK_NIBOR_NIBR_REFERENCE_BANKS = "NOK-NIBOR-NIBR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NOK_NIBOR_OIBOR = "NOK-NIBOR-OIBOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NOK_NIBOR_REFERENCE_BANKS = "NOK-NIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NOK_NOWA = "NOK-NOWA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NOK_NOWA_OIS_COMPOUND = "NOK-NOWA-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  NZD_BBR_BID = "NZD-BBR-BID"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NZD_BBR_FRA = "NZD-BBR-FRA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NZD_BBR_ISDC = "NZD-BBR-ISDC"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NZD_BBR_REFERENCE_BANKS = "NZD-BBR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NZD_BBR_TELERATE = "NZD-BBR-Telerate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NZD_BKBM_BID = "NZD-BKBM Bid"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  NZD_BKBM_FRA = "NZD-BKBM FRA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  NZD_BKBM_FRA_SWAP_RATE_ICAP = "NZD-BKBM FRA Swap Rate ICAP"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  NZD_NZIONA = "NZD-NZIONA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NZD_NZIONA_OIS_COMPOUND = "NZD-NZIONA-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NZD_NZIONA_OIS_COMPOUND_1 = "NZD-NZIONA-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  NZD_SEMI_ANNUAL_SWAP_RATE_11_00_BGCANTOR = "NZD-Semi-Annual Swap Rate-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NZD_SEMI_ANNUAL_SWAP_RATE_BGCANTOR_REFERENCE_BANKS = "NZD-Semi-Annual Swap Rate-BGCANTOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NZD_SWAP_RATE_ICAP = "NZD-Swap Rate-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  NZD_SWAP_RATE_ICAP_REFERENCE_BANKS = "NZD-Swap Rate-ICAP-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  PHP_PHIREF = "PHP-PHIREF"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  PHP_PHIREF_BAP = "PHP-PHIREF-BAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  PHP_PHIREF_BLOOMBERG = "PHP-PHIREF-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  PHP_PHIREF_REFERENCE_BANKS = "PHP-PHIREF-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  PHP_SEMI_ANNUAL_SWAP_RATE_11_00_BGCANTOR = "PHP-Semi-Annual Swap Rate-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  PHP_SEMI_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "PHP-Semi-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  PLN_POLONIA = "PLN-POLONIA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  PLN_POLONIA_OIS_COMPOUND = "PLN-POLONIA-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  PLN_POLONIA_OIS_COMPOUND_1 = "PLN-POLONIA-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  PLN_WIBID = "PLN-WIBID"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  PLN_WIBOR = "PLN-WIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  PLN_WIBOR_REFERENCE_BANKS = "PLN-WIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  PLN_WIBOR_WIBO = "PLN-WIBOR-WIBO"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  PLZ_WIBOR_REFERENCE_BANKS = "PLZ-WIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  PLZ_WIBOR_WIBO = "PLZ-WIBOR-WIBO"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  REPOFUNDS_RATE_FRANCE_OIS_COMPOUND = "REPOFUNDS RATE-FRANCE-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  REPOFUNDS_RATE_GERMANY_OIS_COMPOUND = "REPOFUNDS RATE-GERMANY-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  REPOFUNDS_RATE_ITALY_OIS_COMPOUND = "REPOFUNDS RATE-ITALY-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  RON_ANNUAL_SWAP_RATE_11_00_BGCANTOR = "RON-Annual Swap Rate-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  RON_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "RON-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  RON_RBOR_REUTERS = "RON-RBOR-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  RON_ROBID = "RON-ROBID"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  RON_ROBOR = "RON-ROBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  RUB_ANNUAL_SWAP_RATE_11_00_BGCANTOR = "RUB-Annual Swap Rate-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  RUB_ANNUAL_SWAP_RATE_12_45_TRADITION = "RUB-Annual Swap Rate-12:45-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  RUB_ANNUAL_SWAP_RATE_4_15_TRADITION = "RUB-Annual Swap Rate-4:15-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  RUB_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "RUB-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  RUB_ANNUAL_SWAP_RATE_TRADITION_REFERENCE_BANKS = "RUB-Annual Swap Rate-TRADITION-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  RUB_KEY_RATE_CBRF = "RUB-Key Rate CBRF"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  RUB_MOSPRIME_NFEA = "RUB-MOSPRIME-NFEA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  RUB_MOSPRIME_REFERENCE_BANKS = "RUB-MOSPRIME-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  RUB_MOS_PRIME = "RUB-MosPrime"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  RUB_RUONIA = "RUB-RUONIA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  RUB_RUONIA_OIS_COMPOUND = "RUB-RUONIA-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  RUB_RUONIA_OIS_COMPOUND_1 = "RUB-RUONIA-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  SAR_SAIBOR = "SAR-SAIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  SAR_SRIOR_REFERENCE_BANKS = "SAR-SRIOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SAR_SRIOR_SUAA = "SAR-SRIOR-SUAA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SEK_ANNUAL_SWAP_RATE = "SEK-Annual Swap Rate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SEK_ANNUAL_SWAP_RATE_SESWFI = "SEK-Annual Swap Rate-SESWFI"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SEK_SIOR_OIS_COMPOUND = "SEK-SIOR-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SEK_STIBOR = "SEK-STIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  SEK_STIBOR_BLOOMBERG = "SEK-STIBOR-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SEK_STIBOR_OIS_COMPOUND = "SEK-STIBOR-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  SEK_STIBOR_REFERENCE_BANKS = "SEK-STIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SEK_STIBOR_SIDE = "SEK-STIBOR-SIDE"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SEK_SWESTR = "SEK-SWESTR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SEK_SWESTR_AVERAGE_1_M = "SEK-SWESTR Average 1M"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SEK_SWESTR_AVERAGE_1_W = "SEK-SWESTR Average 1W"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SEK_SWESTR_AVERAGE_2_M = "SEK-SWESTR Average 2M"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SEK_SWESTR_AVERAGE_3_M = "SEK-SWESTR Average 3M"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SEK_SWESTR_AVERAGE_6_M = "SEK-SWESTR Average 6M"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SEK_SWESTR_COMPOUNDED_INDEX = "SEK-SWESTR Compounded Index"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SEK_SWESTR_OIS_COMPOUND = "SEK-SWESTR-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SIBOR = "SGD-SIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  SGD_SIBOR_REFERENCE_BANKS = "SGD-SIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SIBOR_REUTERS = "SGD-SIBOR-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SIBOR_TELERATE = "SGD-SIBOR-Telerate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SONAR_OIS_COMPOUND = "SGD-SONAR-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SONAR_OIS_VWAP_COMPOUND = "SGD-SONAR-OIS-VWAP-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SOR = "SGD-SOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  SGD_SORA = "SGD-SORA"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SORA_COMPOUND = "SGD-SORA-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SORA_OIS_COMPOUND = "SGD-SORA-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  SGD_SOR_REFERENCE_BANKS = "SGD-SOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SOR_REUTERS = "SGD-SOR-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SOR_TELERATE = "SGD-SOR-Telerate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SOR_VWAP = "SGD-SOR-VWAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SOR_VWAP_REFERENCE_BANKS = "SGD-SOR-VWAP-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SEMI_ANNUAL_CURRENCY_BASIS_SWAP_RATE_11_00_TULLETT_PREBON = "SGD-Semi-Annual Currency Basis Swap Rate-11:00-Tullett Prebon"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SEMI_ANNUAL_CURRENCY_BASIS_SWAP_RATE_16_00_TULLETT_PREBON = "SGD-Semi-Annual Currency Basis Swap Rate-16:00-Tullett Prebon"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SEMI_ANNUAL_SWAP_RATE_11_00_BGCANTOR = "SGD-Semi-Annual Swap Rate-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SEMI_ANNUAL_SWAP_RATE_11_00_TRADITION = "SGD-Semi-Annual Swap Rate-11.00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SEMI_ANNUAL_SWAP_RATE_11_00_TULLETT_PREBON = "SGD-Semi-Annual Swap Rate-11:00-Tullett Prebon"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SEMI_ANNUAL_SWAP_RATE_16_00_TULLETT_PREBON = "SGD-Semi-Annual Swap Rate-16:00-Tullett Prebon"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SEMI_ANNUAL_SWAP_RATE_ICAP = "SGD-Semi-Annual Swap Rate-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SEMI_ANNUAL_SWAP_RATE_ICAP_REFERENCE_BANKS = "SGD-Semi-Annual Swap Rate-ICAP-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SEMI_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "SGD-Semi-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SGD_SEMI_ANNUAL_SWAP_RATE_TRADITION_REFERENCE_BANKS = "SGD-Semi-Annual Swap Rate-TRADITION-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SKK_BRIBOR_BRBO = "SKK-BRIBOR-BRBO"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SKK_BRIBOR_BLOOMBERG = "SKK-BRIBOR-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SKK_BRIBOR_NBSK07 = "SKK-BRIBOR-NBSK07"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  SKK_BRIBOR_REFERENCE_BANKS = "SKK-BRIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  THB_SOR_REFERENCE_BANKS = "THB-SOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  THB_SOR_REUTERS = "THB-SOR-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  THB_SOR_TELERATE = "THB-SOR-Telerate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  THB_SEMI_ANNUAL_SWAP_RATE_11_00_BGCANTOR = "THB-Semi-Annual Swap Rate-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  THB_SEMI_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "THB-Semi-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  THB_THBFIX = "THB-THBFIX"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  THB_THBFIX_REFERENCE_BANKS = "THB-THBFIX-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  THB_THBFIX_REUTERS = "THB-THBFIX-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  THB_THOR = "THB-THOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  THB_THOR_COMPOUND = "THB-THOR-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  THB_THOR_OIS_COMPOUND = "THB-THOR-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  TRY_ANNUAL_SWAP_RATE_11_00_TRADITION = "TRY Annual Swap Rate-11:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TRY_ANNUAL_SWAP_RATE_11_15_BGCANTOR = "TRY-Annual Swap Rate-11:15-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TRY_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "TRY-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TRY_SEMI_ANNUAL_SWAP_RATE_TRADITION_REFERENCE_BANKS = "TRY-Semi-Annual Swap Rate-TRADITION-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TRY_TLREF = "TRY-TLREF"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  TRY_TLREF_OIS_COMPOUND = "TRY-TLREF-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TRY_TLREF_OIS_COMPOUND_1 = "TRY-TLREF-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  TRY_TRLIBOR = "TRY-TRLIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  TRY_TRYIBOR_REFERENCE_BANKS = "TRY-TRYIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TRY_TRYIBOR_REUTERS = "TRY-TRYIBOR-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TWD_QUARTERLY_ANNUAL_SWAP_RATE_11_00_BGCANTOR = "TWD-Quarterly-Annual Swap Rate-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TWD_QUARTERLY_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "TWD-Quarterly-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TWD_REFERENCE_DEALERS = "TWD-Reference Dealers"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TWD_REUTERS_6165 = "TWD-Reuters-6165"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TWD_TAIBIR01 = "TWD-TAIBIR01"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TWD_TAIBIR02 = "TWD-TAIBIR02"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TWD_TAIBOR = "TWD-TAIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  TWD_TAIBOR_BLOOMBERG = "TWD-TAIBOR-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TWD_TAIBOR_REUTERS = "TWD-TAIBOR-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TWD_TWCPBA = "TWD-TWCPBA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  TWD_TELERATE_6165 = "TWD-Telerate-6165"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  UK_BASE_RATE = "UK Base Rate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_3_M_LIBOR_SWAP_CME_VS_LCH_ICAP = "USD-3M LIBOR SWAP-CME vs LCH-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_3_M_LIBOR_SWAP_CME_VS_LCH_ICAP_BLOOMBERG = "USD-3M LIBOR SWAP-CME vs LCH-ICAP-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_6_M_LIBOR_SWAP_CME_VS_LCH_ICAP = "USD-6M LIBOR SWAP-CME vs LCH-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_6_M_LIBOR_SWAP_CME_VS_LCH_ICAP_BLOOMBERG = "USD-6M LIBOR SWAP-CME vs LCH-ICAP-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_AMERIBOR = "USD-AMERIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_AMERIBOR_AVERAGE_30_D = "USD-AMERIBOR Average 30D"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_AMERIBOR_AVERAGE_90_D = "USD-AMERIBOR Average 90D"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_AMERIBOR_TERM = "USD-AMERIBOR Term"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_AMERIBOR_TERM_STRUCTURE = "USD-AMERIBOR Term Structure"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_AXI_TERM = "USD-AXI Term"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_ANNUAL_SWAP_RATE_11_00_BGCANTOR = "USD-Annual Swap Rate-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_ANNUAL_SWAP_RATE_11_00_TRADITION = "USD-Annual Swap Rate-11:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_ANNUAL_SWAP_RATE_4_00_TRADITION = "USD-Annual Swap Rate-4:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_BA_H_15 = "USD-BA-H.15"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_BA_REFERENCE_DEALERS = "USD-BA-Reference Dealers"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_BMA_MUNICIPAL_SWAP_INDEX = "USD-BMA Municipal Swap Index"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_BSBY = "USD-BSBY"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_CD_H_15 = "USD-CD-H.15"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_CD_REFERENCE_DEALERS = "USD-CD-Reference Dealers"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_CMS_REFERENCE_BANKS = "USD-CMS-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_CMS_REFERENCE_BANKS_ICAP_SWAP_PX = "USD-CMS-Reference Banks-ICAP SwapPX"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_CMS_REUTERS = "USD-CMS-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_CMS_TELERATE = "USD-CMS-Telerate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_CMT = "USD-CMT"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_CMT_AVERAGE_1_W = "USD-CMT Average 1W"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_CMT_T7051 = "USD-CMT-T7051"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_CMT_T7052 = "USD-CMT-T7052"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_COF11_FHLBSF = "USD-COF11-FHLBSF"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_COF_11_REUTERS = "USD-COF11-Reuters"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_COF_11_TELERATE = "USD-COF11-Telerate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_COFI = "USD-COFI"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_CP_H_15 = "USD-CP-H.15"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_CP_MONEY_MARKET_YIELD = "USD-CP-Money Market Yield"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_CP_REFERENCE_DEALERS = "USD-CP-Reference Dealers"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_CRITR = "USD-CRITR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_FFCB_DISCO = "USD-FFCB-DISCO"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_FXI_TERM = "USD-FXI Term"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_FEDERAL_FUNDS = "USD-Federal Funds"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_FEDERAL_FUNDS_H_15 = "USD-Federal Funds-H.15"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_FEDERAL_FUNDS_H_15_BLOOMBERG = "USD-Federal Funds-H.15-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_FEDERAL_FUNDS_H_15_OIS_COMPOUND = "USD-Federal Funds-H.15-OIS-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_FEDERAL_FUNDS_OIS_COMPOUND = "USD-Federal Funds-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_FEDERAL_FUNDS_REFERENCE_DEALERS = "USD-Federal Funds-Reference Dealers"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_ISDAFIX_3_SWAP_RATE = "USD-ISDAFIX3-Swap Rate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_ISDAFIX_3_SWAP_RATE_3_00 = "USD-ISDAFIX3-Swap Rate-3:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_ISDA_SWAP_RATE = "USD-ISDA-Swap Rate"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_ISDA_SWAP_RATE_3_00 = "USD-ISDA-Swap Rate-3:00"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_LIBOR = "USD-LIBOR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_LIBOR_BBA = "USD-LIBOR-BBA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_LIBOR_BBA_BLOOMBERG = "USD-LIBOR-BBA-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_LIBOR_ICE_SWAP_RATE_11_00 = "USD-LIBOR ICE Swap Rate-11:00"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_LIBOR_ICE_SWAP_RATE_15_00 = "USD-LIBOR ICE Swap Rate-15:00"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_LIBOR_ISDA = "USD-LIBOR-ISDA"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_LIBOR_LIBO = "USD-LIBOR-LIBO"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_LIBOR_REFERENCE_BANKS = "USD-LIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_MUNICIPAL_SWAP_INDEX = "USD-Municipal Swap Index"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_MUNICIPAL_SWAP_LIBOR_RATIO_11_00_ICAP = "USD-Municipal Swap Libor Ratio-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_MUNICIPAL_SWAP_RATE_11_00_ICAP = "USD-Municipal Swap Rate-11:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_OIS_11_00_BGCANTOR = "USD-OIS-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_OIS_11_00_LON_ICAP = "USD-OIS-11:00-LON-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_OIS_11_00_NY_ICAP = "USD-OIS-11:00-NY-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_OIS_11_00_TRADITION = "USD-OIS-11:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_OIS_3_00_BGCANTOR = "USD-OIS-3:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_OIS_3_00_NY_ICAP = "USD-OIS-3:00-NY-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_OIS_4_00_TRADITION = "USD-OIS-4:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_OVERNIGHT_BANK_FUNDING_RATE = "USD-Overnight Bank Funding Rate"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_PRIME = "USD-Prime"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_PRIME_H_15 = "USD-Prime-H.15"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_PRIME_REFERENCE_BANKS = "USD-Prime-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SIBOR_REFERENCE_BANKS = "USD-SIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SIBOR_SIBO = "USD-SIBOR-SIBO"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SIFMA_MUNICIPAL_SWAP_INDEX = "USD-SIFMA Municipal Swap Index"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR = "USD-SOFR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_AVERAGE_180_D = "USD-SOFR Average 180D"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_AVERAGE_30_D = "USD-SOFR Average 30D"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_AVERAGE_90_D = "USD-SOFR Average 90D"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_CME_TERM = "USD-SOFR CME Term"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_COMPOUND = "USD-SOFR-COMPOUND"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_COMPOUNDED_INDEX = "USD-SOFR Compounded Index"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_ICE_COMPOUNDED_INDEX = "USD-SOFR ICE Compounded Index"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_ICE_COMPOUNDED_INDEX_0_FLOOR = "USD-SOFR ICE Compounded Index 0 Floor"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_ICE_COMPOUNDED_INDEX_0_FLOOR_2_D_LAG = "USD-SOFR ICE Compounded Index 0 Floor 2D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_ICE_COMPOUNDED_INDEX_0_FLOOR_5_D_LAG = "USD-SOFR ICE Compounded Index 0 Floor 5D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_ICE_COMPOUNDED_INDEX_2_D_LAG = "USD-SOFR ICE Compounded Index 2D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_ICE_COMPOUNDED_INDEX_5_D_LAG = "USD-SOFR ICE Compounded Index 5D Lag"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_ICE_SWAP_RATE = "USD-SOFR ICE Swap Rate"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix and 2006 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_ICE_TERM = "USD-SOFR ICE Term"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_SOFR_OIS_COMPOUND = "USD-SOFR-OIS Compound"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_S_P_INDEX_HIGH_GRADE = "USD-S&P Index-High Grade"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_SAND_P_INDEX_HIGH_GRADE = "USD-SandP Index High Grade"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_SWAP_RATE_BCMP_1 = "USD Swap Rate-BCMP1"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_TBILL_H_15 = "USD-TBILL-H.15"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_TBILL_H_15_BLOOMBERG = "USD-TBILL-H.15-Bloomberg"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_TBILL_SECONDARY_MARKET = "USD-TBILL-Secondary Market"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_TBILL_SECONDARY_MARKET_BOND_EQUIVALENT_YIELD = "USD-TBILL Secondary Market-Bond Equivalent Yield"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  USD_TIBOR_ISDC = "USD-TIBOR-ISDC"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_TIBOR_REFERENCE_BANKS = "USD-TIBOR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_TREASURY_19901_3_00_ICAP = "USD-Treasury-19901-3:00-ICAP"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_TREASURY_RATE_BCMP_1 = "USD Treasury Rate-BCMP1"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_TREASURY_RATE_ICAP_BROKER_TEC = "USD-Treasury Rate-ICAP BrokerTec"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_TREASURY_RATE_SWAP_MARKER_100 = "USD-Treasury Rate-SwapMarker100"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_TREASURY_RATE_SWAP_MARKER_99 = "USD-Treasury Rate-SwapMarker99"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_TREASURY_RATE_T_19901 = "USD-Treasury Rate-T19901"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  USD_TREASURY_RATE_T_500 = "USD-Treasury Rate-T500"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  VND_SEMI_ANNUAL_SWAP_RATE_11_00_BGCANTOR = "VND-Semi-Annual Swap Rate-11:00-BGCANTOR"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  VND_SEMI_ANNUAL_SWAP_RATE_REFERENCE_BANKS = "VND-Semi-Annual Swap Rate-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  ZAR_DEPOSIT_REFERENCE_BANKS = "ZAR-DEPOSIT-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  ZAR_DEPOSIT_SAFEX = "ZAR-DEPOSIT-SAFEX"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  ZAR_JIBAR = "ZAR-JIBAR"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  ZAR_JIBAR_REFERENCE_BANKS = "ZAR-JIBAR-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  ZAR_JIBAR_SAFEX = "ZAR-JIBAR-SAFEX"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  ZAR_PRIME_AVERAGE = "ZAR-PRIME-AVERAGE"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  ZAR_PRIME_AVERAGE_REFERENCE_BANKS = "ZAR-PRIME-AVERAGE-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  ZAR_PRIME_AVERAGE_1 = "ZAR-Prime Average"
  """
  Per 2021 ISDA Interest Rate Derivatives Definitions Floating Rate Matrix, as amended through the date on which parties enter into the relevant transaction.
  """
  ZAR_QUARTERLY_SWAP_RATE_1_00_TRADITION = "ZAR-Quarterly Swap Rate-1:00-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  ZAR_QUARTERLY_SWAP_RATE_5_30_TRADITION = "ZAR-Quarterly Swap Rate-5:30-TRADITION"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
  ZAR_QUARTERLY_SWAP_RATE_TRADITION_REFERENCE_BANKS = "ZAR-Quarterly Swap Rate-TRADITION-Reference Banks"
  """
  Per 2006 ISDA Definitions or Annex to the 2000 ISDA Definitions, Section 7.1 Rate Options, as amended and supplemented through the date on which parties enter into the relevant transaction.
  """
