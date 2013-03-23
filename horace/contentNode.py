from horace.elements import Elements
from horace.exceptions import ElementNotFoundException


class ContentNode(object):

    def __init__(self, driver):
        self._driver = driver
        self._content_instances = {}
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
        content = self._content
        for contentItemName in self._content:
            contentItem = content[contentItemName]

            if 'module' in contentItem and contentItem['module'] is not None:
                moduleClass = content[contentItemName]['module']
                isList = False
                if 'isList' in content[contentItemName]:
                    isList = content[contentItemName]['isList']

                moduleArgs = {key: value for key, value in contentItem.items()
                              if key is not 'module' and key is not 'isList'}
                if not isList:
                    self.initializeModule(moduleClass, contentItemName, moduleArgs)
                else:
                    self.initializeModules(moduleClass, contentItemName, moduleArgs)
            elif 'selector' in contentItem and contentItem['selector'] \
                    is not None:
                required = content[contentItemName]['required'] \
                    if 'required' in content[contentItemName] else True
                self.initializeElement(contentItemName, required)

    def initializeModule(self, moduleClass, module_name, configuration):
        content = moduleClass(self._driver, **configuration)
        self._content_instances[module_name] = content

    def initializeModules(self, moduleClass, module_name, configuration):
        content = []
        elemList = self.getElementBySelector(
            selector=configuration['selector'],
            required=configuration['required']
        )
        for elem in elemList:
            configuration['element'] = elem
            content.append(moduleClass(self._driver, **configuration))
        self._content_instances[module_name] = content

    def getElementBySelector(self, selector, container=None, required=True):
        self._driver.switch_to_default_content()
        if container is None:
            container = self._driver

        element = container.find_elements_by_css_selector(selector)
        if required and len(element) == 0:
            raise ElementNotFoundException(selector)
        return element


def contentElement(selector=None, required=True):
    if not selector:
        raise Exception('selector required')
    return {
        'selector': selector,
        'required': required
    }


def contentModule(module=None, selector=None, required=True):
    if not module:
        raise Exception('selector or module required')

    return {
        'module': module,
        'required': required,
        'selector': selector
    }


def contentModuleList(module=None, selector=None, required=True):
    module = contentModule(module, selector, required)
    module['isList'] = True
    return module

