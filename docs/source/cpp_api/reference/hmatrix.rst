Hierarchical matrix
===================

Builder
--------

.. doxygenclass:: htool::HMatrixBuilder

.. doxygenclass:: htool::HMatrixTreeBuilder

HMatrix
-------

.. doxygenclass:: htool::HMatrix

Admissibility conditions
------------------------

.. doxygenclass:: htool::VirtualAdmissibilityCondition

.. doxygenclass:: htool::RjasanowSteinbach

Low-rank compression
--------------------

.. doxygenclass:: htool::VirtualLowRankGenerator

.. doxygenclass:: htool::SVD

.. doxygenclass:: htool::fullACA

.. doxygenclass:: htool::partialACA

.. doxygenclass:: htool::sympartialACA

Visualisation
-------------

.. doxygenfunction:: htool::save_leaves_with_rank

.. doxygenfunction:: htool::get_tree_parameters

.. doxygenfunction:: htool::print_tree_parameters

.. doxygenfunction:: htool::get_hmatrix_information

.. doxygenfunction:: htool::print_hmatrix_information

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
