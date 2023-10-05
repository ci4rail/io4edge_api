# io4edge_api

This repository contain all proto files for communicate with io4edge modules.

## How to build

Run this repo from a vscode devcontainer. (CTRL+SHIFT+P -> Remote-Containers: Open Folder in Container, or clone the repo in the devcontainer)

Run `make` to generate all the files.

Currently implemented:
- golang
- protobuf-c 
- python

# CI 

When you push to main, the CI will build the go/python/protobuf-c files and check if the files are up to date. If not, the CI will push the changes to the main branch.