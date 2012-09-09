from zope import component
from plone.app.layout.viewlets import common
from plone.registry.interfaces import IRegistry


class BaseLineViewlet(common.ViewletBase):
    """base line viewlet"""

    def update(self):
        self.registry = component.queryUtility(IRegistry)
        if self.registry:
            self.baseline = self.registry['collective.baseline']

        if not self.baseline:
            portal = self.portal_state.portal()
            self.baseline = portal.getProperty('description')
