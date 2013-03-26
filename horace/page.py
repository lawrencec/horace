from horace.contentNode import ContentNode


class Page(ContentNode):
    url = None
    title = None
    _content = {}

    def __init__(self, driver):
        super(Page, self).__init__(driver)

    def at(self, title):
        return unicode(title) == unicode(self.title)

    def toFrame(self, frame):
        self._driver.switch_to_frame(frame.id)

    def to_default_content(self):
        self._driver.switch_to_default_content()

    @property
    def url(self):
        return self.url

    @property
    def title(self):
        return self.title


