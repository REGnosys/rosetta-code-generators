from enum import Enum

all = ['CreditEventTypeEnum']
  
class CreditEventTypeEnum(Enum):
  """
  Represents the enumerated values to specify a credit event type.
  """
  BANKRUPTCY = "BANKRUPTCY"
  """
  The reference entity has been dissolved or has become insolvent. It also covers events that may be a precursor to insolvency such as instigation of bankruptcy or insolvency proceedings. Sovereign trades are not subject to Bankruptcy as technically a Sovereign cannot become bankrupt. ISDA 2003 Term: Bankruptcy.
  """
  DEFAULT_REQUIREMENT = "DEFAULT_REQUIREMENT"
  """
  In relation to certain credit events, serves as a threshold for Obligation Acceleration, Obligation Default, Repudiation/Moratorium and Restructuring. Market standard is USD 10,000,000 (JPY 1,000,000,000 for all Japanese Yen trades). This is applied on an aggregate or total basis across all Obligations of the Reference Entity. Used to prevent technical/operational errors from triggering credit events. ISDA 2003 Term: Default Requirement.
  """
  DISTRESSED_RATINGS_DOWNGRADE = "DISTRESSED_RATINGS_DOWNGRADE"
  """
  Results from the fact that the rating of the reference obligation is downgraded to a distressed rating level. From a usage standpoint, this credit event is typically not applicable in case of RMBS trades.
  """
  FAILURE_TO_PAY = "FAILURE_TO_PAY"
  """
  This credit event triggers, after the expiration of any applicable grace period, if the reference entity fails to make due payments in an aggregrate amount of not less than the payment requirement on one or more obligations (e.g. a missed coupon payment). ISDA 2003 Term: Failure to Pay.
  """
  FAILURE_TO_PAY_INTEREST = "FAILURE_TO_PAY_INTEREST"
  """
  Corresponds to the failure by the Reference Entity to pay an expected interest amount or the payment of an actual interest amount that is less than the expected interest amount. ISDA 2003 Term: Failure to Pay Interest.
  """
  FAILURE_TO_PAY_PRINCIPAL = "FAILURE_TO_PAY_PRINCIPAL"
  """
  This credit event triggers, after the expiration of any applicable grace period, if the reference entity fails to make due payments in an aggregrate amount of not less than the payment requirement on one or more obligations (e.g. a missed coupon payment). ISDA 2003 Term: Failure to Pay.
  """
  GOVERNMENTAL_INTERVENTION = "GOVERNMENTAL_INTERVENTION"
  """
  A governmental intervention is an event resulting from an action by a governmental authority that materially impacts the reference entity's obligations, such as an interest rate reduction, principal reduction, deferral of interest or principal, change in priority ranking, or change in currency or composition of payment. ISDA 2014 Term: Governmental Intervention.
  """
  IMPLIED_WRITEDOWN = "IMPLIED_WRITEDOWN"
  """
  Results from the fact that losses occur to the underlying instruments that do not result in reductions of the outstanding principal of the reference obligation.
  """
  MATURITY_EXTENSION = "MATURITY_EXTENSION"
  """
  Results from the fact that the underlier fails to make principal payments as expected.
  """
  OBLIGATION_ACCELERATION = "OBLIGATION_ACCELERATION"
  """
  One or more of the obligations have been declared due and payable before they would otherwise have been due and payable as a result of, or on the basis of, the occurrence of a default, event of default or other similar condition or event other than failure to pay (preferred by the market over Obligation Default, because more definitive and encompasses the definition of Obligation Default - this is more favorable to the Seller). Subject to the default requirement amount. ISDA 2003 Term: Obligation Acceleration.
  """
  OBLIGATION_DEFAULT = "OBLIGATION_DEFAULT"
  """
  One or more of the obligations have become capable of being declared due and payable before they would otherwise have been due and payable as a result of, or on the basis of, the occurrence of a default, event of default or other similar condition or event other than failure to pay. ISDA 2003 Term: Obligation Default.
  """
  REPUDIATION_MORATORIUM = "REPUDIATION_MORATORIUM"
  """
  The reference entity, or a governmental authority, either refuses to recognise or challenges the validity of one or more obligations of the reference entity, or imposes a moratorium thereby postponing payments on one or more of the obligations of the reference entity. Subject to the default requirement amount. ISDA 2003 Term: Repudiation/Moratorium.
  """
  RESTRUCTURING = "RESTRUCTURING"
  """
  A restructuring is an event that materially impacts the reference entity's obligations, such as an interest rate reduction, principal reduction, deferral of interest or principal, change in priority ranking, or change in currency or composition of payment. ISDA 2003 Term: Restructuring.
  """
  WRITEDOWN = "WRITEDOWN"
  """
  Results from the fact that the underlier writes down its outstanding principal amount.
  """
