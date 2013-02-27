from contentNode import ContentNode
from horace.element import Element


class Module(ContentNode):
    base = None
    required = True

    def __init__(self, driver, selector=None, required=True):
        self.required = required
        self.base = selector if selector else self.base
        super(Module, self).__init__(driver)

    def initializeContent(self):
        element = None
        if self.base is not None:
            element = super(Module, self).getElementBySelector(self.base)
        if len(element) > 0:
            self._baseElement = Element(element[0])
        super(Module, self).initializeContent()

    def getElementBySelector(self, selector, container=None, required=True):
        return super(Module, self).getElementBySelector(
            selector,
            self._baseElement._element,
            required
        )

    @property
    def text(self):
        return self._baseElement.text
