Hierarchical compression
########################

Available customizations
------------------------

Compression made via :cpp:class:`htool::HMatrixTreeBuilder` can be customized in the following aspects:

1. :cpp:class:`htool::VirtualAdmissibilityCondition` which is the admissible condition, i.e., the geometric a priori we have to define admissible bloc, see :ref:`introduction/hmatrix:hierarchical clustering`.
2. :cpp:class:`htool::VirtualLowRankGenerator` which defines the low-rank compression, see :ref:`introduction/hmatrix:low-rank compression`.

Current available strategies are (see their documentation for more details):

1. For admissible condition:
    - :cpp:class:`htool::RjasanowSteinbach`
2. For low-rank compression:
    - :cpp:class:`htool::SVD`
    - :cpp:class:`htool::fullACA`
    - :cpp:class:`htool::partialACA`
    - :cpp:class:`htool::sympartialACA`

Strategies are then given to :cpp:class:`htool::HMatrixTreeBuilder` via its constructor or its function members

1. :cpp:func:`htool::HMatrixTreeBuilder::set_admissibility_condition`,
2. :cpp:func:`htool::HMatrixTreeBuilder::set_low_rank_generator`.

The constructor of :cpp:class:`htool::HMatrixTreeBuilder` also takes the usual parameters for :math:`\mathcal{H}`-matrix compression (tolerance for low-rank compression, symmetry, etc.), see its documentation.

Output
------

Blocks from a :cpp:class:`htool::HMatrix` can be exported to a file with :cpp:func:`htool::save_leaves_with_rank`.

Information about compression can also but accessed from a :cpp:class:`htool::HMatrix` with 

- :cpp:func:`htool::get_tree_parameters`,
- :cpp:func:`htool::get_hmatrix_information`,

or directly exported to an output stream with

- :cpp:func:`htool::print_tree_parameters`,
- :cpp:func:`htool::print_hmatrix_information`.
