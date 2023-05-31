# Tests of Python Generation

The differents tests that are inside the project are divided in 4 different files. These ones are the following:

## Enum Tests
It contains a single test that chechs if its generation is well performed

## MetaData Tests

At the moment there is a tests that checks several things from the metadata. Though this test is invalit because the meta data part of the proejct is not done at the moment.

## Type Tests
Here there is the most extense part of the tests, the type generation contains several tests that checks different functionalities of the type generation. Such as the type that inherit from other types, conditions inside type declaration, etc.

## File Generation Tests

Here it's used a test called 
```
generateStructuredPython()
```

which give a folder as an input, which contains the rosetta samples, it will create a folder called "results" which will contain all the sub-folders and generated python files.

## Parsers

Inside the project there are two types of parsers. The firt one is 
```
parseRosettaWithNoErrors(CharSequence)
```
which it parses all the rosetta information and it creates the Rosetta Model, this one has already the resourceSet created inside of it, which means that is not usefull when using objects from different files, beacuse they will not be stored in the resourceSet.

The other parser is called

```
parse(CharSequence, resourceSet)
```

this one apart from giving as a parameter the CharSequence of the rosseta file, it is also given as an input a resourceSet. In that way, we can use that parser to store the information of the rossetaModel in the given resourceSet and in that way we can use objects from different files.
