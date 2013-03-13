#!/usr/bin/env python
try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

setup(
    name="twistar",
    version="1.1",
    description="An implementation of the Active Record pattern for Twisted",
    author="Brian Muller",
    author_email="bamuller@gmail.com",
    license="MIT",
    url="http://findingscience.com/twistar",
    packages=["twistar", "twistar.dbconfig", "twistar.tests", 'BermiInflector', 'BermiInflector.Rules',
              'txconnectionpool', 'txthreadworker' ],
    requires=["twisted.enterprise.adbapi"]
)
