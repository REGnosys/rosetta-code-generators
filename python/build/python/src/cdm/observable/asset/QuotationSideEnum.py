from enum import Enum

all = ['QuotationSideEnum']
  
class QuotationSideEnum(Enum):
  """
  The enumerated values to specify the side from which perspective a value is quoted.
  """
  AFTERNOON = "AFTERNOON"
  """
  Denotes a value as the Afternoon fixing reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  ASK = "ASK"
  """
  Denotes a value 'asked' by a seller for an asset, i.e. the value at which a seller is willing to sell.
  """
  BID = "BID"
  """
  Denotes a value 'bid' by a buyer for an asset, i.e. the value a buyer is willing to pay.
  """
  CLOSING = "CLOSING"
  """
  Denotes a value as the Closing price reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  HIGH = "HIGH"
  """
  Denotes a value as the High price reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  INDEX = "INDEX"
  """
  Denotes a value as the Index price reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  LOCATIONAL_MARGINAL = "LOCATIONAL_MARGINAL"
  """
  Denotes a value as the Locational Marginal price reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  LOW = "LOW"
  """
  Denotes a value as the Low price reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  MARGINAL_HOURLY = "MARGINAL_HOURLY"
  """
  Denotes a value as the Marginal Hourly price reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  MARKET_CLEARING = "MARKET_CLEARING"
  """
  Denotes a value as the Market Clearing price reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  MEAN_OF_BID_AND_ASK = "MEAN_OF_BID_AND_ASK"
  """
  Denotes a value as the Average of the Bid and Ask prices reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  MEAN_OF_HIGH_AND_LOW = "MEAN_OF_HIGH_AND_LOW"
  """
  Denotes a value as the Average of the High and Low prices reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  MID = "MID"
  """
  Denotes a value as the Average of the Midpoint of prices reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  MORNING = "MORNING"
  """
  Denotes a value as the Morning fixing reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  NATIONAL_SINGLE = "NATIONAL_SINGLE"
  """
  Denotes a value as the National Single price reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  OSP = "OSP"
  """
  Denotes a value as the Official Settlement Price reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  OFFICIAL = "OFFICIAL"
  """
  Denotes a value as the Official price reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  OPENING = "OPENING"
  """
  Denotes a value as the Opening price reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  SETTLEMENT = "SETTLEMENT"
  """
  Denotes a value as the Settlement price reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  SPOT = "SPOT"
  """
  Denotes a value as the Spot price reported in or by the relevant Price Source as specified in the relevant Confirmation.
  """
  UN_WEIGHTED_AVERAGE = "UN_WEIGHTED_AVERAGE"
  """
  Denotes a value as the Non-volume Weighted Average of prices effective on the Pricing Date.
  """
  WEIGHTED_AVERAGE = "WEIGHTED_AVERAGE"
  """
  Denotes a value as the Volume Weighted Average of prices effective on the Pricing Date.
  """
