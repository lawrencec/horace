from horace.exceptions import NotAtPageException


class Agent(object):
    def __new__(cls, *p, **k):
        if not '_the_instance' in cls.__dict__:
            cls._the_instance = object.__new__(cls)
        return cls._the_instance

    def __init__(self, driver):
        self._driver = driver
        self._currentPage = None

    def __getattr__(self, name):
        if name == 'page':
            return self._currentPage
        else:
            return object.__getattribute__(self, name)

    def to(self, Page):
        self._driver.get(Page.url)

    def at(self, Page):
        if not self._currentPage:
            self._currentPage = Page(self._driver)
        title = self._driver.title
        if title != self._currentPage.title:
            raise NotAtPageException(self._currentPage.title, title)

    def toAt(self, Page):
        self._currentPage = Page(self._driver)
        self.to(Page)
        self.at(Page)

    def drive(self):
        pass

    def close(self):
        self._driver.close()