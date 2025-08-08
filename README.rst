.. Htool documentation master file, created by
   sphinx-quickstart on Tue Sep 15 15:21:56 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Htool-DDM -- Parallel solvers for compressed matrices
=====================================================




**Htool-DDM** is a lightweight header-only C++14 library that provides an easy-to-use interface for parallel iterative solvers and a default matrix compression via in-house hierarchical matrix implementation. Its goal is to provide modern iterative solvers for dense/compressed linear systems.

It is also an extensible framework which contains several customization points. For example, one can provide its own compression algorithm, or customize the default hierarchical compression. Via its interface with `HPDDM`_, it is also a flexible tool to test various iterative solvers and preconditioners.

The project is hosted on `GitHub <https://github.com/htool-ddm>`_, under the permissive `MIT license <https://en.wikipedia.org/wiki/MIT_License>`_.

.. only:: not latex
   
   .. list-table::
      :header-rows: 1
      :stub-columns: 1

      * - C++
        - |cpp_repo|
        - |cpp_cov|
      * - Python
        - |python_repo|
        - |python_cov|

Projects including Htool-DDM
   Htool-DDM provides distributed solvers and black-box hierarchical compression. It can be used directly in C++, via its Python interface, or in the following projects:

   - `FreeFEM`_ to compress matrices stemming from the discretisation of boundary integral equations and iterative solvers,
   - `PETSc`_ for black-box compression and iterative solvers.

License
   Htool is licensed under the terms of the MIT license that can be found in the LICENSE file. By using, distributing, or contributing to this project, you agree to the terms and conditions of this license.

Authors
   If you need help or have questions regarding Htool, feel free to contact the main developers or to leave a report on our GitHub issue tracker!
   
   *Developers:*

   - `Pierre Marchand`_
   - `Pierre-Henri Tournier`_

   *Contributors/Collaborators:*

   - `Xavier Claeys`_ 
   - `Virgile Dubos`_
   - `Pierre Jolivet`_ 
   - `Frédéric Nataf`_

   *Acknowledgements*

   - `Centre Inria de Saclay - Île-de-France <https://www.inria.fr/en/centre-inria-saclay-ile-de-france>`_, France 
   - `ANR NonlocalDD <https://www.ljll.math.upmc.fr/~claeys/nonlocaldd/index.html>`_, (grant ANR-15-CE23-0017-01), France 
   - `Centre Inria de Paris <https://www.inria.fr/en/centre-inria-de-paris>`_, France 
   - `Laboratoire Jacques-Louis Lions <https://www.ljll.math.upmc.fr/en/>`_,Paris, France



.. Badges

.. |cpp_repo| image:: https://img.shields.io/badge/repo-GitHub-blue?style=flat&link=https%3A%2F%2Fgithub.com%2Fhtool-ddm%2Fhtool
   :alt: Static Badge
   :target: https://github.com/htool-ddm/htool

.. |python_repo| image:: https://img.shields.io/badge/repo-GitHub-blue?style=flat&link=https%3A%2F%2Fgithub.com%2Fhtool-ddm%2Fhtool
   :alt: Static Badge
   :target: https://github.com/htool-ddm/htool_python

.. |cpp_cov| image:: https://codecov.io/gh/htool-ddm/htool/branch/main/graph/badge.svg?token=1JJ40GPFA5
   :alt: cpp_cov
   :target: https://codecov.io/gh/htool-ddm/htool

.. |python_cov| image:: https://codecov.io/gh/htool-ddm/htool_python/branch/main/graph/badge.svg?token=P3FQNL8E64
   :target: https://codecov.io/gh/htool-ddm/htool_python
   :alt: python_cov
