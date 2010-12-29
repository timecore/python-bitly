#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

VERSION = '0.3-CORE'

setup(
    name='python-bitly',
    version=VERSION,
    description='Pure python interface for the bit.ly API.',
    author=u'Yoav Aviram ',
    author_email='yoav.aviram@gmail.com',
    url='http://github.com/jcfigueiredo/python-bitly',
    py_modules=['bitly','socks'],
    install_requires=[
        'simplejson',
        'httplib2'
    ],
)

