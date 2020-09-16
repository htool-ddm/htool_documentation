# Repository for Htool's Documentation

## What is Htool?

Htool is an implementation of hierarchical matrices (cf. this [reference](http://www.springer.com/gp/book/9783662473238) or this [one](http://www.springer.com/gp/book/9783540771463)), it was written to test Domain Decomposition Methods (DDM) applied to Boundary Element Method (BEM). It provides:

* routines to build hierarchical matrix structures (cluster trees, block trees, low-rank matrices and block matrices),
* parallel matrix-vector and matrix-matrix product using MPI and OpenMP,
* preconditioning techniques using domain decomposition methods,
* the possibility to use Htool with any generator of coefficients (e.g., your own BEM library),
* an interface with [HPDDM](https://github.com/hpddm/hpddm) for iterative solvers,
* and several utility functions to display information about matrix structures and timing.

It is now used in [FreeFEM](https://freefem.org) starting from version 4.5.

## How to install locally Htool's documentation?

At the root of the repository do:

`pip install -r requirement.txt`

It will install the necessary dependencies. You can build the documentation using a `<builder>`

`cd docs & make <builder>`

where `<builder>` can be any supported builder by `Sphinx`. In particular, you can use `html` or `latex`.
