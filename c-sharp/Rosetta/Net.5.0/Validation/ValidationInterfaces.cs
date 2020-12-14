#nullable enable // Allow nullable reference types

namespace Rosetta.Lib.Validation
{
    using System;

    public interface IValidator<T> where T : IRosettaModelObject<T>
    {
        IValidationResult Validate(T obj);
    }

    public interface IValidatorWithArg<T1, T2> where T1 : IRosettaModelObject<T1>
    {
        IValidationResult Validate(T1 obj, T2 field);
    }

    public enum ValidationType
    {
        DATA_RULE, CHOICE_RULE, MODEL_INSTANCE, ONLY_EXISTS, POST_PROCESS_EXCEPTION
    }

    public interface IValidationResult
    {
        bool IsSuccess { get; }

        string ModelObjectName { get; }

        string Name { get; }

        ValidationType ValidationType { get; }

        string Definition { get; }

        string? FailureReason { get; }

        //RosettaPath Path { get; }
    }
}