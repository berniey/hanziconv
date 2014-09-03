#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals
import sys
import codecs

try:
    from setuptools import setup, Command
    extra = dict(include_package_data=True)
except:
    from distutils.core import setup, Command
    extra = dict()
from hanziconv import __version__, __author__


_classifiers = '''
        Development Status :: 4 - Beta
        Environment :: Console
        Environment :: Web Environment
        Intended Audience :: End Users/Desktop
        Intended Audience :: Developers
        Intended Audience :: System Administrators
        License :: OSI Approved :: Apache Software License
        Natural Language :: Chinese (Simplified)
        Natural Language :: Chinese (Traditional)
        Operating System :: OS Independent
        Operating System :: MacOS
        Operating System :: Microsoft :: Windows
        Operating System :: POSIX
        Programming Language :: Python
        Programming Language :: Python :: 2
        Programming Language :: Python :: 2.6
        Programming Language :: Python :: 2.7
        Programming Language :: Python :: 3
        Programming Language :: Python :: 3.2
        Programming Language :: Python :: 3.3
        Programming Language :: Python :: 3.4
        Programming Language :: Python :: Implementation :: CPython
        Programming Language :: Python :: Implementation :: PyPy
        Topic :: System
        Topic :: Text Processing
        Topic :: Utilities
        '''
_classifiers = [s.strip() for s in _classifiers.splitlines() if s.strip()]


filename = 'README.rst'
encoding = 'utf-8'
if sys.version >= '3':
    with open(filename, 'r', encoding=encoding) as fh:
        docstring = fh.read()
    packages = ['hanziconv']
else:
    with open(filename, 'rU') as fh:
        fh = codecs.getreader(encoding)(fh)
        docstring = fh.read()
    packages = [b'hanziconv']


class PyTest(Command):
    """This class implement `python setup.py test` support for pytest"""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


setup(name='hanziconv',
      version=__version__,
      description='Hanzi Converter for Traditional and Simplified Chinese',
      long_description=docstring,
      author=__author__,
      author_email='hanzi.converter@gmail.com',
      url='https://github.com/berniey/hanziconv',
      packages=packages,
      scripts=['hanzi-convert', ],
      cmdclass=dict(test=PyTest),
      classifiers=_classifiers,
      license='Apache 2.0',
      **extra)
