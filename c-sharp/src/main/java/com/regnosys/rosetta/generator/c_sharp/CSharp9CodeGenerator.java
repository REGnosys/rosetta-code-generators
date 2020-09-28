package com.regnosys.rosetta.generator.c_sharp;

/**
 * Code generator for C# 9, which corresponds to .NET 5.0
 */
public class CSharp9CodeGenerator extends CSharpCodeGenerator {
	private static int VERSION = 9;
	
	public CSharp9CodeGenerator() {
		 super(VERSION);
	}
	
	@Override
	public int getCSharpVersion() {
		return VERSION;
	}

	@Override
	public String getDotNetVersion() {
		return ".NET 5.0";
	}
}
