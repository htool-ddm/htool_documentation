Quickstart
##########

Htool-DDM can be used for different use cases:

* :ref:`python_api/quickstart:geometric clustering`
* :ref:`python_api/quickstart:hierarchical compression`
* :ref:`python_api/quickstart:distributed operator`
* :ref:`python_api/quickstart:ddm solver`

Dependencies
============

Htool-DDM's Python interface is based on `pybind11 <https://pybind11.readthedocs.io/en/stable/>`__ and Htool-DDM :ref:`C++ header-only library <cpp_api/quickstart:Quickstart>`. It requires

* C++ compiler with standard 14,
* `BLAS`_, to perform algebraic dense operations,
* Python 3,
* `cmake`_ to build the python interface,
* `numpy`_ for basic linear algebra in Python.

And

* For DDM solvers: a MPI implementation, `mpi4py`_ for using MPI via Python, `HPDDM`_ and `LAPACK`_.
* `HPDDM`_ and its dependencies (BLAS, LAPACK) to use iterative solvers and DDM preconditioners,
* for SVD (re)compression: `LAPACK`_

.. note:: Htool-DDM :ref:`C++ header-only library <cpp_api/quickstart:Quickstart>`, HPDDM and pybind11 are git submodules of Htool-DDM python interface. Thus, users do not need to install them.

And optionally,

* `matplotlib`_ for visualisation.

Installation
============

First, you need to clone this repository with its submodules:

.. code-block:: bash

    git clone --recurse-submodules https://github.com/htool-ddm/htool_python.git && cd htool_python

In the folder of this repository, do:

.. code-block:: bash

    pip install .

In case you need to pass cmake variables, you can use

.. code-block:: bash

    CMAKE_ARGS="-DCMAKE_VAR=VALUE1 -DCMAKE_VAR_2=VALUE2" pip install .

Geometric clustering
====================

Hierarchical compression
========================

Coefficient generator
---------------------

Build a hierarchical matrix
---------------------------

Use a hierarchical matrix
-------------------------

Distributed operator
====================

Build a distributed operator
----------------------------

Use a distributed operator
--------------------------

DDM Solver
==========
