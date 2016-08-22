Hanzi Converter 繁簡轉換器 | 繁简转换器
=======================================

This tool converts between simplified and traditional Chinese Characters.
It consists of two parts:

  - a command line tool: ``hanzi-convert``
  - a python library: ``hanziconv``

.. image:: https://travis-ci.org/berniey/hanziconv.png?branch=master
   :target: https://travis-ci.org/berniey/hanziconv
   :alt: Build Status

.. image:: https://img.shields.io/badge/version-0.3-brightgreen.svg?style=plastic
   :target: https://pypi.python.org/pypi/hanziconv/
   :alt: Latest Version

.. image:: https://img.shields.io/badge/doc-0.3-brightgreen.svg?style=plastic
   :target: https://pythonhosted.org/hanziconv/
   :alt: Documentation

.. image:: https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=plastic
   :target: https://raw.githubusercontent.com/berniey/hanziconv/master/LICENSE
   :alt: License

Installation
------------

.. code-block:: sh

    $ pip install hanziconv


Command Line Tool
-----------------

The tool requires Python 2.6+

Synopsis
********

.. code-block:: sh

    $ ./hanzi-convert --help
    usage: hanzi-convert [-h] [-o OUTFILE] [-s] [-v] infile

    Simplified and Traditional Chinese Character Conversion
    Version 0.2.3 (By Bernard Yue)

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

This module requires Python 2.6+.  See https://pythonhosted.org/hanziconv/
for full documentation.

String Conversion
*****************

.. code-block:: pycon

    >>> from hanziconv import HanziConv
    >>> print(HanziConv.toSimplified('繁簡轉換器'))
    繁简转换器
    >>> print(HanziConv.toTraditional('繁简转换器'))
    繁簡轉換器
    >>> print(HanziConv.toSimplified(u'繁簡轉換器'))
    繁简转换器
    >>> print(HanziConv.toTraditional(u'繁简转换器'))
    繁簡轉換器
    >>> print(HanziConv.toSimplified(u'mix English and Chinese. 繁簡轉換器')
    mix English and Chinese. 繁简转换器
    >>> print(HanziConv.toTraditional(u'mix English and Chinese. 繁简转换器'))
    mix English and Chinese. 繁簡轉換器
    >>> print(HanziConv.toSimplified('mix English and Chinese. 繁簡轉換器'))
    mix English and Chinese. 繁简转换器
    >>> print(HanziConv.toTraditional('mix English and Chinese. 繁简转换器'))
    mix English and Chinese. 繁簡轉換器


Comparing String
****************

.. code-block:: pycon

    >>> from hanziconv import HanziConv
    >>> u'繁簡轉換器' ==  u'繁简转换器'
    False
    >>> HanziConv.same(u'繁簡轉換器', u'繁简转换器')
    True
    >>> str1 = 'mix English and Chinese. 繁簡轉換器'
    >>> str2 = 'mix English and Chinese. 繁简转换器'
    >>> str3 = 'mix Chinese and English. 繁简转换器'
    >>> str4 = u'mix English and Chinese. 繁簡轉換器'
    >>> HanziConv.same(str1, str2)
    True
    >>> HanziConv.same(str2, str3)
    False
    >>> HanziConv.same(str1, str4)
    True


Testing
-------
You can either run the standalone ``runtests.py`` or standard
``python setup.py test``

.. code-block:: sh

    $ tar zxf hanziconv-0.2.3.tar.gz
    $ cd hanziconv-0.2.3
    $ python setup.py test


License
-------
This module is distributed under Apache License Version 2.0.

