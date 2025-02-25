Quickstart
##########

Htool-DDM can be used for different use cases:

* :ref:`cpp_api/quickstart:geometric clustering`
* :ref:`cpp_api/quickstart:hierarchical compression`
* :ref:`cpp_api/quickstart:ddm solver`

Dependencies
============

Htool-DDM is a C++ header-only library, it requires:

* C++ compiler with standard 14.
* `BLAS`_, to perform algebraic dense operations.

And

* For DDM solvers: a MPI implementation, `HPDDM`_ and `LAPACK`_.
* For shared memory parallelism when using in-house :math:`\mathcal{H}`-matrix algebra: `OpenMP`_
* for SVD (re)compression: `LAPACK`_
* `CMake`_ to generate a build-system for the examples and tests.

.. * MPI implementation for distributed parallelism when using DDM solvers.
.. * OpenMP for shared memory parallelism when using in-house :math:`\mathcal{H}`-matrix algebra,
.. * LAPACK, to perform SVD compression,
.. * `HPDDM`_ and its dependencies (BLAS, LAPACK) to use iterative solvers and DDM preconditioners,

Installation
============

It is sufficient to include the :code:`include` folder of this repository in your library. If you prefer, the following command copies the :code:`include` folder your OS-specific include directory to make it more widely available: in the root of this repository on your system,

.. code-block:: bash

    cmake -B build
    cmake --build build --config Release --target install -- -j $(nproc)

.. note::
    The `install` prefix can be modified using :code:`cmake ..  -DCMAKE_INSTALL_PREFIX:PATH=your/install/path` instead of the first line.

Once installed, you can also use Htool-DDM as a cmake `imported target <https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#importing-targets>`__ as follows in your :code:`CMakeLists.txt`:

.. code-block:: cmake

    find_package(Htool REQUIRED)
    find_package(MPI REQUIRED)
    find_package(BLAS REQUIRED)
    # other optional packages

    add_executable(your_target your_file.cpp)
    target_link_libraries(your_target Htool::htool)

Geometric clustering
====================

The hierarchical clustering of a geometry is contained in :cpp:class:`htool::Cluster` and can be created using a :cpp:class:`htool::ClusterTreeBuilder`. For example,

.. code-block:: cpp

        int number_points = 10000;
        int spatial_dimension = 3;
        int number_of_partitions = 2;
        int number_of_children = 2;
        std::vector<double> coordinates(number_points*spatial_dimension); 
        // coordinates = {...}
        htool::ClusterTreeBuilder<double> cluster_tree_builder;
        htool::Cluster<double> cluster = cluster_tree_builder.create_cluster_tree(number_points, spatial_dimension, coordinates.data(), number_of_children, number_of_partitions);

where

* :code:`number_of_partitions` defines the number of children at a level of the cluster tree called "partition", which can be used to distribute data in a MPI context.
* :code:`number_of_children` defines the nulber of children for the other nodes that are not leaves.

Hierarchical compression
========================

To use the in-house hierarchical compression :cpp:class:`htool::HMatrix`, Htool-DDM will need two inputs:

1. The underlying geometry of the kernel to be compressed for the :ref:`introduction/hmatrix:geometric clustering`.
2. A function to generate any coefficient of the matrix to be compressed. 

Coefficient generator
---------------------

A coefficient generator is defined by following the interface :cpp:class:`htool::VirtualGenerator`, and in particular :cpp:func:`htool::VirtualGenerator::copy_submatrix`. For example:

.. code-block:: cpp

    class UserOperator: public htool::VirtualGenerator<double>{
        virtual void copy_submatrix(int M, int N, const int *rows, const int *cols, T *ptr) const override {
            for (int i = 0; i < M; i++) {
                for (int j = 0; j < N; j++) {
                    ptr[i + M * j] = ...// A(rows[i], cols[j]) where A is the kernel to be compressed;
                }
            }
        }
    };

Build a hierarchical matrix
---------------------------

To build a :cpp:class:`htool::HMatrix`, a :cpp:class:`htool::HMatrixBuilder` can be used: 

- Its constructor :cpp:func:`htool::HMatrixBuilder::HMatrixBuilder` takes at least one geometry.
- :cpp:func:`htool::HMatrixBuilder::build` generates a :cpp:class:`htool::HMatrix` from a :ref:`cpp_api/quickstart:coefficient generator`, and a :cpp:class:`htool::HMatrixTreeBuilder` object containing all the parameters related to compression.


