import transaction
from Products.CMFCore.utils import getToolByName

UNINSTALL_PROFILES = [
    'quintagroup.theme.sunrain:uninstall'
]

def uninstall(self):
    """This method is here to make uninstall GS profiles execution
    on portal_quickinstaller's tool Uninstall action.
    """
    portal_setup = getToolByName(self, 'portal_setup')
    for extension_id in UNINSTALL_PROFILES:
        portal_setup.runAllImportStepsFromProfile('profile-%s' % extension_id)
        product_name = extension_id.split(':')[0]
        transaction.savepoint()
