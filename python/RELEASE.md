# _Python Generator v2_

_What is being released?_

This release contains a number of upgrades to the Python generator:

- Migration to Pydantic 2.x
- More comprehensive support for Rosetta's operators (see full list below)
- Resolves the defect exposed by [PR 2766](https://github.com/finos/common-domain-model/pull/2766)
- Includes an update to the Python Rosetta runtime library used to encapsulate the Pydantic support (now version 2.0.0)

Future releases will:

- Enable generation of Python for Rosetta-defined functions
- Provide more complete support for re-use of data designated as "meta"

## New Operators

### Basic Expressions

| Rosetta Syntax | Description | Supported |
|:---|:---|:---:|
| RosettaExpression | The base type for all expressions in the Rosetta DSL.|
| RosettaLiteral | Represents constant values directly in the code. |
| RosettaBooleanLiteral | Represents a true or false value. | :white_check_mark: |
| RosettaIntLiteral | Represents an integer constant. | :white_check_mark:|
| RosettaNumberLiteral | Represents a numeric constant whether an integer or a decimal. | :white_check_mark:|
| RosettaStringLiteral | Represents a sequence of characters, enclosed in quotes. | :white_check_mark:|
| ListLiteral | Represents a fixed list of elements, e.g., \[1, 2, 3]. | :white_check_mark: |

### Reference and Feature Call Expressions

| Rosetta Syntax | Description | Supported |
|:---|:---|:---:|
| RosettaFeatureCall | Calls a feature (attribute or method) of an object or data type. | :white_check_mark: |
| RosettaReference | A reference to another part of the model or DSL. | :white_check_mark: |
| RosettaSymbolReference | A reference to a symbolic constant or a variable. | :white_check_mark: |
| RosettaEnumValue | A specific value from an enumeration. | :white_check_mark:|
| RosettaEnumValueReference | A reference to a specific value within an enumeration. | :white_check_mark:|
| RosettaImplicitVariable | An implicitly declared variable that is available in a certain context. | :white_check_mark:|

### Operation Expressions

| Rosetta Syntax | Description | Supported|
|:---|:---|:---:|
| RosettaUnaryOperation | An operation that takes a single operand, like negation. | :x: |
| RosettaBinaryOperation | An operation that takes two operands, such as addition or logical 'and'. | :white_check_mark:|
| RosettaCountOperation | Counts the number of elements in a collection. | :white_check_mark:|
| ArithmeticOperation | A mathematical calculation like addition, subtraction, multiplication, or division.|
| ComparisonOperation | Compares two expressions, such as greater-than or less-than. | :x: |
| EqualityOperation | Checks for equality (or inequality) between two expressions. | :x: |
| LogicalOperation | Logical operations like AND, OR, and NOT. | :white_check_mark: |
| ChoiceOperation | Allows for selection between multiple potential values or paths. | :white_check_mark:|
| FilterOperation | Filters a collection based on a predicate, returning only those elements that satisfy the predicate. | :white_check_mark: |
| MapOperation | Transforms each element of a collection according to a specified function. | :white_check_mark: |
| ReduceOperation | Combines the elements of a collection down to a single value. | :x: |
| SumOperation | Adds together all elements in a collection. | :white_check_mark: |
| MaxOperation | Determines the maximum value within a collection. | :white_check_mark: |
| MinOperation | Determines the minimum value within a collection. | :white_check_mark: |
| DistinctOperation | Filters a collection to only include distinct elements. | :white_check_mark:|
| SortOperation | Sorts the elements of a collection. | :white_check_mark: |
| FirstOperation | Retrieves the first element from a collection. | :white_check_mark: |
| LastOperation | Retrieves the last element from a collection. | :white_check_mark: |
| FlattenOperation | Flattens nested collections into a single collection. | :white_check_mark:|
| ReverseOperation | Reverses the order of elements in a collection. | :white_check_mark: |
| JoinOperation | Concatenates a collection of strings into a single string, with an optional delimiter. | :white_check_mark: |
| AsKeyOperation | Designates a value as a key in a key-value pair. | :white_check_mark: |
| ThenOperation | Chains multiple operations, where the output of one is the input to the next. | :white_check_mark: |

### Conditional and Specialized Expressions

| Rosetta Syntax | Description | Supported |
|:---|:---|:---:|
| RosettaConditionalExpression | An expression that evaluates a condition and branches accordingly. | :white_check_mark: |
| RosettaContainsExpression | Checks if a collection contains a given element. | :white_check_mark: |
| RosettaDisjointExpression | Determines if two collections have no elements in common. | :white_check_mark: |
| RosettaExistsExpression | Checks if a given value or property exists. | :white_check_mark: |
| RosettaAbsentExpression | Represents the absence of a value. | :white_check_mark: |
| RosettaOnlyElement | Ensures a collection contains exactly one element and retrieves it. | :white_check_mark: |
| RosettaOnlyExistsExpression | Asserts that only one of the given conditions or expressions is true. | :white_check_mark: |
| OneOfOperation | Ensures only one of several possible values is chosen. | :white_check_mark: |
| RosettaConstructorExpression | Creates new objects in Rosetta, translating to Python constructors or dictionaries | :white_check_mark: |

### Conversion Operations

| Rosetta Syntax | Description | Supported |
|:---|:---|:---:|
| ToEnumOperation | Converts a value to an enumeration type. | :x: |
| ToIntOperation | Converts a value to an integer. | :white_check_mark: |
| ToNumberOperation | Converts a value to a number (e.g., BigDecimal in Java). | :white_check_mark: |
| ToStringOperation | Converts a value to a string. | :white_check_mark: |
| ToTimeOperation | Converts a value to a time representation. Python Generator expressions used | :x: |
