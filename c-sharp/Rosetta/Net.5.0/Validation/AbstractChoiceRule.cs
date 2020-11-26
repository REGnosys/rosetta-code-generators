#nullable enable // Allow nullable reference types

namespace Rosetta.Lib.Validation
{
    using System;
    using System.Collections.Generic;

    public abstract class AbstractChoiceRule<T> : IValidator<T> where T : IRosettaModelObject<T>
    {
        protected string Name => GetType().Name;
    }

}
