from __future__ import print_function
import os
import doctest
import sys
try:
    from setuptools import setup
    extra = dict(test_suite="tests.test.suite", include_package_data=True)
except ImportError:
    from distutils.core import setup
    extra = {}





setup(
    name = 'mypytest',
    version = '1.1',
    packages = ["mypytest","mypytest.employee","mypytest.customer"],
    package_data = {
          "mypytest.employee": ["Employeetf.txt"],
          "mypytest.customer": ["Customer.txt"],
      },
    entry_points = {
        'console_scripts': [
            'prog=mypytest.pymain:main']},
    zip_safe = False,
    
      **extra
    )
doctest.testmod()
