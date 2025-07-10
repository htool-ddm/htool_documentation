Hierarchical compression
########################

Available customizations
------------------------

Compression via :cpp:class:`htool::HMatrixTreeBuilder` can be customized in the following aspects:

1. For admissible condition, i.e., the geometric a priori we have to define admissible bloc, see :ref:`introduction/hmatrix:hierarchical clustering`, the current strategy is:
   
   - :cpp:class:`htool::RjasanowSteinbach`

2. For low-rank compression, see :ref:`introduction/hmatrix:low-rank compression`, the available strategies are:

   - :cpp:class:`htool::SVD`
   - :cpp:class:`htool::fullACA`
   - :cpp:class:`htool::partialACA`
   - :cpp:class:`htool::sympartialACA`
   - :cpp:class:`htool::RecompressedLowRankGenerator`

Strategies are then given to :cpp:class:`htool::HMatrixTreeBuilder` via its constructor or its function members

1. :cpp:func:`htool::HMatrixTreeBuilder::set_admissibility_condition`,
2. :cpp:func:`htool::HMatrixTreeBuilder::set_low_rank_generator`.

The constructor of :cpp:class:`htool::HMatrixTreeBuilder` also takes the usual parameters for :math:`\mathcal{H}`-matrix compression (tolerance for low-rank compression, symmetry, etc.), see its documentation.

Visualisation
-------------

Leaves from a :cpp:class:`htool::HMatrix` can be exported to a file with :cpp:func:`htool::save_leaves_with_rank`. The output is a `csv`-like file where 

- The first row corresponds to the number of rows, and then the number of columns, of the initial matrix.
- Then each row corresponds to a leaf of the hierarchical matrix with:

  - the index of its first row,
  - its number of rows,
  - the index of its first column,
  - its number of columns,
  - and its rank if the block is compressed, :math:`-1` otherwise.

A script is provided `here <https://github.com/htool-ddm/htool/blob/main/tools/plot_hmatrix.py>`__ to visualize a :math:`\mathcal{H}`-matrix using this type of file, but feel free to use your own. 

Information about compression can also but accessed from a :cpp:class:`htool::HMatrix` with 

- :cpp:func:`htool::get_tree_parameters`,
- :cpp:func:`htool::get_hmatrix_information`,

or directly exported to an output stream with

- :cpp:func:`htool::print_tree_parameters`,
- :cpp:func:`htool::print_hmatrix_information`.
