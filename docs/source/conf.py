# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

import os
import subprocess

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = "Htool-DDM"
copyright = "2020, Pierre Marchand & Pierre-Henri Tournier"
author = "P. Marchand & P.-H. Tournier"

# The full version, including alpha/beta/rc tags
release = "1.0.0"


# -- General configuration ---------------------------------------------------

master_doc = "index"

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinxcontrib.rsvgconverter",
    "sphinxcontrib.bibtex",
    "sphinx_copybutton",
    "sphinx_contributors",
    "breathe",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "links.rst"]

# make rst_epilog a variable, so you can add other epilog parts to it
rst_epilog = ""
# Read link all targets from file
with open("links.rst") as f:
    rst_epilog += f.read()

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"

html_title = "Htool-DDM documentation"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

bibtex_bibfiles = ["_static/bibliography.bib"]

# -- Breathe Configuration -------------------------------------------------
breathe_projects = {"Htool": "../htool/build/doc/doc/xml/"}
breathe_default_members = ("members", "undoc-members")
breathe_default_project = "Htool"
breathe_domain_by_extension = {"hpp": "cpp"}


# -- Doxygen -------------------------------------------------


def configureDoxyfile(input_dir, output_dir):
    with open("../htool/doc/Doxyfile.in", "r") as file:
        filedata = file.read()

    filedata = filedata.replace(
        "@CMAKE_CURRENT_SOURCE_DIR@/../include/htool/", input_dir
    )
    filedata = filedata.replace("@CMAKE_CURRENT_BINARY_DIR@/doc/", output_dir)

    with open("Doxyfile", "w") as file:
        file.write(filedata)


# Check if we're running on Read the Docs' servers
read_the_docs_build = os.environ.get("READTHEDOCS", None) == "True"

if read_the_docs_build:
    input_dir = "../htool/include/htool/"
    output_dir = "build"
    configureDoxyfile(input_dir, output_dir)
    subprocess.call("doxygen", shell=True)
    breathe_projects["Htool"] = output_dir + "/xml"

# -- Options for LaTeC output -------------------------------------------------
latex_engine = "lualatex"
latex_elements = {"tableofcontents": r""}
