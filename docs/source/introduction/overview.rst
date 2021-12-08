
Hierarchical matrices
#####################

We give here a quick overview on hierarchical matrices, and we refer to :cite:t:`Hackbusch2016,Bebendorf2008,Boerm2003` for a detailed presentation.

Low-rank compression
====================

Low-rank matrix
---------------

Let :math:`\mathbf{B}\in \mathbb{C}^{M\times N}` be a low-rank matrix, i.e, there exist :math:`\mathbf{u}_j\in \mathbb{C}^M`, :math:`\mathbf{v}_j\in \mathbb{C}^N` with :math:`1\leq j \leq r \leq \min (M,N)` such that

.. math::
    \mathbf{B} = \sum_{j=1}^r \mathbf{u}_j \mathbf{v}_j^T.
    
.. note:: Remark that, using the previous expression of :math:`\mathbf{B}`, storage cost and complexity of matrix vector product is :math:`(M+N)r`, which is lower than for the usual dense format as soon as :math:`r< \frac{MN}{M+N}`.

Low-rank approximation
----------------------

Usually, matrices of interest are not low-rank, but they may be well-approximated by low-rank matrices. To build such approximation, one can use a *truncated Singular Value Decomposition* (SVD):

.. math::
    \mathbf{B}^{(r)} = \sum_{j=1}^r \sigma_j \mathbf{u}_j \mathbf{v}_j^T,

where :math:`(\sigma_j)_{j=1}^r` are the singular values of :math:`\mathbf{B}` in decreasing order. Then, the approximation is 

.. math::

    \begin{align*}
        \Vert\mathbf{B} -\mathbf{B}^{(r)}\Vert_{2}^{2} = \sigma_{r+1}^{2}
        \quad\textrm{and}\quad
        \Vert\mathbf{B} -\mathbf{B}^{(r)}\Vert_{\mathrm{F}}^{2} = \sum_{j=r+1}^{n}\sigma_{j}^{2}.
    \end{align*}

In conclusion, a matrix with sufficiently decreasing singular values can be well-approximated by a low-rank approximation.

.. note:: A truncated SVD is actually the best low-rank approximation possible (see Eckart-Young-Mirsky theorem).

.. warning:: Computing a SVD requires the whole matrix, which would require storing all the coefficients, and this is exactly what we want to avoid. There exist several techniques to approximate a truncated SVD computing only some coefficients of the initial matrix, for example, Adaptive Cross Approximation (ACA) or randomized SVD.


Hierarchical clustering
=======================

Generally, matrices of interest are not low-rank matrices, and do not have rapidly decreasing singular values. But they can have sub-blocks with rapidly decreasing singular values. In particular, this is the case of matrices stemming from the discretisation of asymptotically smooth kernel, :math:`\kappa (x,y)`, i.e, for two clusters of geometric points :math:`X` and :math:`Y`,

.. math::
    \rvert \partial_x^{\alpha} \partial_y^{\beta}\kappa (x,y)\lvert \leq C_{\mathrm{as}}\lvert x - y\rvert^{-\lvert \alpha \rvert -\lvert \beta \rvert - s}.

In this case, sub-blocks corresponding to the interaction between two clusters :math:`X` and :math:`Y` satisfying an *admissibility condition*,  

.. math::
    \max (\operatorname{diam} (X), \operatorname{diam}(Y)) \leq \eta \operatorname{dist}(X,Y),

have exponentially decreasing singular values. Thus, they can be well-approximated by low-rank matrices.

Geometric clustering
--------------------

Block cluster tree
------------------

.. bibliography::
