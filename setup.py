# -*- coding: utf-8 -*-
import sys
from os.path import join, dirname
from setuptools import setup, find_packages

VERSION = (5, 4, 0)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

f = open(join(dirname(__file__), 'README'))
long_description = f.read().strip()
f.close()

install_requires = [
    'six',
    'python-dateutil',
    'elasticsearch-unravel==5.5.3'
]
tests_require = [
    "mock",
    "pytest>=3.0.0",
    "pytest-cov",
    "pytz"
]


setup(
    name = "elasticsearch-dsl-unravel",
    description = "Python client for Elasticsearch",
    license="Apache License, Version 2.0",
    url = "https://github.com/unraveldata-org/elasticsearch-dsl-py",
    long_description = long_description,
    version = __versionstr__,
    author = "venkatesh",
    author_email = "pvenkatesh@unraveldata.com",
    packages=find_packages(
        where='.',
        exclude=('test_elasticsearch_dsl*', )
    ),
    classifiers = [
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    install_requires=install_requires,

    test_suite = "test_elasticsearch_dsl.run_tests.run_all",
    tests_require=tests_require,

    extras_require={
        'develop': tests_require + ["sphinx", "sphinx_rtd_theme"]
    },
)
