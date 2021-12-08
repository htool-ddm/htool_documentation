.. Htool documentation master file, created by
   sphinx-quickstart on Tue Sep 15 15:21:56 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Htool -- Parallelised hierarchical matrices
===========================================




**Htool** is a lightweight header-only C++11 library that provides an easy-to-use interface for parallel matrix compression via hierarchical matrices. Its goal is to provide minimal linear algebra and linear solvers for such matrices.

It also offers a modular framework where one can modify, or add other alternatives, for each part of the compression algorithm (low-rank approximation, clustering and admissibility condition). Via its interface with `HPDDM`_, it is also a flexible tool to test various iterative solvers and preconditioners.

The project is hosted on `GitHub <https://github.com/htool-ddm>`_, under the permissive `MIT license <https://en.wikipedia.org/wiki/MIT_License>`_.

.. list-table::
   :header-rows: 1
   :align: center

   * - C++
     - Python
     - Documentation
   * - |cpp_ci|
     - |python_ci|
     - |docs_ci| 
   * - |cpp_cov|
     - |python_cov|
     - 

Projects using Htool
   Htool provides distributed compression using hierarchical matrices, which can be used in many situations. In particular, Htool is used for different applications in the following projects:

   - `FreeFEM`_ to compress matrices stemming from the discretisation of boundary integral equations,
   - `PETSc`_ for black-box compression.

License
   Htool is licensed under the terms of the MIT license that can be found in the LICENSE file. By using, distributing, or contributing to this project, you agree to the terms and conditions of this license.

Authors
   If you need help or have questions regarding Htool, feel free to contact the main developers or to leave a report on our GitHub issue tracker!
   *Developers:*

   - `Pierre Marchand <https://pierremarchand.netlify.app>`_
   - `Pierre-Henri Tournier <https://phtournier.pages.math.cnrs.fr>`_

   *Contributors/Collaborators:*

   - `Xavier Claeys <https://www.ljll.math.upmc.fr/~claeys/>`_ 
   - `Pierre Jolivet <http://jolivet.perso.enseeiht.fr/>`_ 
   - `Frédéric Nataf <https://www.ljll.math.upmc.fr/nataf/](>`_

   *Acknowledgements*

   - `Centre Inria de Saclay - Île-de-France <https://www.inria.fr/en/centre-inria-saclay-ile-de-france>`_, France 
   - `ANR NonlocalDD <https://www.ljll.math.upmc.fr/~claeys/nonlocaldd/index.html>`_, (grant ANR-15-CE23-0017-01), France 
   - `Centre Inria de Paris <https://www.inria.fr/en/centre-inria-de-paris>`_, France 
   - `Laboratoire Jacques-Louis Lions <https://www.ljll.math.upmc.fr/en/>`_,Paris, France



.. Badges

.. |docs_ci| image:: https://readthedocs.org/projects/htool-documentation/badge/?version=latest
   :alt: doc
   :target: https://htool-documentation.readthedocs.io/en/latest/

.. |cpp_ci| image:: https://github.com/htool-ddm/htool/actions/workflows/CI.yml/badge.svg
   :alt: cpp
   :target: https://github.com/htool-ddm/htool

.. |python_ci| image:: https://github.com/htool-ddm/htool_python/actions/workflows/CI.yml/badge.svg
   :alt: python
   :target: https://github.com/htool-ddm/htool_python

.. |cpp_cov| image:: https://codecov.io/gh/htool-ddm/htool/branch/main/graph/badge.svg?token=1JJ40GPFA5
      :alt: cpp_cov
      :target: https://codecov.io/gh/htool-ddm/htool

.. |python_cov| image:: https://codecov.io/gh/htool-ddm/htool_python/branch/main/graph/badge.svg?token=P3FQNL8E64
   :target: https://codecov.io/gh/htool-ddm/htool_python
   :alt: python_cov
