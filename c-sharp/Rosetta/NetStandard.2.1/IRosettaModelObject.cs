namespace Rosetta.Lib
{
    using Rosetta.Lib.Meta;

    public interface IRosettaModelObject<out R> where R : IRosettaModelObject<R>
    {
        IRosettaMetaData<R> MetaData { get; }
    }
}