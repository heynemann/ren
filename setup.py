#!/usr/bin/python
# -*- coding: utf-8 -*-

# ren command
# https://github.com/heynemann/ren

# Licensed under the MIT license: 
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2012 Bernardo Heynemann heynemann@gmail.com

from setuptools import setup, Extension
from ren.version import __version__

def run_setup():
  setup(
      name = 'ren',
      version = __version__,
      description = "ren is a command for easily renaming directories and files.",
      long_description = """
ren is a command for easily renaming directories and files.

Usage:

    ren /tmp/some/folder dir
    # renames /tmp/some/folder to /tmp/some/dir

""",
      keywords = 'filesystem bash rename mv move',
      author = 'Bernardo Heynemann',
      author_email = 'heynemann@gmail.com',
      url = 'https://github.com/heynemann/ren',
      license = 'MIT',
      classifiers = ['Development Status :: 4 - Beta',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: MIT License',
                     'Natural Language :: English',
                     'Operating System :: MacOS',
                     'Operating System :: POSIX :: Linux',
                     'Programming Language :: Python :: 2.6',
      ],
      packages = ['ren'],
      package_dir = {"ren": "ren"},

      install_requires=[
          'argparse'
      ],

      entry_points = {
          'console_scripts': [
              'ren = ren.ren:main',
          ],
      },
  )

run_setup()
