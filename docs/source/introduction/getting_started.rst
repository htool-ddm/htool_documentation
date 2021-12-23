
Getting started
################

Htool can be used directly via

- its C++ API, see :ref:`cpp_api`,
- its Python interface, see :ref:`python_api`.

When used via another library or software, we refer to its own documentation and examples:

.. tabularcolumns:: |l|c|c|c|

.. list-table::
   :header-rows: 1
   :align: center

   * - Library/Software
     - Version
     - Documentation
     - Examples
   * - `FreeFEM <https://freefem.org>`_
     - :math:`\geq` 4.5 
     - `documentation <https://doc.freefem.org/introduction/index.html>`_ 
     - `2D <https://github.com/FreeFem/FreeFem-sources/blob/develop/examples/hpddm/helmholtz-3d-line-PETSc-complex.edp>`_ and `3D <https://github.com/FreeFem/FreeFem-sources/blob/develop/examples/hpddm/helmholtz-3d-surf-PETSc-complex.edp>`_ BEM with PETSc and `without <https://github.com/FreeFem/FreeFem-sources/blob/develop/examples/mpi/Helmholtz_circle_Dirichlet.edp>`_ 
   * - `PETSc <https://petsc.org/release/>`_
     - :math:`\geq` 3.16
     - `documentation <https://petsc.org/main/docs/manualpages/Mat/MATHTOOL.html#MATHTOOL>`_ 
     - `ex82 <https://petsc.org/main/src/ksp/ksp/tutorials/ex82.c.html>`_ 




..   - FreeFEM: `documentation <https://doc.freefem.org/introduction/index.html>`_ 
..   - PETSc: `documentation <https://petsc.org/main/docs/manualpages/Mat/MATHTOOL.html>`_ and `example <https://petsc.org/main/src/ksp/ksp/tutorials/ex82.c.html>`_ 
