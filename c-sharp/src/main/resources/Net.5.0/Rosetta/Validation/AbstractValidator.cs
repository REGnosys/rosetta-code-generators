#nullable enable // Allow nullable reference types

namespace Rosetta.Lib.Validation
{
    using System.Collections.Generic;
    using System.Linq;

    using Rosetta.Lib;

    public abstract class AbstractValidator<T> : IValidator<T> where T : IRosettaModelObject<T>
    {
        protected string Name => GetType().Name;

        protected abstract IEnumerable<IComparisonResult> GetResults(T obj);

        public IValidationResult Validate(T? obj)
        {
            if (obj == null)
            {
                return ModelValidationResult.Failure(Name, ValidationType.MODEL_INSTANCE, nameof(T), "", "Object is not set");
            }

            var errors = GetResults(obj).Where(r => !r.Result);

            if (errors.Any())
            {
                return ModelValidationResult.Failure(Name, ValidationType.MODEL_INSTANCE, nameof(T), "", string.Join("; ", errors.Select(r => r.Error)));
            }

            return ModelValidationResult.Success(Name, ValidationType.MODEL_INSTANCE, nameof(T), "");
        }

        public static IComparisonResult CheckCardinality(string typeName, string propertyName, int actual, int min, int max)
        {
            return CheckCardinality($"{typeName}.{propertyName}", actual, min, max);
        }

        public static IComparisonResult CheckCardinality(string msgPrefix, int actual, int min, int max)
        {
            if (actual < min)
            {
                return ComparisonResult.Failure($"{msgPrefix} - Expected cardinality lower bound of [{min}] found [{actual}]");
            }
            else if (max > 0 && actual > max)
            {
                return ComparisonResult.Failure($"{msgPrefix} - Expected cardinality upper bound of [{max}] found [{actual}]");
            }
            return ComparisonResult.Success();
        }
    }

    public abstract class AbstractOnlyExistsValidator<T> : IValidatorWithArg<T, ISet<string>> where T : IRosettaModelObject<T>
    {
        protected string Name => GetType().Name;

        protected abstract IDictionary<string, bool> GetFields(T obj);

        public IValidationResult Validate(T? obj, ISet<string> fields)
        {
            if (obj == null)
            {
                return ModelValidationResult.Failure(Name, ValidationType.ONLY_EXISTS, nameof(T), "", "Parent object is not set");
            }

            var fieldExistenceMap = GetFields(obj);


            var setFields = fieldExistenceMap.Where(v => v.Value && fields.Contains(v.Key)).Select(v => v.Key);
            if (setFields.Count() != fields.Count())
            {
                return ModelValidationResult.Failure(Name, ValidationType.ONLY_EXISTS, nameof(T), "",
                        $"All fields are not set.  Expected [{string.Join(',', fields)}] but found only [{string.Join(',', setFields)}].");
            }

            var otherSetFields = fieldExistenceMap.Where(v => v.Value && !fields.Contains(v.Key)).Select(v => v.Key);
            if (otherSetFields.Any())
            {
                return ModelValidationResult.Failure(Name, ValidationType.ONLY_EXISTS, nameof(T), "",
                        $"[{string.Join(',', fields)}] are not the only fields set. Other set fields: {string.Join(',', otherSetFields)}");
            }
            return ModelValidationResult.Success(Name, ValidationType.ONLY_EXISTS, nameof(T), "");
        }

        public static bool IsSet(object? field) => field != null;

        public static bool IsSet(IEnumerable<T> field) => field != null && field.Any(e => e != null);

    }
}