from horace.node import Node


class Page(Node):
    url = None
    _title = None

    def __init__(self, driver, config=None):
        self._config = config
        super(Page, self).__init__(driver)

    @property
    def title(self):
        return self._title


