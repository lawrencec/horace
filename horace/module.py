from contentNode import ContentNode
from horace.element import Element
from horace.exceptions import ElementNotFoundException


class Module(ContentNode):
    _content = {}

    def __init__(self, driver, selector=None, required=True, element=None):
        self.required = required
        self._baseNode = None
        if not element:
            self.base = selector if selector else self.base
        else:
            self._baseNode = Element(element)

        super(Module, self).__init__(driver)

    def initializeContent(self):

        if not self._baseNode and self.base is not None:
            node = super(Module, self).getElementBySelector(self.base)
            if len(node) > 0:
                self._baseNode = Element(node[0])

        super(Module, self).initializeContent()

    def getElementBySelector(self, selector, container=None, required=True):

        if self._baseNode.tag_name == 'iframe':
            self.toFrame()
            element = self._driver.find_elements_by_css_selector(selector)
            if required and len(element) == 0:
                raise ElementNotFoundException(selector)
            return element
        else:
            self.toDefaultContent()
            return super(Module, self).getElementBySelector(
                selector,
                self._baseNode._element,
                required
        )

    def getBaseElement(self):
        return self._baseNode

    def toFrame(self):
        self._driver.switch_to_frame(self._baseNode.id)

    def toDefaultContent(self):
        self._driver.switch_to_default_content()

    @property
    def id(self):
        return self._baseNode._element.id

    @property
    def text(self):
        return self._baseNode.text
