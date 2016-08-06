from setuptools import setup

setup(
    cmdclass={},

    name='candybar',
    packages=['candybar'],
    version='0.1.5',

    install_requires=['Pillow>=2.8.1'],

    description='Python library for barcode generator (code128, code39, and pdf417)',

    long_description=
    """
    candybar

    Python 3 barcode generator.
    Code39, Code128, PDF417 - Text mode and all sub-modes are supported
    """,

    url='http://candybar.pw',

    author='Scott Umsted',
    author_email='scott@wildidea.xyz',
    license='Apache',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='pdf417 code128 code39 barcode',
)
