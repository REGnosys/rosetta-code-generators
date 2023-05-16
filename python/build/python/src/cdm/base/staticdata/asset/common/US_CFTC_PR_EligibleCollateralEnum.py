from enum import Enum

all = ['US_CFTC_PR_EligibleCollateralEnum']
  
class US_CFTC_PR_EligibleCollateralEnum(Enum):
  """
  Identifies US Eligible Collateral Assets classification categories based on Uncleared Margin Rules published by the CFTC and the US Prudential Regulator. Note: While the same basic categories exist in the CFTC and US Prudential Regulators margin rules, the precise definitions or application of those rules could differ between the two rules.
  """
  US_CFTC_PR_TYPE_1 = "US_CFTC_PR_TYPE_1"
  """
  Denotes immediately available cash funds denominated in USD, a major currency, a currency of settlement for the uncleared swap.
  """
  US_CFTC_PR_TYPE_2 = "US_CFTC_PR_TYPE_2"
  """
  Denotes a security that is issued by, or unconditionally guaranteed as to the timely payment of principal and interest by, the U.S. Department of the Treasury.
  """
  US_CFTC_PR_TYPE_3 = "US_CFTC_PR_TYPE_3"
  """
  Denotes a security that is issued by, or unconditionally guaranteed as to the timely payment of principal and interest by, a U.S. government agency (other than the U.S. Department of Treasury) whose obligations are fully guaranteed by the full faith and credit of the United States government.
  """
  US_CFTC_PR_TYPE_4 = "US_CFTC_PR_TYPE_4"
  """
  Denotes a security that is issued by, or fully guaranteed as to the payment of principal and interest by, the European Central Bank or a sovereign entity that is assigned no higher than a 20 percent risk weight under the capital rules applicable to swap dealers subject to regulation by a prudential regulator.
  """
  US_CFTC_PR_TYPE_5_A = "US_CFTC_PR_TYPE_5_A"
  """
  Denotes a publicly traded debt security issued by, or an asset-backed security fully guaranteed as to the timely payment of principal and interest by, a U.S. Government-sponsored enterprise that is operating with capital support or another form of direct financial assistance received from the U.S. government that enables the repayments of the U.S. Government-sponsored enterprise's eligible securities.
  """
  US_CFTC_PR_TYPE_5_B = "US_CFTC_PR_TYPE_5_B"
  """
  Denotes a publicly traded debt security, but not an asset backed security, that is investment grade and issued by a U.S. Government-sponsored enterprise that is not operating with capital support or another form of direct financial assistance received from the U.S. government.
  """
  US_CFTC_PR_TYPE_6 = "US_CFTC_PR_TYPE_6"
  """
  Denotes a security that is issued by, or fully guaranteed as to the payment of principal and interest by, the Bank for International Settlements, the International Monetary Fund, or a multilateral development bank.
  """
  US_CFTC_PR_TYPE_7 = "US_CFTC_PR_TYPE_7"
  """
  Denotes publicly-traded debt, but not an asset backed security, that is investment grade and is not a debt security issued by a  U.S. Government-sponsored enterprise. This category excludes a security issued by a non-bank financial institution supervised by the board of governors of the Federal Reserve System under Title I of the Dodd-Frank Wall Street Reform and Consumer Protection Act. This category also excludes a security issued by any of the following entities, by a company that would be any of the following entities if it were the organized under the laws of the United States or any State, or in either case by an affiliate of such an entity: the party posting the collateral, a bank holding company, a savings and loan holding company, a U.S. intermediate holding company, a foreign bank, a depositary institution, a securities holding company, a broker, a dealer, a futures commission merchant, a swap dealer, or a security-based swap dealer.
  """
  US_CFTC_PR_TYPE_8_A = "US_CFTC_PR_TYPE_8_A"
  """
  Denotes a publicly traded common equity security that is included in the Standard & Poor's Composite 500 Index or related indexes. This category excludes a security issued by a non-bank financial institution supervised by the board of governors of the Federal Reserve System under Title I of the Dodd-Frank Wall Street Reform and Consumer Protection Act. This category also excludes a security issued by any of the following entities, by a company that would be any of the following entities if it were the organized under the laws of the United States or any State, or in either case by an affiliate of such an entity: the party posting the collateral, a bank holding company, a savings and loan holding company, a U.S. intermediate holding company, a foreign bank, a depositary institution, a securities holding company, a broker, a dealer, a futures commission merchant, a swap dealer, or a security-based swap dealer.
  """
  US_CFTC_PR_TYPE_8_B = "US_CFTC_PR_TYPE_8_B"
  """
   Denotes a publicly traded common equity security that is included in the Standard & Poor's Composite 1500 Index or related indexes. This category excludes a security issued by a non-bank financial institution supervised by the board of governors of the Federal Reserve System under Title I of the Dodd-Frank Wall Street Reform and Consumer Protection Act. This category also excludes a security issued by any of the following entities, by a company that would be any of the following entities if it were the organized under the laws of the United States or any State, or in either case by an affiliate of such an entity: the party posting the collateral, a bank holding company, a savings and loan holding company, a U.S. intermediate holding company, a foreign bank, a depositary institution, a securities holding company, a broker, a dealer, a futures commission merchant, a swap dealer, or a security-based swap dealer.
  """
  US_CFTC_PR_TYPE_8_C = "US_CFTC_PR_TYPE_8_C"
  """
  Denotes a publicly traded common equity security that is included in an index that a regulated swap entity's supervisor in a foreign jurisdiction recognizes for purposes of including publicly traded common equity as initial margin under applicable regulatory policy, if held in that foreign jurisdiction. This category excludes a security issued by a non-bank financial institution supervised by the board of governors of the Federal Reserve System under Title I of the Dodd-Frank Wall Street Reform and Consumer Protection Act. This category also excludes a security issued by any of the following entities, by a company that would be any of the following entities if it were the organized under the laws of the United States or any State, or in either case by an affiliate of such an entity: the party posting the collateral, a bank holding company, a savings and loan holding company, a U.S. intermediate holding company, a foreign bank, a depositary institution, a securities holding company, a broker, a dealer, a futures commission merchant, a swap dealer, or a security-based swap dealer.
  """
  US_CFTC_PR_TYPE_9 = "US_CFTC_PR_TYPE_9"
  """
  Denotes securities in the form of redeemable securities in a pooled investment fund representing the security-holder's proportional interest in the fund's net assets and that are issued and redeemed only on the basis of the market value of the fund's net assets prepared each business day after the security-holder makes its investment commitment or redemption request to the fund, if the fund's investments are limited to the following: (A) securities that are issued by, or unconditionally guaranteed as to the timely payment of principal and interest by, the U.S. Department of the Treasury, and immediately-available cash funds denominated in U.S. dollars; or (B) securities denominated in a common currency and issued by, or fully guaranteed as to the payment of principal and interest by, the European Central Bank or a sovereign entity that is assigned no higher than a 20 percent risk weight under the capital rules applicable to swap dealers subject to regulation by a prudential regulator, and immediately-available cash funds denominated in the same currency; and (C) assets of the fund may not be transferred through securities lending, securities borrowing, repurchase agreements, reverse repurchase agreements, or other means that involve the fund having rights to acquire the same or similar assets from the transferee.
  """
  US_CTFC_PR_TYPE_10 = "US_CTFC_PR_TYPE_10"
  """
  Denotes Gold.
  """
