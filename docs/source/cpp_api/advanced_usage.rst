Advanced usage
##############

Geometric clustering
====================

1. :cpp:class:`htool::VirtualPartitioning` defines the interface for partitioning a geometry.

Hierarchical compression
========================

1. :cpp:class:`htool::VirtualAdmissibilityCondition` which is the admissible condition, i.e., the geometric a priori we have to define admissible bloc, see :ref:`introduction/hmatrix:hierarchical clustering`.
2. :cpp:class:`htool::VirtualLowRankGenerator` which defines the low-rank compression, see :ref:`introduction/hmatrix:low-rank compression`.

Distributed operator
====================

1. :cpp:class:`htool::VirtualLocalToLocalOperator` defines the interface for an operator taking a local vector and returning a local vector.
2. :cpp:class:`htool::VirtualGlobalToLocalOperator` defines the interface for an operator taking a global vector and returning a local vector. When using default compression via :cpp:class:`htool::DefaultApproximationBuilder`, the resulting :cpp:class:`htool::DistributedOperator` contains a :cpp:class:`htool::HMatrix` as his :cpp:class:`htool::VirtualGlobalToLocalOperator`.

:cpp:class:`htool::DistributedOperator` can contain multiple :cpp:class:`htool::VirtualLocalToLocalOperator` and :cpp:class:`htool::VirtualGlobalToLocalOperator` using :cpp:func:`htool::DistributedOperator::add_global_to_local_operator` and :cpp:func:`htool::DistributedOperator::add_local_to_local_operator`.
