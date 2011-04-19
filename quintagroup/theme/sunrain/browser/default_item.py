from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from collective.blog.view.default_item import DefaultItemView as BaseView

class DefaultItemView(BaseView):
    """
    The default blog item view
    """

    template = ViewPageTemplateFile("templates/default_item.pt")