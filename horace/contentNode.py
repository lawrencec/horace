from horace.elements import Elements
from horace.exceptions import ElementNotFoundException


class ContentNode(object):

    def __init__(self, driver):
        self._driver = driver
        self._content_instances = {}

        self.initialize_base()

    def __getattr__(self, item):
        if item not in self._content_instances:
            self.initialize_content(item)
        if item in self._content_instances:
            return self._content_instances[item]
        else:
            return object.__getattribute__(self, item)

    def refresh_content(self, item):
        if isinstance(self._content_instances[item], ContentNode):
            self._content_instances[item].initialize_content()

    def _content_modules(self, content, list_only=False):
        for contentItemName in content:
            contentItem = content[contentItemName]
            if 'module' in contentItem and contentItem['module'] is not None:
                moduleClass = content[contentItemName]['module']
                isList = False
                if 'isList' in content[contentItemName]:
                    isList = content[contentItemName]['isList']

                moduleArgs = {key: value for key, value in contentItem.items()
                              if key is not 'module' and key is not 'isList'}
                if not list_only and not isList:
                    yield (moduleClass, contentItemName, moduleArgs)
                elif list_only and isList:
                    yield (moduleClass, contentItemName, moduleArgs)

    def content_elements(self, content):
        for contentItemName in content:
            contentItem = content[contentItemName]
            if 'module' not in contentItem and 'selector' in contentItem and \
                    contentItem['selector'] is not None:
                yield contentItemName, content[contentItemName]['required']

    def initialize_element(self, contentItemName, required=True):
        elements = self.get_elements_by_selector(
            self._content[contentItemName]['selector'],
            required=required
        )

        if elements is not None:
            self._content_instances[contentItemName] = Elements(elements)

    def initialize_base(self):
        pass

    def initialize_content(self, item=None):
        if not item:
            for selector, required in self.content_elements(self._content):
                self.initialize_element(selector, required)

            for module, content, module_args in self._content_modules(self._content):
                self.initialize_module(module, content, module_args)

            for module, content, module_args in self._content_modules(self._content, True):
                self.initialize_modules(module, content, module_args)
        else:
            for selector, required in self.content_elements({item: self._content[item]}):
                self.initialize_element(selector, required in self.content_elements({item: self._content[item]}))

            for module, content, module_args in self._content_modules({item: self._content[item]}):
                self.initialize_module(module, content, module_args)

            for module, content, module_args in self._content_modules({item: self._content[item]}, True):
                self.initialize_modules(module, content, module_args)


    def initialize_module(self, moduleClass, module_name, configuration):
        self._content_instances[module_name] = moduleClass(self._driver, **configuration)

    def initialize_modules(self, moduleClass, module_name, configuration):
        content = []
        elemList = self.get_elements_by_selector(
            selector=configuration['selector'],
            required=configuration['required']
        )
        for elem in elemList:
            configuration['element'] = elem
            content.append(moduleClass(self._driver, **configuration))
        self._content_instances[module_name] = content

    def get_elements_by_selector(self, selector, container=None, required=True):
        if container is None:
            container = self._driver
        elements = container.find_elements_by_css_selector(selector)
        if required and len(elements) == 0:
            raise ElementNotFoundException(selector)
        return elements

    def to_default_content(self):
        self._driver.switch_to_default_content()

    def to_frame(self, frameId):
        self._driver.switch_to_frame(frameId)


def element(selector=None, required=True):
    if not selector:
        raise Exception('selector required')
    return {
        'selector': selector,
        'required': required
    }


def content_module(module=None, selector=None, required=True):
    if not module:
        raise Exception('selector or module required')

    return {
        'module': module,
        'required': required,
        'selector': selector
    }


def content_module_list(module=None, selector=None, required=True):
    module = content_module(module, selector if selector else module.selector, required)
    module['isList'] = True
    return module

