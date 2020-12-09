#nullable enable // Allow nullable reference types

namespace Rosetta.Lib.Validation
{
    using System;
    using System.Collections.Generic;
    using System.Linq;

    public abstract class AbstractDataRule<T> : IValidator<T> where T : IRosettaModelObject<T>
    {
        protected string Name => GetType().Name;

        protected abstract string Definition { get; }

        public IValidationResult Validate(T obj)
        {
            IComparisonResult result = ExecuteDataRule(obj);
            if (result.Result)
            {
                return ModelValidationResult.Success(Name, ValidationType.DATA_RULE, nameof(T), Definition);
            }

            return ModelValidationResult.Failure(Name, ValidationType.DATA_RULE, nameof(T), Definition, result.Error);
        }

        private IComparisonResult ExecuteDataRule(T obj)
        {
            var comparisonResult = RuleIsApplicable(obj);

            if (comparisonResult == null)
            {
                return ComparisonResult.FailureEmptyOperand("Unable to determine if rule is applicable");
            }
            if (comparisonResult.Result)
            {
                return EvaluateThenExpression(obj) ?? ComparisonResult.FailureEmptyOperand("No result from then expression");
            }
            return ComparisonResult.Success();
        }

        protected abstract IComparisonResult? RuleIsApplicable(T obj);

        protected abstract IComparisonResult? EvaluateThenExpression(T obj);

        protected IComparisonResult And(IComparisonResult? left, IComparisonResult? right) => left?.And(right) ?? ComparisonResult.FailureEmptyOperand("Missing left operand for And");
        protected IComparisonResult Or(IComparisonResult? left, IComparisonResult? right) => left?.Or(right) ?? right ?? ComparisonResult.FailureEmptyOperand("Missing operands for Or");

        protected IComparisonResult Exists<T1>(T1? obj) where T1 : class
        {
            if (obj != null)
            {
                return ComparisonResult.Success();
            }
            return ComparisonResult.Failure($"{nameof(T1)} does not exist");
        }

        protected IComparisonResult Exists<T1>(T1? obj) where T1 : struct
        {
            if (obj != null)
            {
                return ComparisonResult.Success();
            }
            return ComparisonResult.Failure($"{nameof(T1)} does not exist");
        }

        protected IComparisonResult NotExists<T1>(T1? obj) where T1 : class
        {
            if (obj == null)
            {
                return ComparisonResult.Success();
            }
            return ComparisonResult.Failure($"{nameof(T1)} exists");
        }

        protected IComparisonResult NotExists<T1>(T1? obj) where T1 : struct
        {
            if (obj == null)
            {
                return ComparisonResult.Success();
            }
            return ComparisonResult.Failure($"{nameof(T1)} exists");
        }

        // TODO: What does OnlyExists really mean??!
        protected IComparisonResult OnlyExists<T1>(IEnumerable<T1>? collection)
        {
            if (collection == null)
            {
                return ComparisonResult.FailureEmptyOperand("Collection does not exist");
            }
            if (collection.Count() > 1)
            {
                return ComparisonResult.FailureEmptyOperand("Collection has more than one element");
            }
            return ComparisonResult.Success();
        }

        protected IComparisonResult OnlyExists<T1>(T1? obj) where T1 : class
        {
            if (obj == null)
            {
                return ComparisonResult.FailureEmptyOperand("Object does not exist");
            }
            return ComparisonResult.Success();
        }

        // TODO Can this be converted to use a Func<>?
        protected IComparisonResult IfThen(IComparisonResult ifResult, IComparisonResult thenResult) => ifResult.Result ? thenResult : ComparisonResult.Success();
    }
}
