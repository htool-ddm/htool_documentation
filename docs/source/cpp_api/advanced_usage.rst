Advanced usage
##############

Geometric clustering
====================

1. :cpp:class:`htool::VirtualDirectionComputationStrategy` defines the interface for choosing the direction whose orthogonal plane will be the cutting plane.
2. :cpp:class:`htool::VirtualSplittingStrategy` defines how where split along the previous direction.

Hierarchical compression
========================

1. :cpp:class:`htool::VirtualAdmissibilityCondition` which is the admissible condition, i.e., the geometric a priori we have to define admissible bloc, see :ref:`introduction/hmatrix:hierarchical clustering`.
2. :cpp:class:`htool::VirtualLowRankGenerator` which defines the low-rank compression, see :ref:`introduction/hmatrix:low-rank compression`.
