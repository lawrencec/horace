from horace.contentNode import ContentNode


class Page(ContentNode):
    url = None
    title = None

    def initializeModule(self, moduleClass, module_name, configuration):
        content = moduleClass(self._driver, **configuration)
        self._content_instances[module_name] = content

    @property
    def url(self):
        return self.url

    @property
    def title(self):
        return self.title


