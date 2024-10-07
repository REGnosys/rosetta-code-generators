// This file is included to implement functions which can not currently be generated.
//
#nullable enable // Allow nullable reference types

namespace Org.Isda.Cdm.Functions
{
    using System.Collections.Generic;
    using System.Linq;

    using Org.Isda.Cdm;
    using Org.Isda.Cdm.MetaFields;
    using Rosetta.Lib.Functions;

    public class FpmlIrd8 : IRosettaFunction
    {
        static public bool Evaluate(Trade trade, IEnumerable<Account> accounts)
        {
            if (trade.Counterparty.Count() != 2)
                return false;

            var parties = trade.Counterparty.ToArray();
            ReferenceWithMetaParty? party1 = parties[0].PartyReference;
            ReferenceWithMetaParty? party2 = parties[1].PartyReference;

            if (party1 == null || party2 == null)
                return false;

            if (!party1.Equals(party2))
                return true;

            // Same party on each side of trade, so accounts must different
            return accounts.Count(a => party1.Equals(a.PartyReference)) == 2;
        }
    }

    public class Sum : IRosettaFunction
    {
        static public double Evaluate(IEnumerable<double> values)
        {
            return values.Sum();
        }

        static public decimal Evaluate(IEnumerable<decimal?> values)
        {
            var value = values.Aggregate((total, next) => total + next);
            return value != null ? value.Value : default;
        }

        static public decimal Evaluate(IEnumerable<decimal>? values)
        {
            return values == null ? default : values.Sum();
        }
    }

    // TEMPORARY: Should be generated
    public class PriceQuantityTriangulation : IRosettaFunction
    {
        static public bool Evaluate(IEnumerable<TradeLot> tradeLots)
        {
            return true;
        }
    }

    // TEMPORARY: Should be generated
    public class FilterOpenTradeStates : IRosettaFunction
    {
        static public IEnumerable<TradeState> Evaluate(IEnumerable<TradeState> tradeStates)
        {
            // TODO Implement function
            return tradeStates;
        }
    }

    // TEMPORARY: Implement function
    public class FilterPartyRole : IRosettaFunction
    {
        static public IEnumerable<PartyRole> Evaluate(IEnumerable<PartyRole> partyRoles, Enums.PartyRole partyRoleEnum)
        {
            return Enumerable.Empty<PartyRole>();
        }
    }

    // TEMPORARY: Implement function
    public class Qualify_AssetClass_Equity : IRosettaFunction
    {
        static public bool Evaluate(Product product)
        {
            return false;
        }
    }
}
