namespace Rosetta.Lib.Attributes
{
    using System;
    using System.Collections.Generic;

    /// <summary>
    /// Specify a synonyn for a given valuefor a specific source.
    /// </summary>
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Enum | AttributeTargets.Property | AttributeTargets.Field, AllowMultiple = true, Inherited = false)]
    public class RosettaSynonym : Attribute
    {
        public string Value { get; set; }
        public string Source { get; set; }
        public string Path { get; set; }
        public int Maps { get; set; }

        public RosettaSynonym()
        {
            Path = "";
            Maps = 1;
        }
    }

#if 0
    [AttributeUsage(AttributeTargets.Class | AttributeTargets.Enum | AttributeTargets.Property | AttributeTargets.Field, AllowMultiple = true, Inherited = false)]
    public class RosettaSynonyms : Attribute
    {
        public IEnumerable<RosettaSynonym> Values { get; }
        public RosettaSynonyms(IEnumerable<RosettaSynonym> values)
        {
            Values = values;
        }
    }
#endif
}
