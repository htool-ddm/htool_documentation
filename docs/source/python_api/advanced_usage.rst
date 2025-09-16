Advanced usage
##############

.. Geometric clustering
.. ====================

.. 1. :cpp:class:`htool::VirtualPartitioning` defines the interface for partitioning a geometry.

Hierarchical compression
========================

.. 1. :cpp:class:`htool::VirtualAdmissibilityCondition` which is the admissible condition, i.e., the geometric a priori we have to define admissible bloc, see :ref:`introduction/hmatrix:hierarchical clustering`.

1. :py:class:`Htool.VirtualLowRankGenerator` which defines the low-rank compression, see :ref:`introduction/hmatrix:low-rank compression`.

Distributed operator
====================

1. :py:class:`Htool.VirtualLocalToLocalOperator` defines the interface for an operator taking a local vector and returning a local vector.
2. :py:class:`Htool.RestrictedGlobalToLocalOperator` defines the interface for an operator taking a global vector and returning a local vector. When using default compression via :py:class:`Htool.DefaultApproximationBuilder`, the resulting :py:class:`Htool.DistributedOperator` contains a :py:class:`Htool.HMatrix` as his :py:class:`Htool.RestrictedGlobalToLocalOperator`.

:py:class:`Htool.DistributedOperator` can contain multiple :py:class:`Htool.VirtualLocalToLocalOperator` and :py:class:`Htool.RestrictedGlobalToLocalOperator` using :py:func:`Htool.DistributedOperator.add_global_to_local_operator` and :py:func:`Htool.DistributedOperator.add_local_to_local_operator`.
