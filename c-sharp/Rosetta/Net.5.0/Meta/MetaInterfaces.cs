#nullable enable // Allow nullable reference types

namespace Rosetta.Lib.Meta
{
    using System;
    using System.Collections.Generic;
    using Rosetta.Lib.Validation;

    public interface IFieldWithMeta<T> where T : class
    {
        T? Value { get; }
    }

    public interface IEnumFieldWithMeta<T> where T : struct, System.Enum
    {
        T? Value { get; }
    }

    public interface IValueFieldWithMeta<T> where T : struct
    {
        T? Value { get; }
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

    public interface IReferenceWithMeta<T> : IFieldWithMeta<T> where T : class
    {
        string? GlobalReference { get; }
        string? ExternalReference { get; }
    }

    public interface IValueReferenceWithMeta<T> : IValueFieldWithMeta<T> where T : struct
    {
        string? GlobalReference { get; }
        string? ExternalReference { get; }
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

    public interface IBasicReferenceWithMetaBuilder<I> : IReferenceWithMetaBuilderBase<I> {
        new IBasicReferenceWithMetaBuilder<I> SetGlobalReference(string globalKey) ;
        new IBasicReferenceWithMetaBuilder<I> SetExternalReference(string ExternalKey) ;

        I getValue();
        IBasicReferenceWithMetaBuilder<I> SetValue(I value);
    }

    public interface IRosettaMetaData<out T> where T: IRosettaModelObject<T>
    {
        IEnumerable<IValidator<T>> DataRules { get; }

        IEnumerable<IValidator<T>> ChoiceRuleValidators { get; }


        //TODO: IEnumerable<Function<T, QualifyResult>> GetQualifyFunctions(QualifyFunctionFactory factory);

        IValidator<T> Validator { get; }

        //TODO: ValidatorWithArg<T, string> OnlyExistsValidator { get; }
    }

}

