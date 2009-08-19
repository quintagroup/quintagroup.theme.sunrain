from Acquisition import aq_base
from Products.CMFCore.utils import getToolByName
from Products.ZCatalog.ProgressHandler import ZLogHandler
from plone.app.linkintegrity.handlers import referencedRelationship as li_relation

portal_catalog = None
portal_repository = None
uid_catalog = None
reference_catalog = None

def fix_archivest(ob):
    ''' Fix #7334 bug of CMFEdition.
        Fixed in CMFEdition v1.1.5+
    '''
    if portal_repository.isVersionable(ob):
        portal_repository.save(obj=ob, comment="")

def fix_catalog(ob):
    ob.reindexObject()

def fix_linkintegrity(ob):
    """Fix losed references."""
    uobject = aq_base(ob)
    if reference_catalog.isReferenceable(uobject):
        ob_li_refs = reference_catalog.getReferences(ob, relationship=li_relation)
        if ob_li_refs:
            annotations = ob._getReferenceAnnotations()
            uniqueUIDs = uid_catalog.uniqueValuesFor('UID')
            # delete references to non-existent objects
            [annotations._delObject(ref.id) for ref in ob_li_refs \
             if not ref.targetUID in uniqueUIDs]
        
def fix_all(ob):
    """ Recursive function for perform registered
        actions for all internal objects
    """
    [a(ob) for a in perobject_actions]

    if getattr(ob, 'is_folderish', None):
        [fix_all(o) for o in ob.objectValues()]

perobject_actions = [fix_archivest, fix_catalog, fix_linkintegrity]

def fix(context):
    ''' Main fix function: fix defects of importing:
        imported objects - absence in catalogs, some other issues'''
    global portal_repository, portal_catalog
    global uid_catalog, reference_catalog
    portal_catalog = getToolByName(context,'portal_catalog')
    portal_repository = getToolByName(context,'portal_repository')
    uid_catalog = getToolByName(context,'uid_catalog')
    reference_catalog = getToolByName(context,'reference_catalog')

    fix_all(context)
