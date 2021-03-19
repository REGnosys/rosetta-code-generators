namespace Rosetta.Lib.Attributes
{
    using System;

    /// <summary>
    /// Specifies the name of the data rule being implemented.
    /// </summary>
    [AttributeUsage(AttributeTargets.Class, Inherited = false)]
    public class RosettaChoiceRuleAttribute : Attribute
    {
        public string Value { get; set; }

        public RosettaChoiceRuleAttribute(string value)
        {
            Value = value;
        }
    }
}
