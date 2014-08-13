#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals
from hanziconv import __version__, __author__
from distutils.core import setup
import sys, codecs

_classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System',
        'Topic :: Text Processing',
        'Topic :: Utilities',
        ]

filename = 'README.rst'
encoding= 'utf-8'
if sys.version >= '3':
    with open(filename, 'r', encoding=encoding) as fh:
        docstring = ''.join(fh.readlines())
else:
    with open(filename, 'rU') as fh:
        fh = codecs.getreader(encoding)(fh)
        docstring = ''.join(fh.readlines())

setup(name='hanziconv',
        version=__version__,
        description='Hanzi Converter for Traditional and Simplified Chinese',
        long_description=docstring,
        author=__author__,
        author_email='hanzi.converter@gmail.com',
        url='https://github.com/berniey/hanziconv',
        packages= [ 'hanziconv' ],
        scripts=['hanzi-convert',],
        classifiers=_classifiers,
        license='Apache 2.0',
        )

