#
import os,types
from StringIO import StringIO
from ConfigParser import SafeConfigParser

def write_map(cmd, basename, filename, force=False):
    argname = os.path.splitext(basename)[0]
    value = getattr(cmd.distribution, argname, None)

    if value:
        config = SafeConfigParser()
        config.add_section('qplone3_theme')
        for name, val in value.items():
            val = val and str(val) or ''
            config.set('qplone3_theme', name, val)

        strvalue = StringIO()
        config.write(strvalue)
        value = strvalue.getvalue()

    cmd.write_or_delete_file(argname, filename, value, force)


def assert_dict(dist, attr, value):
    """Verify that value is a dict or None"""
    try:
        assert type(value) == types.DictType
        print 'success assert'
    except (TypeError,ValueError,AttributeError,AssertionError):
        raise DistutilsSetupError(
            "%r must be a dict (got %r)" % (attr,value)
        )
