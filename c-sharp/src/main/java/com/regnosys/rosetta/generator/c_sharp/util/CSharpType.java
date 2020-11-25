package com.regnosys.rosetta.generator.c_sharp.util;

public class CSharpType {

	private String name;
	private String simpleName;

	public CSharpType(String name) {
		this.name = name;
		String[] split = name.split("\\.");
		this.simpleName = split[split.length - 1];
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getSimpleName() {
		return simpleName;
	}

	public void setSimpleName(String simpleName) {
		this.simpleName = simpleName;
	}

	static CSharpType create(String qName) {
		return new CSharpType(qName);
	}

	@Override
	public String toString() {
		return getSimpleName();
	}
}
