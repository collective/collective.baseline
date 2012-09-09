from zope import component
from plone.app.layout.viewlets import common
from plone.registry.interfaces import IRegistry


class BaseLineViewlet(common.ViewletBase):
    """base line viewlet"""

    def update(self):
        super(BaseLineViewlet, self).update()
        self.registry = component.queryUtility(IRegistry)
        self.baseline = u""
        if self.registry:
            try:
                self.baseline = self.registry['collective.baseline']
            except KeyError:
                pass

        if not self.baseline:
            portal = self.portal_state.portal()
            self.baseline = portal.getProperty('description')
