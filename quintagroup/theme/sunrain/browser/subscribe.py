from zope.component import getMultiAdapter

from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

try:
    from quills.core.interfaces import IWeblogEnhanced
    HAS_QUILLS = True
except:
    HAS_QUILLS = False

class SubscribeViewlet(ViewletBase):
    def update(self):
        super(SubscribeViewlet, self).update()

        self.context_state = getMultiAdapter((self.context, self.request),
                                             name=u'plone_context_state')
        plone_utils = getToolByName(self.context, 'plone_utils')
        self.getIconFor = plone_utils.getIconFor
        self.actions = self.context_state.actions().get('subscribe', None)

    index = ViewPageTemplateFile("templates/subscribe.pt")

class RSSType(object):
    """ This view is used in contidion expression for actions in 'subscribe' 
        category in 'portal_actions' tool.
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def quills(self):
        if HAS_QUILLS and IWeblogEnhanced.providedBy(self.context):
            return True

    def other(self):
        return not self.quills()
