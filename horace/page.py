from horace.contentNode import ContentNode


class Page(ContentNode):
    url = None
    title = None
    _content = {}

    def __init__(self, driver):
        super(Page, self).__init__(driver)

    def initializeModule(self, moduleClass, module_name, configuration):
        content = moduleClass(self._driver, **configuration)
        self._content_instances[module_name] = content

    def at(self, title):
        return title == self.title

    @property
    def url(self):
        return self.url

    @property
    def title(self):
        return self.title


