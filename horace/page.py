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

    def toFrame(self, frame):
        self._driver.switch_to_frame(frame._baseNode.id)

    def toDefaultContent(self):
        self._driver.switch_to_default_content()

    @property
    def url(self):
        return self.url

    @property
    def title(self):
        return self.title


