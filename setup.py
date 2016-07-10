from setuptools import setup
from setuptools.command.install_lib import install_lib
from setuptools.command.build_py import build_py
from os import path
import sys

setup(
    cmdclass={},

    name='candybar',
    packages=['candybar'],
    version='0.1',
    install_requires=['Pillow==2.8.1'],

    description='Python library for barcode generator (code128, code39, and pdf417)',

    long_description=open('README.md').read(),

    # The project's main homepage.
    url='https://github.com/sumsted/candybar',

    # Author details
    author='Scott',
    license='Apache',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='pdf417 code128 code39 bar code',
)
