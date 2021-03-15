#nullable enable // Allow nullable reference types

namespace Rosetta.Lib.Functions
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    using NodaTime;

    using Rosetta.Lib.Validation;

    static class Test
    {
        static internal IComparisonResult? Object<T>(T? t)
        {
            if (t == null)
            {
                return ComparisonResult.FailureEmptyOperand("Value does not exist");
            }
            return null;
        }

        static internal IComparisonResult? Collection<T>(IEnumerable<T>? collection)
        {
            if (collection == null)
            {
                return ComparisonResult.FailureEmptyOperand("Collection does not exist");
            }
            return null;
        }
    }

    /// <summary>
    /// Extend <see cref="IEnumerable{T}"/> to ensure a collection can never be null.
    /// </summary>
    public static class EnumerableExtension
    {
        // NB: Required due to design failing of IEnumerable<>.SelectMany method.
        public static IEnumerable<T> EmptyIfNull<T>(this IEnumerable<T>? collection) => collection ?? Enumerable.Empty<T>();
    }

    /// <summary>
    /// Extend <see cref="IEnumerable{T}"/> to test set membership.
    /// </summary>
    public static class IncludesExtension
    {
        // Tests if all elements of the second collection are present in the initial collection.
        public static IComparisonResult Includes<T>(this IEnumerable<T> collection1, IEnumerable<T>? collection2) =>
            Test.Collection(collection1) ??
            Test.Collection(collection2) ??
            ComparisonResult.FromBoolean(collection2?.All(c => collection1.Contains(c)), "First collection does not contain all elements of second collection");

        // Tests if the collection contains the specified value
        public static IComparisonResult Includes<T>(this IEnumerable<T> collection, T obj) =>
            ComparisonResult.FromBoolean(collection.Any(c => c?.Equals(obj) == true), "Collection does not contain the specified value");
    }

    /// <summary>
    /// Extend <see cref="IEnumerable{T}"/> and <see cref="decimal"/> to perform equality and inequality tests.
    /// </summary>
    public static class EqualsExtension
    {
        // IEnumerable<T> equality to a collection.
        public static IComparisonResult IsEqual<T>(this IEnumerable<T>? collection1, IEnumerable<T>? collection2) =>
            Test.Collection(collection1) ??
            Test.Collection(collection2) ??
            ComparisonResult.FromBoolean(collection1!.SequenceEqual(collection2!), "Not all collection values match the specified value");

        public static IComparisonResult NotEquals<T>(this IEnumerable<T>? collection1, IEnumerable<T>? collection2) =>
            Test.Collection(collection1) ??
            Test.Collection(collection2) ??
            ComparisonResult.FromBoolean(!collection1!.SequenceEqual(collection2!), "Some collection values match the specified value");

        // IEnumerable<T> equality to a single value.
        public static IComparisonResult IsEqual<T>(this IEnumerable<T> collection, T obj) =>
            Test.Collection(collection) ??
            ComparisonResult.FromBoolean(collection!.All(c => c?.Equals(obj) == true), "Not all collection values match the specified value");

        public static IComparisonResult NotEquals<T>(this IEnumerable<T> collection, T obj) =>
            Test.Collection(collection) ??
            ComparisonResult.FromBoolean(collection!.All(c => c?.Equals(obj) == false), "Some collection values match the specified value");

        public static IComparisonResult IsEqual<T>(this IEnumerable<T?> collection, T obj) where T : struct, Enum =>
            Test.Collection(collection) ??
            ComparisonResult.FromBoolean(collection!.All(c => c?.Equals(obj) == true), "Not all collection values match the specified value");

        public static IComparisonResult NotEquals<T>(this IEnumerable<T?> collection, T obj) where T : struct, Enum =>
            Test.Collection(collection) ??
            ComparisonResult.FromBoolean(collection!.All(c => c?.Equals(obj) == false), "Some collection values match the specified value");

        public static IComparisonResult IsEqual<T, T1>(this IEnumerable<T1> collection, T obj)
                where T : struct, Enum
                where T1 : Meta.IEnumFieldWithMeta<T> =>
            Test.Collection(collection) ??
            ComparisonResult.FromBoolean(collection.All(c => c.Value.Equals(obj) == true), "Not all collection values match the specified value");

        public static IComparisonResult NotEquals<T, T1>(this IEnumerable<T1> collection, T obj)
                where T : struct, Enum
                where T1 : Meta.IEnumFieldWithMeta<T> =>
            Test.Collection(collection) ??
            ComparisonResult.FromBoolean(collection.All(c => c.Value.Equals(obj) == false), "Some collection values match the specified value");

        // decimal overloads
        public static IComparisonResult IsEqual(this decimal value, IEnumerable<decimal>? values) =>
            Test.Collection(values) ??
            ComparisonResult.FromBoolean(values!.All(v => v == value), "Not all collection values match the specified number");

        public static IComparisonResult NotEquals(this decimal value, IEnumerable<decimal>? values) =>
            Test.Collection(values) ??
            ComparisonResult.FromBoolean(values!.All(v => v != value), "Some collection values match the specified number");

        public static IComparisonResult IsEqual(this decimal value, IEnumerable<decimal?>? values) =>
            Test.Collection(values) ??
            ComparisonResult.FromBoolean(values!.All(v => v == value), "Not all collection values match the specified number");

        public static IComparisonResult NotEquals(this decimal value, IEnumerable<decimal?>? values) =>
            Test.Collection(values) ??
            ComparisonResult.FromBoolean(values!.All(v => v != value), "Some collection values match the specified number");

        public static IComparisonResult IsEqual(this IEnumerable<decimal?>? values, decimal value) =>
            Test.Collection(values) ??
            ComparisonResult.FromBoolean(values!.All(v => v == value), "Not all collection values match the specified number");

        public static IComparisonResult NotEquals(this IEnumerable<decimal?>? values, decimal value) =>
            Test.Collection(values) ??
            ComparisonResult.FromBoolean(values!.All(v => v != value), "Some collection values match the specified number");
    }

    /// <summary>
    /// Extend IEnumerable<> by adding ordering comparisons (<, <=, >, >=) relative to a single value.
    /// </summary>
    public static class GreaterThanExtension
    {
        // generic comparisons
        private static IComparisonResult Compare<T>(IEnumerable<T>? collection, T? obj, Func<int, bool> func, string op) where T : IComparable =>
            Test.Object(obj) ??
            Test.Collection(collection) ??
            ComparisonResult.FromBoolean(collection!.All(c => func(c.CompareTo(obj)) == true), $"Not all elements of collection are ${op} {obj}");

        public static IComparisonResult GreaterThan<T>(this IEnumerable<T>? collection, T? obj) where T : IComparable => Compare(collection, obj, i => i > 0, "greater than");
        public static IComparisonResult GreaterThanEquals<T>(this IEnumerable<T> collection, T obj) where T : IComparable => Compare(collection, obj, i => i >= 0, "greater than or equal to");
        public static IComparisonResult LessThan<T>(this IEnumerable<T> collection, T obj) where T : IComparable => Compare(collection, obj, i => i < 0, "less than");
        public static IComparisonResult LessThanEquals<T>(this IEnumerable<T> collection, T obj) where T : IComparable => Compare(collection, obj, i => i <= 0, "less than or equal to");

        // LocalDate overloads
        private static IComparisonResult Compare(IEnumerable<LocalDate?>? collection, LocalDate? obj, Func<int?, bool> func, string op) =>
            Test.Object(obj) ??
            Test.Collection(collection) ??
            ComparisonResult.FromBoolean(collection!.All(c => c != null && func(c?.CompareTo(obj!.Value)) == true), $"Not all elements of collection are ${op} {obj}");

        public static IComparisonResult GreaterThan(this IEnumerable<LocalDate?>? collection, LocalDate? obj) => Compare(collection, obj, i => i > 0, "greater than");
        public static IComparisonResult GreaterThanEquals(this IEnumerable<LocalDate?>? collection, LocalDate? obj) => Compare(collection, obj, i => i >= 0, "greater than or equal to");
        public static IComparisonResult LessThan(this IEnumerable<LocalDate?>? collection, LocalDate? obj) => Compare(collection, obj, i => i < 0, "less than");
        public static IComparisonResult LessThanEquals(this IEnumerable<LocalDate?>? collection, LocalDate? obj) => Compare(collection, obj, i => i <= 0, "less than or equal to");

        // int overloads
        private static IComparisonResult CompareInt(IEnumerable<int?>? collection, Func<int?, bool> func, string description) =>
            Test.Collection(collection) ??
            ComparisonResult.FromBoolean(collection!.All(c => func(c) == true), $"Not all elements of collection are ${description}");

        public static IComparisonResult GreaterThan(this IEnumerable<int?>? collection, int? obj) =>
            Test.Object(obj) ??
            CompareInt(collection, i => i > obj, $"greater than {obj}");

        public static IComparisonResult GreaterThanEquals(this IEnumerable<int?>? collection, int? obj) =>
            Test.Object(obj) ??
            CompareInt(collection, i => i >= obj, $"greater than or equal to {obj}");

        public static IComparisonResult LessThan(this IEnumerable<int?>? collection, int? obj) =>
            Test.Object(obj) ??
            CompareInt(collection, i => i < obj, $"less than {obj}");

        public static IComparisonResult LessThanEquals(this IEnumerable<int?>? collection, int? obj) =>
            Test.Object(obj) ??
            CompareInt(collection, i => i <= obj, $"less than or equal to {obj}");
    }
}