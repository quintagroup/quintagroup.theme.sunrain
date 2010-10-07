import doctest
import unittest

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from base import *

flags = doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS

def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='quintagroup.theme.sunrain',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='quintagroup.theme.sunrain.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        #ztc.ZopeDocFileSuite(
        #    'README.txt', package='quintagroup.theme.sunrain',
        #    test_class=TestCase),

        ztc.FunctionalDocFileSuite(
           'browser.txt', package='quintagroup.theme.sunrain.tests',
           test_class=FunctionalTestCase, optionflags=flags,
           ),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
