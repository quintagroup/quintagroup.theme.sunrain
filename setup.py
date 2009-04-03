# -*- coding: utf-8 -*-
"""
This module contains the tool of quintagroup.theme.sunrain
"""
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.0'

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
      url='http://svn.quintagroup.com/skins',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['quintagroup', 'quintagroup.theme',],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite = 'quintagroup.theme.sunrain.tests',
      entry_points="""
      # -*- entry_points -*- 
      [distutils.setup_keywords]
      paster_plugins = setuptools.dist:assert_string_list
      theme_vars = distwriters:assert_dict

      [egg_info.writers]
      paster_plugins.txt = setuptools.command.egg_info:write_arg
      theme_vars.txt = distwriters:write_map

      """,
      paster_plugins = ["ZopeSkel",],
      setup_requires = ["setuptools",],
      theme_vars = {'skinname': 'Sun and Rain Theme',
          'skinbase'          : 'Plone Default',
          'namespace_package' : 'quintagroup',
          'namespace_package2': 'theme',
          'package'           : 'sunrain',
          'used_subtemplates' : '',
      },
      )
