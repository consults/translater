#!/usr/bin/env python
# -*- coding: utf-8 -*-
import parser
from setuptools import find_packages, setup, Command

NAME = 'translater'
DESCRIPTION = 'practice setuptools'
REQUIRES_PYTHON = '>=3'
install_requires = ['requests', 'lxml']
setup(
    name=NAME,
    version=2,
    description=DESCRIPTION,
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'console_scripts': ['translater = src.translater:main']
    }
)
