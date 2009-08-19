import transaction
import os, sys, re, string
from sets import Set
from StringIO import StringIO
from time import gmtime, strftime
from zLOG import LOG, INFO
from zExceptions import BadRequest
from App.config import getConfiguration
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.DirectoryView import addDirectoryViews
from Globals import package_home

from fixes import fix
from quintagroup.theme.sunrain import GLOBALS

IMPORT_POLICY = "backup"

osp = os.path
ALLOWED_IMPORT_POLICY = ["only_new", "backup", "overwrite"]
INTRO_TO_INSTANCE = "< Started copying object files from Product import directory to Instance one."
SUMMARY_TO_INSTANCE = "> Finished copying."
INTRO_TO_ROOT = "< Started import %s file[s] with '%s' policy."
SUMMARY_TO_ROOT = "> Finished importing."
INTRO_CLEAN = "< Started cleaning Instance import directory."
SUMMARY_CLEAN = "> Finished cleaning."
CREXP_INVALID_ID = re.compile('^The id \"(.*?)\" is invalid - it is already in use.$', re.DOTALL|re.IGNORECASE|re.MULTILINE)
CSS_BASE_IDS_QPSD053 = ['id','expression','enabled','cookable','media','rel','title','rendering']   # supporting qPSD-0.5.3 version
def checkIfImport():
    """ Return if perform importing, based on checking 
        *zexp files in <SkinProduct>/import directory.
    """
    instance_ipath, product_ipath = getImportedPathes()
    product_ilist = [i for i in os.listdir(product_ipath) \
                     if osp.isfile(osp.join(product_ipath,i)) and i.endswith('.zexp')]
    if product_ilist:
        return 1
    return 0

def getImportedPathes():
    """ Return Plone instance and Skin product import pathes."""
    # Based on instance path, construct import pathes 
    cfg = getConfiguration()
    instance_ipath = osp.join(cfg.instancehome, "import")
    product_ipath = osp.join(package_home(GLOBALS), "import")
    # Check presence of Product import directory
    if not osp.isdir(product_ipath):        
        raise BadRequest, "Skin Product's import directory '%s' - does not exist or is'nt direcory" % product_ipath
    # Check presence of Instance import directory
    if not osp.isdir(instance_ipath):
        raise BadRequest, "Instance import directory '%s' - does not exist or isn't direcory" % instance_ipath
    return [instance_ipath, product_ipath]

def copyFile(src_dir, dst_dir, f_name):
    """ Copy file from src_dir to dst_dir under original name."""
    try:
        src_file = open(osp.join(src_dir, f_name),"rb")
        dst_file = open(osp.join(dst_dir, f_name),"wb")
        dst_file.write(src_file.read())
        dst_file.close()
        src_file.close()
    except Exception, e:
        msg = "!!! In copying files from < %s > dir to < %s > dir exception occur. Details: %s." % (src_dir,dst_dir, str(e))
        print >> import_out, msg
        LOG('performImportToPortal',INFO,'copyFile', msg)

def moveToTemp(same_instance_files, instance_ipath, temp_dir_path):
    """ Move samenamed files from Instanse's dir to temp dir."""
    os.mkdir(temp_dir_path) # Create temp back_[date] dir
    try:
        [copyFile(instance_ipath, temp_dir_path, f_name) for f_name in same_instance_files]
        [os.remove(osp.join(instance_ipath, f_name)) for f_name in same_instance_files]
    except Exception, e:
        msg = "!!! Exception occur during moving files from Instance's dir to temp dir. Detaile:%s." % str(e)
        print >> import_out, msg
        LOG('performImportToPortal',INFO,'moveToTemp', msg)
    
def copyToInstanceImport():
    """ Perform copying imported files from <SkinProduct>/import dir
        to Plone's instance import dir.
    """
    print >> import_out, INTRO_TO_INSTANCE
    instance_ipath, product_ipath = getImportedPathes()
    # Compose temp dir back_[date] dir path in Instance import directory
    temp_dir_id = "back_%s" % strftime("%Y%m%d%H%M%S", gmtime())
    temp_dir_path = osp.join(instance_ipath, temp_dir_id)
    # Get *.zexp files from Skin Product's import dir and Plone's instance import dir files
    product_ilist = [i for i in os.listdir(product_ipath) \
                     if osp.isfile(osp.join(product_ipath,i)) and i.endswith('.zexp')]
    instance_ilist = [i for i in os.listdir(instance_ipath) \
                      if osp.isfile(osp.join(instance_ipath,i)) and i.endswith('.zexp')]
    # Check for presence samenamed files in Instance and Product import directories.
    same_instance_files = [f_name for f_name in instance_ilist if f_name in product_ilist]
    if same_instance_files:
        moveToTemp(same_instance_files, instance_ipath, temp_dir_path)
    # Copy all *zexp files from Product's import dir to Instance's import dir
    [copyFile(product_ipath, instance_ipath, f_name) for f_name in product_ilist]
    print >> import_out, SUMMARY_TO_INSTANCE
    return [instance_ipath, product_ipath, temp_dir_path, product_ilist]

def importObject(portal, file_name):
    """ Work around old Zope bug in importing."""
    try:
        portal.manage_importObject(file_name)
    except:
        portal._p_jar = portal.Destination()._p_jar
        portal.manage_importObject(file_name)

