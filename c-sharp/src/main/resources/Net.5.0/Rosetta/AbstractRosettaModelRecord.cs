namespace Rosetta.Lib
{
    using Rosetta.Lib.Meta;
    using Rosetta.Lib.Validation;

    /// <summary>
    /// Abstract base class for records which implement <see cref="IRosettaModelObject{R}"/>, which implement one-of data restriction.
    /// </summary>
    /// <typeparam name="R">The class which extends this abstract base class</typeparam>
    public abstract record AbstractRosettaModelRecord<R> : IRosettaModelObject<R> where R : AbstractRosettaModelRecord<R>
    {
        public abstract IRosettaMetaData<R> MetaData { get; }

        public IValidationResult Validate()
        {
            var metaData = MetaData;
            IValidationResult result = metaData.Validator.Validate((R)this);

            foreach (var validator in metaData.DataRules)
            {
                if (!result.IsSuccess)
                {
                    break;
                }
                result = validator.Validate((R)this);
            }
            foreach (var validator in metaData.ChoiceRuleValidators)
            {
                if (!result.IsSuccess)
                {
                    break;
                }
                result = validator.Validate((R)this);
            }
            return result;
        }
    }
}