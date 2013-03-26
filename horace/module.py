from contentNode import ContentNode
from horace.element import Element
from horace.exceptions import ElementNotFoundException


class Module(ContentNode):
    _content = {}

    def __init__(self, driver, selector=None, required=True, element=None):
        self.required = required
        self._baseNode = None
        if not element:
            self.baseSelector = selector if selector else self.baseSelector
        else:
            self._baseNode = Element(element)

        super(Module, self).__init__(driver)

    def initialize_content(self):
        if not self._baseNode and self.baseSelector is not None:
            node = super(Module, self).get_elements_by_selector(self.baseSelector)
            if len(node) > 0:
                self._baseNode = Element(node[0])

        super(Module, self).initialize_content()

    def get_elements_by_selector(self, selector, container=None, required=True):
        if self._baseNode.tag_name == 'iframe':
            self.to_frame()
            element = self._driver.find_elements_by_css_selector(selector)
            if required and len(element) == 0:
                raise ElementNotFoundException(selector)
            return element
        else:
            self.to_default_content()
            return super(Module, self).get_elements_by_selector(
                selector,
                self._baseNode._element,
                required
        )

    def get_base_element(self):
        return self._baseNode

    def to_frame(self):
        self._driver.switch_to_frame(self._baseNode.id)

    def to_default_content(self):
        self._driver.switch_to_default_content()

    @property
    def id(self):
        return self._baseNode._element.id

    @property
    def text(self):
        return self._baseNode.text
