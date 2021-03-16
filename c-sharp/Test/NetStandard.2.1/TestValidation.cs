namespace Cdm.Test.NetStandard2_1
{
    using System.IO;
    using Xunit;

    using Org.Isda.Cdm;
    using Newtonsoft.Json;
    using Newtonsoft.Json.Serialization;

    public class TestValidate
    {
        // Assume trade is one part of a larger JSON packet.
        public class Packet
        {
            public Trade Trade { get; set; }
        }

        [Fact]
        public void TestValidation()
        {
            // Load a json file deserialize it into an object and validate it.
            const string fileName = "ird-ex01-vanilla-swap-versioned.json";

            JsonSerializerSettings settings = GetSerializerSettings();

            string json = File.ReadAllText(fileName);
            var packet = JsonConvert.DeserializeObject<Packet>(json, settings);
            Assert.True(packet != null);
#pragma warning disable CS8602 // Dereference of a possibly null reference.
            var trade = packet.Trade;
#pragma warning restore CS8602 // Dereference of a possibly null reference.
            Assert.True(trade != null);

#pragma warning disable CS8602 // Dereference of a possibly null reference.
            Assert.True(trade.Validate().IsSuccess);
#pragma warning restore CS8602 // Dereference of a possibly null reference.
        }

        private static JsonSerializerSettings GetSerializerSettings()
        {
            return new JsonSerializerSettings()
            {
                ContractResolver = new CamelCasePropertyNamesContractResolver(),
                NullValueHandling = NullValueHandling.Ignore,
                Formatting = Formatting.Indented
            };
        }
    }
}
