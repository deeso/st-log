#!/usr/bin/env python
from setuptools import setup, find_packages
import os


data_files = [(d, [os.path.join(d, f) for f in files])
              for d, folders, files in os.walk(os.path.join('src', 'config'))]


setup(name='standard-logger',
      version='.01',
      description='perform some logging consistently across software',
      author='Adam Pridgen',
      author_email='adam.pridgen.phd@gmail.com',
      install_requires=['wheel',],
      packages=find_packages('src'),
      package_dir={'': 'src'},
)
