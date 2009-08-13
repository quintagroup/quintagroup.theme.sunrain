from zope.interface import implements

from zope import schema
from zope.formlib import form

from quintagroup.portlet.cumulus import cumulusportlet as base
from quintagroup.portlet.cumulus import CumulusPortletMessageFactory as _cmf


class ICumulusPortlet(base.ICumulusPortlet):
    """ A cumulus tag cloud portlet.
    """
    # options for generating <embed ... /> tag
    width = schema.Int(
        title=_cmf(u'Width of the Flash tag cloud'),
        description=_cmf(u'Width in pixels (500 or more is recommended).'),
        required=True,
        default=250)

    height = schema.Int(
        title=_cmf(u'Height of the Flash tag cloud'),
        description=_cmf(u'Height in pixels (ideally around 3/4 of the width).'),
        required=True,
        default=250)

    tcolor = schema.TextLine(
        title=_cmf(u'Color of the tags'),
        description=_cmf(u'This and next 3 fields should be 6 character hex color values without the # prefix (000000 for black, ffffff for white).'),
        required=True,
        default=u'5391d0')

    tcolor2 = schema.TextLine(
        title=_cmf(u'Optional second color for gradient'),
        description=_cmf(u'When this color is available, each tag\'s color will be from a gradient between the two. This allows you to create a multi-colored tag cloud.'),
        required=False,
        default=u'333333')

    hicolor = schema.TextLine(
        title=_cmf(u'Optional highlight color'),
        description=_cmf(u'Color of the tag when mouse is over it.'),
        required=False,
        default=u'333333')

    bgcolor = schema.TextLine(
        title=_cmf(u'Background color'),
        description=_cmf(u'The hex value for the background color you\'d like to use. This options has no effect when \'Use transparent mode\' is selected.'),
        required=True,
        default=u'f8f8f8')

    trans = schema.Bool(
        title=_cmf(u'Use transparent mode'),
        description=_cmf(u'Switches on Flash\'s wmode-transparent setting.'),
        required=True,
        default=False)

    speed = schema.Int(
        title=_cmf(u'Rotation speed'),
        description=_cmf(u'Speed of the sphere. Options between 25 and 500 work best.'),
        required=True,
        default=100)

    distr = schema.Bool(
        title=_cmf(u'Distribute tags evenly on sphere'),
        description=_cmf(u'When enabled, the movie will attempt to distribute the tags evenly over the surface of the sphere.'),
        required=True,
        default=True)

    compmode = schema.Bool(
        title=_cmf(u'Use compatibility mode?'),
        description=_cmf(u'Enabling this option switches the plugin to a different way of embedding Flash into the page. Use this if your page has markup errors or if you\'re having trouble getting tag cloud to display correctly.'),
        required=True,
        default=False)

    # options for generating tag cloud data
    smallest = schema.Int(
        title=_cmf(u'Smallest tag size'),
        description=_cmf(u'The text size of the tag with the smallest count value (units given by unit parameter).'),
        required=True,
        default=8)

    largest = schema.Int(
        title=_cmf(u'Largest tag size'),
        description=_cmf(u'The text size of the tag with the highest count value (units given by the unit parameter).'),
        required=True,
        default=20)

    unit = schema.TextLine(
        title=_cmf(u'Unit of measure'),
        description=_cmf(u'Unit of measure as pertains to the smallest and largest values. This can be any CSS length value, e.g. pt, px, em, %.'),
        required=True,
        default=u'pt')

class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(ICumulusPortlet)

    width    = 250
    height   = 250
    tcolor   = u'5391d0'
    tcolor2  = u'333333'
    hicolor  = u'333333'
    bgcolor  = u'f8f8f8'
    speed    = 100
    trans    = False
    distr    = True
    compmode = False

    smallest = 8
    largest  = 20
    unit     = u'pt'


class Renderer(base.Renderer):
    """Portlet renderer.
    """

class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(ICumulusPortlet)

    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(ICumulusPortlet)
