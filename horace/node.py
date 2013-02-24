from horace.elements import Elements
from horace.exceptions import ElementNotFoundException

class Node(object):
    _content = {}
    _content_instances = {}

    def __init__(self, driver):
        self._driver = driver
        try:
            self.initializeContent()
        except Exception, e:
            raise e

    def __getattr__(self, item):
        if item in self._content_instances:
            return self._getContent(item)
        else:
            return object.__getattribute__(self, item)

    def _getContent(self, name):
        return self._content_instances[name]

    def initializeModule(self, key):
        moduleClass = self._content[key]['base']
        content = moduleClass(self._driver, self._content[key])
        self._content_instances[key] = content

    def initializeElement(self, key, required=True):
        element = self.getElementBySelector(
            self._content[key]['selector'],
            required=required
        )
        if element is not None:
            self._content_instances[key] = Elements(element)

    def initializeContent(self):
        for key in self._content:
            kv = self._content[key]
            if 'base' in kv:
                self.initializeModule(key)
            elif 'selector' in kv:
                required = self._content[key]['required'] \
                    if 'required' in self._content[key] else True
                self.initializeElement(key, required)

    def getElementBySelector(self, selector, container=None, required=True):
        if container is None:
            container = self._driver

        element = container.find_elements_by_css_selector(selector)
        if required and len(element) == 0:
            raise ElementNotFoundException(selector)
        return element
