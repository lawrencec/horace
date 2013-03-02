from contentNode import ContentNode
from horace.element import Element


class Module(ContentNode):
    _content = {}

    def __init__(self, driver, selector=None, required=True):
        self.required = required
        self.base = selector if selector else self.base
        super(Module, self).__init__(driver)

    def initializeContent(self):
        node = None
        if self.base is not None:
            node = super(Module, self).getElementBySelector(self.base)
        if len(node) > 0:
            self._baseNode = Element(node[0])
        super(Module, self).initializeContent()

    def getElementBySelector(self, selector, container=None, required=True):
        return super(Module, self).getElementBySelector(
            selector,
            self._baseNode._element,
            required
        )

    @property
    def text(self):
        return self._baseNode.text
