#
# Test product's installation
#
import string
from zope.component import queryMultiAdapter
from zope.viewlet.interfaces import IViewletManager

from base import *

SKIN_NAME = "qThemeRain"
SKIN_LAYERS = ['theme_sunrain_templates', 'theme_sunrain_styles', 'theme_sunrain_images', 'theme_rain', 'theme_sunrain_templates', 'theme_sunrain_styles', 'theme_sunrain_images', 'theme_sun']
CSS_RESOURCES = ['themeSunRain.css']
VIEWLETS = {'plone.portalfooter': ['sunrain.footer'], 'plone.portalheader': ['sunrain.searchbox', 'sunrain.logo', 'sunrain.slogan', 'sunrain.personal_bar'], 'plone.portaltop': ['sunrain.global_sections', 'sunrain.subscribe']}

class TestDefaultInstallation(TestCase):

    def testInstalled(self):
        qi = self.portal.portal_quickinstaller
        self.assertTrue(qi.isProductInstalled(PROJECT_NAME),
            '%s is not installed.' % PROJECT_NAME)

    def testStyles(self):
        """ Test styles registration."""
        cssreg = getToolByName(self.portal, "portal_css")
        for res in CSS_RESOURCES:
            self.assertNotEqual(cssreg.getResource(res), None)

    def testSkins(self):
        """ Test styles registration."""
        skins = getToolByName(self.portal, "portal_skins")
        theme_layers = skins.getSkinPath(SKIN_NAME)
        skins_ids = skins.objectIds()

        self.assertNotEqual(theme_layers, None)
        for sl in SKIN_LAYERS:
            self.assertTrue(sl in skins_ids)
            self.assertTrue(sl in theme_layers)

    def testIconsVisybility(self):
        sp = self.portal.portal_properties.site_properties
        self.assertEqual(sp.getProperty('icon_visibility'), "disabled",
            "Icon visibility not set to 'disabled' after theme installation.")

    def testViewlets(self):
        request = self.app.REQUEST
        view = queryMultiAdapter((self.portal, request), name="plone")
        for manager_name, viewlet_names in VIEWLETS.items():
            manager = queryMultiAdapter(
                (self.portal['front-page'], request, view),
                IViewletManager, name=manager_name)
            for vn in viewlet_names:
                self.assertFalse(manager.get(vn) is None,
                                 "Not registered '%s' viewlet" % vn)

    def testSkinsRequestVarname(self):
        skins = getToolByName(self.portal, "portal_skins")
        req_prop = skins.getRequestVarname()
        self.assertNotEqual(req_prop, '', "Erased 'request_varname' "\
            "portal_skins property: '%s'." % req_prop)


class TestUninstallation(TestCaseUnInstalled):

    def testUninstalled(self):
        qi = self.portal.portal_quickinstaller
        self.assertFalse(qi.isProductInstalled(PROJECT_NAME),
            '%s not uninstalled.' % PROJECT_NAME)

    def testStyles(self):
        """ Test styles registration."""
        cssreg = getToolByName(self.portal, "portal_css")
        for res in CSS_RESOURCES:
            self.assertEqual(cssreg.getResource(res), None)

    def testSkins(self):
        """ Test styles registration."""
        skins = getToolByName(self.portal, "portal_skins")
        themes = skins.getSkinPaths()
        skins_ids = skins.objectIds()

        self.assertEqual(skins.getSkinPath(PROJECT_NAME), None)
        for sl in SKIN_LAYERS:
            self.assertFalse(sl in skins_ids)
            for tn, tlayers in themes:
                self.assertFalse(sl in tlayers,
                    "%s layer still present in %s skin" % (sl, tn))

    def testIconsVisybility(self):
        sp = self.portal.portal_properties.site_properties
        self.assertEqual(sp.getProperty('icon_visibility'), "enabled",
            "Icon visibility not set to 'enabled' after theme uninstallation.")

    def testViewlets(self):
        request = self.app.REQUEST
        view = queryMultiAdapter((self.portal, request), name="plone")
        for manager_name, viewlet_names in VIEWLETS.items():
            manager = queryMultiAdapter(
                (self.portal['front-page'], request, view),
                IViewletManager, name=manager_name)
            for vn in viewlet_names:
                self.assertTrue(manager.get(vn) is None,
                    "Still registered '%s' viewlet after unistallatioin" % vn)


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestDefaultInstallation))
    suite.addTest(makeSuite(TestUninstallation))
    return suite
