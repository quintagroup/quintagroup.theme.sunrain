import transaction
from zope.interface import alsoProvides

from AccessControl.SecurityManagement import newSecurityManager

from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc

from Products.PloneTestCase.layer import PloneSite
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase import setup as ptc_setup

from Products.PloneTestCase.PloneTestCase import portal_owner
from Products.PloneTestCase.PloneTestCase import default_password

from Products.CMFCore.utils import getToolByName

from collective.testcaselayer.ptc import BasePTCLayer, ptc_layer

# from quintagroup.theme.sunrain import PROJECT_NAME
from quintagroup.theme.sunrain.browser.interfaces import IThemeSpecific

PROJECT_NAME = "quintagroup.theme.sunrain"
# This step made in collective.testcaselayer.ptc
#ptc.setupPloneSite()

# Commented until release of Quills for plone4
#ztc.installProduct("Quills")

class NotInstalled(BasePTCLayer):
    """Initialize the package, without installation into portal
    """
    def afterSetUp(self):
        fiveconfigure.debug_mode = True
        import quintagroup.theme.sunrain
        self.loadZCML('configure.zcml', package=quintagroup.theme.sunrain)
        self.loadZCML('tests/tests.zcml', package=quintagroup.theme.sunrain)
        # self.loadZCML('overrides.zcml', package=quintagroup.theme.sunrain)
        fiveconfigure.debug_mode = False
        ztc.installPackage(PROJECT_NAME)

class Installed(BasePTCLayer):
    """ Install product into the portal
    """
    def afterSetUp(self):
        self.addProfile("%s:tests" % PROJECT_NAME)

class UnInstalled(BasePTCLayer):
    """ UnInstall product from the portal
    """
    def afterSetUp(self):
        qi = getattr(self.portal, 'portal_quickinstaller', None)
        qi.uninstallProducts(products=[PROJECT_NAME,])


NotInstalledLayer = NotInstalled([ptc_layer,])
InstalledLayer = Installed([NotInstalledLayer,])
UnInstalledLayer = UnInstalled([InstalledLayer,])


class TestCaseNotInstalled(ptc.PloneTestCase):
    layer = NotInstalledLayer

class TestCase(ptc.PloneTestCase):
    layer = InstalledLayer

    def afterSetUp(self):
        # mark request with our browser layer
        super(TestCase, self).afterSetUp()
        alsoProvides(self.app.REQUEST, IThemeSpecific)

class TestCaseUnInstalled(ptc.PloneTestCase):
    layer = UnInstalledLayer


class FunctionalTestCaseNotInstalled(ptc.FunctionalTestCase):
    layer = NotInstalledLayer

class FunctionalTestCase(ptc.FunctionalTestCase):
    layer = InstalledLayer

    def afterSetUp(self):
        # mark request with our browser layer
        super(FunctionalTestCase, self).afterSetUp()
        alsoProvides(self.app.REQUEST, IThemeSpecific)

class FunctionalTestCaseUnInstalled(ptc.FunctionalTestCase):
    layer = UnInstalledLayer
