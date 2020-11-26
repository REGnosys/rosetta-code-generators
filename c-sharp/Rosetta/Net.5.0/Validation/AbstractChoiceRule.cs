#nullable enable // Allow nullable reference types

namespace Rosetta.Lib.Validation
{
    using System;
    using System.Collections.Generic;

    public abstract class AbstractChoiceRule<T> : IValidator<T> where T : IRosettaModelObject<T>
    {
        protected string Name => GetType().Name;

        protected abstract IEnumerable<string> ChoiceFieldNames { get; }

        protected abstract IChoiceRuleValidationMethod ValidationMethod { get; }

        protected abstract ICollection<string> GetPopulatedFieldNames(T obj);

        public IValidationResult Validate(T obj)
        {
            var validationMethod = ValidationMethod;
            var populatedFieldNames = GetPopulatedFieldNames(obj);

            if (validationMethod.Check(populatedFieldNames.Count))
            {
                return ModelValidationResult.Success(Name, ValidationType.CHOICE_RULE, nameof(T));
            }
            return new ChoiceRuleFailure(Name, nameof(T), ChoiceFieldNames, populatedFieldNames, validationMethod);
        }

    }

}
