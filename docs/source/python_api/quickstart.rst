Quickstart
##########

Dependencies
============

Htool-DDM's Python interface is based on `pybind11 <https://pybind11.readthedocs.io/en/stable/>`__ and Htool-DDM :ref:`C++ header-only library <cpp_api/quickstart:Quickstart>`. It requires

* C++ compiler with standard 14,
* Python 3,
* MPI implementation for distributed parallelism,
* BLAS, to perform algebraic dense operations,
* `pybind11`_ to define the python interface,
* `cmake`_ to build the python interface,
* `HPDDM`_ and its dependencies (BLAS, LAPACK) to use iterative solvers and DDM preconditioners,

.. note:: Htool-DDM :ref:`C++ header-only library <cpp_api/quickstart:Quickstart>`, HPDDM and pybind11 are git submodules of Htool-DDM python interface. Thus, users do not need to install them.

It also requires the following python packages

* `mpi4py`_ for using MPI via Python,
* `numpy`_ for basic linear algebra in Python.

And optionnally,

* `matplotlib`_ for visualisation.

Compilation
===========

First, you need to clone this repository with its submodules:

.. code-block:: bash

    git clone --recurse-submodules https://github.com/htool-ddm/htool_python.git && cd htool_python

In the folder of this repository, do:

.. code-block:: bash

    pip install .

In case you need to pass cmake variables, you can use

.. code-block:: bash

    CMAKE_ARGS="-DCMAKE_VAR=VALUE1 -DCMAKE_VAR_2=VALUE2" pip install .



Hierarchical compression
========================

Coefficient generator
---------------------

Build a hierarchical matrix
---------------------------

Use a hierarchical matrix
-------------------------

DDM Solver
==========
