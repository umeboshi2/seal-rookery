from setuptools import setup, find_packages

NAME = 'seal_rookery'
KEYWORDS = ["legal",]
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

with open('LICENSE.txt') as f:
    LICENSE = f.read()

setup(
    name=NAME,
    packages=find_packages(exclude=('tests',)),
    version='1.0.0',
    description='A collection of court seals that can be used in any project.',
    author='Mike Lissner',
    author_email='info@freelawproject.org',
    license=LICENSE,
    url='https://github.com/freelawproject/seal_rookery',
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    test_suite='test',
)
