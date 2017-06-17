# -*- coding: utf-8 -*-

from setuptools import setup
from test import TestCommand


CLASSIFIERS = [
    'Development Status :: 3 - Alpha',

    'Intended Audience :: Developers',

    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
]

setup(
    name='radio-class',
    version='0.1.0',

    description='An python event-bus implementation',
    long_description='An python event-bus implementation inspired by'
                     'backbone.radio',

    url='https://github.com/unclechu/py-radio-class',

    author='Viacheslav Lotsmanov',
    author_email='lotsmanov89@gmail.com',

    license='MIT',

    platforms=['any'],
    classifiers=CLASSIFIERS,
    keywords='events bus library radio',
    packages=['radio'],
    cmdclass={'test': TestCommand}
)
