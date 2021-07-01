#nullable enable // Allow nullable reference types

namespace Rosetta.Lib.Meta
{
    using System;
    using System.Collections.Generic;
    using Newtonsoft.Json;
    using Rosetta.Lib.Validation;

    public interface IFieldWithMeta<T> where T : class
    {
        T Value { get; }
    }

    public interface IEnumFieldWithMeta<T> where T : struct, System.Enum
    {
        T Value { get; }
    }

    public interface IValueFieldWithMeta<T> where T : struct
    {
        T Value { get; }
    }

    public interface IFieldWithMetaBuilder<T>
    {
        IFieldWithMetaBuilder<T> SetValue(T value);
    }

    public interface IGlobalKeyFields
    {
        string GlobalKey { get; }

        string ExternalKey { get; }
    }

    interface IGlobalKeyFieldsBuilder : IGlobalKeyFields
    {
        IGlobalKeyFieldsBuilder SetGlobalKey(string globalKey);

        IGlobalKeyFieldsBuilder SetExternalKey(string externalKey);
    }

    public interface IMetaDataFields
    {
        string Scheme { get; }
    }

    interface IMetaDataFieldsBuilder : IMetaDataFields
    {
        IMetaDataFieldsBuilder SetScheme(string scheme);
    }

    public interface IReferenceWithMeta<T> where T : class
    {
        string? GlobalReference { get; }
        string? ExternalReference { get; }
        T? Value { get; }
    }

    public interface IValueReferenceWithMeta<T> where T : struct
    {
        string? GlobalReference { get; }
        string? ExternalReference { get; }
        T? Value { get; }
    }

    public interface IReferenceWithMetaBuilderBase<I>
    {
        IReferenceWithMetaBuilderBase<I> SetGlobalReference(string globalKey);
        IReferenceWithMetaBuilderBase<I> SetExternalReference(string ExternalKey);
        string? GlobalReference { get; }
        string? ExternalReference { get; }
        //TODO: Type ValueType { get; }
    }

    public interface IReferenceWithMetaBuilder<I> : IReferenceWithMetaBuilderBase<I>
    {
        new IReferenceWithMetaBuilder<I> SetGlobalReference(string globalKey);
        new IReferenceWithMetaBuilder<I> SetExternalReference(string ExternalKey);

        //TODO: RosettaModelObjectBuilder getValue();
        IReferenceWithMetaBuilder<I> SetValue(I value);
    }

    public interface IBasicReferenceWithMetaBuilder<I> : IReferenceWithMetaBuilderBase<I>
    {
        new IBasicReferenceWithMetaBuilder<I> SetGlobalReference(string globalKey);
        new IBasicReferenceWithMetaBuilder<I> SetExternalReference(string ExternalKey);

        I Value { get; }
        IBasicReferenceWithMetaBuilder<I> SetValue(I value);
    }

    public interface IRosettaMetaData<T> where T : IRosettaModelObject<T>
    {
        [JsonIgnore]
        IEnumerable<IValidator<T>> DataRules { get; }

        [JsonIgnore]
        IEnumerable<IValidator<T>> ChoiceRuleValidators { get; }

        /*
        [JsonIgnore]

        TODO: IEnumerable<Function<T, QualifyResult>> GetQualifyFunctions(QualifyFunctionFactory factory);
        */

        [JsonIgnore]
        IValidator<T> Validator { get; }

        [JsonIgnore]
        IValidatorWithArg<T, ISet<string>> OnlyExistsValidator { get; }
    }
}
