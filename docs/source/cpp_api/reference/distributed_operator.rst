Distributed operator
====================

Builder
-------

.. doxygenclass:: htool::DefaultApproximationBuilder

.. doxygenclass:: htool::DefaultLocalApproximationBuilder

.. doxygenclass:: htool::CustomApproximationBuilder

DistributedOperator
-------------------

.. doxygenclass:: htool::DistributedOperator

Linear algebra
--------------

.. doxygenfunction:: htool::add_distributed_operator_vector_product_local_to_local

.. doxygenfunction:: htool::add_distributed_operator_matrix_product_local_to_local(char trans, typename MatIn::value_type alpha, const DistributedOperator<typename MatIn::value_type> &A, const MatIn &in, typename MatIn::value_type beta, MatOut &out, typename MatIn::value_type *work)

.. doxygenfunction:: htool::add_distributed_operator_vector_product_global_to_global

.. doxygenfunction:: htool::add_distributed_operator_matrix_product_global_to_global

Operators
---------

.. doxygenclass:: htool::VirtualLocalToLocalOperator

.. doxygenclass:: htool::VirtualGlobalToLocalOperator