.. code-block:: cpp

        int number_points = 10000;
        int spatial_dimension = 3;
        double epsilon = 1e-3;
        double eta = 10;
        char symmetry = 'N';
        char uplo = 'N';
        std::vector<double> coordinates(number_points*spatial_dimension); 
        // coordinates = {...}
        htool::HMatrixBuilder<double> hmatrix_builder(number_points, spatial_dimension, coordinates.data());
        htool::HMatrix<double> hmatrix = hmatrix_builder.build(UserOperator(),htool::HMatrixTreeBuilder<double>(epsilon, eta, symmetry, uplo));

.. note:: The geometric clustering is done within the constructor of :cpp:class:`htool::HMatrixBuilder`. You can still access the resulting target and source clusters as public members of :code:`hmatrix_builder`.

Use a hierarchical matrix
-------------------------

Basic linear algebra is provided for :cpp:class:`htool::HMatrix`. Shared-memory parallelism is also supported via execution policy traits.

.. list-table:: Supported linear algebra
    :header-rows: 1

    * - Operations
      - C++ function
      - Supported execution policy
    * - :math:`\mathcal{H}`-matrix vector product
      - :cpp:func:`htool::add_hmatrix_vector_product`
      - `std::execution::seq <https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag>`_, `std::execution::par <https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag>`_
    * - :math:`\mathcal{H}`-matrix matrix product
      - :cpp:func:`htool::add_hmatrix_matrix_product`
      - `std::execution::seq <https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag>`_, `std::execution::par <https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag>`_
    * - :math:`\mathcal{H}`-LU factorisation
      - :cpp:func:`htool::lu_factorization`
      - None
    * - :math:`\mathcal{H}`-LU solve
      - :cpp:func:`htool::lu_solve`
      - None
    * - :math:`\mathcal{H}`-Cholesky factorisation
      - :cpp:func:`htool::cholesky_factorization`
      - None
    * - :math:`\mathcal{H}`-Cholesky solve
      - :cpp:func:`htool::cholesky_solve`
      - None

.. note:: We try to have a similar API to `BLAS`_/`LAPACK`_ or `<linalg> <https://en.cppreference.com/w/cpp/numeric/linalg>`_. In particular, parallel version of linear algebra functions are available using execution policy traits. If none is given, it defaults to sequential operation.

DDM Solver
==========

Distributed operator
--------------------

To assemble a distributed operator, first a :ref:`geometric clustering <cpp_api/quickstart:geometric clustering>` needs to be applied. The partition defined by the target geometric cluster tree is then used to define a row-wise distributed operator (see :ref:`introduction/ddm:row-wise distributed operator`). :cpp:class:`htool::DefaultApproximationBuilder` builds a row-wise distributed operator :cpp:class:`htool::DistributedOperator` where each block of rows is compressed using a :cpp:class:`htool::HMatrix`, which can be accessed as a public member.

.. code-block:: cpp

    htool::HMatrixTreeBuilder<double> hmatrix_tree_builder(epsilon, eta, symmetry, uplo)
    htool::DefaultApproximationBuilder<double> distributed_operator_builder(UserOperator(), target_cluster, source_cluster, hmatrix_tree_builder,MPI_COMM_WORLD);
    DistributedOperator<double> &distributed_operator = distributed_operator_builder.distributed_operator;

A :cpp:class:`htool::DistributedOperator` object provides distributed products with matrices and vectors.

Linear solver
-------------

The iterative linear solve will be done via a :cpp:class:`htool::DDM` object, which can be built using :cpp:class:`htool::DDMSolverBuilder`. We give here an example for a simple block-Jacobi solver, in particular we use :cpp:member:`htool::DefaultApproximationBuilder::block_diagonal_hmatrix`, which is a pointer to the :math:`\mathcal{H}` matrix for the block diagonal associated with the local subdomain.

.. code-block:: cpp

    // Create DDM object
    htool::DDMSolverBuilder<double> ddm_solver_build(distributed_operator,distributed_operator_builder.block_diagonal_hmatrix);
    htool::DDM<double> solver = ddm_solver_build.solver;

    // Prepare solver
    HPDDM::Option &opt = *HPDDM::Option::get();
    opt.parse("-hpddm_schwarz_method asm ");
    ddm_with_overlap.facto_one_level();

    // Solve
    int mu = 1 // number of right-hand side
    std::vector<double> x = ...// unknowns
    std::vector<double> b = ...// right-hand sides
    ddm_with_overlap.solve(b.data(), x.data(), mu);

.. note:: We rely on the external library `HPDDM`_ for the implementation of efficient iterative solvers. We refer to its `cheatsheet <https://github.com/hpddm/hpddm/raw/main/doc/cheatsheet.pdf>`_ listing the various possible options for the solver.