def makeBackUp(portal, portal_objects, temp_dir_path, obj_id):
    """ Perfom backup same named portal objects in temp folder."""
    # Get id of temp folder-object
    durty_path,temp_id = osp.split(temp_dir_path)
    if not temp_id:
        durty_path,temp_id = osp.split(durty_path)
    # Get temp folder-object
    if temp_id not in portal_objects:
        portal.invokeFactory('Large Plone Folder', id=temp_id)
        print >> import_out, "! Created '%s' backup directory with same-ids " \
                             "objects from portal root." % temp_id
    temp_dir = getattr(portal, temp_id)
    # Move object with same id to temp folder-object
    #get_transaction().commit(1)
    transaction.savepoint()
    obj = portal.manage_cutObjects(ids=[obj_id])
    temp_dir.manage_pasteObjects(obj)
    print >> import_out, "! '%s' Object moved from portal root to '%s' backup directory." % (obj_id, temp_id)

def performImport(portal, temp_dir_path, file_name):
    """ Importing an object to portal."""
    portal_objects = portal.objectIds()
    try:
        portal.manage_importObject(file_name)
    except Exception, e:
        msg = str(e)
        is_invalid_id = CREXP_INVALID_ID.match(msg)
        if is_invalid_id:
            obj_id = is_invalid_id.group(1)
            if IMPORT_POLICY == "only_new":
                msg = "! Object with '%s' id was not importing because it's already exist " \
                      "in portal root." % obj_id
                print >> import_out, msg
            elif IMPORT_POLICY == "backup":
                makeBackUp(portal, portal_objects, temp_dir_path, obj_id)
                importObject(portal, file_name)
            elif IMPORT_POLICY == "overwrite":
                portal.manage_delObjects(ids=[obj_id])
                importObject(portal, file_name)
        else:
            # work around old Zope bug in importing
            portal._p_jar = portal.Destination()._p_jar
            portal.manage_importObject(file_name)

def importToPortalRoot(portal, product_file_names, temp_dir_path):
    """ Import all objects from *zexp files to portal root (based on IMPORT_POLICY)."""
    if not IMPORT_POLICY in ALLOWED_IMPORT_POLICY:
        raise Exception("%s - wrong import policy, must be one of the %s" \
                        % (IMPORT_POLICY, ALLOWED_IMPORT_POLICY) )
    print >> import_out, INTRO_TO_ROOT % (product_file_names, IMPORT_POLICY)
    for file_name in product_file_names:
        try:
            # Temporary allow implicitly adding Large Plone Folder
            types_tool = getToolByName(portal, 'portal_types')
            lpf_fti = types_tool['Large Plone Folder']
            lpf_global_setting = lpf_fti.global_allow
            lpf_fti.global_allow = 1
            try:
                performImport(portal, temp_dir_path, file_name)
            finally:
                lpf_fti.global_allow = lpf_global_setting
        except Exception, error:
            msg = '!!! Under "%s" policy importing exception occur: %s.' % (IMPORT_POLICY, str(error))
            print >> import_out, msg
            LOG('performImportToPortal',INFO,'importToPortalRoot', msg)
    print >> import_out, SUMMARY_TO_ROOT

def cleanInstanceImport(instance_ipath, product_file_names, temp_dir_path):
    """ Cleaning Plone's import dir."""
    print >> import_out, INTRO_CLEAN
    # Erase all copied *zexp files from Instance's import dir
    for f_name in product_file_names:
        f_path = osp.join(instance_ipath, f_name)
        if osp.exists(f_path) and osp.isfile(f_path):
            os.remove(f_path)
        else:
            msg = '! "%s" file was not deleted from "%s" import directory.' %\
                   (f_name, osp.join(instance_ipath))
            print >> import_out, msg
            LOG('performImportToPortal',INFO,'cleanInstanceImport', msg)
    # Move all files from temp back_[date] dir to Instance's import dir
    if osp.exists(temp_dir_path) and osp.isdir(temp_dir_path):
        f_names = os.listdir(temp_dir_path)
        try:
            [copyFile(temp_dir_path, instance_ipath, f_name) for f_name in f_names]
            [os.remove(osp.join(temp_dir_path, f_name)) for f_name in f_names]
            # Erase temp back_[date] dir
            os.rmdir(temp_dir_path)
        except Exception, e:
            msg = "!!! In moving files from temp dir to Instance's import dir exception occur."
            print >> import_out, msg
            LOG('performImportToPortal',INFO,'moveFromTempToImport', msg)
    print >> import_out, SUMMARY_CLEAN

def fixImportingIssues(portal, beforeimporting_objects):
    ''' Fix defects of importing process: reindexing, other'''
    afterimporting_objects = portal.objectItems()
    diff_objects = list(Set(afterimporting_objects)-Set(beforeimporting_objects))
    for id, ob in diff_objects:
        if id.startswith('back_'):
            continue
        fix(ob)

def performImportToPortal(portal):
    """ Import objects from Skin Product to Portal root."""
    globals()['import_out'] = StringIO()
    instance_ipath, product_ipath, temp_dir_path, product_file_names = copyToInstanceImport()
    if product_file_names:
        beforeimporting_objects = portal.objectItems()
        importToPortalRoot(portal, product_file_names, temp_dir_path)
        fixImportingIssues(portal, beforeimporting_objects)
        cleanInstanceImport(instance_ipath, product_file_names, temp_dir_path)
    else:
        print >> import_out, "!!! Failure importing: there is no file for importing to be found."
    result = import_out.getvalue()
    del globals()['import_out']
    return result

#