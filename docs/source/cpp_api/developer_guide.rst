Developer guide
###############

Build and run tests
===================

In the main repository, do

.. code-block:: bash

    mkdir build && cd build
    cmake ..
    make build-tests
    ctest 


The following cmake options can be used:

- :code:`-DCMAKE_BUILD_TYPE=Debug` for running tests in debug mode.
- :code:`-DHTOOL_WITH_STRICT_TESTS=ON` to use warnings as errors.
- :code:`-DUSE_SANITIZER=Address` to use the address sanitizer.
- :code:`-DCODE_COVERAGE` to activate code coverage.

Formatting
==========

After configuring CMake as in :ref:`cpp_api/developer_guide:build and run tests`, one can use the following targets:

.. code-block:: bash

    make format
    make cmake-format

- :code:`format` applies formatting to C++ code and requires `ClangFormat <https://clang.llvm.org/docs/ClangFormat.html>`__.
- :code:`cmake-format` applies formatting to CMake files and requires Python and the package `cmakelang <https://cmake-format.readthedocs.io/en/latest/>`__.

Formatting options are configured respectively in `.clang-format <https://github.com/htool-ddm/htool/blob/main/.clang-format>`__ and `cmake-format.py <https://github.com/htool-ddm/htool/blob/main/cmake-format.py>`__.

Build Doxygen documentation 
===========================

Similar to :ref:`cpp_api/developer_guide:build and run tests`, with cmake option :code:`-DHTOOL_WITH_DOC=ON` and :code:`make doc`.
