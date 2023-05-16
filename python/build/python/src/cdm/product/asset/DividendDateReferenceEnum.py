from enum import Enum

all = ['DividendDateReferenceEnum']
  
class DividendDateReferenceEnum(Enum):
  """
  The enumerated values to specify the date by reference to which the dividend will be paid.
  """
  AD_HOC_DATE = "AD_HOC_DATE"
  """
  The dividend date will be specified ad-hoc by the parties, typically on the dividend ex-date.
  """
  CASH_SETTLE_PAYMENT_DATE_EX_DIV = "CASH_SETTLE_PAYMENT_DATE_EX_DIV"
  """
  If 'Dividend Payment Date(s)' is specified in the Transaction Supplement as 'Cash Settlement Payment Date – Ex Dividend'', then the Dividend Payment Date in respect of a Dividend Amount shall be the Cash Settlement Payment Date relating to the end of the Dividend Period during which the Shares commenced trading 'ex' the relevant dividend on the Exchange.
  """
  CASH_SETTLE_PAYMENT_DATE_ISSUER_PAYMENT = "CASH_SETTLE_PAYMENT_DATE_ISSUER_PAYMENT"
  """
  If 'Dividend Payment Date(s)' is specified in the Transaction Supplement as 'Cash Settlement Payment Date – Issuer Payment', then the Dividend Payment Date in respect of a Dividend Amount shall be the Cash Settlement Payment Date relating to the end of the Dividend Period during which the issuer pays the relevant dividend to a holder of record provided that in the case where the Equity Amount Payer is the party specified to be the sole Hedging Party and the Hedging Party has not received the Dividend Amount by such date, then the date falling a number of Currency Business Days as specified in the Cash Settlement Payment Date after actual receipt by the Hedging Party of the Received Ex Amount or Paid Ex Amount (as applicable).
  """
  CASH_SETTLEMENT_PAYMENT_DATE = "CASH_SETTLEMENT_PAYMENT_DATE"
  """
  If 'Dividend Payment Date(s)' is specified in the Transaction Supplement as 'Cash Settlement Payment Date', then the Dividend Payment Date in respect of a Dividend Amount shall be the Cash Settlement Payment Date relating to the end of the Dividend Period during which the Shares commenced trading 'ex' the relevant dividend on the Exchange.
  """
  CUMULATIVE_EQUITY_EX_DIV = "CUMULATIVE_EQUITY_EX_DIV"
  """
  Total of dividends which go ex, paid on next following Equity Payment Date, which is immediately following the Dividend Period during which the Shares commence trading ex-dividend on the Exchange.
  """
  CUMULATIVE_EQUITY_EX_DIV_BEFORE_RESET = "CUMULATIVE_EQUITY_EX_DIV_BEFORE_RESET"
  """
  Total of paid dividends, paid on next following Equity Payment Date, which is immediately following the Dividend Ex Date, unless the Dividend Ex Date is between the Equity Valuation and Payment Date in which case the dividend is deferred to the following Equity Payment Date
  """
  CUMULATIVE_EQUITY_PAID = "CUMULATIVE_EQUITY_PAID"
  """
  Total of paid dividends, paid on next following Equity Payment Date, which is immediately following the Dividend Period during which the dividend is paid by the Issuer to the holders of record of a Share.
  """
  CUMULATIVE_EQUITY_PAID_BEFORE_RESET = "CUMULATIVE_EQUITY_PAID_BEFORE_RESET"
  """
  Total of paid dividends, paid on next following Equity Payment Date, which is immediately following the Dividend Pay Date, unless the Dividend Pay Date is between the Equity Valuation and Payment Date (not including the Valuation Date) in which case the dividend is deferred to the following Equity Payment Date
  """
  CUMULATIVE_EQUITY_PAID_INCL_RESET = "CUMULATIVE_EQUITY_PAID_INCL_RESET"
  """
  Total of paid dividends, paid on next following Equity Payment Date, which is immediately following the Dividend Pay Date, unless the Dividend Pay Date is between the Equity Valuation and Payment Date (including the Valuation Date) in which case the dividend is deferred to the following Equity Payment Date
  """
  CUMULATIVE_INTEREST_EX_DIV = "CUMULATIVE_INTEREST_EX_DIV"
  """
  Total of dividends which go ex, paid on next following Interest Payment Date, which is immediately following the Dividend Period during which the Shares commence trading ex-dividend on the Exchange, or where the date on which the Shares commence trading ex-dividend is a Payment Date, such Payment Date.
  """
  CUMULATIVE_INTEREST_PAID = "CUMULATIVE_INTEREST_PAID"
  """
  Total of paid dividends, paid on next following Interest Payment Date, which is immediately following the Dividend Period during which the dividend is paid by the Issuer to the holders of record of a Share.
  """
  CUMULATIVE_INTEREST_PAID_BEFORE_RESET = "CUMULATIVE_INTEREST_PAID_BEFORE_RESET"
  """
  Total of paid dividends, paid on next following Interest Payment Date, which is immediately following the Dividend Pay Date, unless the Dividend Pay Date is between the Equity Valuation and Payment Date (not including the Valuation Date) in which case the dividend is deferred to the following Interest Payment Date.
  """
  CUMULATIVE_INTEREST_PAID_INCL_RESET = "CUMULATIVE_INTEREST_PAID_INCL_RESET"
  """
  Total of paid dividends, paid on next following Interest Payment Date, which is immediately following the Dividend Pay Date, unless the Dividend Pay Date is between the Equity Valuation and Payment Date (including the Valuation Date) in which case the dividend is deferred to the following Interest Payment Date.
  """
  DIVIDEND_PAYMENT_DATE = "DIVIDEND_PAYMENT_DATE"
  """
  Date on which the dividend will be paid by the issuer.
  """
  DIVIDEND_VALUATION_DATE = "DIVIDEND_VALUATION_DATE"
  """
  In respect of each Dividend Period, the relevant Dividend Valuation Date.
  """
  EQUITY_PAYMENT_DATE = "EQUITY_PAYMENT_DATE"
  """
  Equity payment date of the swap.
  """
  EX_DATE = "EX_DATE"
  """
  Date on which a holder of the security is entitled to the dividend.
  """
  FLOATING_AMOUNT_PAYMENT_DATE = "FLOATING_AMOUNT_PAYMENT_DATE"
  """
  If 'Dividend Payment Date(s)' is specified in the Transaction Supplement as 'Floating Amount Payment Date', then the Dividend Payment Date in respect of a Dividend Amount shall be the first Payment Date falling at least one Settlement Cycle after the date that the Shares have commenced trading 'ex' the relevant dividend on the Exchange.
  """
  FOLLOWING_PAYMENT_DATE = "FOLLOWING_PAYMENT_DATE"
  """
  The next payment date of the swap.
  """
  RECORD_DATE = "RECORD_DATE"
  """
  Date on which the dividend will be recorded in the books of the paying agent.
  """
  SHARE_PAYMENT = "SHARE_PAYMENT"
  """
  If 'Dividend Payment Date(s)' is specified in the Transaction Supplement as 'Share Payment', then the Dividend Payment Date in respect of a Dividend Amount shall fall on a date on or before the date that is two (or any other number that is specified in the Transaction Supplement) Currency Business Days following the day on which the Issuer of the Shares pays the relevant dividend to holders of record of the Shares.
  """
  TERMINATION_DATE = "TERMINATION_DATE"
  """
  Termination date of the swap.
  """
  TRADE_DATE = "TRADE_DATE"
  """
  Trade date of the swap
  """
  UNWIND_EX_DIV = "UNWIND_EX_DIV"
  """
  Pays a fraction of the total on each Unwind Trade Settlement Date which occurs after the Dividend Ex Date, until trade is fully unwound.
  """
  UNWIND_OR_EQUITY_EX_DIV = "UNWIND_OR_EQUITY_EX_DIV"
  """
  Pays a fraction of the Dividend Amount on each Unwind Trade Settlement Date which occurs after the Dividend Ex Date, until position is fully unwound OR on the next Equity Pay Date after the Dividend Pay Date. This will be whichever date comes first or a combination of both.
  """
  UNWIND_OR_EQUITY_PAID = "UNWIND_OR_EQUITY_PAID"
  """
  Pays a fraction of the Dividend Amount on each Unwind Trade Settlement Date which occurs after the Dividend Pay Date, until position is fully unwound OR on the next Equity Pay Date after the Dividend Pay Date. This will be whichever date comes first or a combination of both.
  """
  UNWIND_OR_INTEREST_EX_DIV = "UNWIND_OR_INTEREST_EX_DIV"
  """
  Pays a fraction of the Dividend Amount on each Unwind Trade Settlement Date which occurs after the Dividend Ex Date, until position is fully unwound OR on the next Interest Pay Date after the Dividend Ex Date. This will be whichever date comes first or a combination of both.
  """
  UNWIND_OR_INTEREST_PAID = "UNWIND_OR_INTEREST_PAID"
  """
  Pays a fraction of the Dividend Amount on each Unwind Trade Settlement Date which occurs after the Dividend Pay Date, until position is fully unwound OR on the next Interest Pay Date after the Dividend Pay Date. This will be whichever date comes first or a combination of both.
  """
  UNWIND_PAID = "UNWIND_PAID"
  """
  Pays a fraction of the total on each Unwind Trade Settlement Date which occurs after the Dividend Pay Date, until trade is fully unwound.
  """
