#nullable enable // Allow nullable reference types

namespace Rosetta.Lib.Validation
{
    using System;

    public interface IValidator<T> // where T: RosettaModelObject
    {
//        ValidationResult<T> Validate(RosettaPath path, T objectToBeValidated);
//        ValidationResult<T> Validate(RosettaPath path, RosettaModelObjectBuilder objectToBeValidated);
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

		/*
			static <T> ValidationResult<T> success(string name, ValidationType validationType, string modelObjectName, RosettaPath path, string definition)
			{
				return new ModelValidationResult<>(name, validationType, modelObjectName, path, definition, Optional.empty());
			}

			static <T> ValidationResult<T> failure(string name, ValidationType validationType, string modelObjectName, RosettaPath path, string definition, string failureMessage)
			{
				return new ModelValidationResult<>(name, validationType, modelObjectName, path, definition, Optional.of(failureMessage));
			}
		*/
	}
}