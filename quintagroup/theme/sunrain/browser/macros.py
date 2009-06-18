"""Overrides quills.app macros."""

from quills.app.browser.macros import *

class SunRainWeblogEntryMacros(WeblogEntryMacros):
    template = ViewPageTemplateFile('templates/quills_entry_macros.pt')

class SunRainWeblogMacros(WeblogMacros):
    template = ViewPageTemplateFile('templates/quills_weblog_macros.pt')
