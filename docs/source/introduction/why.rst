

Why using Htool-DDM?
####################

Htool-DDM aims to provide iterative solvers with preconditioners stemming from domain decomposition methods (DDM). It uses matrix compression via **hierarchical matrices**, and in particular, it provides

- parallel matrix-vector and matrix-matrix product using MPI and OpenMP,
- iterative solvers via `HPDDM`_,
- preconditioning techniques using domain decomposition methods.


Why?
   The storage and cost of assembly for dense matrices are both quadratic with respect to their size, while the cost of using linear solvers is cubic for direct solvers. For iterative solvers, the matrix-vector product has quadratic complexity, which is to be multiplied by the number of iterations. To reduce these costs, several compression techniques have been developed, which gives approximated representation of matrix-vector product and other operations. Htool provides compression via :ref:`sec_hierarchical_matrices`, and emphasize has been put on

   - parallelisation for **high-performance computing**, 
   - a **black box** interface, to tackle a great variety of problems.
   

Applications
   Hierarchical matrices are generally used to compress matrices stemming from the discretisation of asymptotically smooth kernels :math:`\kappa (x,y)`, i.e, for two cluster of geometric points :math:`X` and :math:`Y`,

.. math::
    \rvert \partial_x^{\alpha} \partial_y^{\beta}\kappa (x,y)\lvert \leq C_{\mathrm{as}}\lvert x - y\rvert^{-\lvert \alpha \rvert -\lvert \beta \rvert - s}.

\

   with :math:`x\in X`, :math:`y\in Y`, :math:`x\neq y`, :math:`\alpha, \beta \in \mathbb{N}_0^d` and :math:`\alpha+\beta \neq 0`.

   Such matrices arise in the context of

   - discretisation of boundary integral equations :footcite:`Boerm2003`,
   - solving Lyapunov and Riccati equations :footcite:`Boerm2003`,
   - discretization of the integral Fractional laplacian :footcite:`Ainsworth2018`,
   - kernel-based scattered data interpolation :footcite:`Iske2017`.
   



.. footbibliography::
