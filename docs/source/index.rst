.. Htool documentation master file, created by
   sphinx-quickstart on Tue Sep 15 15:21:56 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Htool -- Parallelised hierarchical matrices
===========================================

========  =========== =============
C++       Python      Documentation
========  =========== =============
|cpp_ci|  |python_ci| |docs_ci|
========  =========== =============


**Htool** is a lightweight header-only C++11 library that provides an easy-to-use interface for parallel matrix compression via hierarchical matrices. Its goal is to provide minimal linear algebra and linear solvers for such matrices.

For a more advanced usage, it also offers a modular framework where one can modify, or add other alternatives, for each part of the compression algorithm (low-rank approximation, clustering and admissibility condition). For example, if you look for testing a new low-rank approximation, it should be fairly easy to add it to Htool, and it would allow you to use it with all the features of Htool. 


About
-----

Htool has been developed and is maintained by `Pierre Marchand <https://pierremarchand.netlify.app>`_  and Pierre-Henri Tournier. If you need help or have questions regarding Htool, feel free to contact them.

License
-------

Acknowledgements
----------------

- `ANR NonlocalDD <https://www.ljll.math.upmc.fr/~claeys/nonlocaldd/index.html>`_ , (grant ANR-15-CE23-0017-01), France 
- `Inria <http://www.inria.fr/en/>`_ , Paris, France 
- `Laboratoire Jacques-Louis Lions <https://www.ljll.math.upmc.fr/en/>`_ ,Paris, France  


Collaborators/contributors
----------------

- `Xavier Claeys <https://www.ljll.math.upmc.fr/~claeys/>`_ 
- `Pierre Jolivet <http://jolivet.perso.enseeiht.fr/>`_ 
- `Frédéric Nataf <https://www.ljll.math.upmc.fr/nataf/](>`_



Contents
--------

.. toctree::
   :maxdepth: 4
   
   introduction
   overview
   installation
   basic_usage_cpp
   basic_usage_py
   advanced_usage

.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

.. Badges

.. |docs_ci| image:: https://readthedocs.org/projects/htool-documentation/badge/?version=latest
   :alt: doc
   :target: https://htool-documentation.readthedocs.io/en/latest/

.. |cpp_ci| image:: https://travis-ci.com/htool-ddm/htool.svg?branch=master
   :alt: cpp
   :target: https://github.com/htool-ddm/htool

.. |python_ci| image:: https://travis-ci.com/htool-ddm/htool_python.svg?branch=master
   :alt: python
   :target: https://github.com/htool-ddm/htool_python

