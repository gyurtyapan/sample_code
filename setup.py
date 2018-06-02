#!/usr/bin/env python
"""
setup for phoenixcli
"""
from codecs import open as cd_open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from phoenixcli import __version__


THIS_DIR = abspath(dirname(__file__))
with cd_open(join(THIS_DIR, 'README.rst'), encoding='utf-8') as readme_file:
    LONG_DESCRIPTION = readme_file.read()

with open(join(THIS_DIR, 'requirements.txt')) as req_file:
    REQUIREMENTS = req_file.readlines()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=phoenixcli', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name='phoenixcli',
    version=__version__,
    description='ETL Framework',
    long_description=LONG_DESCRIPTION,
    url='https://matt.com',
    author='ABC',
    author_email='abc@abc.com',
    license='UNLICENSE',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='cli',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['docopt'],
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'] + REQUIREMENTS,
    },
    entry_points={
    },
    cmdclass={'test': RunTests},
)
