DDM solvers
###########

Preconditioner with overlap
---------------------------

To use :ref:`introduction/ddm:schwarz preconditioners` with overlap, there are two possibilities using :cpp:class:`htool::DDMSolverBuilder`: 

1. Reuse a previous :cpp:class:`htool::HMatrix` associated with the local problem without overlap. Typically, it can be taken from a :cpp:class:`htool::DistributedOperator` using :math:`\mathcal{H}`-matrices for compression. See this :cpp:func:`constructor <DDMSolverBuilder htool::DDMSolverBuilder::DDMSolverBuilder(DistributedOperator<CoefficientPrecision> &, HMatrix<CoefficientPrecision, CoordinatePrecision> &, const VirtualGenerator<CoefficientPrecision> &, const std::vector<int> &, const std::vector<int> &, const std::vector<int> &, const std::vector<std::vector<int>> &)>`.

1. Assemble a :cpp:class:`htool::HMatrix` associated with the local problem with overlap. See this :cpp:func:`constructor <DDMSolverBuilder htool::DDMSolverBuilder::DDMSolverBuilder(DistributedOperator<CoefficientPrecision> &, const std::vector<int> &, const std::vector<int> &, const std::vector<int> &, const std::vector<std::vector<int>> &, const VirtualGenerator<CoefficientPrecision> &, int, const CoordinatePrecision *, const CoordinatePrecision *, const CoordinatePrecision *, const ClusterTreeBuilder<CoordinatePrecision> &, const HMatrixTreeBuilder<CoefficientPrecision, CoordinatePrecision> &)>`.

.. note:: In both cases, additional information about the partitioning need to be given to :cpp:class:`htool::DDMSolverBuilder` constructors.
