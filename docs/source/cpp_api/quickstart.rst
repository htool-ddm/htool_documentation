Quickstart
##########

Htool-DDM can be used for different use cases:

* :ref:`cpp_api/quickstart:geometric clustering`
* :ref:`cpp_api/quickstart:hierarchical compression`
* :ref:`cpp_api/quickstart:distributed operator`
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

It is sufficient to include the :code:`include` folder of this repository in your library. If you prefer, the following command copies the :code:`include` folder to your OS-specific include directory to make it more widely available: in the root of this repository on your system,

.. code-block:: bash

    cmake -B build
    cmake --build build --config Release --target install -- -j $(nproc)

.. note::
    The `install` prefix can be modified using :code:`cmake ..  -DCMAKE_INSTALL_PREFIX:PATH=your/install/path` instead of the first line.

Once installed, you can also use Htool-DDM as a cmake `imported target <https://cmake.org/cmake/help/latest/guide/importing-exporting/index.html#importing-targets>`__ as follows in your :code:`CMakeLists.txt`:

.. code-block:: cmake

    find_package(Htool REQUIRED)

    add_executable(your_target your_file.cpp)
    target_link_libraries(your_target Htool::htool)
    target_include_directories(your_target PUBLIC "path/to/hpddm") # if using Htool/HPDDM solvers

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
* :code:`number_of_children` defines the number of children for the other nodes that are not leaves.
* :code:`coordinates` stores all geometric points associated with the evaluation or discretisation of the kernel to be compressed, e.g., in 2d :math:`(x_0,y_0,x_1,y_1,...)`.

.. note:: See example in `use_cluster.cpp <https://github.com/htool-ddm/htool/blob/main/examples/use_clustering.cpp>`__ which creates a file containing the first three levels of a cluster tree. The output file can be visualized with `tools/plot_cluster.py <https://github.com/htool-ddm/htool/blob/main/tools/plot_cluster.py>`__ and the command line 

  .. code-block:: bash

      python3 plot_cluster.py --inputfile path/to/clustering_output.csv --depth 1

Hierarchical compression
========================

To use the in-house hierarchical compression :cpp:class:`htool::HMatrix`, Htool-DDM will need two inputs:

1. The underlying geometry of the kernel to be compressed for the :ref:`introduction/hmatrix:geometric clustering`.
2. A function to generate any coefficient of the matrix to be compressed. 

.. note:: See example in `use_hmatrix.cpp <https://github.com/htool-ddm/htool/blob/develop/examples/use_hmatrix.cpp>`__ which assembles a :math:`\mathcal{H}`-matrix, prints several outputs, and creates a file containing the rank of its leaves. The output file can be visualized with `tools/plot_hmatrix.py <https://github.com/htool-ddm/htool/blob/main/tools/plot_hmatrix.py>`__ and the command line 

  .. code-block:: bash

      python3 plot_hmatrix.py --inputfile path/to/hmatrix.csv


Coefficient generator
---------------------

A coefficient generator is defined by following the interface :cpp:class:`htool::VirtualGenerator`, and in particular :cpp:func:`htool::VirtualGenerator::copy_submatrix`. For example, a user could define the following generator:

