Hierarchical compression
########################

.. Available customizations
.. ------------------------

.. Compression via :cpp:class:`htool::HMatrixTreeBuilder` can be customized in the following aspects:

.. 1. For admissible condition, i.e., the geometric a priori we have to define admissible bloc, see :ref:`introduction/hmatrix:hierarchical clustering`, the current strategy is:
   
..    - :cpp:class:`htool::RjasanowSteinbach`

.. 2. For low-rank compression, see :ref:`introduction/hmatrix:low-rank compression`, the available strategies are:

..    - :cpp:class:`htool::SVD`
..    - :cpp:class:`htool::fullACA`
..    - :cpp:class:`htool::partialACA`
..    - :cpp:class:`htool::sympartialACA`
..    - :cpp:class:`htool::RecompressedLowRankGenerator`

.. Strategies are then given to :cpp:class:`htool::HMatrixTreeBuilder` via its constructor or its function members

.. 1. :cpp:func:`htool::HMatrixTreeBuilder::set_admissibility_condition`,
.. 2. :cpp:func:`htool::HMatrixTreeBuilder::set_low_rank_generator`.

.. The constructor of :cpp:class:`htool::HMatrixTreeBuilder` also takes the usual parameters for :math:`\mathcal{H}`-matrix compression (tolerance for low-rank compression, symmetry, etc.), see its documentation.

Visualisation
-------------

Information about compression can also be accessed from a :py:class:`Htool.HMatrix` with 

- :py:meth:`Htool.HMatrix.get_tree_parameters`,
- :py:meth:`Htool.HMatrix.get_local_information`.

.. code-block:: python

   fig = plt.figure()

   if dimension == 2:
      ax = fig.add_subplot(1, 1 ,1)
   elif dimension == 3:
      ax = fig.add_subplot(1, 1, 1, projection="3d")

   ax.set_title("Hmatrix")
   Htool.plot(ax, hmatrix)
   plt.show()
