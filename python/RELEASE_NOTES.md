# CDM Distribution - Python Implementation

## What is being released?

This release introduces comprehensive Python support for CDM functionality modeled in Rosetta.  The package implements a class library mirroring the model's hierarchy and supporting its full capabilities including object construction, validation, and ingestion/serialization of types so enabled.  Facilitating development, the package provides as Python docstrings documentation of all Rosetta elements (data types, enums, members, and validation conditions) described in the model.  The current implementation supports CDM version 4.0.0+.  It does not support functionality natively implemented in the underlying language.

## Installation

Download the package from the Downloads section in the CDM Portal.  The library comes in two parts.  Each must be installed via pip.

- a static runtime that provides certain core functionality: rosetta_runtime-1.0.0-py3-none-any.whl.  Install this package first.
- the CDM library: python_cdm-x.x.x-py3-none-any.whl

These libraries are compatible with Python 3.10+ and rely upon [Pydantic](https://pydantic.dev).

## Generator
The repo expands the generator framework to enable Python translation.  The implementation follows the same approach as those completed for other languages in that it does not include functionality natively implemented in Java.

## License
Use of this release is under the [FINOS Community License](<https://github.com/finos/common-domain-model/blob/master/LICENSE.md>) 

## Contributors
- [CloudRisk](https://www.cloudrisk.uk)
- [FT Advisory LLC](http://www.ftadvisory.co)
- [TradeHeader SL](https://www.tradeheader.com)
