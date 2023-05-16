from enum import Enum

all = ['ContractualSupplementTypeEnum']
  
class ContractualSupplementTypeEnum(Enum):
  """
  The enumerated values to define the supplements to a base set of ISDA Definitions that are applicable to the transaction.
  """
  ABX = "ABX"
  """
  Standard Terms Supplement for ABX Transactions.
  """
  ABX_TRANCHE = "ABX_TRANCHE"
  """
  Standard Terms Supplement for Asset-Backed Tranche Transactions.
  """
  CD_SON_LEVERAGED_LOANS = "CD_SON_LEVERAGED_LOANS"
  """
  ISDA Standard Terms Supplement for use with Credit Derivative Transactions on Leveraged Loans.
  """
  CD_SON_MBS = "CD_SON_MBS"
  """
  ISDA Standard Terms Supplement for use with Credit Derivative Transactions on Mortgage-backed Security with Pay-As-You-Go or Physical Settlement.
  """
  CDX = "CDX"
  """
  Standard Terms Supplement for CDX Untranched Transactions.
  """
  CDX_EMERGING_MARKETS = "CDX_EMERGING_MARKETS"
  """
  Standard Terms Supplement for CDX Emerging Markets Untranched Transactions.
  """
  CDX_EMERGING_MARKETS_DIVERSIFIED = "CDX_EMERGING_MARKETS_DIVERSIFIED"
  """
  Standard Terms Supplement for CDX Emerging Markets Diversified Untranched Transactions..
  """
  CDX_SWAPTION = "CDX_SWAPTION"
  """
  Standard Terms Supplement for CDX Swaption Transactions.
  """
  CDX_TRANCHE = "CDX_TRANCHE"
  """
  Standard Terms Supplement for Dow Jones CDX Tranche Transactions.
  """
  CMBX = "CMBX"
  """
  Standard Terms Supplement for CMBX Transactions.
  """
  EUROPEAN_CMBS = "EUROPEAN_CMBS"
  """
  Standard Terms Supplement for Single Name European CMBS Transactions.
  """
  EUROPEAN_RMBS = "EUROPEAN_RMBS"
  """
  Standard Terms Supplement for Single Name European RMBS Transactions.
  """
  IOS = "IOS"
  """
  Standard Terms Supplement for IOS Transactions.
  """
  ISDA_1999_CREDIT_CONVERTIBLE_EXCHANGEABLE_ACCRETING_OBLIGATIONS = "ISDA_1999_CREDIT_CONVERTIBLE_EXCHANGEABLE_ACCRETING_OBLIGATIONS"
  """
  Supplement to the 1999 ISDA Credit Derivatives Definitions Relating to Convertible, Exchangeable or Accreting Obligations dated November 9, 2001.
  """
  ISDA_1999_CREDIT_RESTRUCTURING = "ISDA_1999_CREDIT_RESTRUCTURING"
  """
  Restructuring Supplement to the 1999 ISDA Credit Derivatives Definitions dated May 11, 2001.
  """
  ISDA_1999_CREDIT_SUCCESSOR_AND_CREDIT_EVENTS = "ISDA_1999_CREDIT_SUCCESSOR_AND_CREDIT_EVENTS"
  """
  Supplement Relating to Successor and Credit Events to the 1999 ISDA Credit Derivatives Definitions dated November 28, 2001.
  """
  ISDA_2003_ADDITIONAL_PROVISIONS_LPN = "ISDA_2003_ADDITIONAL_PROVISIONS_LPN"
  """
  Additional Provisions for LPN dated December 6, 2007.
  """
  ISDA_2003_CONTINGENT_CREDIT_SPREAD_TRANSACTION = "ISDA_2003_CONTINGENT_CREDIT_SPREAD_TRANSACTION"
  """
  Additional Provisions for Contingent Credit Spread Transactions dated August 15, 2008.
  """
  ISDA_2003_CREDIT_2005_MATRIX_SUPPLEMENT = "ISDA_2003_CREDIT_2005_MATRIX_SUPPLEMENT"
  """
  2005 Matrix Supplement to the 2003 ISDA Credit Derivatives.
  """
  ISDA_2003_CREDIT_ARGENTINE_REPUBLIC = "ISDA_2003_CREDIT_ARGENTINE_REPUBLIC"
  """
  Additional Provisions for the Argentine Republic: Excluded Obligations and Excluded Deliverable Obligations dated December 21, 2005.
  """
  ISDA_2003_CREDIT_AUCTION_SUPPLEMENT = "ISDA_2003_CREDIT_AUCTION_SUPPLEMENT"
  """
  ISDA Credit Derivatives Determinations Committees and Auction Settlement Supplement to the 2003 ISDA Credit Derivatives Definitions (published on [TBD]).
  """
  ISDA_2003_CREDIT_MAY_2003 = "ISDA_2003_CREDIT_MAY_2003"
  """
  May 2003 Supplement to the 2003 ISDA Credit Derivatives Definitions.
  """
  ISDA_2003_CREDIT_MONOLINE_INSURERS = "ISDA_2003_CREDIT_MONOLINE_INSURERS"
  """
  Additional Provisions for Physically Settled Default Swaps Monoline Insurer as Reference Entity dated May 9, 2003.
  """
  ISDA_2003_CREDIT_MONOLINE_INSURERS_2005 = "ISDA_2003_CREDIT_MONOLINE_INSURERS_2005"
  """
  Additional Provisions for Physically Settled Default Swaps Monoline Insurer as Reference Entity dated January 21, 2005.
  """
  ISDA_2003_CREDIT_REPUBLIC_OF_HUNGARY = "ISDA_2003_CREDIT_REPUBLIC_OF_HUNGARY"
  """
  Additional Provisions for the Republic of Hungary: Obligation Characteristics and Deliverable Obligation Characteristics dated August 13, 2004.
  """
  ISDA_2003_CREDIT_REPUBLIC_OF_HUNGARY_2005 = "ISDA_2003_CREDIT_REPUBLIC_OF_HUNGARY_2005"
  """
  Additional Provisions for the Republic of Hungary: Obligation Characteristics and Deliverable Obligation Characteristics dated February 14, 2005. 
  """
  ISDA_2003_CREDIT_RUSSIAN_FEDERATION = "ISDA_2003_CREDIT_RUSSIAN_FEDERATION"
  """
  Additional Provisions for the Russian Federation: Obligation Characteristics and Deliverable Obligation Characteristics dated August 13, 2004.
  """
  ISDA_2003_CREDIT_US_MUNICIPALS = "ISDA_2003_CREDIT_US_MUNICIPALS"
  """
  Additional Provisions for Credit Derivative Transactions - U.S. Municipal Entity as Reference Entity dated September 17, 2004.
  """
  ISDA_2003_ST_MICROELECTRONICS_NV = "ISDA_2003_ST_MICROELECTRONICS_NV"
  """
  Additional Provisions for STMicroelectronics NV dated December 6, 2007.
  """
  ISDA_2007_FULL_LOOKTHROUGH_DEPOSITORY_RECEIPT_SUPPLEMENT = "ISDA_2007_FULL_LOOKTHROUGH_DEPOSITORY_RECEIPT_SUPPLEMENT"
  """
  2007 Full Lookthrough Depository Receipt Supplement to the 2002 Equity Derivatives Definitions.
  """
  ISDA_2007_PARTIAL_LOOKTHROUGH_DEPOSITORY_RECEIPT_SUPPLEMENT = "ISDA_2007_PARTIAL_LOOKTHROUGH_DEPOSITORY_RECEIPT_SUPPLEMENT"
  """
  2007 Partial Lookthrough Depository Receipt Supplement to the 2002 ISDA Equity Derivatives Definitions.
  """
  ISDA_CREDIT_MONOLINE_INSURERS = "ISDA_CREDIT_MONOLINE_INSURERS"
  """
  Additional Provisions for Physically Settled Default Swaps Monoline Insurer.
  """
  ISDA_DELIVERY_RESTRICTIONS = "ISDA_DELIVERY_RESTRICTIONS"
  """
  Additional Provisions for Fixed Recovery Credit Default Swap Transactions
  """
  ISDA_FIXED_RECOVERY = "ISDA_FIXED_RECOVERY"
  """
  Additional Provisions for Fixed Recovery Credit Default Swap Transactions.
  """
  ISDALPN_REFERENCE_ENTITIES = "ISDALPN_REFERENCE_ENTITIES"
  """
  Additional Provisions for LPN Reference Entities.
  """
  ISDA_MARCH_2004_EQUITY_CANADIAN_SUPPLEMENT = "ISDA_MARCH_2004_EQUITY_CANADIAN_SUPPLEMENT"
  """
  Canadian Supplement to the 2004 Americas Interdealer Master Equity Derivatives Confirmation Agreement dated March 29, 2004.
  """
  ISDA_RECOVERY_LOCK = "ISDA_RECOVERY_LOCK"
  """
  Additional Provisions for Recovery Lock Credit Default Swap Transactions.
  """
  ISDA_SECURED_DELIVERABLE_OBLIGATION_CHARACTERISTIC = "ISDA_SECURED_DELIVERABLE_OBLIGATION_CHARACTERISTIC"
  """
  Additional Provisions for Secured Deliverable Obligation Characteristic.
  """
  LCDX = "LCDX"
  """
  Standard Terms Supplement for Syndicated Secured Loan Credit Default Swap Index Transactions.
  """
  LCDX_TRANCHE = "LCDX_TRANCHE"
  """
  Standard Terms Supplement for Syndicated Secured Loan Credit Default Swap Index Tranche Transactions.
  """
  MBX = "MBX"
  """
  Standard Terms Supplement for MBX Transactions.
  """
  MCDX = "MCDX"
  """
  Standard Terms Supplement for Municipal CDX Untranched Transactions.
  """
  PO = "PO"
  """
  Standard Terms Supplement for PO Index Transactions.
  """
  PRIME_X = "PRIME_X"
  """
  Standard Terms Supplement for PrimeX Transactions.
  """
  STANDARD_CDX_TRANCHE = "STANDARD_CDX_TRANCHE"
  """
  Standard Terms Supplement for Standard CDX Tranche Transactions.
  """
  STANDARD_LCDS = "STANDARD_LCDS"
  """
  Standard Syndicated Secured Loan Credit Default Swap Standard Terms Supplement.
  """
  STANDARD_LCDS_BULLET = "STANDARD_LCDS_BULLET"
  """
  Standard Terms Supplement for Standard Syndicated Secured Loan Credit Default Swap Bullet Transactions.
  """
  STANDARD_LCDX_BULLET = "STANDARD_LCDX_BULLET"
  """
  Standard Terms Supplement for Standard Syndicated Secured Loan Credit Default Swap Index Bullet Transactions.
  """
  STANDARD_LCDX_BULLET_TRANCHE = "STANDARD_LCDX_BULLET_TRANCHE"
  """
  Standard Terms Supplement for Standard Syndicated Secured Loan Credit Default Swap Index Bullet Tranche Transactions.
  """
  STANDARDI_TRAXX_EUROPE_TRANCHE = "STANDARDI_TRAXX_EUROPE_TRANCHE"
  """
  Standard Terms Supplement for Standard iTraxx Europe Tranched Transactions.
  """
  SYNDICATED_SECURED_LOAN_CDS = "SYNDICATED_SECURED_LOAN_CDS"
  """
  Syndicated Secured Loan Credit Default Swap Standard Terms Supplement.
  """
  TRX = "TRX"
  """
  Standard Terms Supplement for TRX Transactions.
  """
  TRX_II = "TRX.II"
  """
  Standard Terms Supplement for TRX.II Transactions.
  """
  I_TRAXX_ASIA_EX_JAPAN = "I_TRAXX_ASIA_EX_JAPAN"
  """
  Standard Terms Supplement for iTraxx Asia Excluding Japan.
  """
  I_TRAXX_ASIA_EX_JAPAN_SWAPTION = "I_TRAXX_ASIA_EX_JAPAN_SWAPTION"
  """
  Standard Terms Supplement for iTraxx Asia Ex-Japan Swaption Transactions.
  """
  I_TRAXX_ASIA_EX_JAPAN_TRANCHE = "I_TRAXX_ASIA_EX_JAPAN_TRANCHE"
  """
  Standard Terms Supplement for iTraxx Asia Excluding Japan Tranched Transactions.
  """
  I_TRAXX_AUSTRALIA = "I_TRAXX_AUSTRALIA"
  """
  Standard Terms Supplement for iTraxx Australia.
  """
  I_TRAXX_AUSTRALIA_SWAPTION = "I_TRAXX_AUSTRALIA_SWAPTION"
  """
  Standard Terms Supplement for iTraxx Australia Swaption Transactions.
  """
  I_TRAXX_AUSTRALIA_TRANCHE = "I_TRAXX_AUSTRALIA_TRANCHE"
  """
  Standard Terms Supplement for iTraxx Australia Tranched Transactions.
  """
  I_TRAXX_CJ = "I_TRAXX_CJ"
  """
  Standard Terms Supplement for iTraxx CJ.
  """
  I_TRAXX_CJ_TRANCHE = "I_TRAXX_CJ_TRANCHE"
  """
  Standard Terms Supplement for iTraxx CJ Tranched Transactions.
  """
  I_TRAXX_EUROPE = "I_TRAXX_EUROPE"
  """
  Standard Terms Supplement for iTraxx Europe Transactions.
  """
  I_TRAXX_EUROPE_DEALER = "I_TRAXX_EUROPE_DEALER"
  """
  Standard Terms Supplement for iTraxx Europe Dealer Form.
  """
  I_TRAXX_EUROPE_NON_DEALER = "I_TRAXX_EUROPE_NON_DEALER"
  """
  Standard Terms Supplement for iTraxx Europe Non-Dealer Form.
  """
  I_TRAXX_EUROPE_SWAPTION = "I_TRAXX_EUROPE_SWAPTION"
  """
  Standard Terms Supplement for iTraxx Europe Swaption Transactions.
  """
  I_TRAXX_EUROPE_TRANCHE = "I_TRAXX_EUROPE_TRANCHE"
  """
  Standard Terms Supplement for iTraxx Europe Tranched Transactions.
  """
  I_TRAXX_JAPAN = "I_TRAXX_JAPAN"
  """
  Standard Terms Supplement for iTraxx Japan.
  """
  I_TRAXX_JAPAN_SWAPTION = "I_TRAXX_JAPAN_SWAPTION"
  """
  Standard Terms Supplement for iTraxx Japan Swaption Transactions.
  """
  I_TRAXX_JAPAN_TRANCHE = "I_TRAXX_JAPAN_TRANCHE"
  """
  Standard Terms Supplement for iTraxx Japan Tranched Transactions.
  """
  I_TRAXX_LEV_X = "I_TRAXX_LEV_X"
  """
  Standard Terms Supplement for iTraxx LevX.
  """
  I_TRAXX_SDI_75_DEALER = "I_TRAXX_SDI_75_DEALER"
  """
  Standard Terms Supplement for iTraxx SDI 75 Dealer Transactions.
  """
  I_TRAXX_SDI_75_NON_DEALER = "I_TRAXX_SDI_75_NON_DEALER"
  """
  Standard Terms Supplement for iTraxx SDI 75 Non-Dealer Transactions.
  """
  I_TRAXX_SOV_X = "I_TRAXX_SOV_X"
  """
  Standard Terms Supplement for iTraxx SovX.
  """
