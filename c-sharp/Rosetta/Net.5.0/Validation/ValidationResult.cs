#nullable enable // Allow nullable reference types

namespace Rosetta.Lib.Validation
{
	using System;
	using System.Collections.Generic;
	using System.Linq;

	public class RosettaPath
	{
		public string BuildPath()
        {
			return "<RosettaPath>";
        }
	}

	public abstract class AbstractValidationResult : IValidationResult
	{
		public AbstractValidationResult(string name, string modelObjectName, RosettaPath path)
		{
			this.Name = name;
			this.Path = path;
			this.ModelObjectName = modelObjectName;
		}

		public abstract bool IsSuccess { get; }

		public abstract string Definition { get; }

		public abstract string? FailureReason { get; }

		public abstract ValidationType ValidationType { get; }

		protected virtual string ValidationDescriptor => ValidationType.ToString();

		public string ModelObjectName { get; }

		public string Name { get; }

		public RosettaPath Path { get; }

		public override string ToString()
		{
			var failureReason = FailureReason;
			var reason = (failureReason != null ? $"because [{failureReason}]" : string.Empty);
			return $"Validation {(IsSuccess ? "SUCCESS" : "FAILURE")} on [{Path.BuildPath()}] for [{ValidationDescriptor}] [{Name}] {reason}";
		}
	}

	public class ModelValidationResult : AbstractValidationResult
	{
		public ModelValidationResult(string name, ValidationType validationType, string modelObjectName, RosettaPath path, string definition, string? failureReason) :
			base(name, modelObjectName, path)
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
        public ChoiceRuleFailure(string name, string modelObjectName, IEnumerable<string> choiceFieldNames, RosettaPath path, IEnumerable<string> populatedFields,
								 IChoiceRuleValidationMethod validationMethod) :
			base(name, modelObjectName, path)
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

	public class OptionalChoiceRuleValidationMethod : IChoiceRuleValidationMethod {
		public string Description => "Zero or one field must be set";

		public bool Check(int fieldCount)
		{
			return fieldCount == 1 || fieldCount == 0;
		}
	}

	public class RequiredChoiceRuleValidationMethod : IChoiceRuleValidationMethod
	{
		public string Description => "One and only one field must be set";

		public bool Check(int fieldCount)
		{
			return fieldCount == 1;
		}
	}

	public class ProcessValidationResult : AbstractValidationResult
	{
		public ProcessValidationResult(string message, string modelObjectName, string processorName, RosettaPath path) :
			base(processorName, modelObjectName, path)
		{
			this.FailureReason = message;
		}

		public override bool IsSuccess => false;

		public override ValidationType ValidationType => ValidationType.POST_PROCESS_EXCEPTION;

		public override string Definition => string.Empty;

		public override string? FailureReason { get; }
	}
}
