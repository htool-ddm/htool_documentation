Geometric clustering
####################

A geometric clustering is a hierarchical partition of the underlying geometry on which the kernel matrix is defined. See :cpp:func:`htool::ClusterTreeBuilder::create_cluster_tree` for more information about the available parameters to customize :cpp:class:`htool::Cluster` construction.

Available customizations
------------------------

To create geometric clustering with :cpp:class:`htool::ClusterTreeBuilder`, two types of strategies allow customization of the algorithm defining :math:`n_{\mathrm{children}}` children of a cluster node:

1. Computation of the main directions for a given cluster node. Available strategies are:

   - :cpp:class:`htool::ComputeLargestExtent`
   - :cpp:class:`htool::ComputeBoundingBox`

2. Splitting position of a cluster node along a given direction. Available strategies are
   
   - :cpp:class:`htool::RegularSplitting`
   - :cpp:class:`htool::GeometricSplitting`

Strategies can be used to define a :cpp:class:`htool::Partitioning` that can be given to :cpp:class:`htool::ClusterTreeBuilder` via :cpp:func:`htool::ClusterTreeBuilder::set_partitioning_strategy`.

In any case, :cpp:class:`htool::Partitioning` will compute the main direction of the current cluster, using the first strategy, and split the current cluster :math:`n_{\mathrm{children}}` times orthogonally to this direction using the second strategy.

See :ref:`here <cpp_api/advanced_usage:geometric clustering>` for more advanced customization.

Visualisation
-------------

The geometric clustering can be exported to a file using :cpp:func:`htool::save_clustered_geometry`.
