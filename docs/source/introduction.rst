

Introduction
############

Htool aims to provide matrix compression via **parallelized hierarchical matrices**, and in particular, it provides

- parallel matrix-vector and matrix-matrix product using MPI and OpenMP,
- iterative solvers via `HPDDM <https://github.com/hpddm/hpddm>`_,
- preconditioning techniques using domain decomposition methods.


.. ~4 paragraphes, pourquoi compresser, comment compresser, keski se compresse bien, applications

Why?
   The storage and cost of assembly for dense matrices are both quadratic with respect to their size, while the cost of using linear solvers is cubic for direct solvers, and quadratic for iterative solvers (time the number of iterations). To avoid such costs, several compression techniques have been developed, and it is sill an active area of research. Htool provides compression via hierarchical matrices :footcite:`Hackbusch2016` :footcite:`Bebendorf2008` :footcite:`Boerm2003` because
   
   - they can be parallelized, which makes them relevant for **high-performance computing**, 
   - it is a **black box approach**, and thus it can be used in a great variety of problems.
   

.. How?
..    Htool can be used to compress a matrix, if it can be seen as the interaction between two clusters of geometric points. Then, 

Applications
   Htool has been used so far for

   - the discretization of boundary integral equations, via `FreeFEM <https://freefem.org>`_ for example.

   It could be used for

   -  the discretization of the integral Fractional laplacian,
   -  kernel-based scattered data interpolation :footcite:`Iske2017`.






.. footbibliography::