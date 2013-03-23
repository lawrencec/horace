from horace.exceptions import NotAtPageException


class Agent(object):

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
        self._currentPage = Page(self._driver)
        title = self._driver.title
        if not self._currentPage.at(title):
            raise NotAtPageException(self._currentPage.title, title)

    def to_at(self, Page):
        self.to(Page)
        self.at(Page)

    def drive(self):
        pass

    def close(self):
        self._driver.close()