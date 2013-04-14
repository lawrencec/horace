from horace.contentNode import ContentNode


class Page(ContentNode):
    url = None
    title = None
    _content = {}
    wait = 0

    def at(self, title):
        return unicode(title) == unicode(self.title)

    def at(self, title):
        return unicode(title) == unicode(self.title)

    def initialize_content(self, item):
        self.to_default_content()
        super(Page, self).initialize_content()

    @property
    def url(self):
        return self.url

    @property
    def title(self):
        return self.title


