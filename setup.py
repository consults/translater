#!/usr/bin/env python
# -*- coding: utf-8 -*-
import parser
from setuptools import find_packages, setup, Command

NAME = 'translater'
FOLDER = 'src'
DESCRIPTION = 'practice setuptools'
URL = ''
EMAIL = '949628322@qq.com'
AUTHOR = 'pillow'
REQUIRES_PYTHON = '>=3'
VERSION = None
LONG_DESCRIPTION = 'practice setuptools'
install_requires = ['requests', 'lxml']
setup(
    name=NAME,
    version=1,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    license='MIT',
    entry_points={
        'console_scripts': ['translater = src.translater:main']
    }
)
