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

    def initializeElement(self, contentItemName, required=True):
        element = self.getElementBySelector(
            self._content[contentItemName]['selector'],
            required=required
        )
        if element is not None:
            self._content_instances[contentItemName] = Elements(element)

    def initializeContent(self):
        for contentItemName in self._content:
            contentItem = self._content[contentItemName]
            if 'module' in contentItem:
                moduleClass = self._content[contentItemName]['module']
                del self._content[contentItemName]['module']
                self.initializeModule(moduleClass, contentItemName, contentItem)
            elif 'selector' in contentItem:
                required = self._content[contentItemName]['required'] \
                    if 'required' in self._content[contentItemName] else True
                self.initializeElement(contentItemName, required)

    def getElementBySelector(self, selector, container=None, required=True):
        if container is None:
            container = self._driver

        element = container.find_elements_by_css_selector(selector)
        if required and len(element) == 0:
            raise ElementNotFoundException(selector)
        return element
