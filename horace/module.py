from contentNode import ContentNode
from horace.element import Element

class Module(ContentNode):

    def __init__(self, driver, selector=None, required=True, element=None):
        self.required = required
        self._baseNode = None

        self.baseSelector = selector if selector else self.baseSelector
        if element:
            self._baseNode = Element(element)

        super(Module, self).__init__(driver)

    def __getattr__(self, item):
        valid_keys = Element.__dict__.keys()
        if item in valid_keys and self._baseNode:
            return Element.__dict__[item].__get__(self._baseNode)
        else:
            return super(Module, self).__getattr__(item)

    def initialize_base(self):
        if not self._baseNode and self.baseSelector is not None:
            node = super(Module, self).get_elements_by_selector(self.baseSelector)
            if len(node) > 0:
                self._baseNode = Element(node[0])
        super(Module, self).initialize_base()


    def get_elements_by_selector(self, selector, container=None, required=True):
        return super(Module, self).get_elements_by_selector(
                selector,
                self._baseNode._element,
                required
        )

    def get_base_element(self):
        return self._baseNode


    @property
    def id(self):
        return self._baseNode._element.id

    @property
    def text(self):
        return self._baseNode.text


class IFrameModule(Module):

    def initialize_content(self, item):


        self.activate()

        super(IFrameModule, self).initialize_content()
        self.to_default_content()

    def get_elements_by_selector(self, selector, container=None, required=True):
        return super(Module, self).get_elements_by_selector(
                selector,
                self._driver,
                required
        )

    def activate(self):
        if self._baseNode.tag_name == 'iframe':
            self.to_frame(self._baseNode.id)