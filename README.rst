Hanzi Converter 繁簡轉換器 | 繁简转换器
=======================================

This tool converts between simplified and traditional Chinese Characters.
This package consists of two parts:

  - a command line tool, ``hanzi-convert``
  - a python library: ``hanziconv``

.. image:: https://travis-ci.org/berniey/hanziconv.png?branch=master
   :target: https://travis-ci.org/berniey/hanziconv

Installation
------------

.. code-block:: sh

    $ pip install hanziconv


Command Line Tool
-----------------

The tool requires Python 2.7+ (should work for Python 2.6, 3.0 and 3.1 but
was not tested)

Synopsis
********

.. code-block:: sh

    $ ./hanzi-convert --help
    usage: hanzi-convert [-h] [-o OUTFILE] [-s] [-v] infile

    Simplified and Traditional Chinese Character Conversion
    Version 0.2.2 (By Bernard Yue)

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

Conversion from stdin (press Ctrl-D to terminate input on POSIX systems)

.. code-block:: sh

    $ ./hanzi-convert.py -
    Press Crtl-D when finished
    Typing away
    Now write some chinese characters
    繁简转换器
    Press Ctrl-D after 2 new lines

    Typing away
    Now write some chinese characters
    繁簡轉換器
    Press Ctrl-D after 2 new lines

    $


Python API
----------

This module works for both Python 2.x and 3.x.

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
If you download the source distribution, you can run unit tests by running
standrad ``python setup.py test``

.. code-block:: sh

    $ tar zxf hanziconv-0.2.2.tar.gz
    $ cd hanziconv-0.2.2
    $ python setup.py test


License
-------
This module is distributed under Apache License Version 2.0.

