package com.regnosys.rosetta.generator.c_sharp;

/**
 * Code generator for C# 8, which corresponds to .NET Standard 2.1
 */
public class CSharp8CodeGenerator extends CSharpCodeGenerator {
	private static final int VERSION = 8;
	
	public CSharp8CodeGenerator() {
		 super(VERSION);
	}

	
	@Override
	public int getCSharpVersion() {
		return VERSION;
	}

	@Override
	public String getDotNetVersion() {
		return ".NET Standard 2.1";
	}
}
