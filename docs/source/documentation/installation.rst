
Build documentation
-------------------

At the root of the `repository <https://github.com/htool-ddm/htool_documentation>`_ do:

.. code-block:: bash

    pip install -r requirements.txt

It will install the necessary dependencies. The documentation can be built using a ``<builder>``

.. code-block:: bash

    cd docs & make <builder>

where ``<builder>`` can be any supported builder by Sphinx, e.g, ``html`` or ``latex``.
