Benchmarks
##########

We conducted benchmarks to evaluate the performance of the :math:`\mathcal{H}`-matrix implementation and identify areas for improvement, results are presented `here <https://pierremarchand20.github.io/htool-benchmarks-app/app.html>`_.
The benchmarks were conducted on different thread configurations and problem sizes, and we measured: 

- execution times, and performance of our algorithm.
- resulting compression,

obtained using our in-house :math:`\mathcal{H}`-matrix implementation.

In addition, we also provide a detailed explanation of how to use the benchmarks in :ref:`introduction/benchmarks:usage` and how to customize them to suit user specific needs in :ref:`introduction/benchmarks:customization`.

Overview
========

Our aim is to study the execution times and the resulting compression given by different functions with several sets of parameters. The studied functions correspond to the following type of benchmark ``<bench_type>``:

- The assembly of :math:`\mathcal{H}`-matrices ``bench_hmatrix_build``,
- The product of :math:`\mathcal{H}`-matrices and matrices ``bench_hmatrix_matrix_product``,
- The factorization of :math:`\mathcal{H}`-matrices ``bench_hmatrix_factorization``.

Each feature is tested against at least one of the following test cases ``<test_case_name>``:

- The problem size ``pbl_size``,
- The number of thread ``thread``,
- The ratio of the problem size on the number of thread (weak scaling) ``ratio``.

The results are saved as CSV files. The above-mentioned names are used in the executables and CSV files names in the format ``<bench_type>_vs_<test_case_name>.*``. For example: ``bench_hmatrix_build_vs_pbl_size``, ``bench_hmatrix_matrix_product_vs_pbl_size``, ``bench_hmatrix_matrix_product_vs_thread``, etc...

To simplify our approach and avoid the complexities associated with solving boundary integral equations using :math:`\mathcal{H}`-matrices, such as handling singular integrals and complex geometries, we focus on relatively simple problems for the time being. In the following, we introduce the kernel function and geometry used for all our tests.

Kernels
=======

The kernel functions are functions :math:`G(\boldsymbol{x},\boldsymbol{y})` where :math:`\boldsymbol{x}, \boldsymbol{y} \in \mathbb{R}^3`. The following are defined:

- Laplace like

.. math::

  G(\boldsymbol{x},\boldsymbol{y})=\frac{1}{|\boldsymbol{x} - \boldsymbol{y}| + 10^{-5}}

- Helmholtz like

.. math::

  G(\boldsymbol{x},\boldsymbol{y})=\frac{e^{i10 |\boldsymbol{x} - \boldsymbol{y}|}}{|\boldsymbol{x} - \boldsymbol{y}| + 10^{-5}}

The user can find several implementation of these kernel functions in ``include/htool_benchmark/generator_types.hpp`` and use them in ``<bench_type>.cpp`` by replacing ``LaplaceLikeGenerator`` by the wanted kernel.

Geometry
========

The geometry is a cylinder defined in ``include/htool_benchmark/generator_fixture.hpp``. For clarity’s sake, we define here the geometry in Python:

.. code-block:: python

  from math import pi, cos, sin, sqrt
  import numpy as np

  def createCylinder(n):
      step = 1.75*pi/sqrt(n)
      pts = np.empty((3,n))
      length          = 2*pi
      pointsPerCircle = length/step
      angleStep       = 2*pi/pointsPerCircle
      for i in range(0,n-1):
          x = cos(angleStep*i)
          y = sin(angleStep*i)
          z = step*i/pointsPerCircle
          pts[0,i] = x
          pts[1,i] = y
          pts[2,i] = z
      return pts


Output format
=============

In the result CSV files one can find the following columns:

- The tolerance which controls the relative error on block approximation ``epsilon``,
- The size of the problem ``size``,
- The number of threads ``number_of_threads``,
- The type of implementation ``policy_type`` (``seq``, ``par`` or ``omp_task``, see remark below),
- The index of the repetition ``id_rep`` of the benchmark,
- The compression ratio (number of rows times number of columns divided by number of stored coefficients in low-rank and dense blocks) ``compression_ratio``,
- The storage saving ratio (1 - 1 /compression_ratio) ``space_saving``,
- The execution time ``time``. If several times are measured, several columns are added with appropriated names, for example: ``factorization_time`` and ``solve_time`` in :math:`\mathcal{H}`-matrix factorization benchmarks.
- The type of clustering ``clustering_type``, see :ref:`cpp_api/basic_usage/geometric_clustering:available customizations`,
- The type of low rank generator ``low_rank_generator_type``, see :ref:`cpp_api/basic_usage/hierarchical_compression:available customizations`,
- The symmetry ``symmetry_type``,
- The hardware used for the result ``hardware_type``, and
- The version of Htool used ``version``.
  
**Remark** : The ``par`` execution policy corresponds to the use of shared parallelism with OpenMP, typically with ``# pragma omp for`` instructions if possible (products) or task-based parallelism (factorizations) with ``# pragma omp task`` instructions otherwise. The ``omp_task`` implementation only uses task-based parallelism with ``# pragma omp task`` instructions.

Results
=======

The results can be found `here <https://pierremarchand20.github.io/htool-benchmarks-app/app.html>`_.

Usage
=====

The repository containing the benchmarks is `github.com/PierreMarchand20/htool_benchmarks <https://github.com/PierreMarchand20/htool_benchmarks>`_.
Once the repository and its submodules are cloned, the user needs to build the library and make the executables with the following commands in `htool_benchmark/` directory:

.. code-block:: bash

  mkdir build
  cd build
  cmake ..
  # you can also use cmake.. -DCMAKE_BUILD_TYPE=Release_w_vecto
  # to enable vectorization
  make


Then, to run a benchmark based on a specific test case, the user can run of the following commands:

- :code:`./bench_hmatrix_build`,
- :code:`./bench_hmatrix_matrix_product`,
- :code:`./bench_hmatrix_factorization`.

It should output all the possible options for each specific benchmark.

Customization
=============

The benchmark parameters are accessible in the hpp files ``bench_hmatrix_build``, ``bench_hmatrix_matrix_product`` and ``bench_hmatrix_factorization`` located in the ``include/htool_benchmark`` folder. The user will find the following parameters in the ``custom parameters`` section of the code :

- ``number_of_repetitions``: the number of repetitions of the benchmark (see remark below),
- ``List_policy_type`` : the set of implementations,
- ``List_epsilon`` : the set of epsilon values (the tolerance which controls the relative error on block approximation),
- ``eta``: constant in the admissibility condition, see :ref:`introduction/hmatrix:hierarchical clustering`,
- ``List_pbl_size``: the set of problem size values,
- ``List_thread``: the set of values for the number of threads,
- ``number_of_products`` : the number of timed :math:`\mathcal{H}`-matrix products,
- ``number_of_solves`` : the number of timed linear system solves,
- ``trans`` : form of the system of equations :math:`A * X = B` or :math:`A^{**}T * X = B`.
