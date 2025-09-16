DDM solvers
###########

Preconditioner with overlap
---------------------------

To use :ref:`introduction/ddm:schwarz preconditioners` with overlap, there are two possibilities using :py:class:`Htool.DDMSolverBuilder`: 

- Reuse a previous :py:class:`Htool.HMatrix` associated with the local problem without overlap. Typically, it can be taken from a :py:class:`Htool.DistributedOperator` using :math:`\mathcal{H}`-matrices for compression. See second overload of :py:meth:`Htool.DDMSolverBuilder.__init__`.

- Assemble a :py:class:`Htool.HMatrix` associated with the local problem with overlap. See thid overload of :py:meth:`Htool.DDMSolverBuilder.__init__`.

.. note:: In both cases, additional information about the partitioning need to be given to :py:class:`Htool.DDMSolverBuilder` constructors.
