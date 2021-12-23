
.. _cpp_api:

C++ -- Basic usage
##################

Installation
------------

Htool is a C++11 header library, you need to download it, using for example

.. code-block:: bash

    git clone https://github.com/htool-ddm/htool

and you need to include the header files contained in `include/htool <https://github.com/htool-ddm/htool/tree/main/include/htool>`_. Note that Htool requires

- a MPI implementation, to perform communications on parallel computing architectures,
- a BLAS implementation, to perform algebraic operations (dense matrix-matrix or matrix-vector operations).

And optionally 

- LAPACK, to perform SVD compression,
- `HPDDM`_ and its dependencies (BLAS, LAPACK) to use iterative solvers and DDM preconditioners.

Required inputs
---------------

At the very least, Htool requires a geometry and a function to generate the coefficients of the matrix you wish to compress. More precisely,

- the geometry is a matrix of size :math:`d\times N`, where :math:`N` is the number of points and :math:`d` the geometric dimension, stored in a column-major array,
- the function generating the coefficients is passed to Htool using the interface ``VirtualGenerator``


Defining a IMatrix
------------------

Build a HMatrix
---------------

Use a HMatrix
-------------

Full example
------------

Solvers
-------
