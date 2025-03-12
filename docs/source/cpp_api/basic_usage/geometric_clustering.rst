Geometric clustering
####################

A geometric clustering is a hierarchical partition of the underlying geometry on which the kernel matrix is defined.

Available customizations
------------------------

To create geometric clustering with :cpp:class:`htool::ClusterTreeBuilder`, two strategies allow customization of the geometric clustering:

1. :cpp:class:`htool::VirtualDirectionComputationStrategy` defines the interface for choosing the direction whose orthogonal plane will be the cutting plane.
2. :cpp:class:`htool::VirtualSplittingStrategy` defines how where split along the previous direction.

Current available strategies are (see their documentation for more details):

1. For direction computation:
    - :cpp:class:`htool::ComputeLargestExtent`
    - :cpp:class:`htool::ComputeBoundingBox`
2. For splitting:
    - :cpp:class:`htool::RegularSplitting`
    - :cpp:class:`htool::GeometricSplitting`

Strategies are then given to :cpp:class:`htool::ClusterTreeBuilder` via its function members 

1. :cpp:func:`htool::ClusterTreeBuilder::set_direction_computation_strategy` 
2. :cpp:func:`htool::ClusterTreeBuilder::set_splitting_strategy` 

The builder also accepts one parameter which is the minimal size of a cluster node via :cpp:func:`htool::ClusterTreeBuilder::set_minclustersize`.

See :ref:`here <cpp_api/advanced_usage:geometric clustering>` for more advanced customization.

Output
------

The geometric clustering can be exported to a file using :cpp:func:`htool::save_clustered_geometry`.
