from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common
from plone.app.layout.viewlets import content

class LogoViewlet(common.LogoViewlet):
    render = ViewPageTemplateFile('templates/logo.pt')
