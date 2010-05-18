# -*- coding: utf-8 -*-
"""
This module contains the tool of quintagroup.theme.sunrain
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.2.1'

tests_require=['zope.testing']

setup(name='quintagroup.theme.sunrain',
      version=version,
      description="An installable Quintagroup theme for Plone 3",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='web zope plone theme quintagroup',
      author='Quintagroup',
      author_email='skins@quintagroup.com',
      url='http://skins.quintagroup.com/sunrain',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['quintagroup', 'quintagroup.theme',],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'Products.Quills',
                        'quintagroup.portlet.static',
                        'quintagroup.portlet.cumulus',
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'quintagroup.theme.sunrain.tests',
      entry_points="""
      # -*- entry_points -*-
      """,
      setup_requires = ["setuptools",],
      )
