# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='seed-cli',
    version='0.1.0',
    description='A CLI-based tool made with Python.',
    long_description=readme,
    author='Billy Arante',
    author_email='arantebillywilson@gmail.com',
    url='https://github.com/arantebw/seed-cli',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
