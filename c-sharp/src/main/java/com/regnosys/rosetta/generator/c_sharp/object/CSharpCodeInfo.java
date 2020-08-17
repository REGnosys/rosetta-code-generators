package com.regnosys.rosetta.generator.c_sharp.object;

/**
 *  Interface containing information about targetted C# code.
 */
public interface CSharpCodeInfo {

	/**
	 * Returns the targetted C# version.
	 * 
	 * @return <code>int</code> containing the C# version number.
	 */
	int getCSharpVersion();

	/**
	 * Returns a string describing the targettted .NET version.
	 * 
	 * @return <code>String</code> containing a descripton of the .NET version.
	 */
	String getDotNetVersion();

}
