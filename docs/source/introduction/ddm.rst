Domain decomposition solvers
############################

This is a quick introduction to domain decomposition solvers for dense/compressed systems, and how they are implemented in Htool-DDM. These techniques have been introduced in :footcite:t:`Hebeker1990PSA` and analysed in papers like :footcite:t:`StephanTran1998DDA,Heuer1996EA$` for application to boundary integral equations. One goal of this library is to provide DD solvers with a GenEO coarse space :footcite:t:`MarchandClaeysEtAl2020TLP,Marchand2020SMB`.

Iterative solvers
=================

For a given linear system :math:`\mathbf{A}\in \mathbb{C}^{n\times n}`, we want to solve

.. math::
    \mathbf{A}\mathbf{x}=\mathbf{b},

where 

- :math:`\mathbf{b}` is a given right-hand side stemming from the data of the underlying problem, and,
- :math:`\mathbf{x}` is the unknown to be computed.

There are mainly two strategies to solve a linear system:

- A *direct* linear solver, which typically relies on a factorisation of :math:`\mathbf{A}`.
- An *iterative* linear solver, which requires multiples matrix-vector products for a given precision.

This library focuses on the second approach because it is easier to adapt such algorithms in a distributed-memory context. The issue is that the number of matrix-vector products can be large, making the method less efficient. Thus, a preconditioner :math:`\mathbf{P}\in \mathbb{C}^{n\times n}` is often used to solve the alternative linear system

.. math::
    \mathbf{P} \mathbf{A}\mathbf{x}= \mathbf{P}\mathbf{b},

with the aim of making the preconditioned linear system :math:`\mathbf{P} \mathbf{A}` more suitable for iterative resolution.

Schwarz preconditioners
=======================

A specific class of preconditionners stemming from Domain Decomposition Methods (DDM) are *Schwarz preconditioners*. They rely on a decomposition with overlap of our set of unknowns in :math:`N` subdomains. Each subdomain defines a local numbering with :math:`\sigma_p:\left\{1,\dots,n_p\right\}\to\left\{1,...,n\right\}`, where :math:`n_p` is the number of unknows in the p\ :superscript:`th` subdomain. Thus, the restriction matrix can be defined as :math:`\mathbf{R}_p\in \mathbb{R}^{n_p\times n}`

.. math::
    \left(\mathbf{R}\right)_{j,k} = 
    \left\{
    \begin{aligned}
        1 & \quad\text{if }k=\sigma_p(j),\\
        0 &  \quad\text{otherwise}.
    \end{aligned}
    \right.

Its transpose :math:`\mathbf{R}_p^T` defines the extension by zero, and :math:`\mathbf{R}_p \mathbf{A}\mathbf{R}_p^T` is the diagonal block of the original linear system associated with the p\ :superscript:`th` subdomain. An example of one-level Schwarz preconditioner can then be defined as

.. math::
    \mathbf{P}_{\mathrm{ASM}}= \sum_{p=1}^N \mathbf{R}_p^T(\mathbf{R}_p \mathbf{A}\mathbf{R}_p^T)^{-1} \mathbf{R}_p,

which is called a *Additive Schwarz Method* (ASM) preconditionner.

.. note:: It lends itself well in a distributed-memory context because it relies on solving local problem independently. Typically, a subdomain will be associated with one MPI process.

GenEO coarse space
==================

If Schwarz preconditioners, and DD preconditioners in general, improve iterative solving of linear systems (by lowering the number of required matrix-vector products), their efficiency decrease when the number of subdomains (and thus MPI processes) increases.

To make those preconditionners more robust when :math:`N` increases, a recurring technique is to add a small *coarse space*. It defines the columns of :math:`\mathbf{R}_0^T` so that :math:`\mathbf{R}_0 \mathbf{A}\mathbf{R}_0^T` is a global matrix of small size. Then, a coarse space can be used additively with :math:`\mathbf{P}_{\mathrm{ASM}}`:

.. math::
    \mathbf{P}_{\mathrm{ASM},2}= \mathbf{R}_0^T(\mathbf{R}_0 \mathbf{A}\mathbf{R}_0^T)^{-1} \mathbf{R}_0 + \sum_{p=1}^N \mathbf{R}_p^T(\mathbf{R}_p \mathbf{A}\mathbf{R}_p^T)^{-1} \mathbf{R}_p.

It is also called a two-level Schwarz preconditioner because we solve

1. local problems to the subdomains: :math:`\mathbf{R}_p \mathbf{A}\mathbf{R}_p^T` and,
2. a global problem :math:`\mathbf{R}_0 \mathbf{A}\mathbf{R}_0^T` (but hopefully of small size).

Various definitions of coarse spaces have been introduced, they usually rely on a coarser discretization of the underlying problem, or on well-chosen local eigenproblems. This library focuses on the latter with the so-called "Generalized Eigenproblems in the Overlap" (GenEO) coarse space, where local eigenproblems are of the form

.. math::
    \mathbf{D}_p \mathbf{R}_p \mathbf{A} \mathbf{R}_p^T \mathbf{D}_p \mathbf{v}_p = \lambda_p \mathbf{B}_p \mathbf{v}_p,

where 

* :math:`\mathbf{D}_p` defines a partition of the unity and,
* :math:`\mathbf{B}_p` is well-chosen matrix depending on the underlying problem.

We refer :footcite:t:`MarchandClaeysEtAl2020TLP,Marchand2020SMB` where such coarse space is analysed in the context of boundary integral equations.

Row-wise distributed operator
=============================

We focused so far on the preconditionner :math:`\mathbf{P}`, but the actual linear system :math:`\mathbf{A}` we want to solve also needs to be parallelized. We use a simple row-wise data-layout so that applying the preconditionner is relatively easy:

.. image:: /_static/hmat_parallelization.*
    :align: center

The distribution of the linear system is defined via a partition induced by a level of the target cluster tree.


.. footbibliography::
