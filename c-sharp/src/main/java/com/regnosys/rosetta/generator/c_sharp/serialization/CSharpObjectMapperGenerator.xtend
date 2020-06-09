package com.regnosys.rosetta.generator.c_sharp.serialization

import static com.regnosys.rosetta.generator.c_sharp.util.CSharpModelGeneratorUtil.*

class CSharpObjectMapperGenerator {

	/**
	 * Hardcode objectMapper until a better set up is found.
	 */
	def generateObjectMapper(String version) '''
		«fileComment(version)»
		'''
		/*
		
		package com.regnosys.rosetta.common.serialisation
		
		import com.fasterxml.jackson.annotation.JsonInclude
		import com.fasterxml.jackson.annotation.JsonSubTypes.Type
		import com.fasterxml.jackson.annotation.JsonTypeInfo.Id
		import com.fasterxml.jackson.annotation.{JsonSubTypes, JsonTypeInfo}
		import com.fasterxml.jackson.core._
		import com.fasterxml.jackson.databind._
		import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule
		import com.fasterxml.jackson.module.c_sharp.DefaultCSharpModule
		import com.fasterxml.jackson.module.c_sharp.experimental.CSharpObjectMapper
		
		import com.fasterxml.jackson.databind.module.SimpleModule
		import com.fasterxml.jackson.databind.ser.std.StdSerializer
		import com.fasterxml.jackson.databind.deser.std.StdDeserializer
		
		import java.time.LocalDate
		
		object RosettaDateModule extends SimpleModule {
		
		  addDeserializer(
		    classOf[LocalDate],
		    new StdDeserializer[LocalDate](classOf[LocalDate]) {
		      override def deserialize(p: JsonParser,
		                               ctxt: DeserializationContext): LocalDate = {
		        val DateExtended(day, month, year) =
		          p.readValueAs(classOf[DateExtended])
		        LocalDate.of(year, month, day)
		      }
		    }
		  )
		
		  addSerializer(
		    classOf[LocalDate],
		    new StdSerializer[LocalDate](classOf[LocalDate]) {
		      override def serialize(value: LocalDate,
		                             gen: JsonGenerator,
		                             serializers: SerializerProvider) = {
		        serializers.defaultSerializeValue(DateExtended(value.getDayOfMonth, value.getMonthValue, value.getYear), gen)
		      }
		    }
		  )
		}
		
		case class DateExtended(day: Int, month: Int, year: Int)
		
		object RosettaObjectMapper {
		  val mapper = new ObjectMapper() with CSharpObjectMapper
		
		  mapper.registerModule(new JavaTimeModule())
		  mapper.registerModule(DefaultCSharpModule)
		  mapper.registerModule(RosettaDateModule)
		  mapper.setSerializationInclusion(JsonInclude.Include.NON_ABSENT)
		  mapper.configure(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS, false)
		  mapper.configure(SerializationFeature.WRITE_ENUMS_USING_TO_STRING, true)
		  mapper.configure(DeserializationFeature.READ_ENUMS_USING_TO_STRING, true)
		  mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false)
		  mapper.configure(DeserializationFeature.USE_BIG_DECIMAL_FOR_FLOATS, true);
		
		  def parse[T: Manifest](json: String): T = {
		    val cls = manifest.runtimeClass.asInstanceOf[Class[T]]
		    mapper.readValue[T](json, cls)
		  }
		
		  def write[T](obj: T): String = {
		    mapper.writeValueAsString(obj)
		  }
		}
	''' */
}
