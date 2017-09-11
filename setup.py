""" This is the setup.py script for setting up the package and fulfilling any
necessary requirements.

References:
https://github.com/pypa/sampleproject/blob/master/setup.py
https://github.com/biopython/biopython/blob/master/setup.py
http://python-packaging.readthedocs.io/en/latest/index.html
"""
# Modules Used
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path
# import sys

# Save the standard error of the setup file. This can be removed soon.
# sys.stderr = open('err.txt', 'w')

# Set the home path of the setup script/package
home = path.abspath(path.dirname(__file__))
name = 'py3utils'


def readme():
    """Get the long description from the README file."""
    with open(path.join(home, 'README.md'), encoding='utf-8') as f:
        return f.read()


setup(
    name=name,
    author='Rob Gilmore & Shaurita Hutchins',
    description="",
    version='0.1',
    long_description=readme(),
    url='https://github.com/datasnakes/py3utils',
    license='MIT',
    keywords='bioinformatics utilities',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    # Packages will be automatically found if not in this list.
    packages=['py3utils'],
    include_package_data=True,
    entry_points={},
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose']
)
