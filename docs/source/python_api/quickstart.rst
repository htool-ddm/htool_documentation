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

The hierarchical clustering of a geometry is contained in :py:class:`Htool.Cluster` and can be created using a :py:class:`Htool.ClusterTreeBuilder`. For example,

.. code-block:: python

        number_of_points = 10000
        dimension = 3
        number_of_children = 2
        # coordinates = ...10000 x 3 column-major numpy array 
        cluster_builder = Htool.ClusterTreeBuilder()
        cluster: Htool.Cluster = cluster_builder.create_cluster_tree(
            coordinates, number_of_children
        )

where

* :code:`number_of_children` defines the number of children in the cluster tree.
* :code:`coordinates` stores all geometric points associated with the evaluation or discretisation of the kernel to be compressed, e.g., in 2d :math:`(x_0,y_0,x_1,y_1,...)`.

.. note:: See `example <https://github.com/htool-ddm/htool_python/blob/update_htool/example/use_cluster.py>`__

Hierarchical compression
========================

To use the in-house hierarchical compression :py:class:`Htool.HMatrix`, Htool-DDM will need two inputs:

1. The underlying geometry of the kernel to be compressed for the :ref:`introduction/hmatrix:geometric clustering`.
2. A function to generate any coefficient of the matrix to be compressed. 

.. note:: See `example <https://github.com/htool-ddm/htool_python/blob/update_htool/example/use_hmatrix.py>`__

Coefficient generator
---------------------

A coefficient generator is defined by following the interface :py:class:`Htool.VirtualGenerator`, and in particular :py:meth:`Htool.VirtualGenerator.build_submatrix`. For example, a user could define the following generator:

.. code-block:: python

    class CustomGenerator(Htool.VirtualGenerator):
        def build_submatrix(self, J, K, mat):
            for j in range(0, len(J)):
                for k in range(0, len(K)):
                    mat[j, k] = ... # A(J[j],K[k]) where A is the kernel to be compressed


Build a hierarchical matrix
---------------------------

To build a :py:class:`Htool.HMatrix`, you need: 

- One or two cluster trees, as illustrated in :ref:`python_api/quickstart:geometric clustering`.
- A generator modelling the kernel to be compressed, see :ref:`python_api/quickstart:coefficient generator`.

.. code-block:: python

        # HMatrix parameters
        epsilon  = 0.01;
        eta      = 10;
        symmetry = 'S';
        UPLO     = 'L';

        #  Generator
        # CustomOperator A = ...;

        hmatrix_builder = Htool.HMatrixTreeBuilder(epsilon, eta, symmetry, UPLO)
        hmatrix: Htool.HMatrix = hmatrix_builder.build(
            A, cluster, cluster
        )


where 

* :code:`epsilon` is the parameter controlling the relative error when compressing a subblock with a low-rank approximation.
* :code:`eta` is the parameter :math:`\eta` in the admissibility condition :eq:`admissibility_condition`.

Use a hierarchical matrix
-------------------------

Basic linear algebra is provided for :py:class:`Htool.HMatrix`:

.. code-block:: python

    size = hmatrix.shape[1]
    x = np.random.rand(size)
    y = hmatrix * x

Distributed operator
====================

A :py:class:`Htool.DistributedOperator` mainly consists in a vector of global-to-local and local-to-local operators. Here, local means a vector local to the current MPI process/partition.

.. note:: See `example <https://github.com/htool-ddm/htool_python/blob/update_htool/example/use_distributed_operator.py>`__

Build a distributed operator
----------------------------

To assemble a distributed operator, first a :ref:`geometric clustering <python_api/quickstart:geometric clustering>` needs to be applied. The partition defined by the target geometric cluster tree is then used to define a row-wise distributed operator (see :ref:`introduction/ddm:row-wise distributed operator`). :py:class:`Htool.DefaultApproximationBuilder` builds a row-wise distributed operator :py:class:`Htool.DistributedOperator` where each block of rows is compressed using a :py:class:`Htool.HMatrix`, which can be accessed as a public member.

.. code-block:: python

    default_approximation = Htool.DefaultApproximationBuilder(
        A,
        cluster,
        cluster,
        Htool.HMatrixTreeBuilder(epsilon, eta, "N", "N"),
        mpi4py.MPI.COMM_WORLD,
    )

    distributed_operator = default_approximation.distributed_operator
    local_hmatrix = default_approximation.hmatrix

Use a distributed operator
--------------------------

Basic linear algebra is provided for :py:class:`Htool.DistributedOperator`:

.. code-block:: python

    # Matrix vector product
    nb_cols = hmatrix.shape[1]
    x = np.random.rand(nb_cols)
    y_1 = distributed_operator * x

    # Matrix matrix product
    X = np.asfortranarray(np.random.rand(nb_cols, 2))
    Y_1 = distributed_operator @ X

DDM Solver
==========

To solve the linear system associated with :py:class:`Htool.DistributedOperator`, an iterative linear solve can be used via a :py:class:`Htool.Solver` object. It can be built via a :py:class:`Htool.DDMSolverBuilder`. We give here an example for a simple block-Jacobi solver, in particular we use :py:attr:`Htool.DefaultApproximationBuilder.block_diagonal_hmatrix`, which corresponds to the :math:`\mathcal{H}` matrix for the block diagonal associated with the local subdomain.

.. code-block:: python

    # Create DDM object
    block_diagonal_hmatrix = copy.deepcopy(
        default_approximation.block_diagonal_hmatrix
    )  # inplace factorization requires deepcopy

    default_solver_builder = Htool.DDMSolverBuilder(
        default_approximation.distributed_operator, block_diagonal_hmatrix
    )
    solver = default_solver_builder.solver

    # Prepare solver
    hpddm_args = "-hpddm_compute_residual l2 "
    solver.set_hpddm_args(hpddm_args)
    solver.facto_one_level() # block_diagonal_hmatrix is factorized in-place

    # Solve
    x = ...# unknowns
    b = ...# right-hand sides
    solver.solve(x, b)

.. note:: We rely on the external library `HPDDM`_ for the implementation of efficient iterative solvers. We refer to its `cheatsheet <https://github.com/hpddm/hpddm/raw/main/doc/cheatsheet.pdf>`_ listing the various possible options for the solver.

.. note:: See `example <https://github.com/htool-ddm/htool_python/blob/update_htool/example/use_ddm_solver.py>`__
