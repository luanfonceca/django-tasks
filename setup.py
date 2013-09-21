#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='django-tasks',
      version='0.1',
      description='Python Django Tasks.',
      author='Luan Fonseca',
      author_email='luanfonceca@gmail.com',
      url='https://github.com/luanfonceca/todo-list/',
      packages=find_packages(),
      license='License :: Public Domain',
      install_requires=[
        'django==1.5',
        'south'
      ],
      
      test_suite='setuptest.setuptest.SetupTestSuite',
      tests_require=(
        'django-setuptest',
        'argparse'
      ),
)
