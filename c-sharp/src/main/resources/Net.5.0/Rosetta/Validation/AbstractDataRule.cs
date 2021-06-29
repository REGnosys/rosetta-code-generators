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
            IComparisonResult? result = ExecuteDataRule(obj);

            if (result == null)
            {
                // Rule is not applicable
                return ModelValidationResult.Success(Name, ValidationType.DATA_RULE, nameof(T));
            }
            if (result.Result)
            {
                // Rule passed
                return ModelValidationResult.Success(Name, ValidationType.DATA_RULE, nameof(T), Definition);
            }

            // Rule failed
            return ModelValidationResult.Failure(Name, ValidationType.DATA_RULE, nameof(T), Definition, result.Error);
        }

        private IComparisonResult? ExecuteDataRule(T obj)
        {
            var comparisonResult = RuleIsApplicable(obj);

            // Only evaluate if applicable
            if (comparisonResult?.Result == true)
            {
                comparisonResult = EvaluateThenExpression(obj) ?? ComparisonResult.FailureEmptyOperand("No result from then expression");
            }
            else
            {
                comparisonResult = null;
            }
            return comparisonResult;
        }

        protected abstract IComparisonResult? RuleIsApplicable(T obj);

        protected abstract IComparisonResult? EvaluateThenExpression(T obj);

        protected IComparisonResult And(IComparisonResult? left, IComparisonResult? right) => left?.And(right) ?? ComparisonResult.FailureEmptyOperand("Missing left operand for And");
        protected IComparisonResult Or(IComparisonResult? left, IComparisonResult? right) => left?.Or(right) ?? right ?? ComparisonResult.FailureEmptyOperand("Missing operands for Or");

        protected IComparisonResult Exists<T1>(T1? obj)
        {
            return Exists(obj, nameof(T1));
        }

        protected IComparisonResult Exists<T1>(T1? obj, string name)
        {
            if (obj != null)
            {
                return ComparisonResult.Success();
            }
            return ComparisonResult.Failure($"{name} does not exist");
        }

        protected IComparisonResult NotExists<T1>(T1? obj)
        {
            return NotExists(obj, nameof(T1));
        }

        protected IComparisonResult NotExists<T1>(T1? obj, string name)
        {
            if (obj == null)
            {
                return ComparisonResult.Success();
            }
            return ComparisonResult.Failure($"{name} exists");
        }

        protected IComparisonResult OnlyExists<T1>(T1? parent, ISet<string> fields) where T1 : IRosettaModelObject<T1>
        {
            return OnlyExists(parent, fields, nameof(T1));
        }

        protected IComparisonResult OnlyExists<T1>(T1? parent, ISet<string> fields, string name) where T1 : IRosettaModelObject<T1>
        {
            if (parent == null)
            {
                return ComparisonResult.FailureEmptyOperand($"Object {name} does not exist");
            }

            var validationResult = parent.MetaData.OnlyExistsValidator.Validate(parent, fields);

            if (validationResult.IsSuccess)
            {
                return ComparisonResult.Success();
            }
            return ComparisonResult.Failure(validationResult.FailureReason);
        }

        // TODO Can this be converted to use a Func<>?
        protected IComparisonResult IfThen(IComparisonResult ifResult, IComparisonResult thenResult) => ifResult.Result ? thenResult : ComparisonResult.Success();
    }
}
