from enum import Enum

all = ['RegulatoryRegimeEnum']
  
class RegulatoryRegimeEnum(Enum):
  """
  The enumerated values to specify the regulatory regimes. The display name corresponds to the regulatory regime name or acronym specified as part of the Regime table in the ISDA CSA for Initial Margin, paragraph 13, General Principles. 2016 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles: Regime. | 2018 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles: Regime.
  """
  AUSTRALIA_MARGIN_RULES = "Australia"
  """
  Australian Prudential Standard CPS 226 Margining and risk mitigation for non-centrally cleared derivatives. 2018 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles.
  """
  BRAZIL_MARGIN_RULES = "Brazil"
  """
  the Central Bank of Brazil margin requirements adopted pursuant to Resolution no. 4,662, of 25 May 2018, enacted by the National Monetary Council.
  """
  CFTC_MARGIN_RULES = "CFTC"
  """
  Margin requirements adopted by the U.S. Commodity Futures Trading Commission pursuant to CEA § 4s(e). 2016 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles. | 2018 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles.
  """
  CANADA_MARGIN_RULES = "Canada"
  """
  Guideline E-22, Margin Requirements for Non-Centrally Cleared Derivatives issued by the Canadian Office of the Superintendent of Financial Institutions in February 2016. 2016 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles. | 2018 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles.
  """
  EMIR_MARGIN_RULES = "EMIR"
  """
  Regulation (EU) No 648/2012 of the European Parliament and of the Council of 4 July 2012 on OTC derivatives, central counterparties and trade repositories (including the EMIR RTS, which means the published regulatory technical standards on risk-mitigation techniques for OTC-derivative contracts not cleared by a CCP under Article 11(15) of EMIR). 2016 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles. | 2018 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles.
  """
  HONG_KONG_MARGIN_RULES = "Hong Kong"
  """
  Chapter CR-G-14 'Non-centrally Cleared OTC Derivatives Transactions – Margin and Other Risk Mitigation Standards' in the Banking Supervisory Policy Manual issued by the Hong Kong Monetary Authority. 2018 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles.
  """
  HONG_KONG_SFC_MARGIN_RULES = "Hong Kong SFC"
  """
  Part III of Schedule 10 to Code of Conduct for Persons Licensed by or Registered with the Securities and Futures Commission of Hong Kong.
  """
  JAPAN_MARGIN_RULES = "Japan"
  """
  Margin rules adopted by the Financial Services Agency of Japan pursuant to Article 40, Item 2 of the Financial Instruments and Exchange Act (kin’yuu shouhin torihiki hou) (Act No. 25 of 1948) and by the Ministry of Agriculture, Forestry and Fisheries and the Ministry of Economy, Trade and Industry pursuant to the Commodity Derivatives Act (shouhin sakimono torihiki hou) (Act No. 239 of 1950) (including their subordinated regulations and the related supervisory guidelines). 2016 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles. | 2018 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles.
  """
  SEC_MARGIN_RULES = "SEC"
  """
  Margin requirements adopted by the U.S. Securities and Exchange Commission pursuant to Exchange Act § 15F(e). 2016 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles. | 2018 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles.
  """
  SINGAPORE_MARGIN_RULES = "Singapore"
  """
  Guidelines on Margin Requirements for Non-centrally Cleared OTC Derivatives Contracts issued by the Monetary Authority of Singapore (MAS) pursuant to section 321 of the Securities and Futures Act, Chapter 289 of Singapore. 2018 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles.
  """
  SOUTH_AFRICA_MARGIN_RULES = "South Africa"
  """
  the requirements contained in Joint Standard 2 of 2020 made in terms of the South African Financial Sector Regulation Act, 2017.
  """
  SOUTH_KOREA_MARGIN_RULES = "South Korea"
  """
  margin requirements adopted by the Korean Financial Services Commission and Financial Supervisory Service pursuant to the Guidelines on Margin Requirements for Non-Centrally Cleared OTC Derivatives Transactions, which are expected to be incorporated into the Financial Investment Services and Capital Markets Act.
  """
  SWITZERLAND_MARGIN_RULES = "Switzerland"
  """
  Margin rules adopted by the Swiss Federal Council pursuant to Article 110-111 of the Financial Market Infrastructure Act as well as Articles 100 to 107 and Annexes 3 to 5 of the Financial Market Infrastructure Ordinance. 2018 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles.
  """
  US_PRUDENTIAL_MARGIN_RULES = "Prudential"
  """
  Margin requirements adopted by a 'prudential regulator' (as defined in CEA § 1a(39)) pursuant to CEA § 4s(e) and Exchange Act § 15F(e). 2016 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles. | 2018 ISDA Credit Support Annex for Initial Margin, paragraph 13, General Principles.
  """
  UNITED_KINGDOM_MARGIN_RULES = "United Kingdom"
  """
  EMIR (including, for the avoidance of doubt, the EMIR RTS) as it forms part of UK domestic law by virtue of section 3 of the European Union (Withdrawal) Act 2018 (as amended) (the EUWA) (including any amendments made to such legislation when it is brought into UK domestic law pursuant to section 8 of the EUWA or any regulations made thereunder), and which, for the avoidance of doubt, shall be subject to the interpretation provision in Paragraph [11(g)].3
  """
