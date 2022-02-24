
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
- the function generating the coefficients is passed to Htool using the interface :cpp:class:`htool::VirtualGenerator`.

Here is an example where we define the interaction between to set of points ``target_points`` and ``source_points`` with :math:`\kappa (x,y)=e^{-|x-y|}`:

.. code-block:: cpp

    class MyMatrix : public VirtualGenerator<double> {
     const vector<double> & target_points;
     const vector<double> & source_points;
     int dimension;
 
     public:
     MyMatrix(int dimension0, int nr, int nc, const vector<double> &p10, const  vector<double> &p20) : VirtualGenerator(nr, nc), target_points (target_points_0), source_points(source_points_0), dimension(dimension0) {}
 
     void copy_submatrix(int M, int N, const int *const rows, const int *const  cols, double *ptr) const override {
      for (int j = 0; j < M; j++) {
       for (int k = 0; k < N; k++) {
        double norm2=0;
        for (int p = 0; p < dimension; p++) {
         norm2+= (target_points[p+dimension*row[j]]-source_points[p+dimension*cols[k]])*(target_points[p+dimension*row[j]]-source_points[p+dimension*cols[k]]);
        }
        ptr[j + M * k] = exp(-sqrt(norm2));
       }
      }
     }
    };


.. note:: Htool does not have any a priori information on the kernel, so it is up to the user to optimize the computations in :cpp:class:`htool::VirtualGenerator::copy_submatrix`.


Build a HMatrix
---------------

Use a HMatrix
-------------

Full example
------------

Solvers
-------
