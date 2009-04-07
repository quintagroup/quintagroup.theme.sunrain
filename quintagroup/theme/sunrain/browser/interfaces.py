from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """

class IRainThemeSpecific(IThemeSpecific):
    """Marker interface that defines a Zope 3 browser layer for Rain Theme.
    """

class ISunThemeSpecific(IThemeSpecific):
    """Marker interface that defines a Zope 3 browser layer for Sun Theme.
    """

