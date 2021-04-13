#nullable enable // Allow nullable reference types

namespace Rosetta.Lib.Validation
{
	using System;
	using System.Collections.Generic;
	using System.Linq;

	/*
	public class RosettaPath
	{
		public string BuildPath()
        {
			return "<RosettaPath>";
        }
	} */

	public abstract class AbstractValidationResult : IValidationResult
	{
		public AbstractValidationResult(string name, string modelObjectName)
		{
			this.Name = name;
			this.ModelObjectName = modelObjectName;
		}

		public abstract bool IsSuccess { get; }

		public abstract string Definition { get; }

		public abstract string? FailureReason { get; }

		public abstract ValidationType ValidationType { get; }

		protected virtual string ValidationDescriptor => ValidationType.ToString();

		public string ModelObjectName { get; }

		public string Name { get; }

		public override string ToString()
		{
			var failureReason = FailureReason;
			var reason = (failureReason != null ? $"because [{failureReason}]" : string.Empty);
			return $"Validation {(IsSuccess ? "SUCCESS" : "FAILURE")} for [{ValidationDescriptor}] [{Name}] {reason}";
		}
	}

	public class ModelValidationResult : AbstractValidationResult
	{
		public static IValidationResult Success(string name, ValidationType validationType, string modelObjectName)
		{
			return new ModelValidationResult(name, validationType, modelObjectName, string.Empty);
		}

		public static IValidationResult Success(string name, ValidationType validationType, string modelObjectName, string definition)
		{
			return new ModelValidationResult(name, validationType, modelObjectName, definition);
		}

		public static IValidationResult Failure(string name, ValidationType validationType, string modelObjectName, string definition, string failureMessage)
		{
			return new ModelValidationResult(name, validationType, modelObjectName, definition, failureMessage);
		}

		public ModelValidationResult(string name, ValidationType validationType, string modelObjectName, string definition, string? failureReason = null) :
			base(name, modelObjectName)
		{
			this.ValidationType = validationType;
			this.Definition = definition;
			this.FailureReason = failureReason;
		}

        public override bool IsSuccess => FailureReason == null;

		public override string? FailureReason { get; }

		public override string Definition { get; }

		public override ValidationType ValidationType { get; }
	}

	public class ChoiceRuleFailure : AbstractValidationResult
	{
        public ChoiceRuleFailure(string name, string modelObjectName, IEnumerable<string> choiceFieldNames, IEnumerable<string> populatedFields,
								 IChoiceRuleValidationMethod validationMethod) :
			base(name, modelObjectName)
		{
			this.PopulatedFields = populatedFields;
			this.ChoiceFieldNames = choiceFieldNames;
			this.ValidationMethod = validationMethod;
		}

		public override bool IsSuccess => false;

        public IEnumerable<string> PopulatedFields { get; }

        public IEnumerable<string> ChoiceFieldNames { get; }

        public IChoiceRuleValidationMethod ValidationMethod { get; }

        public override string Definition => string.Join(", ", ChoiceFieldNames.Select(n => $"{ValidationMethod.Description} of '{n}'. ").ToArray());

		public override string? FailureReason => Definition + (PopulatedFields.Any() ? string.Join(", ", PopulatedFields.Select(f => $"Set fields are '{f}'.").ToArray()) : "No fields are set.");

		public override ValidationType ValidationType => ValidationType.CHOICE_RULE;

		protected override string ValidationDescriptor => $"{base.ValidationDescriptor}:{ValidationMethod.ToString()}";
	}

	public interface IChoiceRuleValidationMethod
	{
		string Description { get; }

		bool Check(int fieldCount);
	}

	public sealed class OptionalChoiceRuleValidationMethod : IChoiceRuleValidationMethod {
        private static readonly IChoiceRuleValidationMethod singleton = new OptionalChoiceRuleValidationMethod();

		public static IChoiceRuleValidationMethod Instance => singleton;

		public string Description => "Zero or one field must be set";

		public bool Check(int fieldCount)
		{
			return fieldCount == 1 || fieldCount == 0;
		}
	}

	public class RequiredChoiceRuleValidationMethod : IChoiceRuleValidationMethod
	{
		private static readonly IChoiceRuleValidationMethod singleton = new RequiredChoiceRuleValidationMethod();

		public static IChoiceRuleValidationMethod Instance => singleton;

		public string Description => "One and only one field must be set";

		public bool Check(int fieldCount)
		{
			return fieldCount == 1;
		}
	}

	public class ProcessValidationResult : AbstractValidationResult
	{
		public ProcessValidationResult(string message, string modelObjectName, string processorName) :
			base(processorName, modelObjectName)
		{
			this.FailureReason = message;
		}

		public override bool IsSuccess => false;

		public override ValidationType ValidationType => ValidationType.POST_PROCESS_EXCEPTION;

		public override string Definition => string.Empty;

		public override string? FailureReason { get; }
	}
}
