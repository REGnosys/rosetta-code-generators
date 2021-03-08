namespace Rosetta.Lib
{
    using Rosetta.Lib.Meta;
    using Rosetta.Lib.Validation;

    public interface IRosettaModelObject<R> where R : IRosettaModelObject<R>
    {
        /// <summary>
        /// Gets the meta data associated with this object.
        /// </summary>
        IRosettaMetaData<R> MetaData { get; }

        /// <summary>
        /// Determines whether the object is valid according to the validation rules defined for it.
        /// </summary>
        /// <returns><see cref="IValidationResult"/></returns>
        IValidationResult Validate();
    }
}