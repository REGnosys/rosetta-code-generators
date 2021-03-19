namespace Rosetta.Lib
{
    using Rosetta.Lib.Meta;
    using Rosetta.Lib.Validation;

    /// <summary>
    /// Abstract base class for <see cref="IRosettaModelObject{R}"/> which is not defined to use one-of.
    /// </summary>
    /// <typeparam name="R">Class extending the abstract base class</typeparam>
    public abstract class AbstractRosettaModelObject<R> : IRosettaModelObject<R> where R : AbstractRosettaModelObject<R>
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