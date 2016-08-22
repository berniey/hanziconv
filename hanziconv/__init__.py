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

__version__ = '0.3'
__author__ = 'Bernard Yue'
__doc__ = """
This module converts between simplified and traditional Chinese Characters.
It consists of two parts:

      - a command line tool: ``hanzi-convert``
      - a python library: ``hanziconv``

**Command Line Tool Usage:**

.. code-block:: sh

    $ ./hanzi-convert --help
    usage: hanzi-convert [-h] [-o OUTFILE] [-s] [-v] infile

    Simplified and Traditional Chinese Character Conversion
    Version {0} (By {1})

    Converting to Traditional Hanzi by default with no -s flag

    positional arguments:
      infile                filename | "-", corresponds to stdin

    optional arguments:
      -h, --help            show this help message and exit
      -o OUTFILE, --output OUTFILE
                            filename to save output, stdout if omitted
      -s, --simplified      convert to simplified characters
      -v, --version         show program's version number and exit

**Python Library Example:**

    >>> from hanziconv import HanziConv
    >>> print(HanziConv.toSimplified('繁簡轉換器'))
    繁简转换器
    >>> print(HanziConv.toTraditional('繁简转换器'))
    繁簡轉換器
    >>> HanziConv.same('繁簡轉換器', '繁简转换器')
    True


""".format(__version__, __author__)

__all__ = ["HanziConv"]
