package com.regnosys.rosetta.generator.c_sharp.util

class CSharpModelGeneratorUtil {
     
     static def classComment(String definition) '''
          «IF definition !==null && !definition.isEmpty »
               /// <summary>
               /// «definition»
               /// </summary>
          «ENDIF»
     '''

     static def comment(String definition) '''
          «IF definition !==null && !definition.isEmpty »
               /// <summary>
               /// «definition»
               /// </summary>
          «ENDIF»
     '''
     
     static def fileComment(String version) '''
               // This file is auto-generated from the ISDA Common Domain Model, do not edit.
               //
               // Version: «version»
               //
     '''
}
