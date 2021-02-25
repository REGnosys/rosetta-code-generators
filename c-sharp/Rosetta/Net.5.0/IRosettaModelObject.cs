namespace Rosetta.Lib
{
    using Rosetta.Lib.Meta;

    public interface IRosettaModelObject<R> where R : IRosettaModelObject<R>
    {
        IRosettaMetaData<R> MetaData { get; }
    }
}