.. code-block:: cpp

    class UserOperator: public htool::VirtualGenerator<double>{
        virtual void copy_submatrix(int M, int N, const int *rows, const int *cols, double *ptr) const override {
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
- :cpp:func:`htool::HMatrixBuilder::build <HMatrix<CoefficientsPrecision, CoordinatesPrecision> htool::HMatrixBuilder::build(const VirtualGenerator<CoefficientsPrecision> &, const HMatrixTreeBuilder<CoefficientsPrecision, CoordinatesPrecision> &)>` generates a :cpp:class:`htool::HMatrix` from a :ref:`cpp_api/quickstart:coefficient generator`, and a :cpp:class:`htool::HMatrixTreeBuilder` object containing all the parameters related to compression.

.. code-block:: cpp

        // Geometry
        const int number_points     = 10000;
        const int spatial_dimension = 3;
        std::vector<double> coordinates(number_points*spatial_dimension); 
        // coordinates = {...}

        // HMatrix parameters
        const double epsilon = 0.01;
        const double eta     = 10;
        char symmetry        = 'S';
        char UPLO            = 'L';

        // Generator
        //UserOperator A = ...;

        // HMatrix
        HMatrixBuilder<double> hmatrix_builder(number_points, spatial_dimension, coordinates.data());
        HMatrix<double> hmatrix = hmatrix_builder.build(A, htool::HMatrixTreeBuilder<double>(epsilon, eta, symmetry, UPLO));


where 

* :code:`epsilon` is the parameter controlling the relative error when compressing a subblock with a low-rank approximation.
* :code:`eta` is the parameter :math:`\eta` in the admissibility condition :eq:`admissibility_condition`.
* :code:`coordinates` stores all geometric points associated with the evaluation or discretisation of the kernel to be compressed, e.g., in 2d :math:`(x_0,y_0,x_1,y_1,...)`.

.. note:: The geometric clustering is done within the constructor of :cpp:class:`htool::HMatrixBuilder`. You can still access the resulting target and source clusters as public members of :code:`hmatrix_builder`.

.. warning:: :cpp:class:`htool::HMatrix` contains pointers to its target and source clusters. Thus, in general, clusters need to be deleted after :cpp:class:`htool::HMatrix` objects. In particular, when using a :cpp:class:`htool::HMatrixBuilder`, which contains the cluster, it needs to be deleted after :cpp:class:`htool::HMatrix`.

Use a hierarchical matrix
-------------------------

Basic linear algebra is provided for :cpp:class:`htool::HMatrix`. Shared-memory parallelism is also supported via execution policy traits for C++17 and above. 

.. list-table:: Supported operations
    :header-rows: 1

    * - Operations
      - C++ function
      - Supported execution policy
    * - Assembly
      - :cpp:func:`htool::HMatrixTreeBuilder::build <template<typename ExecutionPolicy> HMatrixType htool::HMatrixTreeBuilder::build(ExecutionPolicy&&, const VirtualInternalGenerator<CoefficientPrecision>&, const ClusterType&, const ClusterType&, int, int) const>` 
      - `std::execution::seq <https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag>`_, `std::execution::par <https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag>`_
    * - :math:`\mathcal{H}`-matrix vector product
      - :cpp:func:`htool::add_hmatrix_vector_product`
      - `std::execution::seq <https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag>`_, `std::execution::par <https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag>`_
    * - :math:`\mathcal{H}`-matrix matrix product
      - :cpp:func:`htool::add_hmatrix_matrix_product`
      - `std::execution::seq <https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag>`_, `std::execution::par <https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag>`_
    * - :math:`\mathcal{H}`-LU factorisation
      - :cpp:func:`htool::lu_factorization`
      - `std::execution::seq <https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag>`_, `std::execution::par <https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag>`_
    * - :math:`\mathcal{H}`-LU solve
      - :cpp:func:`htool::lu_solve`
      - None
    * - :math:`\mathcal{H}`-Cholesky factorisation
      - :cpp:func:`htool::cholesky_factorization`
      - `std::execution::seq <https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag>`_, `std::execution::par <https://en.cppreference.com/w/cpp/algorithm/execution_policy_tag>`_
    * - :math:`\mathcal{H}`-Cholesky solve
      - :cpp:func:`htool::cholesky_solve`
      - None

.. note:: We try to have a similar API to `BLAS`_/`LAPACK`_ or `<linalg> <https://en.cppreference.com/w/cpp/numeric/linalg>`_. In particular, parallel version of linear algebra functions are available using execution policy traits. If none is given, it defaults to sequential operation. If the standard execution policy traits are unavailable, you can still use exec_compat::seq and exec_compat::par in C++17 and later, or invoke the underlying function directly with the parallelism type you need.

Distributed operator
====================

A :cpp:class:`htool::DistributedOperator` mainly consists in a vector of global-to-local and local-to-local operators. Here, local means a vector local to the current MPI process/partition.

.. note:: See example in `use_distributed_operator.cpp <https://github.com/htool-ddm/htool/blob/develop/examples/use_distributed_operator.cpp>`__ which assembles a distributed operator with local :math:`\mathcal{H}`-matrices, prints several outputs, and creates files containing the rank of each local :math:`\mathcal{H}`-matrix leaves. The output files can be visualized with `tools/plot_hmatrix.py <https://github.com/htool-ddm/htool/blob/main/tools/plot_hmatrix.py>`__ and the command line 

  .. code-block:: bash

      python3 plot_hmatrix.py --inputfile path/to/local_hmatrix_0.csv

Build a distributed operator
----------------------------

To assemble a distributed operator, first a :ref:`geometric clustering <cpp_api/quickstart:geometric clustering>` needs to be applied. The partition defined by the target geometric cluster tree is then used to define a row-wise distributed operator (see :ref:`introduction/ddm:row-wise distributed operator`). :cpp:class:`htool::DefaultApproximationBuilder` builds a row-wise distributed operator :cpp:class:`htool::DistributedOperator` where each block of rows is compressed using a :cpp:class:`htool::HMatrix`, which can be accessed as a public member.

.. code-block:: cpp

    htool::HMatrixTreeBuilder<double> hmatrix_tree_builder(epsilon, eta, symmetry, uplo)
    htool::DefaultApproximationBuilder<double> default_approximation_builder(UserOperator(), target_cluster, source_cluster, hmatrix_tree_builder,MPI_COMM_WORLD);
    DistributedOperator<double> &distributed_operator = default_approximation_builder.distributed_operator;

A :cpp:class:`htool::DistributedOperator` object provides distributed products with matrices and vectors.

Use a distributed operator
--------------------------

Basic linear algebra is provided for :cpp:class:`htool::DistributedOperator`. "Local" means local to the current MPI process/partition.

.. list-table:: Supported operations
    :header-rows: 1

    * - Distributed operations
    * - :cpp:func:`htool::add_distributed_operator_vector_product_local_to_local` 
    * - :cpp:func:`htool::add_distributed_operator_matrix_product_local_to_local`
    * - :cpp:func:`htool::add_distributed_operator_vector_product_global_to_global`
    * - :cpp:func:`htool::add_distributed_operator_matrix_product_global_to_global`

DDM Solver
==========

To solve the linear system associated with :cpp:class:`htool::DistributedOperator`, an iterative linear solve can be used via a :cpp:class:`htool::DDM` object. It can be built via a :cpp:class:`htool::DDMSolverBuilder`. We give here an example for a simple block-Jacobi solver, in particular we use :cpp:member:`htool::DefaultApproximationBuilder::block_diagonal_hmatrix`, which is a pointer to the :math:`\mathcal{H}` matrix for the block diagonal associated with the local subdomain.

.. code-block:: cpp

    // Create DDM object
    HMatrix<double> local_hmatrix = *default_approximation_builder.block_diagonal_hmatrix; // copy the block diagonal block to factorize it later
    htool::DDMSolverBuilder<double> ddm_solver_build(distributed_operator,local_hmatrix);
    htool::DDM<double> solver = ddm_solver_build.solver;

    // Prepare solver
    HPDDM::Option &opt = *HPDDM::Option::get();
    opt.parse("-hpddm_schwarz_method asm ");
    ddm_with_overlap.facto_one_level(); // block_diagonal_hmatrix is factorized in-place

    // Solve
    int mu = 1 // number of right-hand side
    std::vector<double> x = ...// unknowns
    std::vector<double> b = ...// right-hand sides
    ddm_with_overlap.solve(b.data(), x.data(), mu);

.. note:: We rely on the external library `HPDDM`_ for the implementation of efficient iterative solvers. We refer to its `cheatsheet <https://github.com/hpddm/hpddm/raw/main/doc/cheatsheet.pdf>`_ listing the various possible options for the solver.

.. note:: See example `use_ddm_solver.cpp <https://github.com/htool-ddm/htool/blob/develop/examples/use_ddm_solver.cpp>`__ which solves a linear system stored in a :cpp:class:`htool::DistributedOperator` object using CG and a block-Jacobi preconditioner.
