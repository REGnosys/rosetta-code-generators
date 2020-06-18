package com.regnosys.rosetta.generator.golang.enums

import com.google.inject.Inject
import com.regnosys.rosetta.generator.golang.object.GolangModelObjectBoilerPlate
import com.regnosys.rosetta.rosetta.RosettaEnumValue
import com.regnosys.rosetta.rosetta.RosettaEnumeration
import java.util.ArrayList
import java.util.HashMap
import java.util.List
import java.util.Map

import static com.regnosys.rosetta.generator.golang.util.GolangModelGeneratorUtil.*
import com.regnosys.rosetta.generator.java.enums.EnumHelper
import java.nio.file.Files
import java.nio.file.Paths

class GolangEnumGenerator {
	
	@Inject extension GolangModelObjectBoilerPlate
	
	static final String FILENAME = 'enums.go'
		
	def Map<String, ? extends CharSequence> generate(Iterable<RosettaEnumeration> rosettaEnums, String version) {
		val result = new HashMap
		val enums = rosettaEnums.sortBy[name].generateEnums(version).replaceTabsWithSpaces
		result.put(FILENAME,enums)
		return result;
	}
	
	//generates struct representations of enums
	def Map<String, ? extends CharSequence> generate2(Iterable<RosettaEnumeration> rosettaEnums, String version) {
		val result = new HashMap
		val enums = rosettaEnums.sortBy[name].generateEnums2(version)
		result.put(FILENAME,enums)
		return result;
	}
	
	def Map<String, ? extends CharSequence>generate3(Iterable<RosettaEnumeration> rosettaEnums, String version) {
		val result = new HashMap
		val enums = rosettaEnums.sortBy[name].generateEnums3(version)
		result.put(FILENAME,enums)
		return result;
		
	}

	def static toJavaEnumName(RosettaEnumeration enumeration, RosettaEnumValue rosettaEnumValue) {
		return enumeration.name + '.' + EnumHelper.convertValues(rosettaEnumValue)
	}

	private def allEnumsValues(RosettaEnumeration enumeration) {
		val enumValues = new ArrayList
		var e = enumeration;

		while (e !== null) {
			e.enumValues.forEach[enumValues.add(it)]
			e = e.superType
		}
		return enumValues.sortBy[name];
	}

	private def generateEnums(List<RosettaEnumeration> enums, String version)  '''		
		package enums
		
		«fileComment(version)»			
		
		«FOR e : enums»
			«val allEnumValues = allEnumsValues(e)»
			«classComment(e.definition)»
			type «e.name» int
			const (
			«FOR value: allEnumValues»
				«methodComment(value.definition)»
				«e.name»_«EnumHelper.convertValues(value)» «e.name» = iota + 1
			«ENDFOR»
			)
		«ENDFOR»
	'''
	//generates struct representations of enums
	private def generateEnums2(List<RosettaEnumeration> enums, String version){
		val eString='''
		package preenums
		«FOR e : enums»					
			type «e.name» int							
		«ENDFOR»
		'''
		val enumDir = Files.createDirectories(Paths.get('''cdm/preenums'''))
		Files.write(enumDir.resolve('''preenums.go'''), eString.toString.bytes)
		
		return	'''
		package enums
		import . "cdm/preenums"
		«FOR e : enums»					
		«fileComment(version)»			
					
			«val allEnumValues = allEnumsValues(e)»
			«classComment(e.definition)»			
			type «e.name.toLowerCase» struct {
			«FOR value: allEnumValues»
				«methodComment(value.definition)»
				«EnumHelper.convertValues(value)» «e.name»
			«ENDFOR»
			}
		«ENDFOR»
		
		«FOR e : enums»					
			var «e.name.toUpperCase» = «e.name.toLowerCase»{}							
		«ENDFOR»
		
		func init(){
			«FOR e : enums»
				«val allEnumValues = allEnumsValues(e)»
				«var counter=1»				
				«FOR value: allEnumValues»								
					«e.name.toUpperCase».«EnumHelper.convertValues(value)» = «e.name»(«counter.toString»)
					«{counter++; null}»
				«ENDFOR»				
			«ENDFOR»
		}	
		'''.replaceTabsWithSpaces
		
		
	}
	
	private def generateEnums3(List<RosettaEnumeration> enums, String version){
		for (e: enums){
			val eString = '''		
		«fileComment(version)»			
			package «e.name»
			import . "cdm/enums"
			«val allEnumValues = allEnumsValues(e)»
			«classComment(e.definition)»
			
			const (
			«FOR value: allEnumValues»
				«methodComment(value.definition)»
				«EnumHelper.convertValues(value)» «e.name» = iota + 1
			«ENDFOR»
			)		
		'''.replaceTabsWithSpaces
		val enumDir = Files.createDirectories(Paths.get('''cdm/«e.name»'''))
		Files.write(enumDir.resolve('''«e.name».go'''), eString.toString.bytes)
		}
		
		return '''		
		package enums
		
		«fileComment(version)»			
		
		«FOR e : enums»			
			«classComment(e.definition)»
			type «e.name» int			
		«ENDFOR»
	'''
		
	}
	
	def boolean anyValueHasSynonym(RosettaEnumeration enumeration) {
		enumeration.allEnumsValues.map[enumSynonyms].flatten.size > 0
	}
}
