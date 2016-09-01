# -*- coding: utf-8 -*-
# Copyright 2014 Bernard Yue
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from __future__ import unicode_literals, absolute_import
from .hanziconv import HanziConv

__version__ = '0.3.2'
__author__ = 'Bernard Yue'
__doc__ = """
This module converts between simplified and traditional Chinese Characters.
It consists of two parts:

  - a command line tool: ``hanzi-convert``
  - a python library: ``hanziconv``

It supports both Python 2 and 3

.. image:: https://travis-ci.org/berniey/hanziconv.png?branch=master
   :target: https://travis-ci.org/berniey/hanziconv
   :alt: Build Status

.. image:: https://img.shields.io/badge/version-{0}-brightgreen.svg?style=plastic
   :target: https://pypi.python.org/pypi/hanziconv/
   :alt: Latest Version

.. image:: https://img.shields.io/badge/doc-{1}-brightgreen.svg?style=plastic
   :target: https://pythonhosted.org/hanziconv/
   :alt: Documentation

.. image:: https://img.shields.io/badge/source-latest-blue.svg?style=plastic
   :target: https://github.com/berniey/hanziconv
   :alt: Source Code

.. image:: https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=plastic
   :target: https://raw.githubusercontent.com/berniey/hanziconv/master/LICENSE
   :alt: License


Installation
------------

.. code-block:: sh

    $ pip install hanziconv


Uninstallation
--------------

.. code-block:: sh

    $ [sudo] pip uninstall hanziconv


Command Line Tool
-----------------

Synopsis
********

.. code-block:: sh

    $ ./hanzi-convert --help
    usage: hanzi-convert [-h] [-o OUTFILE] [-s] [-v] infile

    Simplified and Traditional Chinese Character Conversion
    Version {2} (By {3})

    Converting to Traditional Hanzi by default with no -s flag

    positional arguments:
      infile                filename | "-", corresponds to stdin

    optional arguments:
      -h, --help            show this help message and exit
      -o OUTFILE, --output OUTFILE
                            filename to save output, stdout if omitted
      -s, --simplified      convert to simplified characters
      -v, --version         show program's version number and exit


Example
*******

Conversion from stdin

.. code-block:: sh

    $ ./hanzi-convert -
    Press Crtl-D when finished
    Typing away
    Now write some chinese characters
    繁简转换器
    ^D
    Typing away
    Now write some chinese characters
    繁簡轉換器
    $


Testing
-------
The module uses `pytest <http://pytest.org/latest/>`_.  Use pip to install `pytest`.

.. code-block:: sh

    $ [sudo] pip install pytest

Then checkout source code and run test as normal.

.. code-block:: sh

    $ git clone https://github.com/berniey/hanziconv.git
    $ cd hanziconv
    $ python setup.py test

You are encouraged to use `virtualenv <https://virtualenv.pypa.io/en/stable/>`_
and `virtualenvwrapper <https://virtualenvwrapper.readthedocs.io/en/latest/>`_
for to avoid changing your currently operating environment.


License
-------
| This module is distributed under Apache License Version 2.0.
The character map used in this module is based on the Multi-function
Chinese Character Database developed by Chinese University of Hong Kong.


Python API
----------

Example
*******

    >>> from hanziconv import HanziConv
    >>> print(HanziConv.toSimplified('繁簡轉換器'))
    繁简转换器
    >>> print(HanziConv.toTraditional('繁简转换器'))
    繁簡轉換器
    >>> HanziConv.same('繁簡轉換器', '繁简转换器')
    True

API
***
""".format(__version__, __version__, __version__, __author__)

__all__ = ["HanziConv"]
