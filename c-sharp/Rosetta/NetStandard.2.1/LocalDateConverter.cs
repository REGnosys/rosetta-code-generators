#nullable enable // Allow nullable reference types

namespace Rosetta.Lib
{
    using System;
    using Newtonsoft.Json;
    using Newtonsoft.Json.Linq;

    /// <summary>
    /// Provides a JSON converter to override the default provided <see cref="NodaTime.LocalDate" />.
    /// </summary>
    /// <remarks>
    /// <see cref="NodaTime.LocalDate" /> uses ISO date format. e.g. "2020-02-05"
    /// CDM requires that we use the following instead:
    /// {
    ///     "day" : 5,
    ///     "month" : 2,
    ///     "year" : 2020
    /// }
    ///
    /// This converter needs to be registered via something like this:
    ///         <c>new JsonSerializerSettings().Converters.Add(new LocalDateConverter());</c>
    /// </remarks>
    public class LocalDateConverter : JsonConverter
    {
        class LocalDate
        {
            internal LocalDate() { }
            internal LocalDate(NodaTime.LocalDate localDate)
            {
                Day = localDate.Day;
                Month = localDate.Month;
                Year = localDate.Year;
            }

            public int Day { get; set; }
            public int Month { get; set; }
            public int Year { get; set; }
        }

        public override void WriteJson(JsonWriter writer, object? value, JsonSerializer serializer)
        {
            if (value != null)
            {
                var nodaLocalDate = (NodaTime.LocalDate)value;
                var localDate = new LocalDate(nodaLocalDate);
                serializer.Serialize(writer, localDate);
            }
        }

        public override object? ReadJson(JsonReader reader, Type objectType, object? existingValue, JsonSerializer serializer)
        {
            var jobject = JObject.Load(reader);
            var localDate = new LocalDate();
            serializer.Populate(jobject.CreateReader(), localDate);
            return new NodaTime.LocalDate(localDate.Year, localDate.Month, localDate.Day);
        }

        public override bool CanConvert(Type objectType)
        {
            return typeof(NodaTime.LocalDate).IsAssignableFrom(objectType) || typeof(NodaTime.LocalDate?).IsAssignableFrom(objectType);
        }
    }
}
