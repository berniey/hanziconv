Hanzi Converter 繁簡轉換器 | 繁简转换器
=======================================

This tool converts between simplified and traditional Chinese Characters.
It consists of two parts:

  - a command line tool: ``hanzi-convert``
  - a python library: ``hanziconv``

This module supports both Python 2 and 3

.. image:: https://travis-ci.org/berniey/hanziconv.png?branch=master
   :target: https://travis-ci.org/berniey/hanziconv
   :alt: Build Status

.. image:: https://img.shields.io/badge/version-0.3.2-brightgreen.svg?style=plastic
   :target: https://pypi.python.org/pypi/hanziconv/
   :alt: Latest Version

.. image:: https://img.shields.io/badge/doc-0.3.2-brightgreen.svg?style=plastic
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
    Version 0.3.2 (By Bernard Yue)

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


Python API
----------

Example
*******

.. code-block:: pycon

    >>> from hanziconv import HanziConv
    >>> print(HanziConv.toSimplified('繁簡轉換器'))
    繁简转换器
    >>> print(HanziConv.toTraditional('繁简转换器'))
    繁簡轉換器
    >>> HanziConv.same('繁簡轉換器', '繁简转换器')
    True


Testing
-------
The module uses `pytest <http://pytest.org/latest/>`_.  Use pip to install `pytest`.

.. code-block:: sh

    $ [sudo] pip install pytest

Then checkout source code and run test as normal.

.. code-block:: sh

    $ git clone https://github.com/berniey/hanziconv
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

