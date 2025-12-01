Developer guide
###############

Run tests
=========

Python tests use `pytest <https://docs.pytest.org/en/stable/>`__. They can be executed as follows for parallel and non-parallel tests:

.. code-block:: bash

    mpirun -np 2 python3 -m pytest tests/test_cluster.py
    python3 -m pytest tests/test_hmatrix.py
