## Docker build files
This folder contains docker context files to build various rosetta images. 

#### Dockerfile.codegen:

This file defines a container with the complete code generation modules, including the python module. It can be build with the follwoing command, from the root floder of the repository:

```bash
# docker build -t rosetta-codegen:0.0.1 -f docker/Dockerfile-codegen .
```

The container can be started in interactive mode with the following:

```bash
# docker run -it rosetta-codegen:0.0.1 bash
```