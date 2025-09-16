Geometric clustering
####################

A geometric clustering is a hierarchical partition of the underlying geometry on which the kernel matrix is defined. See :py:func:`Htool.ClusterTreeBuilder.create_cluster_tree` for more information about the available parameters to customize :py:class:`Htool.Cluster` construction.

Available customizations
------------------------

To create geometric clustering with :py:class:`Htool.ClusterTreeBuilder`, two types of strategies allow customization of the algorithm defining :math:`n_{\mathrm{children}}` children of a cluster node:

1. Computation of the main directions for a given cluster node. Available strategies are: 

   - Applying a principale component analysis on the geometry to compute the main direction.
   - Computing the largest side of the bounding box.

2. Splitting position of a cluster node along a given direction. Available strategies are
   
   - Splitting such that children clusters have about the same number of elements.
   - Splitting such that children clusters have about the same geometric side.

These strategies are defined via

- :py:class:`Htool.PCARegular`, (default)
- :py:class:`Htool.BoundingBoxRegular`,
- :py:class:`Htool.PCAGeometric`,
- :py:class:`Htool.BoundingBoxGeometric`,

and be used with :py:meth:`Htool.ClusterTreeBuilder.set_partitioning_strategy`.

In any case, the partitioning strategy will compute the main direction of the current cluster, using the first strategy, and split the current cluster :math:`n_{\mathrm{children}}` times orthogonally to this direction using the second strategy.

.. See :ref:`here <python_api/advanced_usage:geometric clustering>` for more advanced customization.

Visualisation
-------------

The geometric clustering can be visualized using `matplotlib`_:

.. code-block:: python

   depth = 2
   fig = plt.figure()

   if dimension == 2:
      ax= fig.add_subplot(1, 1, 1)
   elif dimension == 3:
      ax = fig.add_subplot(1, 1, 1, projection="3d")

   ax1.set_title("cluster\ndepth 2")
   Htool.plot(ax1, cluster, coordinates, depth)
   plt.show()
