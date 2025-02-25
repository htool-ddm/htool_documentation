Hierarchical matrix
===================

Builders
--------

.. doxygenclass:: htool::HMatrixBuilder

.. doxygenclass:: htool::HMatrixTreeBuilder

HMatrix
-------

.. doxygenclass:: htool::HMatrix

Linear algebra
--------------

.. doxygenfunction:: htool::add_hmatrix_vector_product(ExecutionPolicy&& execution_policy, char trans, CoefficientPrecision alpha, const HMatrix<CoefficientPrecision, CoordinatePrecision> &A, const CoefficientPrecision *in, CoefficientPrecision beta, CoefficientPrecision *out, CoefficientPrecision *buffer = nullptr)
.. doxygenfunction:: htool::add_hmatrix_vector_product(char trans, CoefficientPrecision alpha, const HMatrix<CoefficientPrecision, CoordinatePrecision> &A, const CoefficientPrecision *in, CoefficientPrecision beta, CoefficientPrecision *out, CoefficientPrecision *buffer = nullptr)

.. doxygenfunction:: htool::add_hmatrix_matrix_product(ExecutionPolicy&& execution_policy, char transa, char transb, CoefficientPrecision alpha, const HMatrix<CoefficientPrecision, CoordinatePrecision> &A, const Matrix<CoefficientPrecision>& B, CoefficientPrecision beta, Matrix<CoefficientPrecision>& C, CoefficientPrecision *buffer = nullptr)
.. doxygenfunction:: htool::add_hmatrix_matrix_product(char transa, char transb, CoefficientPrecision alpha, const HMatrix<CoefficientPrecision, CoordinatePrecision> &A, const Matrix<CoefficientPrecision>& B, CoefficientPrecision beta, Matrix<CoefficientPrecision>& C, CoefficientPrecision *buffer = nullptr)


.. doxygenfunction:: htool::lu_factorization(HMatrix<CoefficientPrecision, CoordinatePrecision> &hmatrix) 

.. doxygenfunction:: htool::lu_solve(char trans, const HMatrix<CoefficientPrecision, CoordinatePrecision> &A, Matrix<CoefficientPrecision> &X)

.. doxygenfunction:: htool::cholesky_factorization(char UPLO, HMatrix<CoefficientPrecision, CoordinatePrecision> &hmatrix)
    
.. doxygenfunction:: htool::cholesky_solve(char UPLO, const HMatrix<CoefficientPrecision, CoordinatePrecision> &A, Matrix<CoefficientPrecision> &X)
