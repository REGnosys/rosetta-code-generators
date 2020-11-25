#nullable enable // Allow nullable reference types

namespace Rosetta.Lib.Functions
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    using NodaTime;

    public static class ContainsExtension
    {
        public static bool Contains<T>(this IEnumerable<T> collection1, IEnumerable<T> collection2)
        {
            return collection2.All(c => collection1.Contains(c));
        }
    }

    /// <summary>
    /// Extend <see cref="decimal"/> and <see cref="IEnumerable{T}"/> to perform equality and inequality tests.
    /// </summary>
    public static class EqualsExtension
    {
        // decimal equality
        public static bool Equals(this decimal? value, IEnumerable<decimal>? values)
        {
            return value != null && values?.All(v => v == value) == true;
        }

        public static bool NotEquals(this decimal? value, IEnumerable<decimal>? values) => !value.Equals(values);


        // IEnumerable<T> equality to a single value.
        public static bool Equals<T>(this IEnumerable<T>? collection, T? obj) where T : class
        {
            return collection?.All(c => c != null && c.Equals(obj)) == true;
        }

        public static bool Equals<T>(this IEnumerable<T>? collection, T? obj) where T : struct, Enum
        {
            return collection?.All(c => c.Equals(obj)) == true;
        }
        public static bool Equals<T>(this IEnumerable<T?>? collection, T obj) where T : struct, Enum
        {
            return collection?.All(c => c != null && c.Equals(obj)) == true;
        }
        public static bool Equals<T>(this IEnumerable<T?>? collection, T? obj) where T : struct, Enum
        {
            return collection?.All(c => c != null && c.Equals(obj)) == true;
        }

        public static bool NotEquals<T>(this IEnumerable<T>? collection, T? obj) where T : class => collection?.Equals(obj) != true;
        public static bool NotEquals<T>(this IEnumerable<T>? collection, T? obj) where T : struct, Enum => collection?.Equals(obj) != true;
        public static bool NotEquals<T>(this IEnumerable<T?>? collection, T? obj) where T : struct, Enum => collection?.Equals(obj) != true;
        public static bool NotEquals<T>(this IEnumerable<T?>? collection, T obj) where T : struct, Enum => collection?.Equals(obj) != true;

        // Special case for decimals
        public static bool Equals(this IEnumerable<decimal?>? collection, decimal obj) {
            return collection?.All(c => c.Equals(obj)) == true;
        }
        public static bool Equals(this IEnumerable<decimal>? collection, decimal obj)
        {
            return collection?.All(c => c.Equals(obj)) == true;
        }

        public static bool NotEquals(this IEnumerable<decimal?>? collection, decimal obj) => collection?.Equals(obj) != true;
        public static bool NotEquals(this IEnumerable<decimal>? collection, decimal obj) => collection?.Equals(obj) != true;

        // Special case for integers
        public static bool Equals(this IEnumerable<int?>? collection, int obj)
        {
            return collection?.All(c => c.Equals(obj)) == true;
        }
        public static bool Equals(this IEnumerable<int>? collection, int obj)
        {
            return collection?.All(c => c.Equals(obj)) == true;
        }

        public static bool NotEquals(this IEnumerable<int?>? collection, int obj) => collection?.Equals(obj) != true;
        public static bool NotEquals(this IEnumerable<int>? collection, int obj) => collection?.Equals(obj) != true;

        // IEnumerable<T> equality to a collection.
        public static bool Equals<T>(this IEnumerable<T>? collection1, IEnumerable<T>? collection2)
        {
            return collection2 != null && collection1?.SequenceEqual(collection2) == true;
        }

        public static bool NotEquals<T>(this IEnumerable<T> collection1, IEnumerable<T> collection2) => collection1?.Equals(collection2) != true;
    }

    /// <summary>
    /// Extend IEnumerable<> by adding ordering comparisons (<, <=, >, >=) relative to a single value.
    /// </summary>
    public static class GreaterThanExtension
    {
        // generic comparisons
        private static bool Compare<T>(IEnumerable<T>? collection, T? obj, Func<int, bool> func) where T : class, IComparable
        {
            return collection?.All(c => func(c.CompareTo(obj))) == true;
        }

        private static bool Compare<T>(IEnumerable<T>? collection, T? obj, Func<int, bool> func) where T : struct, IComparable
        {
            return collection?.All(c => func(c.CompareTo(obj))) == true;
        }

        public static bool GreaterThan<T>(this IEnumerable<T>? collection, T? obj) where T : class, IComparable => Compare(collection, obj, i => i > 0);
        public static bool GreaterThanEquals<T>(this IEnumerable<T>? collection, T? obj) where T : class, IComparable => Compare(collection, obj, i => i >= 0);
        public static bool LessThan<T>(this IEnumerable<T>? collection, T? obj) where T : class, IComparable => Compare(collection, obj, i => i < 0);
        public static bool LessThanEquals<T>(this IEnumerable<T>? collection, T? obj) where T : class, IComparable => Compare(collection, obj, i => i <= 0);

        public static bool GreaterThan<T>(this IEnumerable<T>? collection, T? obj) where T : struct, IComparable => Compare(collection, obj, i => i > 0);
        public static bool GreaterThanEquals<T>(this IEnumerable<T>? collection, T? obj) where T : struct, IComparable => Compare(collection, obj, i => i >= 0);
        public static bool LessThan<T>(this IEnumerable<T>? collection, T? obj) where T : struct, IComparable => Compare(collection, obj, i => i < 0);
        public static bool LessThanEquals<T>(this IEnumerable<T>? collection, T? obj) where T : struct, IComparable => Compare(collection, obj, i => i <= 0);

        // LocalDate comparisons
        private static bool Compare(IEnumerable<LocalDate?>? collection, LocalDate? obj, Func<int?, bool> func)
        {
            return obj != null && collection?.All(c => c != null && func(c?.CompareTo(obj.Value))) == true;
        }

        public static bool GreaterThan(this IEnumerable<LocalDate?>? collection, LocalDate? obj) => Compare(collection, obj, i => i > 0);
        public static bool GreaterThanEquals(this IEnumerable<LocalDate?>? collection, LocalDate? obj) => Compare(collection, obj, i => i >= 0);
        public static bool LessThan(this IEnumerable<LocalDate?>? collection, LocalDate? obj) => Compare(collection, obj, i => i < 0);
        public static bool LessThanEquals(this IEnumerable<LocalDate?>? collection, LocalDate? obj) => Compare(collection, obj, i => i <= 0);

        // int comparisons
        private static bool CompareInt(IEnumerable<int?>? collection, Func<int?, bool> func)
        {
            return collection?.All(c => func(c)) == true;
        }

        public static bool GreaterThan(this IEnumerable<int?>? collection, int? obj) => obj != null && CompareInt(collection, i => i > obj);
        public static bool GreaterThanEquals(this IEnumerable<int?>? collection, int? obj) => obj != null && CompareInt(collection, i => i >= obj);
        public static bool LessThan(this IEnumerable<int?>? collection, int? obj) => obj != null && CompareInt(collection, i => i < obj);
        public static bool LessThanEquals(this IEnumerable<int?>? collection, int? obj) => obj != null && CompareInt(collection, i => i <= obj);
    }
}