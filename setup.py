# -*- coding: utf-8 -*-
from distutils.core import setup


setup(
    name = 'ireload',
    version = '0.1.0',
    py_modules = ['ireload'],
    description = 'Load or reload python object',
    long_description = open('README').read(),
    author = 'huyx',
    author_email = 'ycyuxin@gmail.com',
    url = 'https://github.com/huyx/ireload',
    keywords = ['reload'],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ]
    )
