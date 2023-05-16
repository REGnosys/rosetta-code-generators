from enum import Enum

all = ['TaxonomySourceEnum']
  
class TaxonomySourceEnum(Enum):
  """
  Represents the enumerated values to specify taxonomy sources.
  """
  CFI = "CFI"
  """
  Represents the ISO 10962 Classification of Financial Instruments code.
  """
  EMIR = "EMIR"
  """
  Represents the EMIR Article 9 Asset Definition Identifier code.
  """
  EU_EMIR_ELIGIBLE_COLLATERAL_ASSET_CLASS = "EU_EMIR_ELIGIBLE_COLLATERAL_ASSET_CLASS"
  """
  Identifies European Union Eligible Collateral Assets classification categories based on EMIR Uncleared Margin Rules.
  """
  ICAD = "ICAD"
  """
  Represents the ISDA Collateral Asset Definition Idenifier code.
  """
  ISDA = "ISDA"
  """
  Represents the ISDA product taxonomy.
  """
  OTHER = "OTHER"
  """
  Denotes a user-specific scheme or taxonomy or other external sources not listed here.
  """
  UK_EMIR_ELIGIBLE_COLLATERAL_ASSET_CLASS = "UK_EMIR_ELIGIBLE_COLLATERAL_ASSET_CLASS"
  """
  Identifies United Kingdom Eligible Collateral Assets classification categories based on UK Onshored EMIR Uncleared Margin Rules Eligible Collateral asset classes for both initial margin (IM) and variation margin (VM) posted and collected between specified entities.Please note: UK EMIR regulation will detail which eligible collateral assets classes apply to each type of entity pairing (counterparty) and which apply to posting of IM and VM.
  """
  US_CFTC_PR_ELIGIBLE_COLLATERAL_ASSET_CLASS = "US_CFTC_PR_ELIGIBLE_COLLATERAL_ASSET_CLASS"
  """
  Identifies US Eligible Collateral Assets classification categories based on Uncleared Margin Rules published by the CFTC and the US Prudential Regulator. Note: While the same basic categories exist in the CFTC and US Prudential Regulators margin rules, the precise definitions or application of those rules could differ between the two rules.
  """
